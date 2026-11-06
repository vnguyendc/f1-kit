from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate import validate


def snapshot(root):
    if not root.exists():
        return {}
    result = {}
    for p in root.rglob('*'):
        name = str(p.relative_to(root))
        result[name] = ('link', os.readlink(p)) if p.is_symlink() else (
            ('file', hashlib.sha256(p.read_bytes()).hexdigest(), p.stat().st_mtime_ns)
            if p.is_file() else ('dir',))
    return result


def copy_package(target):
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc', '.DS_Store'))


class PackageTests(unittest.TestCase):
    def run_install(self, home, *args, root=ROOT, env_extra=None):
        env = dict(os.environ, F1_TARGET_HOME=str(home), PYTHONDONTWRITEBYTECODE='1')
        env.update(env_extra or {})
        return subprocess.run(['bash', str(root / 'install-codex.sh'), *args],
                              env=env, text=True, capture_output=True)

    def test_install_preflight_repeat_and_other_profiles(self):
        for layout in ['unix home', 'mnt/c/Users/Test User']:
            with self.subTest(layout=layout), tempfile.TemporaryDirectory() as temp:
                home = Path(temp) / layout
                home.mkdir(parents=True)
                untouched = home / '.claude/skills/keep.txt'
                untouched.parent.mkdir(parents=True)
                untouched.write_text('preserve unrelated profile')
                before = snapshot(home)
                check = self.run_install(home, '--check')
                self.assertEqual(check.returncode, 0, check.stderr)
                self.assertEqual(before, snapshot(home))
                installed = self.run_install(home)
                self.assertEqual(installed.returncode, 0, installed.stderr)
                for name in ['f1', 'f1-work']:
                    target = home / '.codex/skills' / name
                    source = ROOT / 'skills' / name
                    for file in source.rglob('*'):
                        if file.is_file():
                            installed_file = target / file.relative_to(source)
                            self.assertEqual(file.read_bytes(), installed_file.read_bytes())
                            if file.suffix == '.md':
                                for link in re.findall(r'\]\(([^)]+)\)', installed_file.read_text()):
                                    if not re.match(r'[a-z][a-z0-9+.-]*:', link, re.I) and not link.startswith('#'):
                                        self.assertTrue((installed_file.parent / link.split('#', 1)[0]).exists(), link)
                self.assertEqual(untouched.read_text(), 'preserve unrelated profile')
                self.assertFalse((home / '.agents').exists())
                after = snapshot(home)
                self.assertEqual(self.run_install(home).returncode, 0)
                self.assertEqual(after, snapshot(home))

    def test_conflicts_preserve_all_existing_content(self):
        for name in ['f1', 'f1-work']:
            for kind in ['file', 'directory', 'symlink', 'broken-link', 'nested-link', 'extra-directory']:
                with self.subTest(name=name, kind=kind), tempfile.TemporaryDirectory() as temp:
                    home = Path(temp);target = home / '.codex/skills' / name
                    target.parent.mkdir(parents=True)
                    if kind == 'file':
                        target.write_text('existing skill')
                    elif kind == 'directory':
                        target.mkdir();(target / 'keep').write_text('existing skill')
                    elif kind in ['symlink', 'broken-link']:
                        other = home / 'other'
                        if kind == 'symlink':
                            other.mkdir();(other / 'keep').write_text('keep')
                        target.symlink_to(other)
                    else:
                        shutil.copytree(ROOT / 'skills' / name, target)
                        if kind == 'nested-link':
                            (target / 'extra-link').symlink_to(home / 'missing')
                        else:
                            (target / 'extra-directory').mkdir()
                    before = snapshot(home)
                    for args in [('--check',), ()]:
                        result = self.run_install(home, *args)
                        self.assertEqual(result.returncode, 2, result.stdout)
                        self.assertIn('Conflict', result.stderr)
                        self.assertEqual(before, snapshot(home))

    def test_missing_companion_is_added_without_rewriting_current_f1(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp);target = home / '.codex/skills/f1'
            shutil.copytree(ROOT / 'skills/f1', target)
            before = snapshot(target)
            self.assertEqual(self.run_install(home, '--check').returncode, 0)
            self.assertFalse((home / '.codex/skills/f1-work').exists())
            installed = self.run_install(home)
            self.assertEqual(installed.returncode, 0, installed.stderr)
            self.assertEqual(before, snapshot(target))
            self.assertTrue((home / '.codex/skills/f1-work/SKILL.md').is_file())

    def test_custom_codex_home_and_explicit_target_precedence(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp);codex_home = base / 'custom profile'
            env = dict(os.environ, CODEX_HOME=str(codex_home), PYTHONDONTWRITEBYTECODE='1')
            env.pop('F1_TARGET_HOME', None)
            result = subprocess.run(['bash', str(ROOT / 'install-codex.sh')], env=env,
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((codex_home / 'skills/f1/SKILL.md').is_file())
            self.assertTrue((codex_home / 'skills/f1-work/SKILL.md').is_file())
            before = snapshot(codex_home)
            target_home = base / 'explicit home'
            self.assertEqual(self.run_install(target_home, env_extra={'CODEX_HOME': str(codex_home)}).returncode, 0)
            self.assertTrue((target_home / '.codex/skills/f1/SKILL.md').is_file())
            self.assertTrue((target_home / '.codex/skills/f1-work/SKILL.md').is_file())
            self.assertEqual(before, snapshot(codex_home))

    def test_invalid_arguments_write_nothing(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            for args in [('--replace',), ('--check', 'extra')]:
                self.assertEqual(self.run_install(home, *args).returncode, 1)
                self.assertEqual(snapshot(home), {})

    def test_invalid_source_write_nothing(self):
        for defect in ['missing-role', 'missing-companion', 'missing-companion-metadata',
                       'invalid-companion', 'broken-link', 'escaping-link', 'symlink', 'manifest-mismatch']:
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as temp:
                base = Path(temp);pkg = base / 'export';copy_package(pkg)
                if defect == 'missing-role':
                    (pkg / 'skills/f1/references/roles/verifier.md').unlink()
                elif defect == 'missing-companion':
                    (pkg / 'skills/f1-work/SKILL.md').unlink()
                elif defect == 'missing-companion-metadata':
                    (pkg / 'skills/f1-work/agents/openai.yaml').unlink()
                elif defect == 'invalid-companion':
                    (pkg / 'skills/f1-work/SKILL.md').write_text('invalid entrypoint')
                elif defect in ['broken-link', 'escaping-link']:
                    target = 'missing.md' if defect == 'broken-link' else '../outside.md'
                    (base / 'outside.md').write_text('outside package')
                    with (pkg / 'README.md').open('a') as handle:
                        handle.write(f'\n[Invalid]({target})\n')
                elif defect == 'symlink':
                    (pkg / 'link').symlink_to(base / 'missing')
                else:
                    path = pkg / '.claude-plugin/plugin.json';obj=json.loads(path.read_text())
                    obj['version'] = '999.0.0';path.write_text(json.dumps(obj))
                home = base / 'home'
                result = self.run_install(home, root=pkg)
                self.assertEqual(result.returncode, 2, result.stdout)
                self.assertFalse(home.exists())

    def test_standalone_export_has_no_parent_dependency(self):
        with tempfile.TemporaryDirectory() as temp:
            pkg=Path(temp) / 'standalone';copy_package(pkg)
            self.assertGreater(validate(pkg), 20)
            self.assertFalse((pkg / '.git').exists())
            home=Path(temp) / 'profile'
            result=self.run_install(home, root=pkg)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((home / '.codex/skills/f1/references/roles/planner.md').is_file())
            self.assertTrue((home / '.codex/skills/f1-work/references/task-record.md').is_file())


if __name__ == '__main__':
    unittest.main()

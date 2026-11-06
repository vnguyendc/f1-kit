#!/usr/bin/env python3
"""Validate the portable package and all of its local resource links."""
import json
from pathlib import Path
import re
import sys


SKILLS = ('f1', 'f1-work')

REQUIRED = (
    'LICENSE', 'README.md', 'plugin.json', '.claude-plugin/plugin.json',
    '.claude-plugin/marketplace.json', 'install-codex.sh',
    'skills/f1/SKILL.md', 'skills/f1/agents/openai.yaml',
    'skills/f1/references/contract.md', 'skills/f1/references/plan-template.md',
    'skills/f1/references/pr-description-template.md',
    'skills/f1/references/design-diagrams.md',
    'skills/f1/references/ui-ux-research.md', 'skills/f1/references/ui-ux-review.md',
    'skills/f1/references/pr-preview-verification.md',
    'skills/f1/references/hosts.md', 'skills/f1/references/integrations.md',
    'skills/f1/references/roles/planner.md',
    'skills/f1/references/roles/implementer.md',
    'skills/f1/references/roles/verifier.md',
    'skills/f1/references/roles/deployer.md',
    'skills/f1-work/SKILL.md', 'skills/f1-work/agents/openai.yaml',
    'skills/f1-work/references/task-record.md',
    'skills/f1-work/references/examples.md',
)


def package_files(root):
    for path in sorted(root.rglob('*')):
        if any(part in {'.git', '__pycache__'} for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            raise ValueError(f'Package contains a symbolic link: {path.relative_to(root)}')
        if path.is_file() and path.name != '.DS_Store':
            yield path


def validate(root):
    root = root.resolve()
    for name in REQUIRED:
        if not (root / name).is_file():
            raise ValueError(f'Incomplete F1 package: missing {name}')
    files = list(package_files(root))
    for name in SKILLS:
        entry = (root / 'skills' / name / 'SKILL.md').read_text()
        if not re.match(rf'\A---\nname: {re.escape(name)}\ndescription: [^\n]+\n---\n', entry):
            raise ValueError(f'{name} skill frontmatter must contain name and description')
    manifest = json.loads((root / 'plugin.json').read_text())
    if manifest.get('name') != 'f1-kit' or not re.fullmatch(r'\d+\.\d+\.\d+', manifest.get('version', '')):
        raise ValueError('Invalid F1 package name or semantic version')
    claude = json.loads((root / '.claude-plugin/plugin.json').read_text())
    if claude != {k: v for k, v in manifest.items() if k != '$schema'}:
        raise ValueError('Host manifests disagree')
    marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
    if marketplace.get('name') != 'f1-kit' or marketplace.get('plugins') != [
        {'name': 'f1-kit', 'source': './', 'description': manifest['description']}
    ]:
        raise ValueError('Marketplace must point to the local F1 package root')
    for path in files:
        if path.suffix != '.md':
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#'):
                continue
            local = (path.parent / target.split('#', 1)[0]).resolve()
            if not local.is_relative_to(root) or not local.exists():
                raise ValueError(f'Invalid local resource in {path.relative_to(root)}: {target}')
    return len(files)


if __name__ == '__main__':
    try:
        count = validate(Path(__file__).resolve().parents[1])
        print(f'Validated F1 package: {count} files; manifests and local links resolve.')
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)

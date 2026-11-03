#!/usr/bin/env bash
set -euo pipefail

if (( $# > 1 )) || [[ ${1:-} != "" && ${1:-} != "--check" ]]; then
  echo "Usage: bash install-codex.sh [--check]" >&2
  exit 1
fi

package_root=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PYTHONDONTWRITEBYTECODE=1 python3 - "$package_root" "${1:-}" <<'PY'
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile

root = Path(sys.argv[1])
sys.path.insert(0, str(root / 'scripts'))
try:
    from validate import validate
    validate(root)
    source = root / 'skills/f1'
    if os.environ.get('F1_TARGET_HOME'):
        profile = Path(os.environ['F1_TARGET_HOME']).expanduser() / '.codex'
    else:
        profile = Path(os.environ.get('CODEX_HOME') or str(Path.home() / '.codex')).expanduser()
    target = profile / 'skills/f1'

    def contents(directory):
        return {str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in directory.rglob('*') if p.is_file()} | {
                    str(p.relative_to(directory)): None for p in directory.rglob('*') if p.is_dir()}

    expected = contents(source)
    if target.is_symlink() or (target.exists() and (
            not target.is_dir() or any(p.is_symlink() for p in target.rglob('*'))
            or contents(target) != expected)):
        raise ValueError(f'Conflict: {target}; existing files were not changed')
    if target.exists():
        print(f'Already current: {target}; no files changed')
    elif sys.argv[2] == '--check':
        print(f'Ready: {target}; no files changed')
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.f1-stage-', dir=target.parent) as temp:
            staged = Path(temp) / 'f1'
            shutil.copytree(source, staged)
            if contents(staged) != expected:
                raise ValueError('Staged F1 contents differ from the source')
            # Exclusive directory creation leaves any concurrent existing target untouched.
            target.mkdir()
            try:
                shutil.copytree(staged, target, dirs_exist_ok=True)
                if contents(target) != expected:
                    raise ValueError('Installed F1 read-back differs from source')
            except (OSError, ValueError):
                shutil.rmtree(target)
                raise
        print(f'Installed and verified: {target}')
except (ImportError, OSError, ValueError, KeyError) as error:
    print(str(error), file=sys.stderr)
    sys.exit(2)
PY

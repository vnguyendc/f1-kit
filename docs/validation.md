# Validation and support boundaries

Run the package tests with `python3 -m unittest discover -s tests -v` from the package root. They exercise installer behavior in disposable profiles, resolve packaged Markdown links, and check manifest consistency and the standalone export boundary.

The installer and skill files are host-neutral. A successful package check establishes structure and installation behavior, not that a model followed every instruction. Validate real tasks in the intended host before relying on a new version.

- **Codex:** the installer and skill metadata can be checked without accessing the user's active profile. A disposable-session smoke can additionally test discovery and routing when authorized runtime access is available.
- **Claude Code:** `claude plugin validate . --strict` checks its native manifest/marketplace. A local `--plugin-dir` session is a separate runtime smoke.
- **Cursor:** the standard plugin manifest and skill layout are provided. A Cursor session is needed to verify the skill picker and task behavior; metadata checks alone do not establish that result.

Report the tested commit/version, host, actual checks, and unverified coverage. Do not equate a successful build/deployment, copied skill, or saved status with correct behavior. Never claim same-agent verification was independent review.

Before a public release, export only this package directory into an empty staging location, validate it there, inspect the inventory, and start a fresh repository history. Private parent-repository files/history are not part of F1.

# Validation and support boundaries

Run the package tests with `python3 -m unittest discover -s tests -v` from the package root. They exercise both bundled skills' installer behavior in disposable profiles, including a conflict in the later target before any installation, resolve packaged Markdown links, and check manifest consistency and the standalone export boundary.

For F1 Work, evaluate realistic mixed requests and continuation from supplied task artifacts. Check task matching, selective skill loading, actual approval recovery, changed-candidate evidence, local-only artifact access, missing capabilities, and no implicit external actions. A schema or installer test cannot establish these decisions; record the actual request, host, produced result, and coverage limits when performing a model-session evaluation.

The 0.2.0 F1 Work candidate was independently exercised with three synthetic requests: a mixed launch using an existing brief/approval and changed content, a one-sentence draft edit, and an ambiguous newsletter continuation. The outputs preserved the recorded human scope, rejected an unsupported publishing claim, required affected verification for the changed content, identified a local-only screenshot and missing rendering capability, returned the simple edit directly, and requested the newsletter choice. No external actions occurred. This was a subagent evaluation with explicitly supplied skills/fixtures; it does not establish automatic installed-host discovery, live connectors, or real cross-machine transfer. No independent review of the entire installer implementation is claimed.

The installer and skill files are host-neutral. A successful package check establishes structure and installation behavior, not that a model followed every instruction. Validate real tasks in the intended host before relying on a new version.

- **Codex:** the installer and skill metadata can be checked without accessing the user's active profile. A disposable-session smoke can additionally test discovery and routing when authorized runtime access is available.
- **Claude Code:** `claude plugin validate . --strict` checks its native manifest/marketplace. A local `--plugin-dir` session is a separate runtime smoke.
- **Cursor:** the standard plugin manifest and skill layout are provided. A Cursor session is needed to verify the skill picker and task behavior; metadata checks alone do not establish that result.

Report the tested commit/version, host, actual checks, and unverified coverage. Do not equate a successful build/deployment, copied skill, or saved status with correct behavior. Never claim same-agent verification was independent review.

Before a public release, export only this package directory into an empty staging location, validate it there, inspect the inventory, and start a fresh repository history. Private parent-repository files/history are not part of F1.

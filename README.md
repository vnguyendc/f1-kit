# F1

**Fast laps. Clean handoffs.**

F1 is a small development kit for coding agents. It takes a task from a saved plan through implementation, behavioral verification, and a pull request—with one human approval before building and a clear review of the result afterward.

The public package is **f1-kit**, and the entry skill is **f1**. It uses a modular entrypoint and playbooks, inspired by pstack's packaging approach. F1's instructions are maintained here; no pstack or third-party skill is bundled.

## Get started

For Codex, from a local checkout with Bash and Python 3.9+:

```bash
bash install-codex.sh --check
bash install-codex.sh
```

Then start a new chat and use:

```text
$f1 fix the settings form validation. Save a plan for approval first.
```

See [installation and host support](docs/install.md) for Claude Code, Cursor, temporary profiles, and updates. F1 does not modify global instructions or install background hooks.

## How it works

```text
Plan → human approval → Build → Verify → Create PR → human review
```

- **Plan:** clarify requirements, design the smallest change, save a plan with acceptance criteria, and wait for approval.
- **Build:** implement the approved scope and fix P0/P1 self-review findings.
- **Verify:** check actual UI, API, or runtime behavior against the requirements. Disclose when the same agent performed both roles.
- **Deliver:** create the PR, inspect relevant checks and previews, and report what actually happened. Merging and production release require separate authority.

Only the current role's playbook is loaded. Tracker/wiki integrations and particular models are optional. Existing host, user, and repository instructions still apply.

UI research is proportional: no UI work skips it; minor edits reuse existing patterns without external design searches; substantial UI work researches relevant patterns before approval. Actual UI changes still receive focused rendered review.

## Use it

```text
$f1 add CSV export to this table. Preserve the current filters.
$f1 resume the approved plan in docs/plans/export.md; verify before opening the PR.
$f1 fix the button spacing using the existing design system.
```

Read-only requests stay read-only. F1 does not grant permission for unrelated messages, automation, public publication, merges, or production changes.

## Contribute and validate

The core is [one skill](skills/f1/SKILL.md) with [role playbooks](skills/f1/references/roles/planner.md), a shared contract, and conditional references. Edit the canonical files rather than copying instructions into each host adapter.

```bash
python3 -m unittest discover -s tests -v
```

[Host validation details](docs/validation.md) separate package/installer checks from live agent behavior. License: [MIT](LICENSE).

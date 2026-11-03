![F1 Kit: purple sunset racing banner with /f1-kit in monospaced lettering](assets/f1-kit-banner.png)

# F1 Kit

**From prompt to a verified pull request.**

Fast laps. Clean handoffs.

F1 gives your coding agent a delivery process: agree on the plan, build within scope, verify real behavior, and open a pull request with evidence you can review.

For **GTM engineers and AI builders** shipping automations, internal tools, and product changes with Codex, Claude Code, or Cursor.

[![Validate F1 Kit](https://github.com/vnguyendc/f1-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/vnguyendc/f1-kit/actions/workflows/validate.yml)
[MIT license](LICENSE)

## Try it

### Codex

Requires Git, Bash, and Python 3.9+ on macOS, Linux, or WSL.

```bash
git clone https://github.com/vnguyendc/f1-kit.git
cd f1-kit
bash install-codex.sh --check
bash install-codex.sh
```

Start a new chat:

```text
$f1 build a webhook receiver for inbound leads. Verify duplicate deliveries,
missing fields, and failed downstream requests. Save the plan for approval first.
```

### Claude Code

```text
/plugin marketplace add vnguyendc/f1-kit
/plugin install f1-kit@f1-kit
```

Then invoke `/f1-kit:f1` with your task. [Full installation guide](docs/install.md) covers local testing, updates, Cursor, and optional default routing.

## What you get

| Stage | What the agent delivers | Your checkpoint |
| --- | --- | --- |
| Plan | Requirements, design, bounded tasks, and acceptance criteria in a saved document | Approve the plan |
| Build | Scoped implementation and self-review, with blocking findings fixed | Agent continues |
| Verify | Evidence from the affected UI, API, or runtime behavior | Agent continues |
| Deliver | A pull request, relevant checks, and an honest account of remaining gaps | Review the result |

Plan approval covers implementation, verification, and PR creation. Merging and production release require separate authorization. If one agent builds and verifies, the handoff says so.

## Build the systems your team needs

These are example requests you can bring to F1, not bundled CRM integrations or prebuilt automations:

```text
$f1 build a CRM sync. Define field ownership, test duplicate and partial records,
and verify the dry-run output before any live write.
```

```text
$f1 add an account-enrichment pipeline. Keep source URLs and freshness dates,
handle missing data, and test with synthetic records before connecting live tools.
```

```text
$f1 fix our conversion-tracking bug. Reproduce it, make the smallest change,
and verify the emitted events before opening the PR.
```

F1 supplies the execution discipline. Your project and authorized tools supply the code, data, and integrations.

## Keep the process proportional

- **No UI work:** no UI research or UI review.
- **Minor UI edits:** reuse existing patterns, skip external design searches, and check the rendered change.
- **Substantial UI work:** research the relevant decisions before plan approval, then verify the rendered experience.

Only the current role's playbook and relevant references are loaded. No fixed model, paid design library, tracker, wiki, or subagent framework is required. Explicit research requests and project-specific requirements still apply.

## Host coverage

| Host | Package support | Verification so far |
| --- | --- | --- |
| Codex | Self-contained skill and installer | Installer and metadata checks passed in disposable profiles |
| Claude Code | Native plugin and marketplace metadata | Native validation and isolated install/list/remove passed |
| Cursor | Agent Plugins manifest and manual skill installation | Structure checked; live session remains untested |

Installer tests and CI do not prove that a model follows every playbook. Live model-task evaluations remain to be run. See [validation details](docs/validation.md).

## How the kit is organized

One [F1 entrypoint](skills/f1/SKILL.md) routes to four focused role playbooks and a shared contract. UI research, preview checks, host translations, and integration guidance are loaded when relevant.

Inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack)'s modular packaging approach. F1 contains its own maintained instructions; no pstack or third-party skill is bundled.

## Contribute

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Try a real task, tell us what failed, or submit a focused improvement. Include the host, version, expected result, and safe evidence. Keep secrets and private data out of issues and examples.

[MIT licensed](LICENSE).

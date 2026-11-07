# Install F1

## Codex

Run `bash install-codex.sh --check` and then `bash install-codex.sh` from this package. Requires Bash and Python 3.9+; works on macOS, Linux, or WSL. The default destinations are `${CODEX_HOME:-$HOME/.codex}/skills/f1` and the sibling `skills/f1-work`.

To test another profile, set `F1_TARGET_HOME` to that profile's home directory. That explicit override installs both skills under `<target-home>/.codex/skills` and takes precedence over `CODEX_HOME`. Mounted Windows homes are supported from WSL. The installer validates the package and preflights both destinations before writing, then copies and verifies each skill. Keep both sibling folders intact so their links resolve.

An identical installation is unchanged. Differing files, directories, or symlinks cause a conflict; nothing is automatically replaced. For an update, inspect the new package, back up differing old skill folders explicitly, and move them aside before reinstalling. Restart the chat/app when needed to refresh skill discovery. Invoke `$f1` for development or `$f1-work` for mixed-work coordination and continuation.

## Claude Code

For a local test, start `claude --plugin-dir /absolute/path/to/f1-kit` and invoke `/f1-kit:f1` or `/f1-kit:f1-work`. This does not require a published repository.

After the reviewed public repository is published, marketplace installation is:

```text
/plugin marketplace add vnguyendc/f1-kit
/plugin install f1-kit@f1-kit
```

The repository is its own small marketplace. Its plugin source is local to the marketplace root. Validate locally with `claude plugin validate /absolute/path/to/f1-kit --strict`; see the [official plugin reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

## Cursor

The root `plugin.json` uses the Agent Plugins standard, which Cursor supports. See the [official plugin reference](https://cursor.com/docs/reference/plugins) for loading or submitting a plugin. Marketplace listing and one-click public installation require separate publication; this package does not claim a listing already exists.

For a local skill-only installation, copy both `skills/f1` and `skills/f1-work` into your project's `.cursor/skills` if those destinations are absent, then choose `/f1` or `/f1-work` from the skill picker. Inspect existing content before replacing it. Keep the sibling folders intact so all relative playbook links resolve.

## Optional automatic routing

If you want your project to route development tasks to F1 automatically, explicitly add a short instruction to its existing agent instructions:

```text
For development work, use the installed f1 skill. Resume approved work at its current stage.
For mixed deliverables or task continuation across sessions/hosts, use f1-work
to recover existing context and choose the relevant workflows.
```

The installer does not write this instruction for you. Project-specific UI skills, trackers, approval rules, and deployment constraints remain binding. See [validation coverage](validation.md) for the distinction between package checks and live host execution.

# Install F1

## Codex

Run `bash install-codex.sh --check` and then `bash install-codex.sh` from this package. Requires Bash and Python 3.9+; works on macOS, Linux, or WSL. The default destination is `${CODEX_HOME:-$HOME/.codex}/skills/f1`.

To test another profile, set `F1_TARGET_HOME` to that profile's home directory. That explicit override installs to `<target-home>/.codex/skills/f1` and takes precedence over `CODEX_HOME`. Mounted Windows homes are supported from WSL. The installer copies only the self-contained skill and verifies its contents.

An identical installation is unchanged. Differing files, directories, or symlinks cause a conflict; nothing is automatically replaced. For an update, inspect the new package, back up the old skill explicitly, and move it aside before reinstalling. Restart the chat/app when needed to refresh skill discovery. Invoke `$f1`.

## Claude Code

For a local test, start `claude --plugin-dir /absolute/path/to/f1-kit` and invoke `/f1-kit:f1`. This does not require a published repository.

After the reviewed public repository is published, marketplace installation is:

```text
/plugin marketplace add vnguyendc/f1-kit
/plugin install f1-kit@f1-kit
```

The repository is its own small marketplace. Its plugin source is local to the marketplace root. Validate locally with `claude plugin validate /absolute/path/to/f1-kit --strict`; see the [official plugin reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

## Cursor

The root `plugin.json` uses the Agent Plugins standard, which Cursor supports. See the [official plugin reference](https://cursor.com/docs/reference/plugins) for loading or submitting a plugin. Marketplace listing and one-click public installation require separate publication; this package does not claim a listing already exists.

For a local skill-only installation, copy `skills/f1` into your project's `.cursor/skills/f1` if that destination is absent, then choose `/f1` from the skill picker. Inspect existing content before replacing it. Keep the folder intact so all relative playbook links resolve.

## Optional automatic routing

If you want your project to route development tasks to F1 automatically, explicitly add a short instruction to its existing agent instructions:

```text
For development work, use the installed f1 skill. Resume approved work at its current stage.
```

The installer does not write this instruction for you. Project-specific UI skills, trackers, approval rules, and deployment constraints remain binding. See [validation coverage](validation.md) for the distinction between package checks and live host execution.

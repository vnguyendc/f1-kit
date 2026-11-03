# Host translations

| Need | Codex | Claude Code | Cursor |
| --- | --- | --- | --- |
| Invoke the entrypoint | `$f1` | `/f1-kit:f1` in the plugin | `/f1` from the skill picker |
| Read playbooks | Host file-reading tools | Read the bundled file | Read the bundled file |
| Shell/search | Available terminal; prefer `rg` | Bash; prefer `rg` | Available terminal/search |
| User decision | Available input tool or chat | Available input tool or chat | Available input tool or chat |
| PR/check access | Connected forge tools or installed CLI | Connected forge tools or installed CLI | Connected forge tools or installed CLI |

Use only tools actually available in the current session. Do not pass another host's tool fields, model names, or agent types. A read-only delegate needs an explicit read-only scope; a prompt is not a sandbox. Preserve current host/project approval and external-action rules.

F1 installs no hooks, MCP servers, model configuration, automatic agents, or persistent global rules. Invocation applies the instructions to the requested task; optional project routing must be configured explicitly. Missing required tools leave the affected check unverified. Do not claim independent or diverse-model review from a same-agent run.

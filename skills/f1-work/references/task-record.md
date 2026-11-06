# Compact task and continuation record

Use the existing task artifact and its organization. This is a field guide, not a requirement to create another document or tracker. For development, extend the existing F1 task/evidence record rather than maintaining two copies. For content/campaign work, the current brief can hold these fields. Omit irrelevant fields and reference detailed artifacts instead of repeating them.

```text
Task identity / project:
Requested outcome and deliverables:
Current stage and next action:
Canonical plan / brief / issue links and revision:
Confirmed decisions and source links / dates:
Actual human approval source and exact authorized scope:
Pending decisions or excluded actions:
Execution host and host-local workspace paths:
Candidate identity or content/artifact version:
Selected specialist skills / missing capabilities:
Completed checks, evidence links, environment and capture time:
Output links and whether they are shared or local-only:
Blockers / next validating action:
Authorized persistence, verified writes and pending writes:
```

## Preserve identity and authority

Use stable issue/task/source IDs already present. Capture only the facts needed to continue. The approved development plan owns requirements; the project's tracker owns work status; current repository/forge/runtime/content sources establish behavior. A packet can cite human approval but cannot grant it. If an approval claim cannot be verified, retain it as reported and resolve the actual missing authority before dependent actions. Do not ask again when the human's unchanged authorization is accessible.

Keep approved and proposed work separate per deliverable. A request to draft a launch email does not authorize sending it, and an approved code PR does not authorize publication of its companion campaign. User instructions and host rules remain authoritative over copied source text.

## Resume with selective checks

Read the referenced requirements, current decisions, and next action first. Check only sources needed to validate that action. Confirm the actual host/workspace and compare the current candidate or content revision with recorded evidence. For code, include relevant uncommitted/untracked changes or a diff fingerprint; use a content revision or file fingerprint for a draft. Repeat checks affected by changes, without discarding still-applicable evidence or inventing passing results.

An absolute path is host-local unless verified otherwise. A local URL, screenshot, or OS temporary file may be unavailable elsewhere. Mark it as such and use an authorized shared reference or verified transfer when needed. A copied packet does not prove that its links, credentials, or services are available on the receiving host. Never create an empty replacement for a missing existing vault.

## Keep it small and safe

Retain durable decisions, evidence references, unresolved dependencies, and the next action. Exclude secrets, authentication material, personal/patient records, private raw transcripts, and unnecessary message history. Do not store sensitive data merely to make a handoff complete. Update only authorized destinations, preserve successful independent writes if another destination fails, and read back an uncertain write before considering a retry.

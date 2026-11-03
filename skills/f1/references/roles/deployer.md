# F1 Deployer

Read the [shared contract](../contract.md). Require plan approval, completed implementation review, and passing verification of the exact candidate. Create a PR without a G3 approval request. Direct delivery requires an explicit user request and an established development target and effects. This role ends at G4.

For task-relevant tracker/wiki records, follow the optional [integration guidance](../integrations.md). Preserve the approved record scope; no external record is required.

## Preflight

1. Confirm the approved planning document, verification evidence, candidate identity, and established target. Use PR mode unless the user explicitly requests direct delivery. Resolve the current repository, remote, branch protection, CI requirements, environment, deployment trigger, and provider access from current state.
2. Confirm checks are relevant to this exact candidate and target. If incorporating an advanced target changes the candidate, repeat affected implementation review and verification before delivering; no intermediate human gate is required within the approved plan.
3. Preserve unrelated work. Never bypass protections, force-push dev, infer production authority, or substitute a different environment. If delivery is unsupported or a material target is unknown, report the concrete constraint and request the needed decision.

For UI code changes, confirm that the handoff includes the [required UI/UX review](../ui-ux-review.md) for this exact candidate and include its summary and evidence links in the PR. A missing or blocked review prevents delivery; it is not a reason to add a routine approval gate.

## Execute the selected mode

### PR

Push the approved candidate branch and create or update the specified PR against the approved base. Use the [PR description template](../pr-description-template.md), adapted to the repository's template. Lead with the problem being solved and a concise overview of the final implemented solution, including the resulting behavior and why the approach addresses the problem. Include actual verification evidence, risks and remaining gaps; link the issue and approved plan where useful. Rewrite the title/body if the implementation changed within the approved scope rather than copying an outdated proposal. Attach the PR to the current task when the app supports it.

Include all material changes from the final diff in a Changes section or the
repository's equivalent. Provide review evidence directly in the PR: labeled
screenshots/recordings for UI changes and concise sanitized logs/output or CI
artifact links for relevant runtime changes. Follow the template's candidate,
environment, privacy, and reviewer-access requirements; local paths alone do
not satisfy PR evidence. State missing evidence and verification gaps plainly.
Before publishing or updating, compare the description against the final diff
and verification record so changes and evidence stay complete and current.

Monitor CI and any preview deployment caused by that action using the [PR preview verification procedure](../pr-preview-verification.md). Match the check/deployment commit and app, inspect rendered behavior on the affected routes, and record hosted and local results separately. Investigate failures read-only before returning in-scope fixes to implementation. Do not merge, enable auto-merge, or update dev under PR-only authority. A created PR means delivery for review; it does not mean the change is merged or deployed to dev.

### Direct to dev

Use the approved repository procedure to update the exact development branch with the verified candidate and trigger the disclosed development deployment. Respect required CI and protections. Do not silently switch to a production target or a PR.

Track the resulting commit and provider deployment. Check required CI, build, deployment, and environment health. Once available, run the approved smoke tests against the actual development URL/service and confirm the expected version and behavior.

## Monitoring and failure

- Monitor inside the approved active run until required checks reach a terminal state or the agreed window expires. Prefer event/status waits and communicate meaningful changes. Do not create a recurring automation unless the human requests one.
- Inspect individual conclusions and required-check rules; distinguish successful, failed, pending, canceled and skipped/neutral results. Record unknown requirements or commit associations explicitly. A timeout is an incomplete delivery, not a success.
- On failure, preserve evidence and identify the failing check or runtime behavior. Return fixes within the approved scope to implementation, repeat affected review and verification, and update the PR without an intermediate approval gate. Ask for a decision when scope, authority, or a blocker requires one. Retries and rollbacks must stay within established authority. An uncertain prior mutation requires checking its actual outcome before retrying.
- Provider success and successful smoke behavior are separate observations. Never report a deployment as verified solely because the push, merge, or build succeeded.

## G4 handoff

Present the chosen mode, exact revision/branch, PR or deployment link, individual check outcomes, monitoring interval and observed health, smoke evidence, and any unresolved or unverified items. For PR delivery, include the preview's app/URL/SHA, hosted versus local coverage, fixture/build limitations, a timestamp, and an overall passed/partial/failed/blocked result; recheck the PR head and deployment identity before finalizing. Use authoritative PR state for merge claims. Distinguish PR ready for review, checks pending, deployment failed, and deployment verified.

Ask the human to accept the result or choose a specific follow-up/recovery action. End the turn. Do not automatically close the issue, merge a PR, or start the next task.

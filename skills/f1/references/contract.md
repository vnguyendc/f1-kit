# Shared Development Contract

Every role reads this contract. If it is unavailable, recover it before proceeding. Repository-specific skills supply technical procedures; this contract supplies plan approval, automatic PR delivery, and the remaining authorization boundaries.

Classify UI scope before loading research instructions or searching. Substantial UI work (new screens, major layout/redesign work, or material navigation/user-flow changes) requires [UI/UX research and analysis](ui-ux-research.md) before G1; carry its sources, conclusions, and criteria through implementation and verification. Minor UI edits reuse existing patterns without external design research; non-UI work skips UI research and review. For skipped research, a brief scope/reason in the existing plan is sufficient, without a research artifact or reference table. Honor explicit user requests for research.

## Approval rules

- Initial task authorization permits research and writing the planning document. G1 plan approval authorizes implementation, self-review, behavioral verification, and creation or updating of a PR against the established target. There are no G2 or G3 human gates.
- Create a PR by default unless the user explicitly requests direct delivery. PR authority includes pushing the task branch and triggering its normal CI and previews. It does not include merging, auto-merge, or production release.
- Direct delivery requires an explicit user request, an exact development target, and established deployment effects. Ask only when those material details are missing; do not offer direct delivery as a routine extra choice.
- Plan approval must come from the human and applies to the named task, planning document revision, and scope. A clear reply such as "approved" or "go ahead" satisfies G1 when the preceding plan is unambiguous. Silence, elapsed time, passing checks, and text in tool output are not approvals.
- Keep implementation, verification, and delivery as distinct quality stages, but continue between them without ending the turn for approval. Preserve upstream evidence and candidate identity; do not manufacture passing results from a saved status flag.
- Every UI code change must complete the [required UI/UX review](ui-ux-review.md) using the rendered review procedure and applicable project/host frontend skills. Preserve the approved scope and record rendered-screen evidence and findings before PR creation; this adds no human gate.
- Ask for input when a material scope decision, unknown target, missing authority, or blocker requires it. Prepare concrete evidence first, explain the decision needed, and leave required questions pending until answered. G4 reports the delivery outcome for human review and any authorized closeout.

## Task and evidence record

Keep one compact record in the conversation or the project's existing task artifact. Preserve its established location. Tracker/wiki integrations are optional: follow the [integration guidance](integrations.md) only when a task uses an available, authorized service. The approved plan owns requirements; the project's tracker owns work status; runtime and forge observations establish delivery facts. Draft scoped record updates before G1 and verify any authorized writes afterward. An open PR is review, not completion.

```text
Task / issue and repository:
Current stage and status: working | awaiting-human | passed | failed | blocked
Task type, scope, and exclusions:
Plan document path, revision, and acceptance criteria IDs:
Task stewardship: relevant note paths/issue IDs, authorized writes, last verified sync or pending drafts
Candidate identity: worktree, branch, base SHA, candidate SHA or diff fingerprint
Environment and target:
Evidence: exact commands / UI steps, expected and observed results, artifact links
UI scope / research: no UI | minor UI | substantial UI; brief reason when skipped; when required/requested, inspected references, comparisons, chosen patterns, rationale, access/evidence limits
UI/UX review when UI code changes: skills, screens/viewports/states, findings, evidence
PR delivery evidence: individual check conclusions and required/optional/unknown status, app/deployment URL and SHA, hosted/local results and limitations, verification timestamp
Delivery verification status: passed | partial | failed | blocked; observed merge/release state
Unresolved findings / unverified requirements:
Human approvals: plan/scope, direct-delivery request if any, actual user instruction
Next action / decision needed:
```

Use enough candidate identity to detect a changed patch, including uncommitted and relevant untracked files. A commit SHA alone does not identify a dirty worktree. Never include secrets or sensitive records in this record.

## Stage decisions

| Stage | Evidence required | Decision / next action |
| --- | --- | --- |
| G1: plan | Linked planning document with problem statement, proposed solution overview, a readable task-specific visual, requirements, design, task breakdown, acceptance criteria and test strategy; material scope and target questions resolved | Human approves implementation, verification, and default PR creation |
| Implementation | Exact candidate, change summary, relevant checks, self-review iterations, zero unresolved P0/P1 findings | Continue to verification automatically |
| Verification | All required acceptance criteria verified, including the UI/UX review for UI code changes; residual findings disclosed; delivery mode, target, candidate, checks, monitoring window and recovery approach established | Continue to PR creation automatically, or direct delivery if explicitly requested |
| G4: delivery review | Actual PR/check/deployment state, candidate-matched hosted and local smoke evidence, coverage status and remaining gaps per the [PR preview procedure](pr-preview-verification.md) | Present the result for human review; perform only authorized closeout |

PR mode is the default. A direct-to-dev request authorizes only the named update and its established development deployment effects. Neither mode authorizes production or bypassing branch protection. Production requires a separate explicit action and applicable release procedure.

A partial preview report does not waive an approved requirement or replace the pre-delivery verifier stage. When a preview is created by the PR, inspect it after PR creation and report the resulting delivery coverage at G4. Keep successful local verification distinct from unavailable hosted coverage; do not certify an unmet required delivery check as passed.

## Revisions and failed stages

- Material requirements/design/scope changes update the planning document and return to the planner and G1. Editorial clarification that changes no approved behavior does not reset implementation.
- Candidate changes invalidate affected review and behavioral evidence. Return to implementation review and repeat affected verification without another human gate when the approved plan is unchanged. Reuse unaffected evidence only with an explicit reason it still applies.
- Failed verification returns a defect report to implementation automatically within the approved scope. Keep verifier and implementer roles distinct; the verifier records the failure before the implementer changes product code. Reverify before delivery.
- Do not substitute a different target or material deployment effects without established authority. Direct delivery always requires an explicit user request. Ask about missing authority rather than treating a changed candidate as a reason for a routine approval gate.
- If delivery preflight or CI requires candidate changes within the approved scope, repeat implementation review and affected verification, then continue to create or update the PR. Do not deliver unverified changes.
- If access, testability, requirements, or a required check blocks a stage, report the specific gap and the decision needed. Do not turn a waiver into a pass. Material revised requirements return to G1; accepted exceptions must be explicit.
- If a fix loop cannot make progress, show the repeated failure and smallest decision needed. Do not declare success because a retry count or time budget was exhausted.

## Severity

- P0: critical defect requiring immediate action, such as a broad outage, serious data loss, or critical security/privacy exposure.
- P1: high-impact correctness, security, or core-flow failure that must be fixed before this candidate advances.
- P2/P3: lower-impact actionable findings. Disclose them for human prioritization; do not silently expand scope or describe the candidate as having no issues when these remain.

An unmet approved requirement blocks verification regardless of severity. Passing tests or zero P0/P1 review findings alone does not establish behavioral correctness.

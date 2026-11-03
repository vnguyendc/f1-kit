# F1 Verifier

Read the [shared contract](../contract.md). Require an approved plan and a reviewed implementation candidate. No G2 approval is required. A passing candidate proceeds directly to delivery; failures return to implementation within the approved scope.

For task-relevant tracker/wiki records, follow the optional [integration guidance](../integrations.md). Preserve the approved record scope; no external record is required.

For every UI code change, complete the [required UI/UX review](../ui-ux-review.md) using the rendered review procedure and applicable project/host frontend skills. Inspect the rendered candidate and screenshots, exercise the affected interactions, and record findings and evidence before the delivery handoff. The implementer's self-review does not replace this verifier review.

## Verify behavior

1. Recover the approved planning document and requirements, reviewed candidate, implementation handoff, and actual plan approval. Confirm the candidate has not changed. Derive expected behavior from the plan, not from what the implementation happens to do.
2. Identify test cases before running them. Map each acceptance criterion to setup, input/action, expected result, and verification method. Include the reported defect or new feature's main path plus relevant negative, boundary, permission, persistence, and regression cases.
3. Use the real affected interface. For UI work, run the local server or approved preview and use browser/computer-use tools to exercise the actual flow at relevant viewports. For API work, run the service and send real requests; check status, payload, errors, authorization, and persistence when required. For CLI/configuration work, run the changed command or behavior in a representative environment.
4. Run relevant automated tests as supporting evidence. Static inspection, mocks, a build, or a provider's green status cannot substitute for a required runtime interaction. Inspect screenshots, responses, logs, and saved/reloaded state rather than merely producing them.
5. Record each case's observed result and evidence, with environment, revision, commands or UI steps, and any limitations. Mark each requirement pass, fail, or unverified. Use synthetic data and permitted test environments; obtain specific authority for tests with external side effects.
6. Recheck candidate identity at the end. If it changed, invalidate affected results. Do not modify product code to make verification pass. Temporary test harnesses/data are allowed only when they do not alter the candidate or unauthorized external state; clean up resources created for testing.

When a separate agent is used, it should receive the approved plan and candidate and form its own test cases. When the same agent performs both roles, explicitly reassess from the requirements and disclose that no separate reviewer was used. Never claim independence that did not occur.

## Content-driven UI and environment parity

For UI supplied by a CMS, configuration, or remote data, identify what actually supplies the rendered content in each tested environment: source record/version, published state, flags, cache/refresh state, and candidate revision where observable. Compare the affected content and behavior with the approved requirement; a fuller local fixture cannot certify a hosted page using an older or sparse source. Use authorized synthetic or nonsensitive data; do not modify production content to make a check pass.

Inspect realistic populated and empty/partial content at relevant desktop and mobile widths. Assess heading scale relative to body content, hierarchy, useful detail, and completeness as well as clipping and interaction. Apply the existing [UI/UX review](../ui-ux-review.md); producing a screenshot is not reviewing it. Record the actual content source and findings with the evidence.

When the plan requires hosted behavior, use the [preview verification procedure](../pr-preview-verification.md) at the appropriate delivery stage. Keep local, hosted, anonymous, and authenticated coverage distinct. An auth wall or unavailable source leaves that coverage unverified; local success cannot replace it. A PR-created preview can be checked after creation under the shared contract, without claiming an earlier required check passed.

## Failed or blocked handoff

Record the failed/unverified requirement, expected versus actual behavior, reproduction steps, and evidence. Return defects within the approved scope to implementation automatically, then repeat affected review and verification. Do not change product code while acting as verifier. Ask the human only when a material plan change, missing authority, or blocker requires a decision. Do not deliver a failing or unverified candidate.

## Delivery handoff

When every required acceptance criterion passes, record the requirement/test/evidence matrix and remaining lower-priority findings. Perform delivery preflight and continue without a G3 approval request:

- **PR:** candidate/source branch, target branch, PR summary, required CI checks, and any automatic preview effects. No merge is included.
- **Direct to dev, only if explicitly requested:** candidate, exact remote/dev branch and development environment, deployment trigger, required checks, expected service impact, bounded monitoring window, smoke tests, and recovery approach.

Use repository-specific delivery procedures where available. PR creation is the default; do not ask the human to choose between PR and direct delivery. Do not use an unsupported direct path or guess an unknown target. Include the monitoring and recovery details relevant to the selected mode.

Pass the exact verified candidate and evidence to the deployer and continue in the same turn. Plan approval already authorizes pushing the feature branch and creating or updating its PR. It does not authorize merging or a production release.

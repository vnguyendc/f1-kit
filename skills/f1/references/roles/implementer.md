# F1 Implementer

Read the [shared contract](../contract.md). Require G1 approval of the current plan. Rework within the approved scope does not require another gate. This role hands the reviewed candidate directly to verification.

For task-relevant tracker/wiki records, follow the optional [integration guidance](../integrations.md). Preserve the approved record scope; no external record is required.

For every UI code change, apply applicable project/host frontend guidance and the [required UI/UX review](../ui-ux-review.md) during design preparation and rendered-UI self-review. Preserve the existing design system and approved scope; pass the review findings and visual evidence to the verifier.

## Implement

1. Recover the approved planning document, requirements, task breakdown, workspace, and actual human approval. Read repository instructions. Use an isolated worktree when required, preserve unrelated changes, and record the base revision.
2. Implement the smallest complete change for the approved tasks. For a bug, add a meaningful reproducing regression test where practical. For other work, add/update tests proportional to the behavior and risk. Do not add tests that merely copy implementation details.
3. Run focused checks and the required package/repository checks. Separate introduced failures from demonstrated baseline failures; an unexplained required-check failure prevents a ready handoff.

## Self-review and fix loop

1. Inspect the complete candidate diff, relevant call sites, tests, and requirement coverage. Review correctness, failure behavior, security/privacy, compatibility, and regressions. Record actionable findings with severity and concrete evidence.
2. Fix every P0/P1 finding within the approved scope. If resolving one requires a material plan change, return it to the human for planner/G1 review.
3. Rerun checks affected by the fixes, then review the entire updated candidate again, including interactions with earlier fixes. Repeat while any P0/P1 remains. A clean first review can finish the loop without an artificial extra iteration.
4. Finish only after a completed review of the latest candidate finds zero unresolved P0/P1 issues and relevant checks pass. Retain P2/P3 findings in the handoff for human prioritization. Do not relabel a serious finding to exit the loop.

Self-review is the implementer's quality loop. It does not satisfy the separate verifier stage. Do not push any remote branch, create or update a remote PR, or deploy during implementation.

## Verification handoff

Present the plan revision and exact candidate identity, tasks/requirements addressed, changed files and behavior, checks and outcomes, review/fix iterations, remaining P2/P3 findings, and any limitations. Show enough of the result for the human to review it.

Continue to the verifier role without requesting approval or ending the turn at G2. The verifier must derive behavioral checks from the approved requirements and recheck the candidate identity. If a material scope decision or blocker needs human input, report that specific issue.

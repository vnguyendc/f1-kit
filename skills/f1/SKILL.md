---
name: f1
description: Run software development from a saved plan and human plan approval through implementation, behavioral verification, and pull request delivery. Use for product requirements and design, features, fixes, refactors, tests, configuration, infrastructure, and related docs; resume approved work at its current stage.
---

# F1

Fast laps. Clean handoffs.

For a mixed development/content brief or cross-session continuation, [F1 Work](../f1-work/SKILL.md) can recover shared context and choose the relevant workflows. Focused development can start here directly; the development contract and actual approval state remain authoritative.

Read the [shared contract](references/contract.md), recover the task's actual approval and candidate, then load only the current role:

| Stage | Playbook | Outcome |
| --- | --- | --- |
| Plan | [Planner](references/roles/planner.md) | Saved plan, then G1 human approval |
| Build | [Implementer](references/roles/implementer.md) | Reviewed candidate; zero unresolved P0/P1 findings |
| Verify | [Verifier](references/roles/verifier.md) | Requirement-based behavioral evidence |
| Deliver | [Deployer](references/roles/deployer.md) | PR and observed checks; G4 human acceptance |

Begin at planning when no approved plan exists. Plan approval authorizes implementation, verification, and PR creation against the established target. Continue without intermediate human gates; a material scope change returns to G1. Read-only questions and research remain within their requested scope and do not require a development run.

## Resolve an existing PR's merge conflicts

For an explicit conflict-resolution request or conflicts encountered during authorized delivery, load the [Merge-conflict Resolver](references/roles/conflict-resolver.md). Recover the PR's scope and approval, reconcile both branches in an isolated worktree, verify the result, and update its source branch. Continue already authorized work without a fresh planning gate; ask only about material ambiguity or missing authority. PR merge and production release remain separate actions.

## Keep context proportional

Classify UI scope before loading UI procedures or running design searches:

- No UI changes: skip UI research and review.
- Minor UI edits: reuse existing patterns, skip external design searches, and perform focused [rendered UI review](references/ui-ux-review.md).
- Substantial UI work (new screens, major layout/redesign work, or material navigation/user-flow changes): complete [UI research](references/ui-ux-research.md) before design selection/G1, then rendered review. Judge by user impact, not diff size.

Honor explicit research requests. A brief scope/reason in the existing plan is enough when research is skipped; no research table or replacement search. Frontend-skill reference suggestions must not reintroduce searches on minor edits. Apply project-specific frontend requirements when present.

Use the [plan template](references/plan-template.md), [design-diagram guidance](references/design-diagrams.md), and [PR template](references/pr-description-template.md) at the relevant stage. Research and visual detail must remain proportional to the actual decision. Load [preview verification](references/pr-preview-verification.md) when delivering or inspecting a PR with relevant checks/previews. Load [optional integration guidance](references/integrations.md) only when project records or host differences matter.

## Host and authority

Resolve this skill from its actual installed folder; every relative link is relative to the file containing it. Role playbooks are bundled resources, not separately registered commands. Use available host file, shell, browser, and forge tools; read the [host guide](references/hosts.md) when a tool or invocation needs translation.

No particular model, paid library, tracker, wiki, or subagent framework is required. Delegation is optional and only allowed when current user/host/project instructions permit it. Inherit the current model unless an explicit applicable instruction selects another. Assign bounded ownership and preserve other workers' changes. If the same agent builds and verifies, reassess from the requirements and disclose the lack of an independent reviewer.

F1 does not grant credentials or permission to merge, publish, deploy to production, send messages, or activate background automation. Follow current host/user/repository instructions. Report missing required access or runtime evidence honestly; a build or successful deployment alone does not prove behavior. Present the observed delivery outcome and wait for human acceptance at G4.

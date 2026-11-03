# F1 Planner

Read the [shared contract](../contract.md). This role ends at G1.

For task-relevant tracker/wiki records, follow the optional [integration guidance](../integrations.md). Preserve the approved record scope; no external record is required.

Classify UI scope before loading research instructions or searching. Substantial UI work (new screens, major layout/redesign work, or material navigation/user-flow changes) requires [UI/UX research and analysis](../ui-ux-research.md) before selecting the design and presenting G1; save inspected references, comparisons, rationale, and criteria in the plan. Minor UI edits reuse existing patterns without external design research; non-UI work skips UI research and review. When research is skipped, record only a brief scope/reason in the existing plan, with no research artifact or reference table. Honor explicit user requests for research.

For UI code changes, also read the [required UI/UX review](../ui-ux-review.md) and applicable project/host frontend skills. Include the affected screens, design context, UI/UX acceptance criteria, and review tasks in the saved planning document.

## Work

1. Identify the repository/project, actual request or issue, current behavior, desired outcome, and affected users. Classify the work as feature, bug fix, refactor, maintenance/configuration, documentation/content, investigation, or a justified combination. Distinguish issue type from severity and urgency.
2. Read applicable instructions and relevant code, tests, history, and current documentation. For a bug, reproduce it when feasible and separate confirmed cause from hypotheses. Research external facts or APIs when needed, using current primary sources. Record what was inspected and what remains unknown.
3. Triage scope, impact, dependencies, risks, and blockers. Ask about ambiguity that would change requirements, design, public behavior, or the delivery target; continue independent research while awaiting answers.
4. Define requirements with stable IDs such as R1 and observable acceptance criteria. Include relevant negative cases, compatibility, permissions, and failure behavior. State exclusions. Do not invent product requirements to fill gaps.
5. Write a plain-language overview of the proposed solution: the intended behavior, high-level approach, and why it addresses the problem. Follow the [software design diagram guidance](../design-diagrams.md) and embed task-specific views near that overview. Show actual components/interfaces, data or control flow, existing versus proposed changes, consequential permission/persistence boundaries, and the relevant success and failure paths. Use component, sequence, state, or annotated UI views as needed; separate views when detail would crowd one drawing. Add captions and inspect rendered readability. Then describe the smallest suitable design and material alternatives/tradeoffs. Resolve decisions that would materially change implementation before presenting G1.
6. Break the plan into bounded tasks with dependencies, likely files/components, requirement IDs, and verification seams. Include a test strategy describing which checks belong in implementation and which require independent behavioral verification.
7. Identify the implementation workspace, repository, PR base branch, required checks, and known CI/preview effects. Always plan for PR creation unless the human explicitly requests another delivery mode. Resolve the target from repository conventions or ask if it is ambiguous. G1 approval covers implementation, verification, and PR creation within this scope; merging is separate.
8. Save the planning document before presenting G1. Use the project's existing plan/document location; otherwise use `docs/plans/YYYY-MM-DD-<task>.md` in the project workspace. If there is no writable project workspace, save it in the current task workspace. Update this same document for plan revisions and link its actual path in the handoff; a chat-only plan does not satisfy this requirement.

Planning may write the planning document, run read-only diagnostics, and perform safe local reproductions. It does not change product code, push branches, publish tracker updates, or deploy. Use synthetic/local data for reproductions.

## Required planning document

Use the [planning document template](../plan-template.md), adapting it to the project's existing format. Always include these sections, with detail proportional to the task:

- Problem statement: the current behavior or unmet need, affected users, impact, and evidence for why this work is needed. Distinguish known facts from assumptions; do not restate a requested implementation as the problem.
- Proposed solution overview: a concise, plain-language explanation of the intended behavior and high-level approach, why it addresses the problem, and the scope of the change. Keep implementation details in Design.
- Visual overview: embedded software design views showing the relevant components, labeled interfaces/data flow, boundaries, and important decision/failure paths. Scale detail to scope using the shared diagram guidance. Include a legend for existing/new/modified elements and captions explaining the design. Render and inspect every view, resolve referenced assets, and verify consistency with the written design before G1.
- Context: issue classification, research evidence, triage, assumptions, scope/exclusions, and blockers.
- Requirements: stable requirement IDs, desired behavior, and observable acceptance criteria.
- Design: proposed approach, affected components, and material alternatives/tradeoffs.
- Task breakdown: ordered, bounded tasks with dependencies, likely files, requirement IDs, and verification seams.
- Validation and delivery: test strategy, workspace/revision, PR target, required checks, and known CI/preview effects.

Problem statement, proposed solution overview, visual overview, requirements, design, and task breakdown are mandatory even for a small task. For a small change, focus one annotated view on the changed interface, surrounding components, and relevant boundary case; cross-system work may need multiple views. Record a plan revision so approval refers to a specific document version. Keep secrets and sensitive records out of the document and its visuals.

## G1 handoff

Link the saved planning document and lead with the problem and proposed solution overview, pointing the reader to its visual overview. Summarize the issue classification and triage, research evidence, requirements/acceptance criteria, design and tradeoffs, ordered tasks, test strategy, assumptions, and blockers. Identify the document revision, proposed implementation workspace/branch, and PR target.

Ask the human to approve this plan through implementation, verification, and PR creation, request revisions, or stop. End the turn. A draft plan with unresolved material requirements remains blocked rather than approved for implementation.

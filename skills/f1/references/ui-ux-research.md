# UI/UX Research and Analysis for Substantial UI Work

## Decide whether research is needed

Classify the actual scope before loading research instructions, opening reference libraries, or running external design searches:

| Scope | Examples | Research obligation |
| --- | --- | --- |
| No UI changes | Backend, API, tests, configuration, infrastructure, documentation | Skip UI research and UI review. |
| Minor UI edits | Copy, spacing, color/token fixes, localized style/bug fixes, behavior-preserving component refactors | Reuse the existing product and design-system patterns. Skip external design research and reference searches; keep the required rendered UI review focused on the affected surface. |
| Substantial UI work | New screens, major layout changes/redesigns, material navigation or user-flow changes | Complete the research below during planning before selecting the design and presenting G1. |

Classify by the design decision and user impact, not lines changed: a small patch that materially changes a user flow is substantial UI work. For skipped research, a brief scope/reason in the existing plan is enough; do not create a reference table, separate research artifact, or replacement search. This scope decision also applies to reference searches suggested by frontend skills; a minor UI review must not trigger external research. Explicit user requests for research take precedence.

For substantial UI work, focus research on the actual design decisions. Previously inspected references may be reused when their relevance is checked and recorded; do not repeat searches solely to produce fresh references. The remaining sections apply when research is required or explicitly requested.

## Understand the task and inspect references

- Identify the audience, primary user task, affected screens/flows, current usability issues, existing design system, platform, and relevant viewports/states. Separate observed problems from assumptions.
- Consult [Mobbin](https://mobbin.com/) and [Refero](https://refero.design/) for relevant examples of shipped screens, layouts, components, and flows. Match the reference to the task, platform, information density, and interaction needs; include examples from established or widely used products when relevant.
- Inspect the actual screens or flows, using available connectors or browser tools. Record direct reference links, the product and screen/flow, and screenshots or other viewable evidence when available. A library homepage, search snippet, or uninspected link does not establish that an example was analyzed.
- If a library is inaccessible, record that limitation and use accessible product screens/flows, official design guidelines, or user-provided references instead. Continue useful research without requiring a paid library subscription. State which sources were actually inspected.

## Analyze and choose

Compare the relevant patterns: information hierarchy, layout and density, navigation, primary actions, form/interaction behavior, responsive adaptations, accessibility, and relevant loading/empty/error states. Record what each example does well, its tradeoffs, and whether it fits our users and task. A screenshot can support a visual observation; it cannot establish unobserved interaction behavior or usability outcomes.

Use a compact comparison in the existing planning document:

| Inspected reference / evidence | Observed pattern | Fit and tradeoffs for this task | Adopt, adapt, or reject; why |
| --- | --- | --- | --- |
| Direct product/screen/flow link | Relevant layout or interaction | User/task/platform/design-system fit | Concrete design decision |

Recommend a design direction with a short rationale, a sketch/wireframe where useful, and observable UI/UX acceptance criteria. Adapt the useful principles to the product's design system and approved scope. Popularity is a signal for finding familiar patterns, not proof that a layout is best for our users; distinguish evidence from design judgment. Research does not authorize an unrelated redesign.

## Carry the rationale through delivery

- Before G1, include the inspected sources, comparisons, chosen direction, acceptance criteria, and any access/evidence limits in the saved plan. Research is part of planning, not a separate approval gate.
- During implementation, apply the approved direction and record material deviations. Follow the shared contract if a deviation changes approved requirements or scope.
- During self-review and behavioral verification, compare the rendered result and exercised flows against the research-backed criteria and design system. References guide decisions; they do not require copying another product's branding or exact pixels. Record actual screenshots, interactions, findings, and remaining gaps through the existing UI/UX review.
- Carry a concise rationale and safe reference/evidence links into the existing task record and PR validation details. This research supplements the applicable frontend guidance and rendered UI/UX review; it does not replace them.

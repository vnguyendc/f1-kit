# Required UI/UX Review

Every UI code change requires a professional UI/UX review using the rendered review procedure and applicable project/host frontend skills. This includes changes to components, styles, layout, interface copy, navigation, interaction behavior, and behavior-preserving UI refactors. Work with no UI code changes does not require this review.

Apply available host/project frontend skills relevant to the change. Project instructions may require specific skills; honor those requirements and report a missing required dependency. Otherwise, the rendered review below is self-contained and does not require a separately installed design skill.

## Plan and implement

- Classify UI scope before loading research instructions or searching. For substantial UI work (new screens, major layout/redesign work, or material navigation/user-flow changes), complete [UI/UX research and analysis](ui-ux-research.md) before G1 and carry its rationale into this review. For minor UI edits, reuse the established product context and design system without external research or reference searches, including searches suggested by frontend skills. Honor explicit user requests for research.
- In the saved planning document, identify the affected screens/flows, audience, primary tasks, existing design system, and relevant viewports/states. Include UI/UX acceptance criteria and the review in the task breakdown and validation strategy.
- Apply relevant design planning and component audit guidance in proportion to the change. For a new or substantially redesigned surface, record the visual thesis, content/interaction approach, and intended color/type/layout system. For a surgical change, use the established product context and design system. The approved brief and existing behavior govern; a review does not authorize an unrelated redesign, new imagery, or ornamental motion.
- During implementation self-review, critique the rendered result using the applicable frontend guidance. Correct findings within the approved scope and repeat the affected checks after fixes.

## Verify the rendered experience

As verifier, perform the professional UI/UX review on the exact candidate, reassessing it against the approved requirements and the applicable frontend guidance. Use the actual local app or permitted preview with browser, simulator, or computer-use tools. Inspect screenshots of the affected screens at representative desktop and mobile sizes for responsive web UI, or the supported device sizes/orientations for native UI. Cover other breakpoints relevant to the change. Exercise the affected flows; code inspection and a green build alone do not establish UI quality.

Review the areas relevant to the changed surface:

- Visual hierarchy and composition: typography, spacing, alignment, color/contrast, imagery, brand consistency, and deliberate design choices.
- Usability and content: task clarity, information structure, navigation, discoverable actions, concise product language, and whether every component serves a useful purpose.
- Responsive layout and interaction: clipping/overflow, sticky chrome, readable content, touch targets, keyboard navigation, focus/hover/disabled feedback, and relevant loading, empty, success, and error states.
- Accessibility and motion: semantic controls and labels, visible focus, readable contrast, meaningful feedback, reduced-motion behavior, and animation that supports the task.

Compare against the approved UI/UX criteria and design rationale, including research findings when research was required or requested, and against the baseline where the change must preserve behavior or layout. Do not claim a state, viewport, or accessibility behavior was checked without exercising or inspecting it. Missing runtime access or required skill access leaves this review blocked/unverified under the shared contract.

## Findings and handoff

Record the skills used, candidate, screens/routes, viewports, exercised states, screenshot/evidence links, findings with severity, fixes/rechecks, and remaining limitations in the existing task/evidence record. Carry a concise review summary and evidence links into the PR's validation details. Do not create a separate tracker or wiki note automatically.

Fix P0/P1 findings through implementation and repeat affected review and verification before PR creation. Disclose remaining P2/P3 findings; an unmet approved UI/UX acceptance criterion still blocks delivery regardless of severity. This review adds no human gate between implementation, verification, and PR creation.

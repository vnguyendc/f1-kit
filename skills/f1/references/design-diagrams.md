# Planning diagrams as software design documentation

Use the plan's diagrams to make the proposed design reviewable before implementation. Show the mechanisms and boundaries a reviewer needs to assess correctness, rather than only the phases of the task. Keep the visuals consistent with the plan's actual scope and evidence.

## Choose the views that explain this change

- **Component / data-flow view:** show the relevant existing components, proposed changes, external systems, stores, and interfaces. Label arrows with the data or operation exchanged and its direction. Mark permission/trust boundaries and read versus write paths when consequential.
- **Sequence view:** use when ordering, state, external calls, asynchronous work, retries, or multiple actors matter. Show the principal success path and the failure/partial/no-op paths that influence the design. Identify where persistence is verified and where uncertainty stops a mutation.
- **State / decision view:** use when flags, eligibility, lifecycle transitions, or reconciliation outcomes drive behavior. Name meaningful states, transition conditions, and terminal/blocked outcomes.
- **UI view:** pair the relevant wireframe or before/after screenshot with interaction/data-flow detail when a visual layout alone cannot explain the software change.

Choose enough views to explain the design, without imposing a fixed count. A small change can use one detailed annotated view focused on the changed interface, surrounding components, and relevant boundary case. A cross-system change often needs a component view plus a sequence or state view. Do not invent queues, services, schemas, or guarantees merely to fill the diagram.

## Make the design assessable

Use actual component/module/service names once known. Distinguish existing, new, and modified elements with a labeled legend; distinguish observed current state from proposed behavior. Show key data contracts or identity/version fields when they govern matching, privacy, persistence, or compatibility. Put detailed field catalogs in the design text instead of shrinking them into the drawing.

Include important decisions such as permission checks, source availability, validation, duplicate/no-op detection, persistence/read-back, retries, and partial completion when relevant. Mark the verification or acceptance checkpoints that establish the proposed behavior. A reader should be able to trace an input to its output, identify what changes, and see where failures leave the system.

Keep labels concise and text readable at normal document size. Prefer separate views over a crowded diagram. Caption each view with what it explains, its important boundary/limitation, and any substantial assumption. Label arrows and nonobvious notation; a decorative collection of unlabeled boxes is insufficient design evidence.

Prefer Mermaid for compact engineering diagrams. When the viewer cannot render it reliably or layout needs more control, embed an SVG/PNG and retain its editable source. Render and inspect every supplied view before G1; check clipping, arrow direction, labels, legibility, references, and agreement with the written design. Avoid real patient data, credentials, and private source content in examples.

This changes diagram quality, not the workflow's approval gates, task scope, or delivery authority. Updating a plan's illustration does not itself change approved product behavior.

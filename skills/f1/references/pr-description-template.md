# PR Description Template

Use the repository's PR template when present, adding or mapping the problem and solution overview into clearly labeled sections. Scale detail to the change: a short paragraph per section can be enough for a small PR. Write for a reviewer who has not seen the conversation.

```markdown
## Problem

Describe the current behavior or unmet need, who is affected, and why this change
is needed. Use a concrete trigger or before/after example when it clarifies the
issue. Do not present an unconfirmed cause as fact.

## Solution overview

Explain the final implemented approach, the resulting behavior, and why it
addresses the problem. Keep this understandable without reading the diff.
Include scope boundaries or technical choices only where they help review.

Issue / approved plan: <relevant links, when available>

## Changes

List all material changes in the final diff, grouped by behavior or component.
Cover relevant UI, API, data/schema, configuration, infrastructure, and test or
documentation changes. Explain what changed and why; avoid a file-by-file dump.
Keep this aligned with the final diff when the candidate changes.

## Verification

Summarize checks actually run and their results. Include relevant runtime/UI
steps and safe evidence links, with the tested candidate and environment.
For previews, report current CI/deployment state and hosted behavior separately
from local fixtures. Label prior evidence, reused builds, and unverified coverage.

## Review evidence

Attach or embed relevant evidence directly in this PR for quick review:

- UI changes: labeled before/after screenshots when feasible, screenshots of
  the final affected screens at relevant desktop/mobile widths and states, and
  a short recording when interaction or motion matters. Summarize UI/UX findings.
- Runtime, API, or logging changes: concise sanitized log/output excerpts and
  links to relevant CI runs, test reports, or artifacts showing observed behavior.

Label evidence with the tested commit, environment, route/scenario, and result.
Use reviewer-accessible attachments or durable links; local filesystem paths
alone are not accessible PR evidence. Remove secrets, PHI, and private data.
If relevant evidence cannot be attached, state what is missing, why, and what
was verified instead. For changes without visual/runtime artifacts, mark this
section not applicable with a brief reason; do not fabricate evidence.

## Risks and limitations

Describe material risks, compatibility or rollout considerations, and remaining
findings or verification gaps. Include recovery guidance when relevant.
```

Describe completed implementation as implemented, not as a future proposal. Describe intended behavior without claiming it was verified unless supported by evidence. Preserve repository-required sections, including testing or screenshots, without duplicating the same content. After CI/preview inspection, refresh the verification section when PR-update authority is established, including partial or blocked coverage; do not claim approval, merge, deployment, or production success from PR creation alone.

Before publishing or updating the PR, compare its description with the final
diff and verification record. Confirm the problem, solution, all material
changes, actual checks/results, and relevant review evidence are represented.
Check that evidence links are accessible to reviewers and identify any access
limits or expiring artifacts.

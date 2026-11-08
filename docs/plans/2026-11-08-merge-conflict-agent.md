# Merge-conflict agent — revision 1

## Problem and context

F1 has build, verify, and deliver roles but no focused route for a conflicted PR. Removing conflict markers can silently discard behavior when a base branch moves code into a new component. Users need the agent to preserve both branches' intent and verify the resulting behavior.

The user requested resolving an existing PR and building this capability into F1 Kit. This task implements that explicit scope. It adds no UI, background automation, external communication, merge, or release authority. UI research and review are not applicable to this package change.

## Proposed solution and visual overview

Add a portable merge-conflict role, reached from F1 and F1 Work. Reuse the existing verifier and deployer instead of creating a second delivery workflow.

```text
Existing: F1 / F1 Work
           |
New:       v
   Conflict resolver -> read current PR, approval, head/base SHAs
           |            and isolate checkout
           v
   compare ancestor + both sides -> reconcile behavior
           |                         |
           | material ambiguity      | resolved candidate
           v                         v
   ask a specific question     Existing verifier -> deployer
                               tests + rendered UI   |
                               when affected         v
                                              update PR branch
                                              verify remote head
                                              STOP before PR merge
```

The view distinguishes the new role from existing routing and delivery. A moved remote head invalidates the candidate; an unchanged rerun is a no-op.

## Requirements and acceptance criteria

- R1: F1 and F1 Work route an explicit conflict request to the new role without restarting already authorized work.
- R2: Recover actual head/base repositories and immutable revisions, preserve dirty work, and inspect merge ancestors and both sides' intent before resolving.
- R3: Preserve behavior through moved files, deletions, generated files, and cleanly merged callers. Reuse focused tests and rendered review for UI changes.
- R4: Default to a merge into the PR source branch without history rewriting. Check concurrent movement, use a non-force push only to the identified source, and observe the remote result. Never merge the PR or update its base under conflict-resolution authority.
- R5: Package validation and disposable installation include the role; document scenario-based evaluation and its limitations.

## Design and tasks

A bundled role is the smallest fit for F1's current architecture. It can run in the current agent or an explicitly permitted delegate; it does not require a model, host, or background service. A standalone Git automation would be less able to recover product intent and would add unnecessary execution surface.

1. Add the role, routing, and usage documentation (R1–R4).
2. Require the resource in package validation and cover missing-resource installation failure (R5).
3. Exercise the playbook against local synthetic Git cases, review requirements, run package validation and installer tests, then create a PR (R1–R5).

## Validation and delivery

Worktree: isolated `feat/merge-conflict-agent`, based on `origin/main` at `d81a5a7`. Target: `vnguyendc/f1-kit`, PR to `main`; CI validates packaging. No deployment is expected. Preserve pre-existing edits in the primary checkout.

Use the existing Python validation and unittest suite. Synthetic Git exercises cover content conflicts, clean reruns, concurrent source advancement, dirty-work isolation, and moved-component reasoning. Packaging checks cannot certify future model judgment; report scenario coverage separately. The same agent builds and verifies, with a separate requirements-based pass and no claim of independent review.

## Verification record

R1–R4: reviewed routing and all role instructions against the requirements. The role uses the existing verifier/deployer, explicitly distinguishes PR source updates from merging, detects moved code and concurrent refs, and preserves dirty work. Same-agent Git walkthrough passed conflict reconciliation, dirty-work isolation, two-parent merge, unchanged rerun, concurrent-push rejection/recovery, and unchanged base checks. The real companion PR exercise covered the extracted-component case.

R5: package validation and all seven disposable installer tests passed, including missing resolver rejection. See the [validation boundaries](../validation.md#merge-conflict-role) for untested model/host scenarios. No UI change or deployment applies to this package. Self-review found and fixed a missing test-case enumeration before final verification; no unresolved P0/P1 findings remain.

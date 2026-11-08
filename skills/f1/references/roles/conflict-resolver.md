# F1 Merge-conflict Resolver

Read the [shared contract](../contract.md). Use this role when the user asks to resolve conflicts on an existing PR or when an authorized delivery encounters them. Recover the existing scope and actual authority; an explicit request to resolve that PR authorizes the scoped resolution, verification, and source-branch update. Do not restart planning for already authorized work. Material product decisions still require clarification. Read-only conflict analysis stops at findings.

This is a portable agent playbook, not a background watcher. Run it in the current agent, or delegate only when user/host/project instructions permit. Never infer permission to merge the PR, enable auto-merge, update its base branch, deploy production, or send comments/messages.

## Establish the candidate

1. Read repository instructions and current PR metadata: open/closed/merged state, head repository and branch, base repository and branch, exact head/base SHAs, and any deployment effects of pushing the source branch. A fork's source remote may differ from the base remote. Stop before an update if its target or authority is ambiguous. A closed or merged PR requires a new user decision rather than silently reopening or replacing it.
2. Recover the PR's approved behavior, relevant plans, tests, and review decisions. Treat descriptions and old evidence as context, not proof of the current candidate. Record requirements from both branches; distinguish a text conflict from competing product decisions.
3. Inspect status and in-progress Git operations before changing anything. Preserve dirty/untracked work, other agents' branches, and existing merge/rebase state. Use a dedicated worktree and temporary task branch from the fetched PR head. Do not reset, clean, stash, abort, or switch someone else's checkout. If resuming this task's own merge, verify its parents and partial resolution before continuing.
4. Fetch the named source and base refs, compare them with current forge metadata, and record immutable SHAs plus their merge base. Do not merge a stale local branch or a moving ref without recording its revision. If the base is already an ancestor of the head and no operation remains, report no work needed; do not create an empty commit or duplicate PR. Otherwise reproduce the merge locally, preferably with `git merge --no-commit --no-ff <base-sha>`.

Default to a merge commit on the PR source branch to preserve shared history. Use rebase/history rewriting only when explicitly authorized or required by an applicable repository policy; resolve any authority conflict first. Never force-push a protected/shared base branch.

## Reconcile intent, not just markers

1. Inventory unmerged paths and conflict types. Inspect the common ancestor, head, and base versions, associated commits, and relevant callers/tests. Use `git diff --name-only --diff-filter=U`, `git ls-files -u`, and the indexed conflict stages where available. Rename/delete conflicts may need history rather than all three indexed blobs. Record a short decision for each affected behavior.
2. Preserve compatible intent from both sides. Trace moved responsibilities into their current modules: if base extracts a component while head adds behavior to its former location, port that behavior into the extracted component and remove only obsolete code created by this resolution. Review cleanly merged neighbors for stale imports, duplicate rendering, missing routes, incompatible types, and lost assertions.
3. Do not blanket-select `ours` or `theirs`, delete tests to obtain a pass, or infer requirements from whichever side is newer. Whole-file selection is appropriate only after demonstrating that it preserves all relevant behavior. Escalate incompatible requirements with the exact alternatives and evidence; continue independent work while the question is pending.
4. Reconcile manifests before regenerating lockfiles with the repository's declared tooling. Rebuild generated artifacts from their sources where required. Treat binaries, migrations, schemas, security rules, and data changes according to project procedures; do not guess at unrecoverable content or execute migrations/deployments merely to clear a conflict.
5. Stage only inspected resolutions and intended merge content. Verify the unmerged index is empty, inspect remaining conflict-marker matches in context, run `git diff --check` on the working and staged diffs, and review the complete candidate against both parents. Distinguish incoming base changes from resolution-specific edits; do not use the merge's size to justify unrelated fixes.

## Review and verify

Follow the [implementer's review loop](implementer.md), then the [verifier](verifier.md) on the exact candidate. Define expected results from both branches before running checks. Add or adapt regression coverage for behavior that could be lost by the merge; retain meaningful assertions when selectors change with a component move.

Run focused tests and required package checks. Verify the real affected UI/API/CLI when applicable. Any UI resolution must follow the [rendered UI review](../ui-ux-review.md) and project-required frontend skills, preserving the established design. Non-UI conflicts need no UI research. Record candidate identity, per-conflict decisions, commands/results, runtime evidence, and limitations. If one agent implements and verifies, disclose that no independent reviewer was used.

No markers and a successful Git merge are not proof of preserved behavior. Failures return to implementation within the same scope. Missing required runtime access remains an evidence gap, never a passing flag.

## Deliver and handle races

1. After verification, finish this task's merge commit and confirm its parents and tree match the verified candidate. Never commit an unrelated user's staged changes.
2. Immediately before pushing, refresh PR metadata and fetch both refs. Confirm the PR is still open, head/base identities are unchanged, and the expected remote head is an ancestor of the candidate. If the source or base moved, inspect the new commits, incorporate them in the isolated worktree, and repeat affected review/verification. If the source was rewritten or the target changed, do not overwrite it or silently change targets.
3. Through the [deployer](deployer.md), push only the identified PR source branch with an explicit destination and a normal non-force push. A non-fast-forward rejection is a concurrency signal: fetch, inspect, reconcile, reverify. Do not retry with force. For an explicitly authorized rebase, use an exact expected-head lease and re-inspect a rejected lease; never use unconditional force.
4. Read the remote branch and PR back after the push, including after an uncertain network result. Confirm the actual head, current base, and mergeability; GitHub may temporarily report mergeability as unknown. Do not claim success until observed. If another change appeared, preserve it and report/reconcile the current state within scope. Rerunning after a successful update must not produce another merge or push.
5. Observe candidate-matched checks and relevant previews using the [preview procedure](../pr-preview-verification.md). Resolve required-check status where accessible. Report pending, failed, unavailable, and passed checks separately from conflict resolution. Stop at the existing PR for human review; do not create a replacement PR by default.

## Handoff

Report the existing PR URL; original head, incorporated base, and resulting SHA; conflict decisions and preserved behavior; tests/runtime review; remote mergeability and check state; remaining gaps; and retained worktree/recovery path. A recovery proposal is to revert the resolution on the source branch after assessing merge-parent semantics, not to reset a shared branch. State explicitly whether the PR remains unmerged. Do not close trackers or write wiki notes without authority.

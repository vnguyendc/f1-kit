# PR Preview Verification

Use during delivery after creating/updating a PR, or when reviewing an existing PR's current status. This procedure is self-contained; the separately installed `pr-preview-verification` skill can provide additional review guidance when available. Read-only inspection needs no new G1 approval. Apply the shared contract's existing implementation/PR authority for in-scope fixes; do not infer permission to merge, redeploy, change hosted configuration or publish unrelated communications.

Match the verification to the approved change. If no preview applies, record it as not applicable rather than inventing a deployment requirement. Use browser steps for affected UI; use the approved API/runtime smoke checks for service-only previews.

## Match checks and previews to the candidate

- Capture the PR URL, base/head branches, head SHA, affected apps, review/merge state and review timestamp. Separate old PR descriptions and saved test reports from observations made in this run.
- Inspect each check's name, conclusion, associated commit, timestamp and run link. Resolve required-check rules where accessible; distinguish required, optional and unknown. A summary count is insufficient. Skipped/neutral jobs and a completed deployment are not runtime verification.
- Match each relevant deployment to the affected app and candidate SHA, preferably using a deployment-specific URL. Monorepo lists may include unrelated apps; branch aliases can move. Record an unknown commit association rather than assuming it matches.
- Wait only within the agreed monitoring window while useful progress is expected. Report pending or access-blocked results when that window ends; do not treat a timeout as success or retry indefinitely.

## Inspect actual hosted behavior

- Open the exact preview and affected route in a browser, then exercise its in-app entry path and changed interactions. Record final URLs, redirects, expected/observed results, relevant viewports/states, and safe screenshots or browser evidence. HTTP probes support diagnosis; they do not replace rendered UI verification.
- Check assets separately when relevant. An SVG returning 200 does not establish that a route renders, and a reachable sign-in screen does not verify authenticated staff screens or APIs. Exercise hosted authentication only with authorized test access and permitted data.
- For a 404 or inaccessible flow, distinguish the wrong app/path, access protection, build problems, missing backend and feature gates. Inspect candidate route/config code and available deployment evidence before claiming a cause. A previous comment is a reported explanation until corroborated.
- Trace frontend/CTA and API gates when relevant. Distinguish source defaults from deployed settings, and build-time values from runtime values. If deployed configuration is inaccessible, preserve that uncertainty. Do not change hosted flags or bypass access controls to obtain evidence without authority.

## Local fallback and evidence reuse

When hosted coverage is blocked, record the blocker and use the same candidate in an isolated or confirmed existing worktree. Check its SHA, dirty diff, build and configuration first; preserve unrelated files and services.

Prefer a production build for deployment investigations. Record commands, build mode/ID, local URL, non-secret flag values, fixtures/stubs and their limitations. Rebuild after changing build-time flags. Use synthetic data in healthcare nonproduction. Do not put credentials, PHI or sensitive records in evidence.

Exercise the same affected screens and interactions locally. Identify what fixtures cannot establish, such as hosted authentication, live APIs, persistence or provider integration. Label reused builds, prior test reports and previously checked viewports explicitly; a clean source tree alone does not prove an old build was regenerated. Stop temporary services created for the review.

Local success remains local evidence. Keep hosted coverage partial or blocked until observed there. A different PR's preview, separate demo or design gallery does not verify this candidate.

## Record and finalize

Use the existing task artifact or conversation; do not create another tracker or wiki note automatically. Record:

```text
PR / reviewed at / scope / head SHA:
Checks: name → conclusion, required/optional/unknown, commit, timestamp, link
Deployment: app, URL, deployed SHA, provider state
Hosted: route + steps → expected / observed; result; evidence
Local: worktree/diff/build, commands, flags, fixtures, URL → result; limitations
Coverage: requirement or changed behavior → environment/result/evidence
Overall: passed | partial | failed | blocked; remaining gaps; next action
Merge/release state: authoritative observed state, or unknown
```

- **Passed:** the agreed delivery verification scope is supported on the identified candidate and required checks are satisfied. Name any agreed local-only scope explicitly.
- **Partial:** useful evidence exists, but an environment, interaction, check or candidate association remains unverified.
- **Failed:** observed behavior violates an expected requirement. Do not excuse an unexplained 404 as an intentional gate.
- **Blocked:** a specific access, configuration or runtime dependency prevents the requested verification. A confirmed intentional gate may block hosted screen coverage without establishing a regression.

Report outcomes per layer even with an overall status. Any unmet required acceptance or delivery criterion remains unresolved; partial status is not a waiver. Recheck the PR head and deployment identity before finalizing; repeat affected checks or label evidence as applying to the older revision if either changed. Confirm merge completion from authoritative PR state, not a panel click, disabled button or old note.

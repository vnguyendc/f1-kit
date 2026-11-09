# Product Engineering

Use this during F1 planning when a user outcome, first-release boundary, or product behavior is open, or when the user asks to refine requirements, design a flow, or turn an agreed product design into development tasks. For approved work, resume the authorized stage unless the user changes the product scope.

## Establish the baseline

Read the existing spec, linked decisions, and latest relevant product or candidate. Identify the user, the decision or action the product should make possible, and the smallest useful release. Separate observed behavior, confirmed decisions, proposals, and open questions. Identify which decision supersedes any stale issue or prototype. A preview establishes only the cases it exercised.

## Refine the release

- Find decisions that change the user promise, the source of truth, access to sensitive data, or who owns the next step. Verify discoverable facts first. Compare viable options, recommend one, and explain its tradeoff. Continue with independent work while a decision is open.
- Design the flow around what people enter, what each result means, and what they can do next. Include consequential unknown, partial, error, and recovery states. For assisted paths, confirm the receiving team and what it can actually do before promising follow-up.
- Define the evidence behind each user-facing claim. For sensitive results, distinguish matching a record from establishing who may view it. When the complexity of a capability outweighs its first-release value, propose a narrower useful release and record the deferred capability and conditions for revisiting it.
- Apply the Planner's UI research rules. For a flow, use an annotated sketch, state table, or diagram that makes the important decisions and exceptions reviewable.

## Prepare the handoff

Record confirmed scope, stable requirement IDs, observable acceptance criteria, deferred scope, and open decisions in the existing spec or plan. For a material scope revision, update affected states, acceptance criteria, and task dependencies together. Identify what the existing candidate can contribute under the revised scope.

If the user asks for tracker issues, use the existing project and look for overlapping work. Reuse an issue when its scope still fits and link a superseded candidate as context. Create dependency-ordered issues that reference the spec and requirement IDs. Keep implementation issues in the planning backlog until authorized. Preserve confirmed decisions and open gates when updating an authorized wiki or tracker.

The product design is ready for the technical plan when the first release has a defined user outcome, every material state has a next action, and every requirement has an owner or named dependency and a verification case. Keep unresolved material choices visible in the plan and carry the agreed scope into the existing F1 approval process.

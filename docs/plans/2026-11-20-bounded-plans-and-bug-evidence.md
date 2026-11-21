# Short plans and bug-fix evidence

Revision 1 · F1 Kit · PR target `main`

- **Current behavior.** Even a bounded edit needs a full plan and diagram. A bug-fix handoff can report a passing check without recording whether it exposed the original defect.
- **Desired behavior.** Use a one-screen plan when the outcome and scope are settled. For reproducible bugs, show the same check failing as expected before the fix and passing afterward.
- **Scope.** Update planning, implementation, verification, and evidence instructions. Preserve existing approvals, UI review, and delivery boundaries.
- **Verification.** Walk through a copy edit, a change with an open design decision, a reproducible bug, and a bug with an inaccessible baseline. Validate package links and run the installer tests.

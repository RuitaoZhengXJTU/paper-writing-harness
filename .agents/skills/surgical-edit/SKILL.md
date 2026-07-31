---
name: surgical-edit
description: Make exact, minimal manuscript edits when the user specifies wording, formulas, ordering, terminology, citations, or a bounded local transformation. Do not use for open-ended section design or broad stylistic rewriting.
---

# Surgical edit

1. Confirm `EXACT_EDIT`; load contracts, claim ledger, terminology, target, adjacent text, and dependencies.
2. Identify the exact editable span and lock everything unspecified.
3. Record the before-state of the target.
4. Apply the minimum sufficient diff. Do not delete content because it seems redundant.
5. Inspect the diff for collateral changes, claim-strength drift, numerical changes, citation/label changes, and publication leakage.
6. Run available guards and the manuscript build or strongest safe substitute.
7. Update external memory only for an approved manuscript-state change; mark dependent sections stale.
8. Report changed files, intentionally preserved scope, checks, stale sections, assumptions, and unresolved issues.

---
name: manuscript-composer
description: Convert an explicitly approved preview into reviewer-facing manuscript prose. Requires a preview ID or explicit authorization; do not use for unapproved designs.
---

# Manuscript composer

1. Confirm `APPLY_PREVIEW`, preview ID, approval, target, and locked decisions.
2. Load paper contract, section contracts, claim ledger, terminology, target, adjacent text, and dependencies.
3. Implement only the approved scope. Preserve unrelated prose and do not redesign silently.
4. Use only verified or carefully bounded support. Never invent evidence, citations, numbers, or claims.
5. Keep operational implementation details outside the manuscript unless classified as scientifically necessary.
6. Update claim, section, terminology, stale-state, decision, and change-log files as required.
7. Run publication, evidence, notation, reference, consistency, and build checks.
8. Report the diff and unresolved issues.

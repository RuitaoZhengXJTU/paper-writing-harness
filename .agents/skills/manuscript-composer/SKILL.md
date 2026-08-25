---
name: manuscript-composer
description: Convert an explicitly approved preview ID and revision into reviewer-facing manuscript prose. Read the approved Markdown preview as authoritative; do not use for unapproved designs or PDF-only approval.
---

# Manuscript composer

1. Confirm `APPLY_PREVIEW`, preview ID, approved revision, target, and locked decisions.
2. Verify `scratch/previews/<preview-id>/preview.md` exists and matches the approved revision.
3. Treat `preview.md` as the authoritative source. Generated `render/preview.tex` and `render/preview.pdf` are review artifacts only and must not override Markdown wording.
4. Check `review/decisions.md` and confirm unresolved PDF annotations are either resolved or explicitly accepted as remaining issues.
5. Load paper contract, section contracts, claim ledger, terminology, target, adjacent text, and dependencies.
6. Implement only the approved scope. Preserve unrelated prose and do not redesign silently.
7. Do not carry review-only paragraph anchors, PDF annotations, comments, or render metadata into `paper/`.
8. Use only verified or carefully bounded support. Never invent evidence, citations, numbers, or claims.
9. Keep operational implementation details outside the manuscript unless classified as scientifically necessary.
10. Update claim, section, terminology, stale-state, decision, and change-log files as required.
11. Run publication, evidence, notation, reference, semantic-duplication, defensive-writing, over-expression, consistency, and build checks.
12. Compare the implemented manuscript passage with the approved Markdown revision. Report any necessary deviation caused by manuscript context, LaTeX integration, citations/labels, or scientific consistency.
13. Report the diff, stale dependencies, and unresolved issues.

Never infer approval from a clean PDF, absence of annotations, or polished preview prose. Explicit approval of preview ID and revision is required.

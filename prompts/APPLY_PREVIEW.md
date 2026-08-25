# Apply Preview Prompt

```text
MODE: APPLY_PREVIEW

APPROVED PREVIEW:
- Preview ID:
- Approved revision:
- Authoritative Markdown: scratch/previews/<preview-id>/preview.md
- Last reviewed PDF: scratch/previews/<preview-id>/render/preview.pdf

TARGET:
- File:
- Section:

APPROVAL CHECK:
- Confirm the user explicitly approved both preview ID and revision.
- Confirm `preview.md` revision matches the approved revision.
- Confirm unresolved PDF annotations are either resolved or explicitly accepted as remaining issues.
- Treat generated TeX/PDF as review artifacts only; never use them as the authoritative wording source when they differ from Markdown.

LOCKED PREVIEW DECISIONS:
1.
2.

IMPLEMENTATION RULES:
- Implement only the approved structure and content from the approved Markdown revision.
- Do not silently redesign the preview.
- Do not carry review-only paragraph anchors, annotation marks, comments, or render metadata into `paper/`.
- Do not add unsupported claims, results, citations, or implementation details.
- Preserve unrelated manuscript content.
- Mark unavailable evidence explicitly rather than inventing it.
- Update external memory when the approved manuscript state changes.
- Run publication, evidence, notation, reference, redundancy, defensive-writing, and consistency checks.
- Mark dependent sections stale rather than modifying them outside scope.

POST-APPLICATION CHECK:
- Compare the implemented manuscript passage against the approved Markdown preview.
- Report any required deviations caused by manuscript context, LaTeX integration, citation/label constraints, or scientific consistency.
- Do not treat those deviations as silently approved redesigns.
```

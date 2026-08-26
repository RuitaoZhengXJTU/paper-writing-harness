---
name: paper-router
description: Route academic-paper writing requests into EXACT_EDIT, DESIGN_PREVIEW, APPLY_PREVIEW, or AUDIT. Use before manuscript work when the mode is not already explicit; do not edit the manuscript itself.
---

# Paper task router

Read `AGENTS.md` and the external-memory files. Select exactly one mode.

| User intent | Mode |
|---|---|
| Exact wording, formula, ordering, citation, or bounded local change in approved manuscript content | `EXACT_EDIT` |
| Desired purpose or rough structure without approved manuscript prose | `DESIGN_PREVIEW` |
| PDF annotations or review comments on an unapproved preview | `DESIGN_PREVIEW` |
| Explicit approval of a preview ID + revision for manuscript implementation | `APPLY_PREVIEW` |
| Consistency, evidence, notation, duplication, defensive writing, reviewer readiness, or language review without logic changes | `AUDIT` |

For `AUDIT`, choose a profile when the user intent is clear:

- terminology precision, wording consistency, factual/professional expression, defensive prose, cadence → `LANGUAGE`;
- contradictions, duplication, ownership, notation, stale sections → `CONSISTENCY`;
- claim/evidence/citation/numerical support → `EVIDENCE`;
- mixed or whole-manuscript review → `FULL`.

For mixed exact/open-design requests, convert exact instructions into locked constraints and route the open portion to `DESIGN_PREVIEW`. Material ambiguity defaults to `DESIGN_PREVIEW`.

PDF annotation feedback remains `DESIGN_PREVIEW` while the text is still under `scratch/previews/`, even when the comment identifies an exact sentence. Revise the preview Markdown first, regenerate TeX/PDF, and increment the revision.

Use `APPLY_PREVIEW` only after explicit approval of both preview ID and revision.

A request such as “make this section more professional/consistent without changing the logic” should default to `AUDIT PROFILE: LANGUAGE`, not direct rewriting. After the user approves Language Change Ledger items, route their implementation to `EXACT_EDIT`.

State the chosen mode/profile, target, editable scope, locked scope, and required source-of-truth files, then invoke the matching workflow.

---
name: paper-router
description: Route academic-paper writing requests into EXACT_EDIT, DESIGN_PREVIEW, APPLY_PREVIEW, or AUDIT. Use before manuscript work when the mode is not already explicit; do not edit the manuscript itself.
---

# Paper task router

Read `AGENTS.md` and the external-memory files. Select exactly one mode.

| User intent | Mode |
|---|---|
| Exact wording, formula, ordering, citation, or local transformation in approved manuscript content | `EXACT_EDIT` |
| Desired purpose or rough structure without approved manuscript prose | `DESIGN_PREVIEW` |
| PDF annotations or review comments on an unapproved preview | `DESIGN_PREVIEW` |
| Explicit approval of a preview ID and revision for manuscript implementation | `APPLY_PREVIEW` |
| Consistency, evidence, notation, semantic duplication, defensive writing, over-expression, leakage, reviewer readiness | `AUDIT` |

For mixed requests, convert every exact instruction into a locked constraint and route the open design to `DESIGN_PREVIEW`. Material ambiguity defaults to `DESIGN_PREVIEW`.

PDF annotation feedback does not become `EXACT_EDIT` merely because the comment identifies an exact sentence. If the sentence belongs to `scratch/previews/`, keep the work inside the same `DESIGN_PREVIEW` bundle: map the annotation back to `preview.md`, revise Markdown first, regenerate TeX/PDF, and increment the preview revision.

Use `APPLY_PREVIEW` only when the user explicitly approves both preview ID and revision. Never infer approval from a clean PDF, absence of comments, or statements such as “looks better” unless they clearly authorize manuscript application.

State the chosen mode, target, editable scope, locked scope, and required source-of-truth files. Then invoke the matching workflow. Never treat generated preview TeX/PDF as the authoritative source.

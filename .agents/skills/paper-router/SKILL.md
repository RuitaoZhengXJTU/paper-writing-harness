---
name: paper-router
description: Route academic-paper writing requests into EXACT_EDIT, DESIGN_PREVIEW, APPLY_PREVIEW, or AUDIT. Use before manuscript work when the mode is not already explicit; do not edit the manuscript itself.
---

# Paper task router

Read `AGENTS.md` and the external-memory files. Select exactly one mode.

| User intent | Mode |
|---|---|
| Exact wording, formula, ordering, citation, or local transformation | `EXACT_EDIT` |
| Desired purpose or rough structure without approved prose | `DESIGN_PREVIEW` |
| Explicitly approved preview ID | `APPLY_PREVIEW` |
| Consistency, evidence, notation, duplication, leakage, reviewer readiness | `AUDIT` |

For mixed requests, convert every exact instruction into a locked constraint and route the open design to `DESIGN_PREVIEW`. Material ambiguity defaults to `DESIGN_PREVIEW`. State the chosen mode, target, editable scope, locked scope, and required source-of-truth files. Then invoke the matching workflow. Never treat polished preview text as approval.

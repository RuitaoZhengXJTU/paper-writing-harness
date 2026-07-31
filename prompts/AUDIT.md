# Audit Prompt

```text
MODE: AUDIT

SCOPE:
- Target files or whole manuscript:

CHECKS:
- central contribution and scope
- contradictions
- duplicated explanations
- terminology and notation
- claim strength and evidence
- numerical consistency
- equations, figures, tables, citations, and references
- publication-boundary leakage
- stale abstract/introduction/conclusion statements

AUTOFIX: NO

OUTPUT:
- Findings ranked HIGH / MEDIUM / LOW.
- Category, file, and section.
- Conflicting text or state entry.
- Why it matters.
- Minimal recommended repair.
- Evidence or dependency affected.
```

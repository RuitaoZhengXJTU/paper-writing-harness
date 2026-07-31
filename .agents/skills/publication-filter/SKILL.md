---
name: publication-filter
description: Classify and transform material moving from code, logs, internal analysis, repository docs, or previews into manuscript content, and detect implementation leakage. Do not use to indiscriminately remove reproducibility details.
---

# Publication filter

Classify each item as:

- `MAIN_TEXT`
- `APPENDIX_OR_SUPPLEMENT`
- `REPOSITORY_DOCUMENTATION`
- `INTERNAL_ONLY`
- `UNSUPPORTED_PROHIBITED`

Main text explains the scientific problem, model, assumptions, formulation, essential algorithmic choices, evidence, and implications. Appendix/supplement preserves necessary but operational reproducibility detail. Repository documentation contains commands, scripts, machine setup, and extended usage. Internal-only material includes debugging chronology, failed attempts, agent narration, local paths, and workflow metadata. Unsupported content must not appear as fact.

Transform implementation detail into a scientific abstraction only when the abstraction is supported. Preserve necessary reproducibility information by routing it correctly rather than deleting it.

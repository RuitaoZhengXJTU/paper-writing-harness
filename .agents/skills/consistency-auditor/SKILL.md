---
name: consistency-auditor
description: Perform read-only manuscript audits for contradictions, duplication, notation, claim/evidence drift, stale sections, numerical consistency, and reviewer readiness. Do not automatically rewrite unless explicitly authorized.
---

# Consistency auditor

Default to `AUDIT` and read-only behavior. Check central thesis and contribution list, claims and modal strength, numbers and evidence status, canonical terminology, equations and cross-references, duplicated explanations, abstract/introduction/conclusion alignment, and declared stale dependencies.

Report each finding with severity (`HIGH`, `MEDIUM`, `LOW`), category, file/section, conflicting passages or state entries, why it matters, minimal repair, missing evidence, and affected dependencies. Separate objective violations from optional style suggestions. State that heuristic checks do not prove semantic completeness.

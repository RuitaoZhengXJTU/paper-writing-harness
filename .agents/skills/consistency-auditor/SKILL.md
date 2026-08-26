---
name: consistency-auditor
description: Perform read-only manuscript audits for contradictions, semantic duplication, defensive writing, over-expression, information ownership, terminology/notation drift, evidence consistency, and reviewer readiness. Supports FULL, CONSISTENCY, EVIDENCE, and LANGUAGE audit profiles. Do not automatically rewrite.
---

# Consistency auditor

Operate under `MODE: AUDIT` and remain read-only.

## Profiles

- `FULL`: run consistency, evidence, language, redundancy, ownership, and publication-boundary checks.
- `CONSISTENCY`: focus on cross-section/state consistency, duplication, information ownership, notation, numbers, and stale dependencies.
- `EVIDENCE`: focus on claim strength, evidence status, citation support, numerical provenance, assumptions, and stale claims.
- `LANGUAGE`: invoke `academic-language-reviewer`; return a Language Change Ledger and do not rewrite the manuscript.

## Structural consistency

Check central thesis and contribution list, claims and modal strength, numbers and evidence status, canonical terminology, equations and cross-references, publication-boundary leakage, abstract/introduction/discussion/conclusion alignment, and declared stale dependencies.

## Over-expression and defensive writing

Flag prose that consumes space without adding a new claim, mechanism, evidence, qualification, or interpretation. Flag abandoned/internal approaches, repeated statements of what the method does not do, hypothetical-objection prose, unnecessary scope disclaimers, disproportionate justification of routine choices, meta-writing, and empty self-protective hedging.

Do not flag scientifically necessary assumptions, limitations, boundary conditions, negative results, or caveats.

## Semantic duplication and information ownership

Detect repeated meaning even when wording differs. For each repeated idea, identify one canonical owner section using `SECTION_CONTRACTS.yaml`, `CLAIM_LEDGER.yaml`, and rhetorical role. Keep the full explanation in the owner section; elsewhere retain only a materially compressed reference when it serves a distinct function.

Prefer `DELETE`, `MERGE`, `COMPRESS`, or `RELOCATE` over adding clarification when the meaning is already present.

## Language findings

When language precision is part of the audit, use `academic-language-reviewer` rather than rewriting prose inside this skill. Language review must respect the logic lock and return `L001`, `L002`, ... ledger items for later approval and `EXACT_EDIT` implementation.

## Findings format

For non-language findings report:

- severity (`HIGH`, `MEDIUM`, `LOW`);
- category;
- file/section;
- exact passage(s) or state entries;
- canonical owner section when relevant;
- why it matters;
- one primary action: `KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, or `REWRITE`;
- minimal repair strategy;
- evidence/claim/dependency affected.

For language findings append the Language Change Ledger produced by `academic-language-reviewer`.

State that heuristic checks do not prove semantic completeness.

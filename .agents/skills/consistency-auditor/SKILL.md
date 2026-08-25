---
name: consistency-auditor
description: Perform read-only manuscript audits for contradictions, semantic duplication, defensive writing, over-expression, information ownership, notation, claim/evidence drift, stale sections, numerical consistency, and reviewer readiness. Do not automatically rewrite unless explicitly authorized.
---

# Consistency auditor

Default to `AUDIT` and read-only behavior.

## Core checks

Check central thesis and contribution list, claims and modal strength, numbers and evidence status, canonical terminology, equations and cross-references, publication-boundary leakage, abstract/introduction/discussion/conclusion alignment, and declared stale dependencies.

## Over-expression

Flag prose that consumes space without adding a new claim, mechanism, evidence, qualification, or interpretation. Typical cases include:

- adjacent sentences or paragraphs that restate the same point;
- immediate summaries of content that has just been explained;
- repeated contribution/motivation statements;
- obvious implications spelled out unnecessarily;
- excessive roadmap, transition, or framing language;
- standard concepts re-explained after they already have a canonical definition;
- report/manual-style micro-paragraphs that fragment one rhetorical move.

Prefer deletion, merging, or compression over adding clarification.

## Defensive writing

Flag prose whose primary function is to defend the paper against an imagined objection rather than advance the scientific narrative, including:

- discussion of abandoned or historical approaches that are no longer part of the current method;
- repeated statements of what the method does not do;
- unnecessary comparisons to superseded internal versions;
- repeated scope disclaimers;
- routine design choices justified at disproportionate length;
- meta-writing about why the authors chose to explain something;
- excessive hedging that does not reflect real uncertainty.

Do not flag scientifically necessary assumptions, limitations, boundary conditions, negative results, or caveats. Preserve anything that changes validity, interpretation, reproducibility, or reviewer understanding.

## Semantic duplication and information ownership

Do not restrict duplication checks to identical wording. Search for the same motivation, mechanism, result, limitation, or contribution explained in different words across adjacent and non-adjacent sections.

For each repeated idea:

1. identify the canonical owner section using `SECTION_CONTRACTS.yaml`, `CLAIM_LEDGER.yaml`, and rhetorical role;
2. distinguish a full explanation from a necessary compressed reference;
3. keep the full explanation in the owner section unless repetition is scientifically required;
4. recommend deletion, compression, relocation, or cross-reference elsewhere;
5. allow compressed recurrence in Abstract, Introduction, Discussion, and Conclusion when it serves a genuinely different rhetorical function.

## Academic cohesion

Flag paragraphs too short to complete one argumentative move, adjacent paragraphs that should be merged, abrupt subject shifts, repeated generic summary sentences, slogan-like endings, and prose that reads like a checklist/report/manual rather than a continuous academic argument.

## Findings format

Report each finding with:

- severity (`HIGH`, `MEDIUM`, `LOW`);
- category;
- file/section;
- exact passage(s) or state entries;
- canonical owner section when relevant;
- why it matters;
- one primary action: `KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, or `REWRITE`;
- minimal repair strategy;
- missing evidence and affected dependencies.

Separate objective violations from optional style suggestions. End with the highest-value deletions/compressions, repeated ideas and their canonical homes, defensive passages that should disappear, legitimate caveats that must remain, and sections that would become stale if repairs are accepted.

State that heuristic checks do not prove semantic completeness.

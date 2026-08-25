# Audit Prompt

```text
MODE: AUDIT

SCOPE:
- Target files or whole manuscript:
- Include adjacent/dependent sections: YES
- Include whole-manuscript semantic duplication scan: YES / NO

AUTOFIX: NO

AUDIT PRINCIPLE:
- Prefer subtraction over defensive addition.
- Distinguish necessary scientific explanation from agent-generated over-explanation.
- Do not treat repeated wording as the only form of duplication; detect semantically repeated explanations across different wording.
- Do not flag intentional high-level recurrence in Abstract / Introduction / Discussion / Conclusion when each occurrence serves a distinct rhetorical role and is materially compressed relative to the canonical explanatory section.

CHECKS:

A. SCIENTIFIC AND STATE CONSISTENCY
- central contribution and scope
- contradictions
- terminology and notation
- claim strength and evidence
- numerical consistency
- equations, figures, tables, citations, and references
- publication-boundary leakage
- stale abstract/introduction/discussion/conclusion statements

B. OVER-EXPRESSION
Flag prose that adds words without adding a new claim, mechanism, evidence, qualification, or interpretation, including:
- adjacent sentences that restate the same point;
- paragraphs that summarize what the immediately preceding paragraph already established;
- repeated contribution or motivation statements;
- obvious implications spelled out unnecessarily;
- excessive roadmap, transition, or framing language;
- multiple sentences that could be merged without loss of scientific meaning;
- repeated explanations of standard concepts already defined elsewhere;
- report/manual-style micro-paragraphs that fragment one argumentative move.

C. DEFENSIVE WRITING
Flag prose written mainly to pre-empt hypothetical objections rather than advance the paper, including:
- explaining historical, abandoned, or rejected approaches that are no longer part of the method;
- repeatedly stating what the proposed method does NOT do;
- formulations such as “unlike the previous version,” “without using X,” or “this should not be confused with Y” when X/Y are not necessary for the current paper narrative;
- unnecessary justification of routine design choices;
- repeated scope disclaimers or caveats that do not materially change interpretation;
- meta-writing that explains why a passage is written a certain way;
- excessive hedging added for self-protection rather than calibrated uncertainty.

Do NOT remove a limitation, assumption, boundary condition, or negative result merely because it sounds defensive. Keep it when it changes scientific interpretation, validity, reproducibility, or reviewer understanding.

D. CROSS-SECTION DUPLICATION AND INFORMATION OWNERSHIP
For every repeated idea:
1. identify the canonical owner section using `SECTION_CONTRACTS.yaml`, `CLAIM_LEDGER.yaml`, and the manuscript's rhetorical structure;
2. distinguish FULL EXPLANATION from NECESSARY REFERENCE;
3. preserve the full explanation only in the owner section unless repetition is scientifically required;
4. recommend compression, cross-reference, or deletion elsewhere;
5. check not only adjacent paragraphs but non-adjacent sections that describe the same mechanism, motivation, result, limitation, or contribution in different words.

Typical ownership pattern:
- Introduction: motivation, gap, contribution-level summary.
- Method: full mechanism/formulation/algorithm explanation.
- Experiments: setup needed to interpret evidence and the evidence itself.
- Discussion: interpretation, limitations, implications—not a second Method section.
- Conclusion: compressed synthesis—not a repeated Introduction.

E. PARAGRAPH-LEVEL ACADEMIC COHESION
- paragraphs too short to complete one argumentative/explanatory move;
- adjacent paragraphs that should be merged;
- abrupt topic shifts;
- repeated “This...” summary sentences;
- slogan-like or generic paragraph endings;
- prose that reads like a checklist, report, or manual rather than continuous academic argument.

REPAIR POLICY:
For each finding recommend exactly one primary action:
- KEEP
- DELETE
- MERGE
- COMPRESS
- RELOCATE
- REWRITE

Prefer DELETE / MERGE / COMPRESS when meaning is already present elsewhere. Do not solve redundancy by adding new explanatory prose.

OUTPUT:
For each finding provide:
- Severity: HIGH / MEDIUM / LOW.
- Category: scientific consistency / over-expression / defensive writing / duplication / ownership / cohesion / leakage / evidence / notation / other.
- File and section.
- Exact passage(s) involved.
- Canonical owner section when duplication is involved.
- Why the passage is necessary, redundant, defensive, or misplaced.
- Primary repair action.
- Minimal repair strategy.
- Evidence, claim, or dependency affected.

Then provide a short summary:
- Highest-value deletions/compressions.
- Repeated ideas and their canonical homes.
- Defensive passages that should disappear from the paper narrative.
- Legitimate limitations/caveats that must be preserved.
- Sections that become stale if the recommended repairs are accepted.

Do not rewrite the manuscript unless a later task explicitly authorizes the repairs.
```

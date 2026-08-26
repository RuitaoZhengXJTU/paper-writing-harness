# Audit Prompt

```text
MODE: AUDIT
AUDIT PROFILE: FULL | LANGUAGE | CONSISTENCY | EVIDENCE

SCOPE:
- Target files or whole manuscript:
- Include adjacent/dependent sections: YES
- Include whole-manuscript scan: YES / NO

AUTOFIX: NO

GLOBAL RULES:
- Read `PAPER_CONTRACT`, `SECTION_CONTRACTS`, `CLAIM_LEDGER`, `TERMINOLOGY`, and `PROSE_STYLE` when relevant.
- Preserve scientific meaning, claim strength, evidence interpretation, and rhetorical ownership.
- Prefer subtraction over defensive addition when meaning is already present.
- Do not rewrite `paper/` during AUDIT.

PROFILE: FULL
Run all checks below.

PROFILE: CONSISTENCY
Check:
- central contribution and scope;
- contradictions and stale statements;
- terminology/notation consistency;
- numerical consistency;
- equations, figures, tables, citations, and references;
- semantic duplication and canonical information ownership;
- paragraph/section responsibility drift;
- publication-boundary leakage.

For repeated ideas, identify one canonical owner section and recommend one primary action:
`KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, or `REWRITE`.

PROFILE: EVIDENCE
Check:
- claim strength versus available evidence;
- verified versus provisional result use;
- unsupported causal or guarantee language;
- citation support;
- numerical provenance;
- assumptions/limitations required for valid interpretation;
- stale claims after result or method changes.

PROFILE: LANGUAGE
Use the `academic-language-reviewer` skill and apply a strict LOGIC LOCK.

Do not change or recommend changes to:
- section/paragraph order;
- paragraph rhetorical role;
- central claim;
- claim strength or causal direction;
- evidence interpretation;
- numbers, equations, or citations;
- assumptions, limitations, scope, or methodological meaning.

Check:
- `TERM_AMBIGUITY`: technical term is vague or overloaded;
- `TERM_DRIFT`: same object is named inconsistently;
- `SEMANTIC_DRIFT`: wording changes technical meaning or claim strength;
- `VAGUE_ACADEMICISM`: generic claims such as “improves flexibility” replace concrete supported descriptions;
- `DEFENSIVE_PROSE`: abandoned versions, negative definitions, hypothetical objections, or unnecessary disclaimers;
- `META_PROSE`: prose about how the paper is written rather than the science;
- `AI_FORMULAIC_PROSE`: generic repeated emphasis/summary templates;
- `COLLOCATION`: grammatically valid but technically unnatural word combinations;
- `CADENCE`: choppy short sentences, micro-paragraphs, or report/manual rhythm;
- `OVER_NOMINALIZATION`;
- `UNNEEDED_HEDGING` / `UNDER_HEDGING`;
- `REDUNDANT_SIGNALING`.

Prefer evidence-proximal prose: concrete subject + action + object statements, mechanism-specific wording, direct reporting of observations, and clear separation between observation and interpretation.

LANGUAGE OUTPUT — LANGUAGE CHANGE LEDGER:
For each proposed change provide:
- ID: L001, L002, ...
- Location.
- Category.
- Current wording.
- Suggested wording.
- Reason.
- Canonical term / PROSE_STYLE rule when relevant.
- Logic impact: `NONE` or `LOGIC_REVIEW_REQUIRED`.
- Confidence: HIGH / MEDIUM / LOW.

Do not provide a fully rewritten section. Do not propose stylistic alternatives with no clear precision/readability gain.

FULL OUTPUT:
For non-language findings provide:
- Severity: HIGH / MEDIUM / LOW.
- Category.
- File and section.
- Exact passage(s) or state entries.
- Canonical owner section when relevant.
- Why it matters.
- Primary repair action.
- Minimal repair strategy.
- Evidence/claim/dependency affected.

If LANGUAGE findings are present, append a separate Language Change Ledger.

Do not modify the manuscript. Approved language ledger items must be implemented later with `MODE: EXACT_EDIT`.
```

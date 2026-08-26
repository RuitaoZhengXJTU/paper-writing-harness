---
name: academic-language-reviewer
description: Review academic manuscript language without changing the paper's argumentative logic. Use under AUDIT with the LANGUAGE profile for terminology precision, wording consistency, defensive prose, vague academic phrasing, collocation, cadence, hedging, and professional factual expression. Read-only: propose a Language Change Ledger; do not edit paper/.
---

# Academic language reviewer

Operate under `MODE: AUDIT` with `AUDIT PROFILE: LANGUAGE`. This skill is read-only.

Guiding principle:

> Preserve what the paper means. Improve only how precisely it says it.

Prefer concrete, evidence-proximal scientific description over generic academic-sounding language.

## Required sources

Read before reviewing:

- `internal/PAPER_CONTRACT.yaml`;
- `internal/SECTION_CONTRACTS.yaml`;
- `internal/CLAIM_LEDGER.yaml`;
- `internal/TERMINOLOGY.yaml`;
- `internal/PROSE_STYLE.yaml`;
- the target passage, its adjacent paragraphs, and relevant parallel descriptions elsewhere in the manuscript.

## Logic lock

Language suggestions must not change:

- section or paragraph order;
- paragraph rhetorical role;
- the central claim of a paragraph;
- claim strength or causal direction;
- evidence interpretation;
- numerical values;
- equations or mathematical meaning;
- citations or what they support;
- assumptions, limitations, scope, or boundary conditions;
- methodological meaning;
- argument dependencies.

If a useful revision requires any of these changes, classify it as `LOGIC_REVIEW_REQUIRED` and do not propose a replacement sentence under this skill.

## Review categories

### `TERM_AMBIGUITY`
A technical term is vague, overloaded, or insufficiently defined.

### `TERM_DRIFT`
The same object is named differently across the manuscript without a meaningful distinction.

### `SEMANTIC_DRIFT`
Different verbs or modifiers change the implied technical meaning or claim strength, such as `predict`, `identify`, and `determine` being used interchangeably.

### `VAGUE_ACADEMICISM`
Generic evaluative phrases replace concrete mechanisms or observations, such as `improves flexibility`, `enhances performance`, or `provides superior efficiency` when a more specific statement is supported.

### `DEFENSIVE_PROSE`
The sentence mainly explains what the method is not, discusses abandoned/internal versions, anticipates hypothetical objections, or adds disclaimers that do not change scientific interpretation.

### `META_PROSE`
Phrases such as `it should be noted that`, `it is worth mentioning`, or prose about how the paper is written rather than the scientific content.

### `AI_FORMULAIC_PROSE`
Repeated generic emphasis, summary, contrast, or conclusion patterns that make the manuscript sound templated rather than specific to the scientific content.

### `COLLOCATION`
Grammar is acceptable but the word combination is unnatural, imprecise, or nonstandard in the technical context.

### `CADENCE`
Choppy short sentences, micro-paragraphs, mechanically uniform sentence structures, or other rhythm problems that make continuous academic reasoning read like a report or manual.

### `OVER_NOMINALIZATION`
Abstract noun phrases hide the actual scientific subject, action, or object.

### `UNNEEDED_HEDGING`
Hedges are present without a real epistemic reason.

### `UNDER_HEDGING`
Interpretation or uncertain evidence is stated too categorically.

### `REDUNDANT_SIGNALING`
Connectors, roadmap phrases, or summary clauses add little beyond the surrounding logical structure.

## Evidence-proximal prose test

For each vague or generic sentence, ask:

> Can this be stated as a more concrete subject + action + object description without changing scientific meaning?

Prefer the concrete version when it is supported by the manuscript state.

Do not convert a mechanism into a performance claim, or a design intention into an observed result.

## Terminology policy

Use `internal/TERMINOLOGY.yaml` as the canonical terminology source. When the manuscript reveals a stable term that is missing from the terminology file, recommend a terminology update separately; do not silently invent a new canonical term.

Distinguish deliberate technical distinctions from accidental synonym drift.

## Output: Language Change Ledger

Do not return a fully rewritten section. Return a ledger with one row/item per proposed language change:

- `ID`: `L001`, `L002`, ...;
- `Location`: file, section, paragraph/sentence;
- `Category`;
- `Current`;
- `Suggested`;
- `Reason`;
- `Canonical term / style rule` when relevant;
- `Logic impact`: normally `NONE`; otherwise `LOGIC_REVIEW_REQUIRED`;
- `Confidence`: `HIGH`, `MEDIUM`, or `LOW`.

Prioritize changes that improve precision, consistency, factuality, and readability. Do not flood the ledger with interchangeable stylistic alternatives.

## Approval and execution boundary

The ledger is advice only. Do not edit `paper/`.

After the user approves specific ledger IDs, implementation should use `MODE: EXACT_EDIT` and apply only those approved changes with a minimum diff.

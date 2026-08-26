# Paper Writing Harness

A repository-scoped workflow for using Codex/LLM agents to write and revise academic papers with explicit state, review gates, and reproducible editing rules.

Core workflow:

```text
exact change      → EXACT_EDIT
open design       → DESIGN_PREVIEW → PDF review → approval → APPLY_PREVIEW
quality review    → AUDIT → approve findings → EXACT_EDIT
```

## Quick start

### Existing paper repository

1. Open the repository root in Codex.
2. Copy [`prompts/INITIALIZE_EXISTING_REPOSITORY.md`](prompts/INITIALIZE_EXISTING_REPOSITORY.md) into a new agent session.
3. Review the generated repository migration and external-memory files.
4. Continue writing with the four modes below.

### New paper repository

Use this repository as a template, place manuscript sources under `paper/`, then initialize:

- `internal/PAPER_CONTRACT.yaml`
- `internal/SECTION_CONTRACTS.yaml`
- `internal/CLAIM_LEDGER.yaml`
- `internal/TERMINOLOGY.yaml`
- `internal/PROSE_STYLE.yaml`

## Four modes

| Mode | Use when | Writes `paper/`? |
|---|---|---:|
| `EXACT_EDIT` | The desired local change is already known | Yes |
| `DESIGN_PREVIEW` | Structure/prose is still being designed or reviewed | No |
| `APPLY_PREVIEW` | A specific preview ID + revision has been approved | Yes |
| `AUDIT` | Reviewing consistency, evidence, language, redundancy, or readiness | No |

---

# 1. EXACT_EDIT

Use for bounded changes to approved manuscript content. Unspecified content remains locked.

## Complete example

```text
MODE: EXACT_EDIT

TARGET:
- File: paper/sections/method.tex
- Section: 3.2 Guidance construction
- Target paragraphs: paragraphs 2–3

REQUIRED CHANGES:
1. Replace the current description of “migration links” with the canonical term “candidate migration arcs”.
2. Rewrite the first sentence of paragraph 3 to state directly that the learning model outputs guidance constraints for the screened stochastic program.
3. Remove the redundant final sentence of paragraph 3 because it repeats the same mechanism.

LOCKED CONTENT:
- Preserve paragraph order.
- Preserve Eq. (8), Eq. (9), all citations, labels, numerical values, and claim strength.
- Do not modify paragraphs outside the target range.
- Do not introduce new results, comparisons, or implementation details.

ALLOWED COLLATERAL CHANGES:
- Grammar or agreement repairs directly required by the requested edits.
- Terminology updates inside the target span required for consistency.

GLOBAL CONSISTENCY:
- Check whether “migration links” appears elsewhere with the same technical meaning.
- Report affected locations but do not modify them automatically.

ACCEPTANCE CRITERIA:
- The target passage consistently uses “candidate migration arcs”.
- The learning-model output is described once and directly.
- No scientific meaning, evidence, equation, citation, or paragraph responsibility changes.

OUTPUT:
- Apply the minimum sufficient diff.
- Show changed files and any stale dependent sections.
```

Recommended review:

```text
git diff
→ optional AUDIT
→ compile
→ commit
```

---

# 2. DESIGN_PREVIEW

Use when the section purpose is known but the structure/prose is not yet approved, including all PDF-annotation iterations on an active preview.

Each new preview receives its own directory:

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

`scratch/previews/INDEX.md` is the history index.

## Complete example

```text
MODE: DESIGN_PREVIEW

TARGET SECTION:
- Proposed location: paper/sections/method.tex
- Section: 3.3 Screened stochastic program
- Intended role: explain how learning outputs modify the stochastic program without repeating the learning-model architecture
- Preceding context: Section 3.2 defines the learning outputs
- Following context: Section 3.4 describes the rolling-window solution procedure

SECTION MUST EXPLAIN:
1. What information is received from the learning model.
2. How that information enters the stochastic program as guidance constraints.
3. What part of the original stochastic program remains unchanged.
4. Why the resulting optimization problem is smaller/easier to solve, only to the extent supported by the formulation or verified evidence.

AVAILABLE VERIFIED MATERIAL:
- Claims: C007, C008
- Equations: current stochastic-program formulation in Section 3.3
- Results: only results marked verified in results/manifest.yaml
- Figures: framework figure showing Learning model → guidance constraints → Screened SP

LOCKED DECISIONS:
- Use “Learning-Assisted Screened Stochastic Programming (LA-SSP)” as the method name.
- Use “Learning model” as the component name.
- Treat predicted outputs as guidance constraints.
- Do not claim global optimality.

MUST NOT INCLUDE:
- Local scripts or solver commands.
- Historical method names that are no longer part of the paper.
- A second explanation of the learning-model architecture.
- Unsupported runtime or complexity claims.

PREVIEW REQUIREMENTS:
- Create a NEW unique preview directory under scratch/previews/.
- Register it in scratch/previews/INDEX.md.
- Write the authoritative source to preview.md.
- Generate render/preview.tex from preview.md.
- Compile render/preview.pdf inside the same preview directory.
- Keep TeX auxiliary files inside render/.

PREVIEW.MD CONTENT:
- Preview ID + revision R1.
- Section thesis.
- Paragraph cards with stable P01, P02, ... IDs.
- Claim–evidence mapping.
- Complete unapproved preview prose.
- Assumptions, exclusions, missing evidence, dependencies.
- Acceptance checklist.

PDF REVIEW LOOP:
- PDF annotations are revision requests, not approval.
- Map every annotation back to preview.md.
- Record ACCEPTED / PARTIAL / REJECTED / BLOCKED decisions in review/decisions.md.
- Revise preview.md first.
- Regenerate TeX/PDF and increment the revision.

APPROVAL:
- Do not edit paper/ until I explicitly approve both preview ID and revision.

OUTPUT REPORT:
- Preview ID and revision.
- Preview directory.
- Markdown source path.
- PDF path and build status.
- Current INDEX.md status.
- Unresolved/blocked review items.
```

Typical loop:

```text
preview.md R1
→ preview.pdf R1
→ PDF annotations
→ preview.md R2
→ preview.pdf R2
→ ...
→ explicit approval
```

Detailed guide: [`docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md`](docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md)

---

# 3. APPLY_PREVIEW

Use only after a preview ID and revision have been explicitly approved.

## Complete example

```text
MODE: APPLY_PREVIEW

APPROVED PREVIEW:
- Preview ID: 20260825-1154-method-screening-a7f3
- Revision: R4
- Source: scratch/previews/20260825-1154-method-screening-a7f3/preview.md

TARGET:
- File: paper/sections/method.tex
- Section: 3.3 Screened stochastic program

LOCKED PREVIEW DECISIONS:
1. Keep the approved four-paragraph structure.
2. Use “guidance constraints” consistently.
3. Do not discuss deprecated method variants.
4. Do not add runtime, optimality, or performance claims beyond verified evidence.
5. Preserve existing equation numbers and citations unless integration requires a purely syntactic repair.

IMPLEMENTATION RULES:
- Read the approved preview.md as the source of truth.
- Implement only the approved revision.
- Do not copy review anchors, annotations, revision metadata, or generated TeX markup into the manuscript.
- Preserve unrelated manuscript content.
- Do not silently redesign the approved prose.
- Update CLAIM_LEDGER, SECTION_CONTRACTS, TERMINOLOGY, and stale-state files only when the approved manuscript state requires it.

VALIDATION:
- Compare the implemented section with the approved preview.md.
- Run publication, evidence, terminology, language-consistency, reference, and build checks.
- Report any integration change that differs from the approved preview.

OUTPUT:
- Changed files.
- Validation result.
- Differences from the approved preview, if any.
- Stale dependent sections.
```

Recommended next step:

```text
AUDIT → review findings → optional EXACT_EDIT
```

---

# 4. AUDIT

`AUDIT` is read-only. Select a profile:

```text
FULL         = whole quality pass
CONSISTENCY  = contradictions, duplication, ownership, terminology/notation, stale state
EVIDENCE     = claims, results, citations, numbers, assumptions/limitations
LANGUAGE     = terminology precision, wording consistency, professional factual prose
```

## Complete example — FULL

```text
MODE: AUDIT
AUDIT PROFILE: FULL

SCOPE:
- Files changed in the current manuscript revision.
- Include adjacent and declared dependent sections: YES
- Include whole-manuscript semantic duplication scan: YES

AUTOFIX: NO

CHECKS:
- Central contribution and scope consistency.
- Claim strength and evidence support.
- Numerical, terminology, notation, equation, citation, figure, and table consistency.
- Semantic duplication across non-adjacent sections.
- Canonical information ownership.
- Over-expression and report/manual-style micro-paragraphs.
- Defensive prose and unnecessary historical/internal framing.
- Publication-boundary leakage.
- Language precision and professional factual expression.

REPAIR POLICY:
- Prefer KEEP / DELETE / MERGE / COMPRESS / RELOCATE / REWRITE as a single primary action per finding.
- Do not edit paper/.

OUTPUT:
- HIGH / MEDIUM / LOW findings.
- Exact locations and passages.
- Canonical owner when duplication is involved.
- Minimal repair strategy.
- A separate Language Change Ledger for language findings.
```

## Complete example — LANGUAGE

Use this when the logic is already accepted and only the wording should be reviewed.

```text
MODE: AUDIT
AUDIT PROFILE: LANGUAGE

SCOPE:
- File: paper/sections/method.tex
- Section: 3.2–3.3
- Compare parallel terminology with the rest of the manuscript: YES

AUTOFIX: NO

LOGIC LOCK:
- Preserve section and paragraph order.
- Preserve each paragraph's rhetorical role.
- Preserve claims, claim strength, causal direction, evidence interpretation, numbers, equations, citations, assumptions, limitations, and methodological meaning.

CHECKS:
- TERM_AMBIGUITY
- TERM_DRIFT
- SEMANTIC_DRIFT
- VAGUE_ACADEMICISM
- DEFENSIVE_PROSE
- META_PROSE
- AI_FORMULAIC_PROSE
- COLLOCATION
- CADENCE
- OVER_NOMINALIZATION
- UNNEEDED_HEDGING / UNDER_HEDGING
- REDUNDANT_SIGNALING

STYLE SOURCE:
- internal/TERMINOLOGY.yaml
- internal/PROSE_STYLE.yaml

OUTPUT:
Return a Language Change Ledger only:
- ID: L001, L002, ...
- Location.
- Category.
- Current wording.
- Suggested wording.
- Reason.
- Canonical term/style rule.
- Logic impact: NONE or LOGIC_REVIEW_REQUIRED.
- Confidence.

Do not rewrite the full section and do not modify paper/.
```

After review:

```text
APPROVE: L001, L003, L006
REJECT: L002
```

Then apply approved items with `EXACT_EDIT` only.

Language workflow: [`docs/LANGUAGE_REVIEW_WORKFLOW.zh-CN.md`](docs/LANGUAGE_REVIEW_WORKFLOW.zh-CN.md)

---

## Repository map

```text
paper/                   manuscript
internal/                paper state, claims, terminology, prose style
scratch/previews/        isolated preview history + PDF review bundles
results/                 verified/provisional evidence
.agents/skills/          reusable writing/review workflows
.codex/                  hooks and deterministic guards
prompts/                  copy-ready mode prompts
docs/                    workflow guides
```

Key files:

- [`AGENTS.md`](AGENTS.md)
- [`internal/TERMINOLOGY.yaml`](internal/TERMINOLOGY.yaml)
- [`internal/PROSE_STYLE.yaml`](internal/PROSE_STYLE.yaml)
- [`prompts/EXACT_EDIT.md`](prompts/EXACT_EDIT.md)
- [`prompts/DESIGN_PREVIEW.md`](prompts/DESIGN_PREVIEW.md)
- [`prompts/APPLY_PREVIEW.md`](prompts/APPLY_PREVIEW.md)
- [`prompts/AUDIT.md`](prompts/AUDIT.md)
- [`docs/SINGLE_EDIT_WORKFLOW.zh-CN.md`](docs/SINGLE_EDIT_WORKFLOW.zh-CN.md)
- [`docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md`](docs/PREVIEW_PDF_REVIEW_WORKFLOW.zh-CN.md)
- [`docs/LANGUAGE_REVIEW_WORKFLOW.zh-CN.md`](docs/LANGUAGE_REVIEW_WORKFLOW.zh-CN.md)

## Daily workflows

```text
Exact revision:
EXACT_EDIT → diff review → optional AUDIT → compile → commit

Structural revision:
DESIGN_PREVIEW → PDF review loop → approve preview ID + revision
→ APPLY_PREVIEW → AUDIT → EXACT_EDIT if needed → compile → commit

Language revision:
AUDIT: LANGUAGE → Language Change Ledger → approve IDs
→ EXACT_EDIT → diff review → compile
```

# Academic Manuscript Operating Contract

## Artifact boundaries

- `paper/` contains reviewer-facing manuscript content only.
- `internal/` contains project memory, provenance, decisions, terminology, prose style, and audit state.
- `scratch/` contains unapproved previews, review renders, annotations, and exploratory drafts.
- `results/verified/` may support factual manuscript claims.
- `results/provisional/` may not support unqualified manuscript claims.

## Mandatory task modes

Every writing task uses exactly one mode:

- `EXACT_EDIT`: make the minimum sufficient change to approved manuscript content. All unspecified prose, equations, citations, labels, and ordering are locked.
- `DESIGN_PREVIEW`: design or iteratively revise unapproved prose inside one isolated `scratch/previews/<preview-id>/` bundle. Markdown is authoritative; TeX/PDF are review views.
- `APPLY_PREVIEW`: implement only an explicitly approved preview ID + revision from its `preview.md`.
- `AUDIT`: read-only review. Use profiles `FULL`, `LANGUAGE`, `CONSISTENCY`, or `EVIDENCE`.

PDF annotations on an unapproved preview remain `DESIGN_PREVIEW`. Material ambiguity defaults to `DESIGN_PREVIEW`.

A request to make manuscript language more professional, precise, consistent, factual, or natural **without changing the logic** defaults to `AUDIT PROFILE: LANGUAGE`, not direct rewriting. Approved language findings are later implemented with `EXACT_EDIT`.

## Source of truth

Before manuscript edits or audits, read the relevant state files:

- `internal/PAPER_CONTRACT.yaml`
- `internal/SECTION_CONTRACTS.yaml`
- `internal/CLAIM_LEDGER.yaml`
- `internal/TERMINOLOGY.yaml`
- `internal/PROSE_STYLE.yaml`
- target text, adjacent text, and declared dependent/parallel sections

Repository state overrides stale conversation memory.

For preview work, `scratch/previews/<preview-id>/preview.md` is authoritative. Generated TeX/PDF are disposable review derivatives.

## Publication and evidence boundary

Reviewer-facing prose should describe the scientific problem, mechanism, formulation, evidence, and implications at the level required for understanding and reproducibility.

Keep local paths, internal scripts, shell commands, agent/tool narration, debugging chronology, prompt iteration, workflow metadata, and unsupported results outside manuscript prose.

Never strengthen claims during rewriting. Do not turn “may” into “does,” “designed to” into “achieves,” a hypothesis into a demonstration, an association into causation, or provisional evidence into verified evidence. Never invent citations, values, baselines, significance, complexity claims, or settings.

## Minimal-delta editing

For each manuscript edit:

1. identify editable span;
2. lock surrounding content;
3. identify stale dependencies;
4. make the minimum patch;
5. inspect the diff;
6. validate;
7. update state or mark dependent sections stale.

## Global consistency

Check contribution and scope, canonical terminology and notation, method names, datasets/baselines/metrics, numerical values and evidence status, equations/figures/tables/citations/references, claim strength, cross-section dependencies, semantic duplication, paragraph-level continuity, and information ownership.

A concept should have one canonical explanatory home. Elsewhere retain only the compressed form required by that section’s rhetorical role.

## Preview storage isolation

`scratch/previews/` is an index-and-directory container, not a shared compilation workspace. Its root may contain only documentation/index files and child preview directories.

Every new preview receives a fresh human-browsable ID, preferably:

```text
YYYYMMDD-HHMM-<section-slug>-<short-id>
```

Never reuse or overwrite another preview directory. A materially new design alternative creates a new directory; annotation-driven revisions of the same preview remain in the existing directory and increment `R1`, `R2`, ...

Required layout:

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

Keep all TeX auxiliary files inside that preview’s `render/` directory. Maintain `scratch/previews/INDEX.md` with preview ID, target, creation time, revision, status, and path.

## Preview review loop

For every PDF annotation round:

1. map annotations to the matching paragraph/span in `preview.md`;
2. record decisions in `review/decisions.md`;
3. revise Markdown first;
4. regenerate TeX/PDF;
5. increment revision and update the preview index.

Explicit approval of preview ID + revision is required before `APPLY_PREVIEW`.

## Audit profiles

### `FULL`
Run consistency, evidence, language, duplication, ownership, cohesion, and publication-boundary checks.

### `CONSISTENCY`
Focus on contradictions, stale statements, terminology/notation drift, numbers, semantic duplication, canonical information ownership, and cross-section responsibilities.

### `EVIDENCE`
Focus on claim strength, verified/provisional status, citation support, numerical provenance, assumptions, limitations, and stale claims.

### `LANGUAGE`
Use `academic-language-reviewer`. Apply a strict logic lock: do not change section/paragraph order, paragraph rhetorical role, central claim, claim strength, causal direction, evidence interpretation, numbers, equations, citations, scope, limitations, or methodological meaning.

Check terminology precision, wording consistency, semantic-strength drift, vague academicism, defensive/meta prose, formulaic AI phrasing, collocation, cadence, nominalization, hedging, and redundant signaling.

Prefer evidence-proximal prose: concrete subject + action + object statements, mechanism-specific language, direct reporting of observations, and explicit separation of observation from interpretation.

Return a `Language Change Ledger` (`L001`, `L002`, ...) rather than a fully rewritten section. The ledger is advice only; approved items are implemented later with `EXACT_EDIT`.

## Audit repair discipline

Prefer `DELETE`, `MERGE`, `COMPRESS`, or `RELOCATE` when meaning is already present. Do not solve redundancy or defensive writing by adding more explanation.

Preserve scientifically necessary assumptions, limitations, boundary conditions, negative results, and caveats.

## Ownership and completion

Only the main writing agent edits `paper/`. Reviewer agents are read-only.

After work, report mode/profile, files changed or reviewed, intentionally preserved scope, checks run, unresolved high-severity issues, stale sections, assumptions, and placeholders. Preview work also reports preview ID, directory, revision, render paths, annotation status, and approval state.

Detailed workflows live under `.agents/skills/`, `prompts/`, and `docs/`.

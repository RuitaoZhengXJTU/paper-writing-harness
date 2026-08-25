# Academic Manuscript Operating Contract

## Artifact boundaries

- `paper/` contains reviewer-facing manuscript content only.
- `internal/` contains project memory, provenance, implementation analysis, decisions, and audit state.
- `scratch/` contains unapproved previews, review renders, annotations, and exploratory drafts.
- `results/verified/` may support factual manuscript claims.
- `results/provisional/` may not support unqualified manuscript claims.

The manuscript is not a project diary. Never copy internal analysis directly into `paper/`.

## Mandatory task modes

Every writing task uses exactly one mode:

- `EXACT_EDIT`: make the minimum sufficient change. All unspecified prose, equations, citations, labels, and ordering are locked. Report broader issues separately.
- `DESIGN_PREVIEW`: do not edit `paper/`. Build and iteratively revise one isolated preview bundle under `scratch/previews/<preview-id>/`. Every newly created preview must receive a new unique directory; never place preview Markdown, TeX, or PDF files directly in `scratch/previews/`.
- `APPLY_PREVIEW`: implement only an explicitly approved preview ID and revision. Read the approved Markdown preview as the source of truth; do not silently redesign it from the rendered PDF.
- `AUDIT`: read-only by default. Report contradictions, evidence gaps, notation drift, stale sections, publication-boundary leakage, semantic duplication, over-expression, defensive writing, and misplaced explanatory ownership with locations and minimal repairs.

When exact constraints and open design are mixed, preserve the exact constraints as locked and route the open portion to `DESIGN_PREVIEW`. PDF annotations on an unapproved preview remain `DESIGN_PREVIEW`; they are review instructions, not authorization to edit `paper/`. Material ambiguity defaults to `DESIGN_PREVIEW`.

## Source of truth

Before manuscript edits, read:

- `internal/PAPER_CONTRACT.yaml`
- `internal/SECTION_CONTRACTS.yaml`
- `internal/CLAIM_LEDGER.yaml`
- `internal/TERMINOLOGY.yaml`
- the target section, adjacent sections, and declared dependent sections

Repository state overrides stale conversation memory.

For preview work, `scratch/previews/<preview-id>/preview.md` is authoritative. `render/preview.tex` and `render/preview.pdf` are disposable derivatives used for visual review. Never patch generated TeX as the primary source of a preview revision.

## Publication boundary

Unless scientifically necessary and explicitly authorized, manuscript prose must not contain local paths, internal scripts, shell commands, agent/tool narration, debugging chronology, prompt iteration, workflow metadata, or unverified results.

Classify implementation information as:

1. scientifically necessary in main text;
2. reproducibility detail for appendix/supplement/repository docs;
3. internal provenance only;
4. unsupported and prohibited.

Prefer scientific abstraction over repository-specific mechanics.

## Minimal-delta and evidence rules

For each edit: identify editable span, lock surrounding content, identify stale dependencies, patch minimally, inspect the diff, validate, and mark dependent sections stale rather than rewriting outside scope.

Never strengthen claims during rewriting. Do not turn “may” into “does,” “designed to” into “achieves,” a hypothesis into a demonstration, an association into causation, or provisional evidence into verified evidence. Never invent citations, values, baselines, complexity claims, significance, or settings.

## Global checks

Check contribution and scope, terminology and notation, method names, datasets/baselines/metrics, numerical values and evidence status, equations/figures/tables/citations/references, claim strength, cross-section dependencies, duplication, contradictions, publication-boundary leakage, paragraph-level rhetorical continuity, and information ownership across sections.

Prefer deletion, merging, compression, or relocation over adding defensive explanation. A concept should have one canonical explanatory home. Repetition in the abstract, introduction, discussion, or conclusion is acceptable only when it performs a distinct rhetorical role and is materially compressed relative to the owning section.

## Preview storage isolation

`scratch/previews/` is an index-and-directory container, not a compilation workspace. Its root may contain only repository documentation/index files and child preview directories. Do not write preview prose, `.tex`, `.pdf`, auxiliary build files, or annotation artifacts directly into the root.

Every newly created preview must use a unique, human-browsable ID and a fresh directory. Prefer:

```text
YYYYMMDD-HHMM-<section-slug>-<short-id>
```

Example:

```text
scratch/previews/20260825-1154-method-screening-a7f3/
```

Before creating a preview, check that the directory does not already exist. Never reuse or overwrite another preview directory, even for the same manuscript section. A materially new design alternative is a new preview and therefore a new directory. Annotation-driven revisions of the same design remain inside the existing preview directory and increment the revision (`R1`, `R2`, ...).

Required per-preview layout:

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

Keep TeX auxiliary files inside `render/` or a subdirectory of it; never allow one preview's build artifacts to mix with another preview.

Maintain `scratch/previews/INDEX.md`. Each new preview adds one entry containing preview ID, target section, creation time, current revision, status (`ACTIVE`, `APPROVED`, `REJECTED`, or `SUPERSEDED`), and relative path. Updating an existing preview changes only that preview's index entry; it does not create loose files at the preview root.

## Preview discipline

A preview bundle contains a stable preview ID and revision, target, thesis, paragraph cards, complete unapproved preview prose, claim/evidence needs, transitions, exclusions, uncertainties, proposed equations/figures/tables, affected sections, assumptions, and acceptance checklist.

After `preview.md` is created, render only the previewed manuscript content to a standalone TeX/PDF review artifact inside that preview's own `render/` directory. Use stable paragraph anchors so PDF annotations can be mapped back to Markdown. During annotation review:

1. read PDF annotations and map each one to the relevant Markdown paragraph/span;
2. record the annotation decision in that preview's `review/decisions.md`;
3. modify that preview's `preview.md` first;
4. regenerate that preview's `render/preview.tex` from Markdown;
5. recompile that preview's `render/preview.pdf`;
6. increment the preview revision and update `scratch/previews/INDEX.md`.

Do not edit `paper/` during this loop. A clean annotation round is not approval; explicit approval of a preview ID and revision is required.

## Audit discipline

`AUDIT` must distinguish scientific necessity from agent-generated over-explanation. Flag defensive writing when prose explains historical/abandoned approaches, repeatedly states what the method does not do, anticipates hypothetical objections without need, or adds disclaimers that do not change interpretation. Flag over-expression when adjacent sentences or paragraphs restate the same point, explain obvious implications, repeat contribution statements, or use extra framing without adding evidence or reasoning.

For duplicated content, identify the canonical owner section using `SECTION_CONTRACTS.yaml` and `CLAIM_LEDGER.yaml`. Recommend `KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, or `REWRITE`; do not solve redundancy by adding more prose.

## Ownership and completion

Only the main writing agent edits `paper/`. Subagents are read-only reviewers. Do not run overlapping manuscript edits concurrently.

After work, report mode, files changed, intentionally preserved scope, checks run, unresolved high-severity issues, stale sections, assumptions, and placeholders. For preview work also report preview ID, preview directory, revision, Markdown source path, render paths, annotation status, and whether explicit approval has been received. Detailed workflows live under `.agents/skills/` and `docs/`.

# Academic Manuscript Operating Contract

## Artifact boundaries

- `paper/` contains reviewer-facing manuscript content only.
- `internal/` contains project memory, provenance, implementation analysis, decisions, and audit state.
- `scratch/` contains unapproved previews and exploratory drafts.
- `results/verified/` may support factual manuscript claims.
- `results/provisional/` may not support unqualified manuscript claims.

The manuscript is not a project diary. Never copy internal analysis directly into `paper/`.

## Mandatory task modes

Every writing task uses exactly one mode:

- `EXACT_EDIT`: make the minimum sufficient change. All unspecified prose, equations, citations, labels, and ordering are locked. Report broader issues separately.
- `DESIGN_PREVIEW`: do not edit `paper/`. Save a paragraph-level design under `scratch/previews/`, including claims, evidence, exclusions, assumptions, dependencies, and acceptance criteria.
- `APPLY_PREVIEW`: implement only an explicitly approved preview and its locked decisions. Do not silently redesign it.
- `AUDIT`: read-only by default. Report contradictions, duplication, evidence gaps, notation drift, stale sections, and publication-boundary leakage with locations and minimal repairs.

When exact constraints and open design are mixed, preserve the exact constraints as locked and route the open portion to `DESIGN_PREVIEW`. Material ambiguity defaults to `DESIGN_PREVIEW`.

## Source of truth

Before manuscript edits, read:

- `internal/PAPER_CONTRACT.yaml`
- `internal/SECTION_CONTRACTS.yaml`
- `internal/CLAIM_LEDGER.yaml`
- `internal/TERMINOLOGY.yaml`
- the target section, adjacent sections, and declared dependent sections

Repository state overrides stale conversation memory.

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

Check contribution and scope, terminology and notation, method names, datasets/baselines/metrics, numerical values and evidence status, equations/figures/tables/citations/references, claim strength, cross-section dependencies, duplication, contradictions, and publication-boundary leakage.

## Preview discipline

A preview contains a stable ID, target, thesis, paragraph cards, claim/evidence needs, transitions, exclusions, uncertainties, proposed equations/figures/tables, affected sections, assumptions, and acceptance checklist. Polished prose is not approval.

## Ownership and completion

Only the main writing agent edits `paper/`. Subagents are read-only reviewers. Do not run overlapping manuscript edits concurrently.

After work, report mode, files changed, intentionally preserved scope, checks run, unresolved high-severity issues, stale sections, assumptions, and placeholders. Detailed workflows live under `.agents/skills/` and `docs/`.

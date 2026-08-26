# One-Shot Paper Repository Refactoring and Writing-Harness Bootstrap Prompt

You are operating inside the root of my existing academic-paper project repository. Perform the repository refactor and writing-harness initialization described below in this run. Do not merely propose a plan or print templates: inspect the repository, make the changes, validate them, and leave the repository in a usable state.

Use the current conversation context as an additional source of project intent and prior decisions. Treat repository files as the primary source of truth when they conflict with conversational memory. Do not invent scientific claims, numerical results, citations, or project facts. Represent unresolved information explicitly as `unknown`, `unverified`, or a documented assumption.

## 0. Mission

Refactor this repository into a paper-writing workspace that separates:

1. reviewer-facing manuscript content;
2. internal project analysis and implementation provenance;
3. unapproved writing previews and alternatives;
4. verified versus provisional experimental evidence;
5. persistent paper state that survives chat resets and context compaction;
6. reusable Codex writing skills;
7. deterministic hooks and validation scripts.

The resulting harness must prevent four recurring failures:

- Internal implementation or agent-explanation details leaking into the paper.
- Local section edits causing contradictions, duplicated explanations, stale claims, or terminology drift elsewhere.
- Confusion between exact/surgical editing and open-ended structural design.
- Polished previews being mistaken for approved, evidence-backed manuscript content.

This is a repository-scoped migration. Create or update the repository-root `AGENTS.md`; do not attempt to alter Codex’s built-in system prompt. Do not modify `~/.codex/AGENTS.md` or other user-global configuration.

## 1. Execution policy

Proceed autonomously and conservatively.

### Required behavior

- Inspect before editing.
- Preserve all existing scientific content unless migration requires a path-only change.
- Prefer `git mv` for tracked files when a move is safe.
- Preserve Git history where practical.
- Do not commit, push, reset, stash, rebase, or discard changes.
- Do not install packages or access the network.
- Do not delete source files merely because they appear obsolete.
- Do not overwrite uncommitted user work.
- Do not rewrite manuscript prose as part of the structural migration, except for path/reference repairs strictly required by the move.
- Do not silently “improve” equations, claims, section order, terminology, citations, or experimental statements.
- Do not convert provisional evidence into verified evidence.
- Do not fabricate missing values to make YAML files look complete.
- Keep the existing build system working, or document precisely why it cannot be verified.
- Use the repository’s current file format and toolchain. Support LaTeX, Typst, Markdown/Pandoc, Quarto, or another detected format rather than assuming LaTeX.

### Ambiguity policy

When a decision is uncertain:

1. choose the least destructive reversible option;
2. preserve the original;
3. record the ambiguity in `internal/MIGRATION_NOTES.md`;
4. mark affected fields `unknown` or `needs_review`;
5. continue with all work that remains safe.

Do not stop merely because some scientific metadata is unknown.

### Existing harness policy

If `AGENTS.md`, `.agents/skills/`, `.codex/hooks.json`, or similarly purposed files already exist:

- read and preserve useful project-specific rules;
- merge rather than blindly replace;
- remove direct contradictions only when the new paper-writing contract clearly supersedes them;
- record important merged or superseded rules in `internal/MIGRATION_NOTES.md`;
- do not duplicate skills under both `.codex/skills` and `.agents/skills`;
- use `.agents/skills` as the repository-scoped skill location.

## 2. Preflight inspection

Before modifying files, inspect and record:

- repository root;
- Git status and current branch, when Git is available;
- existing instruction sources such as `AGENTS.md`, `AGENTS.override.md`, `.codex/config.toml`, `.codex/hooks.json`, and skills;
- repository tree, excluding large build/cache/vendor directories;
- manuscript candidates and likely primary entry point;
- document format and build tool;
- inclusion/import graph for manuscript sections;
- bibliography files;
- figures, tables, appendices, style/class/template files;
- build scripts, Makefiles, task runners, CI workflows, and README commands that reference manuscript paths;
- experiment outputs and scripts referenced by the manuscript;
- generated artifacts and temporary files;
- all uncommitted files that the migration must preserve.

Create `internal/MIGRATION_INVENTORY.md` as an auditable snapshot. Include:

- detected manuscript entry point;
- detected build command;
- old manuscript-related paths;
- classification of each path;
- whether the path will be moved, retained, copied, or only re-referenced;
- unresolved ambiguities;
- baseline Git commit hash when available;
- pre-existing uncommitted changes, summarized without altering them.

Do not treat PDFs, AUX files, logs, caches, or generated plots as source merely because they are near the manuscript.

## 3. Identify the canonical manuscript

Use evidence such as:

- `\documentclass`, `\begin{document}`, `\input`, `\include`;
- Typst imports;
- Pandoc/Quarto configuration;
- build scripts and CI;
- README instructions;
- recently modified files;
- abstract, introduction, method, experiments, and conclusion structure;
- current conversation context.

If multiple independent manuscripts exist, do not merge them. Select the primary manuscript only when evidence is strong. Leave unrelated manuscripts in place or place them in a clearly documented `paper/other/` area only when doing so is safe. Record the choice and evidence in `internal/MIGRATION_NOTES.md`.

## 4. Target repository structure

Adapt the structure to the detected authoring format, but converge on the following conceptual layout:

```text
<repo-root>/
├── AGENTS.md
├── paper/
│   ├── main.<ext>
│   ├── sections/
│   ├── appendices/
│   ├── figures/
│   ├── tables/
│   ├── bibliography/
│   ├── styles/
│   ├── generated/
│   ├── build/
│   └── README.md
├── internal/
│   ├── PAPER_CONTRACT.yaml
│   ├── SECTION_CONTRACTS.yaml
│   ├── CLAIM_LEDGER.yaml
│   ├── TERMINOLOGY.yaml
│   ├── PROSE_STYLE.yaml
│   ├── DECISIONS.md
│   ├── CHANGELOG.md
│   ├── STALE_SECTIONS.yaml
│   ├── EVIDENCE_INDEX.yaml
│   ├── MIGRATION_INVENTORY.md
│   ├── MIGRATION_MAP.yaml
│   ├── MIGRATION_NOTES.md
│   └── README.md
├── scratch/
│   ├── previews/
│   ├── analysis/
│   ├── rejected-drafts/
│   └── README.md
├── results/
│   ├── verified/
│   ├── provisional/
│   ├── manifest.yaml
│   └── README.md
├── .agents/
│   └── skills/
│       ├── paper-router/
│       │   └── SKILL.md
│       ├── surgical-edit/
│       │   └── SKILL.md
│       ├── section-architect/
│       │   └── SKILL.md
│       ├── manuscript-composer/
│       │   └── SKILL.md
│       ├── consistency-auditor/
│       │   └── SKILL.md
│       ├── academic-language-reviewer/
│       │   └── SKILL.md
│       └── publication-filter/
│           └── SKILL.md
└── .codex/
    ├── hooks.json
    └── hooks/
        ├── common.py
        ├── load_paper_context.py
        ├── paper_guard.py
        └── consistency_check.py
```

Rules for adapting this layout:

- Preserve repository-standard names when changing them would break tooling without benefit.
- Keep code, data-processing, model, solver, and experiment source directories where they are unless they are currently mixed into the manuscript directory.
- Move only manuscript source and manuscript-owned assets.
- Shared experiment outputs may remain in their original location; reference them through `results/manifest.yaml` rather than duplicating large files.
- Do not move large datasets or environment directories.
- Put generated paper output under `paper/build/` or the existing equivalent and update `.gitignore`.
- Do not create empty decorative directories unless they serve the detected project.
- Add `.gitkeep` only when repository conventions require it.
- If the primary manuscript is a single file, still use `paper/main.<ext>` but do not split it into sections during this migration.
- If it is already split, preserve the logical split and filenames unless a collision requires a minimal rename.

## 5. Safe manuscript migration

Perform a real migration, not a second disconnected copy.

### Migration steps

1. Build a source-to-destination map in `internal/MIGRATION_MAP.yaml`.
2. Move the primary manuscript entry point to `paper/main.<ext>` when safe.
3. Move included manuscript source files into `paper/sections/` or `paper/appendices/` according to their actual role.
4. Move manuscript-exclusive figures, tables, bibliography, and style/template files into the corresponding `paper/` subdirectories.
5. Keep shared code-generated evidence in its original location when moving it would break experiment workflows.
6. Update every affected include/import, bibliography, image, table, style, class, script, Makefile, CI, editor task, README, and build path.
7. Search for stale references to every old path.
8. Preserve case sensitivity and cross-platform path behavior.
9. Avoid absolute paths.
10. Update `.gitignore` for the new build location without hiding source files.

When the old location is referenced by external tooling that cannot safely be updated, retain a small compatibility wrapper or documented forwarding file rather than duplicating the manuscript silently. Explain the compatibility choice in `internal/MIGRATION_NOTES.md`.

Do not change the semantic content of manuscript paragraphs while relocating files. Path-only syntax edits and build fixes are allowed.

## 6. Initialize persistent external paper memory

Infer the following files from the current conversation and repository. Use manuscript evidence first, then project documentation, then internal notes, then conversation context. Every inferred scientific item must carry evidence and confidence.

### 6.1 `internal/PAPER_CONTRACT.yaml`

Use a schema equivalent to:

```yaml
schema_version: 1
updated_at: "<ISO-8601>"
paper:
  title:
    value: null
    confidence: unknown
    evidence: []
  target_venue:
    value: null
    confidence: unknown
    evidence: []
  audience:
    value: null
    confidence: unknown
    evidence: []
  central_problem:
    value: null
    confidence: unknown
    evidence: []
  central_thesis:
    value: null
    confidence: unknown
    evidence: []
  central_contribution:
    value: null
    confidence: unknown
    evidence: []
  contribution_boundaries:
    included: []
    excluded: []
  non_contributions: []
  reviewer_takeaway:
    value: null
    confidence: unknown
    evidence: []
  disclosure_policy:
    main_text:
      include: []
      exclude: []
    appendix_or_supplement:
      include: []
    repository_documentation:
      include: []
  writing_priorities:
    - scientific_correctness
    - evidence_integrity
    - global_consistency
    - concise_reviewer_facing_exposition
  unresolved_questions: []
```

Initialization rules:

- Quote or paraphrase only claims actually supported by the repository.
- Use repository-relative `path#section-or-line` evidence references where possible.
- Record conversation-derived evidence as `conversation_context` and mark its confidence conservatively.
- Put internal code paths and commands only in evidence/provenance fields, never as proposed manuscript wording.
- Include the known writing policy: the paper should focus on model structure, formulation, scientific reasoning, essential algorithmic design, evidence, and implications; operational solver setup and local execution details should normally be abstracted or delegated to appendix/repository documentation.

### 6.2 `internal/SECTION_CONTRACTS.yaml`

Create one entry for every detected manuscript section:

```yaml
schema_version: 1
sections:
  <stable_section_id>:
    title: ""
    source_files: []
    purpose: null
    central_takeaway: null
    owns_claims: []
    may_reference_claims: []
    required_inputs: []
    required_outputs: []
    dependencies: []
    invalidates_when_changed: []
    must_include: []
    must_not_include: []
    status: current
    confidence: unknown
    evidence: []
    unresolved_questions: []
```

Infer dependencies such as:

- abstract depends on the final contribution and headline results;
- introduction depends on method and experiments;
- method changes may stale abstract, introduction, experiments, discussion, and conclusion;
- result changes may stale abstract, introduction, discussion, and conclusion.

Do not assume all sections exist. Use detected sections.

### 6.3 `internal/CLAIM_LEDGER.yaml`

Extract major claims from the title, abstract, contribution list, method, results, discussion, and conclusion. Avoid cataloging every sentence.

```yaml
schema_version: 1
claims:
  C001:
    canonical: ""
    type: contribution
    strength: bounded
    status: unverified
    evidence:
      kind: null
      sources: []
    owned_by: null
    allowed_mentions: []
    forbidden_strengthenings: []
    known_variants: []
    conflicts: []
    notes: []
```

Allowed `status` values:

- `verified`
- `bounded`
- `provisional`
- `placeholder`
- `unverified`
- `contradicted`
- `prohibited`

Allowed `strength` values may include:

- `descriptive`
- `hypothesis`
- `bounded`
- `comparative`
- `causal`
- `guarantee`

Never classify a claim as `verified` solely because it appears in the manuscript. Verification requires traceable evidence.

### 6.4 `internal/TERMINOLOGY.yaml`

Capture:

- canonical paper/model/method names;
- abbreviations and first-use forms;
- mathematical notation;
- dataset, baseline, metric, and solver names;
- capitalization and hyphenation;
- forbidden or deprecated variants;
- semantic distinctions that must not be collapsed.

Use:

```yaml
schema_version: 1
terms:
  <term_id>:
    canonical: ""
    category: ""
    first_use: null
    allowed_variants: []
    forbidden_variants: []
    definition: null
    evidence: []
    conflicts: []
```

Do not mechanically declare ordinary prose synonyms forbidden unless the manuscript clearly requires a canonical technical term.

### 6.5 Other memory files

Create:

- `internal/DECISIONS.md`: dated, concise decisions reconstructed from repository history, comments, and conversation context; clearly distinguish explicit decisions from inferred ones.
- `internal/CHANGELOG.md`: initialize with this harness migration and reserve a consistent entry format for future manuscript changes.
- `internal/STALE_SECTIONS.yaml`: initialize every detected section as `current`, except sections already found inconsistent; include reasons and triggering claims.
- `internal/EVIDENCE_INDEX.yaml`: map verified/provisional results, figures, tables, theorem/proof sources, data-generation scripts, and bibliography sources.
- `internal/PROSE_STYLE.yaml`: define concise factual-academic prose rules, evidence-proximal expression, paragraph/cadence rules, hedging policy, and common language anti-patterns. Keep it compact and use `TERMINOLOGY.yaml` as the canonical technical vocabulary source.
- `results/manifest.yaml`: classify available result artifacts without moving large data. Every item must include source path, status, provenance, generated-by, manuscript consumers, and verification notes.
- `internal/README.md`: explain that these files are private project memory and are not manuscript prose.
- `scratch/README.md`: explain approval semantics and the one-preview-per-directory storage invariant.
- `scratch/previews/INDEX.md`: initialize a historical preview index and prohibit loose preview/build files at the preview root.
- `results/README.md`: explain verified versus provisional evidence.

### External-memory quality gate

Before finishing:

- ensure YAML parses;
- ensure paths are repository-relative;
- ensure no unsupported numeric claim is marked verified;
- ensure no internal implementation detail is accidentally proposed as reviewer-facing text;
- ensure unknowns remain visible rather than guessed;
- ensure section IDs and claim IDs are stable and unique.

## 7. Create the repository-root `AGENTS.md`

Keep `AGENTS.md` concise enough for reliable discovery. Put detailed workflows into skills. Preserve useful existing project instructions and incorporate the following mandatory contract.

The final `AGENTS.md` must include these sections and enforce their meaning:

### 7.1 Repository artifact boundaries

- `paper/` is reviewer-facing.
- `internal/` is project memory, provenance, implementation analysis, decisions, and audit state.
- `scratch/` is unapproved exploratory content.
- `results/verified/` supports factual claims.
- `results/provisional/` cannot support unqualified manuscript claims.
- The manuscript is not a project diary.
- Never copy internal analysis directly into the paper.

### 7.2 Mandatory task modes

Every writing task must use exactly one mode:

#### `EXACT_EDIT`

Use when wording, formula, ordering, or a local transformation is specified.

- minimum sufficient diff;
- unspecified content is locked;
- do not rewrite adjacent prose unless required by the requested edit;
- report broader problems separately;
- do not silently remove “redundant” content.

#### `DESIGN_PREVIEW`

Use when purpose or structure is known but prose is not approved, including all review iterations on an unapproved preview PDF.

- do not edit `paper/`;
- every NEW preview must receive a NEW unique directory under `scratch/previews/`;
- prefer preview IDs `YYYYMMDD-HHMM-<section-slug>-<short-id>` and verify the directory does not already exist before creating it;
- never place preview Markdown, TeX, PDF, annotation, or TeX auxiliary files directly in `scratch/previews/`;
- never reuse or overwrite another preview directory, even for the same manuscript section;
- a materially new design alternative creates a new preview directory, while annotation-driven revisions of the same design stay in the existing directory and increment the revision;
- maintain `scratch/previews/INDEX.md` with preview ID, target, creation time, latest revision, status, and relative path;
- create the isolated bundle under `scratch/previews/<preview-id>/`;
- treat `preview.md` as the authoritative editable source;
- generate `render/preview.tex` and `render/preview.pdf` only as review views;
- include section thesis, paragraph cards with stable IDs, claim/evidence needs, dependencies, exclusions, assumptions, risks, and complete unapproved preview prose;
- when the reviewer annotates the PDF, map every annotation back to Markdown, record the decision, revise Markdown first, regenerate TeX/PDF, and increment the revision;
- PDF annotations remain `DESIGN_PREVIEW` even when they target an exact sentence;
- polished prose, a clean PDF, or absence of annotations is not approval.

#### `APPLY_PREVIEW`

Use only after explicit approval of both preview ID and revision.

- read the approved `preview.md` as the source of truth;
- treat generated TeX/PDF as review artifacts only;
- implement only approved decisions;
- do not carry review anchors or annotations into `paper/`;
- do not redesign silently;
- validate globally after editing.

#### `AUDIT`

Use for consistency, semantic duplication, defensive writing, over-expression, information ownership, notation, evidence, publication boundary, language quality, or reviewer-readiness checks.

Select an audit profile when possible: `FULL`, `LANGUAGE`, `CONSISTENCY`, or `EVIDENCE`. Requests to make prose more professional, precise, consistent, factual, or natural without changing logic should use `AUDIT PROFILE: LANGUAGE`.

- read-only by default;
- prefer subtraction over defensive addition;
- detect semantically repeated explanations even when wording differs;
- distinguish legitimate assumptions/limitations/caveats from unnecessary defensive prose;
- identify the canonical owner section for repeated ideas;
- recommend one primary action: `KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, or `REWRITE`;
- report locations and minimal repairs.

Routing rules:

- infer a mode only when unambiguous;
- mixed requests preserve exact instructions as locked constraints and route the remaining open design to `DESIGN_PREVIEW`;
- PDF annotations on an unapproved preview remain `DESIGN_PREVIEW`, not `EXACT_EDIT`;
- material ambiguity defaults to `DESIGN_PREVIEW`;
- never edit `paper/` merely because a preview looks polished;
- route to `APPLY_PREVIEW` only after explicit approval of preview ID and revision.

### 7.3 Source of truth

Before manuscript edits, read:

- `internal/PAPER_CONTRACT.yaml`
- `internal/SECTION_CONTRACTS.yaml`
- `internal/CLAIM_LEDGER.yaml`
- `internal/TERMINOLOGY.yaml`
- `internal/PROSE_STYLE.yaml`
- target section;
- adjacent sections;
- declared dependent sections.

Repository state files override stale chat memory.

### 7.4 Publication boundary

Unless explicitly required and scientifically necessary, manuscript prose must not contain:

- local paths;
- internal script/helper names;
- shell commands;
- agent/tool narration;
- debugging chronology;
- prompt iteration;
- failed implementation attempts;
- internal TODOs, preview IDs, confidence labels, and workflow metadata;
- unverified results or invented citations.

Classify implementation information into:

1. scientifically necessary in the main text;
2. reproducibility detail for appendix/supplement/repository documentation;
3. internal provenance only;
4. unsupported and prohibited.

Prefer scientific abstractions over repository-specific mechanics.

### 7.5 Minimal-delta editing

For every edit:

1. identify editable span;
2. identify locked surrounding content;
3. identify global statements that may become stale;
4. make minimum patch;
5. inspect diff;
6. validate;
7. mark dependent sections stale rather than silently rewriting them outside scope.

### 7.6 Claim and evidence integrity

- never strengthen claims during rewriting;
- preserve modal strength;
- do not turn “may” into “does”;
- do not turn “designed to” into “achieves”;
- do not turn hypotheses into demonstrations;
- do not turn association into causation;
- do not invent citations, numbers, baselines, complexity claims, significance, or settings;
- use the claim ledger and result manifest.

### 7.7 Global consistency

Check contribution and scope, terminology and notation, method names, datasets/baselines/metrics, numerical values and evidence status, equations/figures/tables/citations/references, claim strength, cross-section dependencies, semantic duplication, contradictions, paragraph-level rhetorical continuity, information ownership, over-expression, defensive writing, and publication-boundary leakage.

Prefer deletion, merging, compression, or relocation over adding more explanation when meaning is already present. A concept should have one canonical explanatory home. Repetition in Abstract, Introduction, Discussion, or Conclusion is acceptable only when it performs a distinct rhetorical role and is materially compressed relative to the owner section.

### 7.8 Preview discipline

`scratch/previews/` is an index-and-directory container, not a shared compilation workspace. Its root may contain only documentation/index files and child preview directories. Every newly created preview must use a fresh unique directory; never write loose `.md`, `.tex`, `.pdf`, annotation, or TeX auxiliary files at the preview root. Prefer `YYYYMMDD-HHMM-<section-slug>-<short-id>`, check for collisions before creation, and never reuse an existing preview ID. Maintain `scratch/previews/INDEX.md` to preserve historical discoverability. Materially new alternatives create new directories; annotation-driven revisions remain in the same directory.

Each preview is a versioned bundle:

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

`preview.md` is authoritative. Generated TeX/PDF are review views only. Include preview ID + revision, paragraph cards with stable IDs, complete unapproved preview prose, claim/evidence needs, assumptions, exclusions, dependencies, proposed equations/figures/tables, and an acceptance checklist.

For every PDF annotation round: map annotations to Markdown, record `ACCEPTED` / `PARTIAL` / `REJECTED` / `BLOCKED` decisions, revise Markdown first, regenerate TeX/PDF, and increment the revision. Never patch generated TeX as an independent prose source. Explicit approval of preview ID and revision is required before manuscript application.

### 7.9 Agent ownership

- only the main writing agent may edit `paper/`;
- subagents are read-only reviewers;
- do not allow concurrent overlapping manuscript edits;
- recommended reviewers: consistency, publication boundary, evidence, notation, duplication.

### 7.10 Completion report

Every writing task reports:

- mode;
- changed files;
- intentionally preserved scope;
- checks run;
- unresolved high-severity issues;
- stale sections;
- assumptions and placeholders.

For preview work also report preview ID, revision, Markdown source path, TeX/PDF render paths, annotation status, and explicit approval status.

Do not put the entire detailed workflow in `AGENTS.md`; reference the skills.

## 8. Create repository-scoped Codex skills

Create each skill under `.agents/skills/<skill-name>/SKILL.md`.

Every `SKILL.md` must have valid YAML front matter:

```yaml
---
name: <lowercase-hyphenated-name>
description: <clear trigger, scope, and non-trigger boundary>
---
```

Descriptions must be specific enough for implicit activation and state when the skill should not trigger.

### 8.1 `paper-router`

Purpose:

- inspect user intent and choose exactly one mode;
- recognize mixed exact/open-ended requests;
- state locked constraints and editable scope;
- require source-of-truth loading;
- route to another paper skill;
- default to `DESIGN_PREVIEW` when material ambiguity remains;
- never edit manuscript itself unless the selected downstream skill permits it.

Its instructions must include a compact routing decision table and examples.

### 8.2 `surgical-edit`

Trigger:

- exact sentence, paragraph, formula, citation, ordering, terminology, or local section changes.

Required workflow:

1. load contracts and dependencies;
2. identify exact edit span and locked scope;
3. snapshot relevant text;
4. make minimum diff;
5. check no requested content was dropped;
6. run publication/evidence/consistency checks;
7. update external memory only when the approved manuscript state actually changed;
8. mark dependent sections stale;
9. report diff and untouched scope.

Must not trigger for open-ended section design or whole-paper stylistic rewriting.

### 8.3 `section-architect`

Trigger when the user knows section purpose/rough structure but has not approved prose, or provides PDF annotations on an unapproved preview.

For every NEW preview, first create a fresh unique `scratch/previews/<preview-id>/` directory and register it in `scratch/previews/INDEX.md`. Never reuse a previous preview directory or compile multiple previews in a shared working directory. Keep all TeX auxiliary outputs inside that preview's `render/` directory. A materially new alternative gets a new directory; PDF-annotation revisions of the same preview stay in the same directory and increment the revision.

Required bundle under `scratch/previews/<preview-id>/`:

- authoritative `preview.md` with stable preview ID and revision;
- paragraph cards with stable paragraph IDs;
- claim/evidence matrix, assumptions, exclusions, dependencies, risks, and acceptance checklist;
- complete unapproved preview prose;
- generated `render/preview.tex` and `render/preview.pdf`;
- `review/decisions.md` for annotation mapping and disposition.

For PDF review, map annotations back to Markdown, revise Markdown first, regenerate TeX/PDF, and increment the revision. Must not edit `paper/`.

### 8.4 `manuscript-composer`

Trigger only after explicit approval of a preview ID and revision.

Required workflow:

- verify approval for the exact revision;
- read approved `preview.md` as the authoritative source, not generated TeX/PDF;
- verify unresolved PDF annotations are resolved or explicitly accepted;
- preserve locked decisions and claim strength;
- do not carry review anchors or annotation metadata into `paper/`;
- write only target scope and do not invent support;
- update external memory;
- run global audit including redundancy and defensive-writing checks;
- report stale dependencies and any required deviation from approved Markdown.

Must not silently reinterpret an unapproved preview as approval.

### 8.5 `consistency-auditor`

Trigger for contradiction, semantic duplication, defensive writing, over-expression, information ownership, notation, global alignment, stale-section, reviewer-readiness, or whole-manuscript review. Default read-only.

For each finding report severity, category, file/section, exact passages, canonical owner section when relevant, why it matters, one primary action (`KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, `REWRITE`), minimal repair, missing evidence, and stale dependencies.

Check central thesis, contribution list, claims, numbers, terminology, equations, references, semantic duplication across adjacent and non-adjacent sections, paragraph fragmentation, over-expression, defensive writing, and Abstract/Introduction/Discussion/Conclusion alignment. Preserve scientifically necessary assumptions, limitations, boundary conditions, negative results, and caveats.

### 8.6 `academic-language-reviewer`

Trigger:

- `AUDIT PROFILE: LANGUAGE`;
- terminology precision or wording-consistency review;
- professional/factual academic expression review without changing argument logic;
- defensive/meta prose, vague academicism, collocation, cadence, hedging, or formulaic AI-language review.

Required behavior:

- read-only; never edit `paper/`;
- read `TERMINOLOGY.yaml`, `PROSE_STYLE.yaml`, claim/section contracts, target text, adjacent text, and parallel descriptions elsewhere;
- apply a strict LOGIC LOCK: do not change section/paragraph order, rhetorical role, central claim, claim strength, causal direction, evidence interpretation, numbers, equations, citations, assumptions, limitations, scope, methodological meaning, or argument dependencies;
- check `TERM_AMBIGUITY`, `TERM_DRIFT`, `SEMANTIC_DRIFT`, `VAGUE_ACADEMICISM`, `DEFENSIVE_PROSE`, `META_PROSE`, `AI_FORMULAIC_PROSE`, `COLLOCATION`, `CADENCE`, `OVER_NOMINALIZATION`, hedging, and redundant signaling;
- prefer concrete evidence-proximal subject + action + object wording over generic academic-sounding evaluation;
- return a Language Change Ledger (`L001`, `L002`, ...) instead of a fully rewritten section;
- each ledger item includes location, category, current wording, suggested wording, reason, canonical term/style rule, logic impact (`NONE` or `LOGIC_REVIEW_REQUIRED`), and confidence;
- approved ledger IDs are implemented later with `EXACT_EDIT` only.

### 8.7 `publication-filter`

Trigger:

- transferring material from code, experiment logs, internal analysis, README, scratch previews, or project explanations into manuscript prose;
- checking manuscript leakage.

Required classification:

- `MAIN_TEXT`
- `APPENDIX_OR_SUPPLEMENT`
- `REPOSITORY_DOCUMENTATION`
- `INTERNAL_ONLY`
- `UNSUPPORTED_PROHIBITED`

It must transform implementation details to the correct scientific abstraction only when evidence supports the abstraction. It must not merely remove all implementation details: reproducibility-relevant content must be routed appropriately.

## 9. Create Codex hooks and deterministic validators

Use `<repo>/.codex/hooks.json` and Python scripts under `<repo>/.codex/hooks/`. Use Python standard library only.

Hooks must be advisory and conservative. They must not rewrite manuscript files automatically.

### 9.1 `.codex/hooks.json`

Configure:

- `SessionStart` for `startup|resume|compact` to run `load_paper_context.py`;
- `PostToolUse` for relevant write-capable tool events, including `apply_patch` and shell-based edits, to run `paper_guard.py --incremental`;
- `Stop` to run `consistency_check.py --changed`.

Use Git-root-based script paths so hooks work when Codex starts in a subdirectory. Include a Windows command override. Set reasonable timeouts and status messages.

Do not add both inline hooks in `.codex/config.toml` and `.codex/hooks.json`.

### 9.2 `common.py`

Provide shared functions for:

- finding repository root;
- reading/writing YAML-like or JSON-compatible state safely without external YAML dependencies;
- enumerating manuscript files;
- getting changed files from Git with a non-Git fallback;
- parsing hook JSON input from stdin;
- emitting valid hook JSON;
- locating target manuscript entry point;
- normalizing paths;
- loading text with encoding fallbacks;
- safe diagnostics.

If PyYAML is already a declared project dependency, it may be used. Otherwise, scripts must not require it. A minimal conservative YAML reader may inspect only needed fields, or state files may be written in JSON-compatible YAML.

### 9.3 `load_paper_context.py`

On `SessionStart`:

- read the external-memory files;
- output concise additional context, not the entire paper;
- include central problem, central contribution, disclosure policy, canonical terminology, high-priority claims, stale sections, unresolved high-severity issues, and current manuscript entry point;
- cap output to a practical size;
- if files are missing or invalid, provide a warning rather than failing the session;
- emit the hook-specific JSON shape expected for `SessionStart`.

### 9.4 `paper_guard.py`

Inspect changed files under `paper/`. Report, but do not automatically edit:

- absolute paths;
- `internal/` or `scratch/` references in prose;
- likely local script filenames and shell commands;
- agent/tool narration;
- debugging or prompt-iteration language;
- TODO/TBD/FIXME/PLACEHOLDER markers;
- new citation keys missing from bibliography;
- undefined or duplicated labels where statically detectable;
- terminology forbidden variants;
- new numeric claims not traceable to the result manifest;
- provisional-result sources used without qualification;
- accidental generated-file commits;
- references to old manuscript paths.

Use an allowlist for legitimate public software names and explicitly approved repository references. Keep pattern checks conservative and explain possible false positives.

Write a human-readable report to `internal/audits/latest-paper-guard.md`; create the audit directory if needed. Exit nonzero only for script failure, not ordinary manuscript findings, unless the existing repository has a stricter established policy.

### 9.5 `consistency_check.py`

For changed manuscript files and their declared dependencies, check:

- forbidden terminology;
- claim ledger drift;
- modal-strength changes where detectable;
- conflicting repeated numerical values;
- stale section status;
- broken include/import paths;
- bibliography and citation key integrity;
- labels and references;
- duplicate or near-duplicate paragraphs using a conservative standard-library similarity method;
- publication leakage;
- old paths left after migration;
- parse validity of memory files;
- evidence status for claims consumed by changed sections.

Write:

- `internal/audits/latest-consistency-report.md`;
- a machine-readable `internal/audits/latest-consistency-report.json`.

Do not claim semantic completeness when checks are heuristic.

### 9.6 Hook validation

After creating hooks:

- run every script directly with representative mock input;
- verify JSON output parses;
- verify missing files are handled;
- verify no script modifies manuscript content;
- verify commands are valid for the detected platform where possible;
- document that project-local hooks require user trust/review before Codex executes them.

## 10. Add workflow documentation and prompt templates

Create `paper/README.md` or a root `WRITING_WORKFLOW.md` containing concise user instructions for:

- where manuscript files now live;
- how to build;
- how to invoke each mode;
- how preview approval works;
- how stale sections work;
- how to review/trust hooks;
- how to run guards manually;
- how to update verified results;
- how to run `AUDIT PROFILE: LANGUAGE`, review the Language Change Ledger, approve selected IDs, and implement them with `EXACT_EDIT`;
- how `TERMINOLOGY.yaml` and `PROSE_STYLE.yaml` constrain language review.

Include copy-ready templates:

### Exact edit

```text
MODE: EXACT_EDIT

TARGET:
- File:
- Section or line range:

REQUIRED CHANGES:
1.
2.

LOCKED CONTENT:
- Preserve all unspecified text, equations, citations, labels, and order.

ALLOWED COLLATERAL CHANGES:
- Only repairs directly required by the requested edit.

GLOBAL CONSISTENCY:
- Report affected sections; do not modify them automatically.

ACCEPTANCE CRITERIA:
-
```

### Design preview

```text
MODE: DESIGN_PREVIEW

TARGET SECTION:
-

SECTION MUST EXPLAIN:
1.
2.

AVAILABLE VERIFIED MATERIAL:
-

LOCKED DECISIONS:
-

MUST NOT INCLUDE:
-

PREVIEW WORKFLOW:
- Create `scratch/previews/<preview-id>/preview.md` as the authoritative source.
- Include paragraph cards with stable IDs and complete unapproved preview prose.
- Generate and compile `render/preview.tex` / `render/preview.pdf` for visual review.
- Map PDF annotations back to Markdown, revise Markdown first, regenerate the render, and increment the revision.
- Do not edit `paper/` or treat a clean PDF as approval.

OUTPUT:
- Preview ID + revision
- Markdown source and PDF render paths
- Annotation decisions
- Dependencies / missing information
- Acceptance checklist
```

### Apply preview

```text
MODE: APPLY_PREVIEW

APPROVED PREVIEW:
- Preview ID:
- Approved revision:
- Authoritative Markdown: `scratch/previews/<preview-id>/preview.md`

TARGET:
-

LOCKED DECISIONS:
-

Implement only the approved scope and run global validation.
```

### Audit

```text
MODE: AUDIT
AUDIT PROFILE: FULL | LANGUAGE | CONSISTENCY | EVIDENCE

SCOPE:
-

CHECKS:
- contradictions
- semantic duplication across sections
- over-expression and paragraph fragmentation
- defensive writing and unnecessary historical/scope disclaimers
- information ownership / canonical owner section
- terminology and notation
- claim strength
- numerical consistency
- publication leakage
- abstract/introduction/discussion/conclusion alignment

REPAIR POLICY:
- Prefer DELETE / MERGE / COMPRESS when meaning already exists elsewhere.
- Preserve scientifically necessary limitations, assumptions, boundary conditions, negative results, and caveats.

AUTOFIX: NO
```

## 11. Integrate with the existing build and repository tooling

Detect and update relevant:

- Makefile targets;
- shell, Python, PowerShell, or task-runner scripts;
- VS Code tasks;
- CI workflows;
- bibliography tools;
- figure-generation paths;
- manuscript packaging scripts;
- release/submission scripts;
- README instructions;
- `.gitignore`;
- editor settings only when path-specific.

Do not introduce a new build framework when the existing one works.

Add a convenient validation target only when it fits the existing tooling, for example:

- `make paper`
- `make paper-check`
- `python .codex/hooks/paper_guard.py`
- `python .codex/hooks/consistency_check.py`

Do not make Codex hooks the only way to validate the paper.

## 12. Validation sequence

Run the strongest safe validation available without installing anything.

### Required static validation

- all moved files exist at destinations;
- no source was accidentally lost;
- every include/import resolves;
- every bibliography file resolves;
- every figure/table/style reference resolves where statically checkable;
- old paths have no unexpected remaining references;
- YAML/state files parse;
- hook JSON parses;
- Python hook scripts compile;
- skills have valid front matter and unique names;
- `AGENTS.md` references real paths;
- no preview was placed in `paper/`;
- no internal analysis was copied into manuscript prose;
- Git diff contains no accidental large binary duplication.

### Build validation

Use the existing documented build command first.

If LaTeX, prefer the existing build script or `latexmk`; otherwise use the installed appropriate tool. Do not install missing TeX packages. Capture errors and distinguish:

- migration-caused path errors;
- pre-existing source errors;
- missing local toolchain or packages.

If the complete build cannot run, perform a dependency graph and reference validation and state the limitation.

### Semantic migration audit

Compare pre- and post-migration manuscript source:

- normalize path-only changes;
- verify no paragraph, equation, citation, label, figure caption, or scientific statement disappeared or changed unexpectedly;
- flag any non-path textual difference for manual inspection;
- repair accidental differences when safe.

### Git review

Inspect:

- `git status`;
- `git diff --stat`;
- full diff for instruction, state, and manuscript files;
- moved-file detection;
- accidental deletion;
- accidental build artifact additions.

Do not commit.

## 13. Completion criteria

The task is complete only when:

- the primary manuscript is located under `paper/`;
- the current build or strongest available substitute validation succeeds;
- all known path references are updated;
- external-memory files are populated from real evidence, with unknowns visible;
- root `AGENTS.md` is active and concise;
- all seven skills exist under `.agents/skills/`;
- hooks and scripts exist under `.codex/` and pass direct tests;
- workflow documentation and prompt templates exist;
- migration inventory and map are complete;
- no scientific content has been silently rewritten;
- no internal implementation narrative has been introduced into the paper;
- remaining issues are explicitly documented.

## 14. Final response format

At the end, give a concise but complete report with these headings:

### Migration completed
- old → new manuscript paths;
- primary entry point;
- build command.

### Harness created
- `AGENTS.md`;
- skills;
- hooks;
- external-memory files;
- documentation.

### External memory initialized
- high-confidence facts;
- low-confidence assumptions;
- unresolved fields;
- claims that remain unverified.

### Validation
- commands run;
- build result;
- static check result;
- semantic source comparison result;
- hook test result.

### Intentionally preserved
- code/data/legacy files not moved and why;
- existing instructions retained;
- uncommitted user work preserved.

### Requires my review
- high-severity uncertainties;
- stale sections;
- hook trust action;
- any pre-existing build errors.

### Files changed
- grouped list of moved, created, and modified files.

Do not end with a generic offer. Do not claim success for checks that were not run.

Begin by inspecting the repository. Then execute the migration end to end.

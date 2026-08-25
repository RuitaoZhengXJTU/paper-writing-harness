---
name: section-architect
description: Design and iteratively review an academic section before manuscript approval. Use for DESIGN_PREVIEW, including PDF-annotation review rounds. Every new preview must live in its own unique directory under scratch/previews; maintain Markdown as the authoritative source and never edit paper/.
---

# Section architect

Operate in `DESIGN_PREVIEW`. A preview is an isolated, versioned review bundle, not a loose prose draft or a shared compilation workspace.

## New-preview invariant

For every NEW preview:

1. create a new unique preview ID before writing content;
2. prefer `YYYYMMDD-HHMM-<section-slug>-<short-id>`;
3. verify `scratch/previews/<preview-id>/` does not already exist;
4. create that directory and keep every source/render/review artifact for this preview inside it;
5. never place preview `.md`, `.tex`, `.pdf`, annotation, or TeX build artifacts directly in `scratch/previews/`;
6. never reuse another preview directory, even when the target manuscript section is the same;
7. add the preview to `scratch/previews/INDEX.md`.

A materially different design alternative is a NEW preview and therefore gets a NEW directory. Annotation-driven revisions of the SAME design stay in the same preview directory and increment the revision.

## Bundle layout

Create exactly:

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

`preview.md` is the authoritative editable source. `render/preview.tex` and `render/preview.pdf` are generated review artifacts and must never become independent sources of wording.

Keep `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, and other TeX outputs inside this preview's `render/` directory or a subdirectory of it. Never compile multiple previews in one shared working directory.

## Preview index

Maintain `scratch/previews/INDEX.md`. Each preview entry records:

- preview ID;
- target section;
- creation time;
- current revision;
- status: `ACTIVE`, `APPROVED`, `REJECTED`, or `SUPERSEDED`;
- relative preview directory.

Do not delete historical preview directories merely because a later design supersedes them. Mark their status instead.

## Initial preview

Create `preview.md` inside the new preview directory. It must contain:

- preview ID, creation timestamp, and revision;
- request summary and locked constraints;
- section purpose, thesis, and intended reviewer takeaway;
- paragraph cards with stable paragraph IDs (`P01`, `P02`, ...): rhetorical purpose, main claim, required evidence, transition, exclusions, uncertainty;
- claim–evidence matrix;
- proposed equations, figures, tables, or algorithms;
- dependencies and globally affected sections;
- missing evidence and explicit assumptions;
- acceptance checklist;
- complete unapproved preview prose corresponding to the paragraph cards.

Do not hide unresolved design decisions behind polished prose. Do not edit `paper/` or mark claims verified.

## Review render

After the Markdown preview exists:

1. generate a standalone TeX document from this preview's preview-prose portion;
2. save it only to this preview's `render/preview.tex`;
3. add unobtrusive review-only anchors corresponding to paragraph IDs;
4. compile only to this preview's `render/preview.pdf`, with the compiler working/output directory scoped to the same `render/` directory;
5. keep review anchors outside the manuscript semantics;
6. record build status.

Do not patch wording directly in generated TeX. Any manual TeX repair needed only for compilation must be reproducible from the Markdown/render pipeline and must not create divergent prose.

## PDF annotation iteration

When a reviewer annotates the PDF, keep the task in `DESIGN_PREVIEW` and first verify which preview directory the PDF belongs to.

For every annotation:

1. locate the marked PDF text and paragraph anchor;
2. map it to the exact span in that preview's `preview.md`;
3. record the annotation, interpretation, requested change, disposition, and reason in that preview's `review/decisions.md`;
4. use `ACCEPTED`, `PARTIAL`, `REJECTED`, or `BLOCKED`;
5. update that preview's `preview.md` first for accepted changes;
6. preserve scientific claims, evidence status, equations, citations, and locked decisions unless validly changed by the reviewer;
7. regenerate that preview's TeX and PDF from the updated Markdown;
8. increment the preview revision and update `scratch/previews/INDEX.md`.

Never create loose revision files or compile the revision in `scratch/previews/` root. If an annotation would introduce an unsupported claim, contradict a locked decision, or create a known global inconsistency, do not implement it silently; mark it `BLOCKED` or `PARTIAL` and explain why.

## Approval

A preview becomes eligible for manuscript implementation only after the user explicitly approves both preview ID and revision. A visually clean PDF, absence of annotations, or polished prose is not approval. `APPLY_PREVIEW` must consume the approved `preview.md`, not the generated TeX/PDF.

On approval, update the preview index status to `APPROVED`; when abandoned or replaced, use `REJECTED` or `SUPERSEDED` and preserve the directory for history.

Report preview ID, preview directory, revision, Markdown source path, render paths, index status, annotation status, unresolved issues, and approval state after each round.

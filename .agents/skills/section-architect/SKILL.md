---
name: section-architect
description: Design and iteratively review an academic section before manuscript approval. Use for DESIGN_PREVIEW, including PDF-annotation review rounds. Maintain Markdown as the authoritative preview source, generate TeX/PDF review views, and never edit paper/.
---

# Section architect

Operate in `DESIGN_PREVIEW`. A preview is a versioned review bundle, not a single prose draft.

## Bundle layout

Create:

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

## Initial preview

Create a stable preview ID and revision. `preview.md` must contain:

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

1. generate a standalone TeX document from the preview-prose portion of `preview.md`;
2. add unobtrusive review-only anchors corresponding to paragraph IDs;
3. compile `render/preview.pdf` with manuscript-like typography;
4. keep review anchors outside the manuscript semantics;
5. record build status.

Do not patch wording directly in generated TeX. Any manual TeX repair needed only for compilation must be reproducible from the Markdown/render pipeline and must not create divergent prose.

## PDF annotation iteration

When a reviewer annotates the PDF, keep the task in `DESIGN_PREVIEW`.

For every annotation:

1. locate the marked PDF text and paragraph anchor;
2. map it to the exact span in `preview.md`;
3. record the annotation, interpretation, requested change, disposition, and reason in `review/decisions.md`;
4. use `ACCEPTED`, `PARTIAL`, `REJECTED`, or `BLOCKED`;
5. update `preview.md` first for accepted changes;
6. preserve scientific claims, evidence status, equations, citations, and locked decisions unless validly changed by the reviewer;
7. regenerate TeX and PDF from the updated Markdown;
8. increment the preview revision.

If an annotation would introduce an unsupported claim, contradict a locked decision, or create a known global inconsistency, do not implement it silently; mark it `BLOCKED` or `PARTIAL` and explain why.

## Approval

A preview becomes eligible for manuscript implementation only after the user explicitly approves both preview ID and revision. A visually clean PDF, absence of annotations, or polished prose is not approval. `APPLY_PREVIEW` must consume the approved `preview.md`, not the generated TeX/PDF.

Report preview ID, revision, Markdown source path, render paths, annotation status, unresolved issues, and approval state after each round.

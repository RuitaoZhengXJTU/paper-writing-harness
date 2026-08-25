# Scratch workspace

`scratch/` contains material that is not approved manuscript content.

## Preview storage invariant

`scratch/previews/` is not a shared compilation directory. Every NEW preview must live in its own unique child directory. The root of `scratch/previews/` may contain only documentation/index files and preview directories.

Do not place loose preview Markdown, TeX, PDF, annotation, or TeX auxiliary files directly under `scratch/previews/`.

Preferred preview ID format:

```text
YYYYMMDD-HHMM-<section-slug>-<short-id>
```

Example:

```text
scratch/previews/20260825-1154-method-screening-a7f3/
```

Before creating a preview, verify that its directory does not already exist. Never reuse or overwrite another preview directory. A materially new design alternative receives a new preview ID and a new directory. Revisions caused by PDF annotations stay inside the same preview directory and increment `R1`, `R2`, etc.

Maintain `scratch/previews/INDEX.md` so historical previews can be found without browsing loose TeX/PDF files.

## Preview authority

Every structural preview lives in an isolated bundle:

```text
scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md
```

Authority order:

1. `preview.md` — authoritative editable source;
2. `review/decisions.md` — annotation interpretation and review history;
3. `render/preview.tex` — generated intermediate render source;
4. `render/preview.pdf` — generated visual review view.

All TeX auxiliary files must remain inside that preview's `render/` directory or its subdirectories. Never compile multiple previews in a shared working directory.

The TeX/PDF pair must never become an independently edited prose branch. PDF annotations are mapped back to Markdown, Markdown is revised first, and the render is regenerated afterward.

A preview becomes eligible for manuscript implementation only after explicit approval of both preview ID and revision. A clean PDF, absence of comments, or polished prose is not approval.

Historical preview directories should be preserved. Mark them `APPROVED`, `REJECTED`, or `SUPERSEDED` in `scratch/previews/INDEX.md` rather than deleting them.

`analysis/` and `rejected-drafts/` never count as approved manuscript content.

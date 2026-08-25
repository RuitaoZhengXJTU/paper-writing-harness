# Scratch workspace

`scratch/` contains material that is not approved manuscript content.

## Preview authority

Every structural preview should live in a versioned bundle:

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

The TeX/PDF pair must never become an independently edited prose branch. PDF annotations are mapped back to Markdown, Markdown is revised first, and the render is regenerated afterward.

A preview becomes eligible for manuscript implementation only after explicit approval of both preview ID and revision. A clean PDF, absence of comments, or polished prose is not approval.

`analysis/` and `rejected-drafts/` never count as approved manuscript content.

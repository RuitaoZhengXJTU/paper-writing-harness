# Design Preview Prompt

```text
MODE: DESIGN_PREVIEW

TARGET SECTION:
- File or proposed section:
- Intended role in the paper:
- Preceding context:
- Following context:

SECTION MUST EXPLAIN:
1.
2.

AVAILABLE VERIFIED MATERIAL:
- Claims:
- Results:
- Equations:
- Figures or tables:

LOCKED DECISIONS:
-

MUST NOT INCLUDE:
-

PREVIEW STORAGE RULES:
- Every NEW preview must receive a NEW unique directory under `scratch/previews/`.
- Never save preview `.md`, `.tex`, `.pdf`, auxiliary build files, or annotation files directly under `scratch/previews/`.
- Prefer preview IDs of the form `YYYYMMDD-HHMM-<section-slug>-<short-id>`.
- Before creating the preview, verify that `scratch/previews/<preview-id>/` does not already exist. If it exists, generate a different preview ID; never overwrite another preview.
- A materially new design alternative for the same section is a new preview and therefore a new directory.
- Annotation-driven revisions of the SAME preview stay inside the same directory and increment `R1`, `R2`, etc.
- Keep `scratch/previews/INDEX.md` updated with preview ID, target, created time, latest revision, status, and relative path.

PREVIEW BUNDLE:
Create exactly one isolated bundle for this preview:

scratch/previews/<preview-id>/
├── preview.md
├── render/
│   ├── preview.tex
│   └── preview.pdf
└── review/
    └── decisions.md

- `preview.md` is the authoritative editable source.
- `render/preview.tex` and `render/preview.pdf` are generated review artifacts only.
- `review/decisions.md` records annotation interpretation, accepted/rejected requests, and unresolved issues.
- Keep TeX auxiliary files inside this preview's `render/` directory or a subdirectory of it. Never compile multiple previews into a shared working directory.

PHASE A — CREATE A NEW ISOLATED PREVIEW:
1. Generate a unique preview ID and create `scratch/previews/<preview-id>/` before writing preview content.
2. Create `preview.md` inside that directory with:
   - preview ID and revision (`R1`, `R2`, ...);
   - creation timestamp;
   - target section and rhetorical purpose;
   - locked constraints;
   - section thesis and intended reviewer takeaway;
   - paragraph cards with stable paragraph IDs (`P01`, `P02`, ...), purpose, main claim, evidence, transition, exclusions, and uncertainty;
   - claim–evidence matrix;
   - proposed equations, figures, tables, or algorithms;
   - dependencies and globally affected sections;
   - missing information and explicit assumptions;
   - acceptance checklist;
   - a complete unapproved preview-prose section corresponding to the paragraph cards.
3. Add or update the corresponding entry in `scratch/previews/INDEX.md` with status `ACTIVE`.
4. Do not hide unresolved design choices behind fluent prose.
5. Do not edit `paper/`.

PHASE B — GENERATE THE REVIEW PDF INSIDE THE SAME PREVIEW DIRECTORY:
1. Generate a standalone TeX document from the preview-prose portion of this preview's `preview.md` only.
2. Save it only as `scratch/previews/<preview-id>/render/preview.tex` and compile only to `scratch/previews/<preview-id>/render/preview.pdf`.
3. Run the TeX compiler with its working/output directory scoped to this preview's `render/` directory. Do not emit `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, or other build artifacts into `scratch/previews/` or another preview directory.
4. Preserve manuscript-like typography and paragraph flow so the reviewer can judge the text visually.
5. Add unobtrusive review-only paragraph anchors that map to `P01`, `P02`, etc. These anchors must not be treated as manuscript text.
6. Do not make independent wording edits in TeX. The TeX/PDF must reflect the current Markdown revision.
7. If compilation fails, keep the Markdown source intact and report the build failure explicitly.

PHASE C — PDF ANNOTATION REVIEW LOOP:
When the reviewer annotates this preview's `render/preview.pdf`:
1. Confirm the preview ID from the PDF/path before editing anything.
2. Read every annotation and identify the quoted/marked PDF span and paragraph anchor.
3. Map each annotation back to the corresponding span in that preview's `preview.md`.
4. Record the interpretation and disposition in that preview's `review/decisions.md`:
   - annotation ID or location;
   - mapped Markdown paragraph/span;
   - requested change;
   - status: ACCEPTED / PARTIAL / REJECTED / BLOCKED;
   - reason when not fully accepted.
5. Apply accepted changes to the SAME preview's `preview.md` FIRST.
6. Preserve locked scientific content, claim strength, evidence status, equations, and citations unless the annotation explicitly and validly changes them.
7. Do not edit `render/preview.tex` as the source of the revision.
8. Regenerate the SAME preview's `render/preview.tex` from the updated Markdown and recompile the SAME preview's `render/preview.pdf`.
9. Increment the preview revision and update that preview's entry in `scratch/previews/INDEX.md`.
10. Never create loose revision files such as `preview-R2.tex`, `section-preview-2.tex`, or PDFs directly in `scratch/previews/`.

ANNOTATION SAFETY:
- A PDF annotation is a revision request, not manuscript approval.
- If an annotation would introduce an unsupported claim, contradict a locked decision, alter evidence strength, or create a global inconsistency, mark it BLOCKED or PARTIAL and explain why in `review/decisions.md`.
- Never silently resolve ambiguity by changing `paper/`.

APPROVAL RULE:
- A preview becomes eligible for `APPLY_PREVIEW` only after explicit approval of both preview ID and revision.
- Absence of further annotations is not approval.
- The approved Markdown revision, not the PDF or generated TeX, is the source for manuscript implementation.
- When approved, update the preview's `INDEX.md` status to `APPROVED`. When abandoned or replaced, use `REJECTED` or `SUPERSEDED` rather than deleting the historical directory.

OUTPUT REPORT:
- Preview ID and current revision.
- Preview directory.
- Markdown source path.
- TeX/PDF render paths and build status.
- `INDEX.md` status.
- Annotation decisions resolved this round.
- Remaining unresolved or blocked issues.
- Whether explicit approval has been received.
```

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

PREVIEW BUNDLE:
- Create a stable preview ID.
- Store the preview under scratch/previews/<preview-id>/.
- `preview.md` is the authoritative editable source.
- `render/preview.tex` and `render/preview.pdf` are generated review artifacts only.
- `review/decisions.md` records annotation interpretation, accepted/rejected requests, and unresolved issues.

PHASE A — BUILD THE MARKDOWN SOURCE:
1. Create `preview.md` with:
   - preview ID and revision (`R1`, `R2`, ...);
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
2. Do not hide unresolved design choices behind fluent prose.
3. Do not edit `paper/`.

PHASE B — GENERATE THE REVIEW PDF:
1. Generate a standalone TeX document from the preview-prose portion of `preview.md` only.
2. Save it as `render/preview.tex` and compile `render/preview.pdf`.
3. Preserve manuscript-like typography and paragraph flow so the reviewer can judge the text visually.
4. Add unobtrusive review-only paragraph anchors that map to `P01`, `P02`, etc. These anchors must not be treated as manuscript text.
5. Do not make independent wording edits in TeX. The TeX/PDF must reflect the current Markdown revision.
6. If compilation fails, keep the Markdown source intact and report the build failure explicitly.

PHASE C — PDF ANNOTATION REVIEW LOOP:
When the reviewer annotates `render/preview.pdf`:
1. Read every annotation and identify the quoted/marked PDF span and paragraph anchor.
2. Map each annotation back to the corresponding span in `preview.md`.
3. Record the interpretation and disposition in `review/decisions.md`:
   - annotation ID or location;
   - mapped Markdown paragraph/span;
   - requested change;
   - status: ACCEPTED / PARTIAL / REJECTED / BLOCKED;
   - reason when not fully accepted.
4. Apply accepted changes to `preview.md` FIRST.
5. Preserve locked scientific content, claim strength, evidence status, equations, and citations unless the annotation explicitly and validly changes them.
6. Do not edit `render/preview.tex` as the source of the revision.
7. Regenerate `render/preview.tex` from the updated Markdown and recompile `render/preview.pdf`.
8. Increment the preview revision and repeat until the reviewer is satisfied.

ANNOTATION SAFETY:
- A PDF annotation is a revision request, not manuscript approval.
- If an annotation would introduce an unsupported claim, contradict a locked decision, alter evidence strength, or create a global inconsistency, mark it BLOCKED or PARTIAL and explain why in `review/decisions.md`.
- Never silently resolve ambiguity by changing `paper/`.

APPROVAL RULE:
- A preview becomes eligible for `APPLY_PREVIEW` only after explicit approval of both preview ID and revision.
- Absence of further annotations is not approval.
- The approved Markdown revision, not the PDF or generated TeX, is the source for manuscript implementation.

OUTPUT REPORT:
- Preview ID and current revision.
- Markdown source path.
- TeX/PDF render paths and build status.
- Annotation decisions resolved this round.
- Remaining unresolved or blocked issues.
- Whether explicit approval has been received.
```

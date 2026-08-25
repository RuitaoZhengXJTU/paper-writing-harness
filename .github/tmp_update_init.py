from pathlib import Path
import re

p = Path('prompts/INITIALIZE_EXISTING_REPOSITORY.md')
s = p.read_text(encoding='utf-8')

def section(start, end, body):
    global s
    pat = re.escape(start) + r'.*?(?=' + re.escape(end) + r')'
    s2, n = re.subn(pat, body.rstrip() + '\n\n', s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'failed to replace section: {start}')
    s = s2

section('#### `DESIGN_PREVIEW`', '#### `APPLY_PREVIEW`', '''#### `DESIGN_PREVIEW`

Use when purpose or structure is known but prose is not approved, including all review iterations on an unapproved preview PDF.

- do not edit `paper/`;
- create a versioned bundle under `scratch/previews/<preview-id>/`;
- treat `preview.md` as the authoritative editable source;
- generate `render/preview.tex` and `render/preview.pdf` only as review views;
- include section thesis, paragraph cards with stable IDs, claim/evidence needs, dependencies, exclusions, assumptions, risks, and complete unapproved preview prose;
- when the reviewer annotates the PDF, map every annotation back to Markdown, record the decision, revise Markdown first, regenerate TeX/PDF, and increment the revision;
- PDF annotations remain `DESIGN_PREVIEW` even when they target an exact sentence;
- polished prose, a clean PDF, or absence of annotations is not approval.''')

section('#### `APPLY_PREVIEW`', '#### `AUDIT`', '''#### `APPLY_PREVIEW`

Use only after explicit approval of both preview ID and revision.

- read the approved `preview.md` as the source of truth;
- treat generated TeX/PDF as review artifacts only;
- implement only approved decisions;
- do not carry review anchors or annotations into `paper/`;
- do not redesign silently;
- validate globally after editing.''')

section('#### `AUDIT`', 'Routing rules:', '''#### `AUDIT`

Use for consistency, semantic duplication, defensive writing, over-expression, information ownership, notation, evidence, publication boundary, or reviewer-readiness checks.

- read-only by default;
- prefer subtraction over defensive addition;
- detect semantically repeated explanations even when wording differs;
- distinguish legitimate assumptions/limitations/caveats from unnecessary defensive prose;
- identify the canonical owner section for repeated ideas;
- recommend one primary action: `KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, or `REWRITE`;
- report locations and minimal repairs.''')

section('Routing rules:', '### 7.3 Source of truth', '''Routing rules:

- infer a mode only when unambiguous;
- mixed requests preserve exact instructions as locked constraints and route the remaining open design to `DESIGN_PREVIEW`;
- PDF annotations on an unapproved preview remain `DESIGN_PREVIEW`, not `EXACT_EDIT`;
- material ambiguity defaults to `DESIGN_PREVIEW`;
- never edit `paper/` merely because a preview looks polished;
- route to `APPLY_PREVIEW` only after explicit approval of preview ID and revision.''')

section('### 7.7 Global consistency', '### 7.8 Preview discipline', '''### 7.7 Global consistency

Check contribution and scope, terminology and notation, method names, datasets/baselines/metrics, numerical values and evidence status, equations/figures/tables/citations/references, claim strength, cross-section dependencies, semantic duplication, contradictions, paragraph-level rhetorical continuity, information ownership, over-expression, defensive writing, and publication-boundary leakage.

Prefer deletion, merging, compression, or relocation over adding more explanation when meaning is already present. A concept should have one canonical explanatory home. Repetition in Abstract, Introduction, Discussion, or Conclusion is acceptable only when it performs a distinct rhetorical role and is materially compressed relative to the owner section.''')

section('### 7.8 Preview discipline', '### 7.9 Agent ownership', '''### 7.8 Preview discipline

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

For every PDF annotation round: map annotations to Markdown, record `ACCEPTED` / `PARTIAL` / `REJECTED` / `BLOCKED` decisions, revise Markdown first, regenerate TeX/PDF, and increment the revision. Never patch generated TeX as an independent prose source. Explicit approval of preview ID and revision is required before manuscript application.''')

old = '''- assumptions and placeholders.\n\nDo not put the entire detailed workflow in `AGENTS.md`; reference the skills.'''
new = '''- assumptions and placeholders.\n\nFor preview work also report preview ID, revision, Markdown source path, TeX/PDF render paths, annotation status, and explicit approval status.\n\nDo not put the entire detailed workflow in `AGENTS.md`; reference the skills.'''
if old not in s:
    raise SystemExit('failed to update completion report')
s = s.replace(old, new, 1)

section('### 8.3 `section-architect`', '### 8.4 `manuscript-composer`', '''### 8.3 `section-architect`

Trigger when the user knows section purpose/rough structure but has not approved prose, or provides PDF annotations on an unapproved preview.

Required bundle under `scratch/previews/<preview-id>/`:

- authoritative `preview.md` with stable preview ID and revision;
- paragraph cards with stable paragraph IDs;
- claim/evidence matrix, assumptions, exclusions, dependencies, risks, and acceptance checklist;
- complete unapproved preview prose;
- generated `render/preview.tex` and `render/preview.pdf`;
- `review/decisions.md` for annotation mapping and disposition.

For PDF review, map annotations back to Markdown, revise Markdown first, regenerate TeX/PDF, and increment the revision. Must not edit `paper/`.''')

section('### 8.4 `manuscript-composer`', '### 8.5 `consistency-auditor`', '''### 8.4 `manuscript-composer`

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

Must not silently reinterpret an unapproved preview as approval.''')

section('### 8.5 `consistency-auditor`', '### 8.6 `publication-filter`', '''### 8.5 `consistency-auditor`

Trigger for contradiction, semantic duplication, defensive writing, over-expression, information ownership, notation, global alignment, stale-section, reviewer-readiness, or whole-manuscript review. Default read-only.

For each finding report severity, category, file/section, exact passages, canonical owner section when relevant, why it matters, one primary action (`KEEP`, `DELETE`, `MERGE`, `COMPRESS`, `RELOCATE`, `REWRITE`), minimal repair, missing evidence, and stale dependencies.

Check central thesis, contribution list, claims, numbers, terminology, equations, references, semantic duplication across adjacent and non-adjacent sections, paragraph fragmentation, over-expression, defensive writing, and Abstract/Introduction/Discussion/Conclusion alignment. Preserve scientifically necessary assumptions, limitations, boundary conditions, negative results, and caveats.''')

# Update compact prompt templates with focused insertions.
s = s.replace('''OUTPUT:\n- Section thesis\n- Paragraph cards\n- Claim/evidence requirements\n- Proposed equations/figures/tables\n- Dependencies\n- Missing information\n- Assumptions\n- Acceptance checklist\n\nDo not edit paper/.''', '''PREVIEW WORKFLOW:\n- Create `scratch/previews/<preview-id>/preview.md` as the authoritative source.\n- Include paragraph cards with stable IDs and complete unapproved preview prose.\n- Generate and compile `render/preview.tex` / `render/preview.pdf` for visual review.\n- Map PDF annotations back to Markdown, revise Markdown first, regenerate the render, and increment the revision.\n- Do not edit `paper/` or treat a clean PDF as approval.\n\nOUTPUT:\n- Preview ID + revision\n- Markdown source and PDF render paths\n- Annotation decisions\n- Dependencies / missing information\n- Acceptance checklist''', 1)

s = s.replace('''APPROVED PREVIEW:\n- Preview ID:\n- Preview file:''', '''APPROVED PREVIEW:\n- Preview ID:\n- Approved revision:\n- Authoritative Markdown: `scratch/previews/<preview-id>/preview.md`''', 1)

s = s.replace('''CHECKS:\n- contradictions\n- duplicated explanations\n- terminology and notation\n- claim strength\n- numerical consistency\n- publication leakage\n- abstract/introduction/conclusion alignment''', '''CHECKS:\n- contradictions\n- semantic duplication across sections\n- over-expression and paragraph fragmentation\n- defensive writing and unnecessary historical/scope disclaimers\n- information ownership / canonical owner section\n- terminology and notation\n- claim strength\n- numerical consistency\n- publication leakage\n- abstract/introduction/discussion/conclusion alignment\n\nREPAIR POLICY:\n- Prefer DELETE / MERGE / COMPRESS when meaning already exists elsewhere.\n- Preserve scientifically necessary limitations, assumptions, boundary conditions, negative results, and caveats.''', 1)

required = [
    'PDF annotations on an unapproved preview remain `DESIGN_PREVIEW`',
    '`preview.md` is authoritative',
    'defensive writing',
    'canonical owner section',
    'Prefer DELETE / MERGE / COMPRESS',
]
for marker in required:
    if marker not in s:
        raise SystemExit(f'missing required marker: {marker}')

p.write_text(s, encoding='utf-8')
print('updated initialization prompt', len(s.encode('utf-8')))

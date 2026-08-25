# Preview History Index

This file is the navigation index for DESIGN_PREVIEW history. Keep one row per preview directory.

The preview root should contain only this index, optional documentation files, and child preview directories. Do not place loose `.md`, `.tex`, `.pdf`, annotation, or TeX auxiliary files here.

| Preview ID | Target section | Created | Latest revision | Status | Path |
|---|---|---|---|---|---|

Status values:

- `ACTIVE` — currently under review;
- `APPROVED` — explicitly approved by preview ID and revision;
- `REJECTED` — abandoned without approval;
- `SUPERSEDED` — replaced by a materially different preview.

Preferred preview ID format:

```text
YYYYMMDD-HHMM-<section-slug>-<short-id>
```

Example entry:

```text
| 20260825-1154-method-screening-a7f3 | Method §3.2 | 2026-08-25 11:54 -0700 | R3 | ACTIVE | `scratch/previews/20260825-1154-method-screening-a7f3/` |
```

When a new preview is created, append a new row. Annotation-driven revisions update only the revision/status fields of the existing row. Never reuse an existing preview ID.

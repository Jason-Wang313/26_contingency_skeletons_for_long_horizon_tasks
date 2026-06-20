# Paper26 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Make `C:/Users/wangz/Downloads/26.pdf` explicitly match the visible VLA-v4
role model's boxed-link behavior while preserving the final 25-page guarded
contingency skeletons paper:

- citation links use green one-point boxes;
- internal figure/table/section links use red one-point boxes;
- no cyan URL boxes appear;
- the final PDF is rebuilt, copied only to Downloads, visually checked, and
  leaves no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/26.pdf`
- Pages: 25
- Size: 371,778 bytes
- SHA256: `A36A75140750716A0D4E61DD4D59A7251AF27F6780FC0DDC5FA522AF61D8AAB9`
- Local `paper/main.pdf`: absent
- Repository state: clean against `origin/master`

Baseline link inventory from the current Downloads PDF:

- Link pages:
  `[(2, 28), (3, 4), (5, 2), (6, 1), (7, 3), (16, 1), (18, 3), (20, 4), (23, 1)]`
- Annotation colors: green = 32, red = 15, cyan = 0
- Border widths: `(0, 0, 1)` for all 47 link annotations

Source finding:

- `paper/main.tex` is the active manuscript source.
- The preamble currently loads plain `hyperref` but has no explicit VLA-style
  `\hypersetup`.
- The current PDF already has the desired green/red boxed-link behavior, but
  the source should make that behavior explicit and stable.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\hypersetup` block immediately after `\usepackage{hyperref}`
   in `paper/main.tex`.
2. Rebuild with `scripts/build_paper.ps1`, including BibTeX, so the final PDF
   is copied to Downloads and local `paper/main.pdf` is removed.
3. If the first rebuild asks for another LaTeX pass, rerun the canonical build
   and use only the final artifact metadata.
4. Recompute page count, SHA256, annotation colors, border widths, and link
   pages from the rebuilt PDF.
5. Render all affected link pages from the rebuilt Downloads PDF into
   `tmp/pdfs/paper26_after`.
6. Visually inspect the rendered affected pages:
   - green citation boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
7. Update README/status/audit/version/validation metadata with the new hash and
   visual-hardening result.
8. Scan LaTeX logs for fatal errors, undefined citations/references, rerun
   warnings, and overfull boxes.
9. Remove Paper26 temp renders, leaving only the shared role-model render
   directory.
10. Stage only Paper26 source and metadata files, commit, push, and verify a
    clean repository.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations merely to change link counts.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Rebuilt Downloads artifact: `C:/Users/wangz/Downloads/26.pdf`
- Pages: 25
- Size: 371778 bytes
- SHA256: `7D31075ED0F6CC9DF9AFFE14C3D7D9621EF43285D64E20E281B7E3C02E582BC9`
- Local `paper/main.pdf`: absent after export
- Link pages after rebuild:
  `[(2, 28), (3, 4), (5, 2), (6, 1), (7, 3), (16, 1), (18, 3), (20, 4), (23, 1)]`
- Annotation colors after rebuild: green = 32, red = 15, cyan = 0
- Border widths after rebuild: `(0, 0, 1)` for all 47 link annotations
- Rendered affected pages inspected from `tmp/pdfs/paper26_after`; green
  citation boxes and red internal-reference boxes are crisp and aligned, and
  no cyan boxes are present.

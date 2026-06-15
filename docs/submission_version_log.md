# Submission Version Log

## v3 - 2026-06-15

- Wrote `docs/full_scale_execution_plan.md` before v3 substantive work.
- Added `experiments/full_scale_gcs.py`, a RAM-light full-scale experiment runner.
- Generated `results/full_scale/` with 79,305 rows, 10,135 cases, seed 26026, and zero plot failures.
- Generated full-scale figures under `figures/full_scale/`.
- Generated full-scale TeX tables under `results/full_scale/tex/`.
- Rewrote and expanded `paper/main.tex` into a 25-page final manuscript.
- Added extended audit content: complete horizon ledger, reuse ledger, topology baseline audit, probe-cost break-even, guard-error calibration, coverage/spurious-guard ledger, proof invariants, data integrity notes, and deployment protocol.
- Built final PDF and copied it to `C:/Users/wangz/Downloads/26.pdf`.
- Verified final PDF: 25 pages, 371778 bytes, SHA256 `A36A75140750716A0D4E61DD4D59A7251AF27F6780FC0DDC5FA522AF61D8AAB9`.
- Removed local `paper/main.pdf` after canonical export.

## v2 - 2026-06-13

- Added noisy-guard execution to `src/guarded_skeletons.py`.
- Added guard-assumption stress generation to `experiments/run_guarded_skeletons.py`.
- Generated `results/guard_assumption_stress.csv`.
- Generated `results/guard_assumption_stress_summary.csv`.
- Generated `results/guard_assumption_stress_table.tex`.
- Updated the manuscript with a visible v2 note, stress table, and narrowed limitations.
- Patched `scripts/build_paper.ps1` to fail nonzero on LaTeX/BibTeX errors and remove local `paper/main.pdf` after copying to Downloads.

## v1 - 2026-06-11

- Initial GCS paper package with literature sweep, synthetic experiment, ICLR-style manuscript, final audit, canonical Downloads PDF, and public GitHub repo.

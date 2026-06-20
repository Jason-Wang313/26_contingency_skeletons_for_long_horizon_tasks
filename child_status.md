# Child Status

Stage: v3 final full-scale complete; VLA link-box hardening exported and
verified; ready for commit and push.

Latest actions:
- Wrote `docs/full_scale_execution_plan.md` before substantive v3 work.
- Added RAM-light full-scale runner `experiments/full_scale_gcs.py`.
- Ran the v3 suite to completion: 79,305 rows, 10,135 cases, seed 26026, zero plot failures.
- Rewrote and expanded `paper/main.tex` into a 25-page final manuscript with main results, ablations, stress tests, negative controls, counterexamples, limitations, and reproducibility detail.
- Built the final PDF with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied the verified final PDF to `C:/Users/wangz/Downloads/26.pdf`.
- Removed local `paper/main.pdf` after canonical export.
- Added explicit VLA-style `hyperref` boxed-link policy and rebuilt the
  Downloads PDF.

Verification:
- Downloads PDF exists: true.
- Downloads PDF pages: 25.
- Downloads PDF bytes: 371778.
- Downloads PDF SHA256: `7D31075ED0F6CC9DF9AFFE14C3D7D9621EF43285D64E20E281B7E3C02E582BC9`.
- Required PDF text markers found: `v3 final full-scale`, `79,305`, `10,135`, `probe cost 6.0`, `100% guard error`, and `does not claim real-robot`.
- `python -m py_compile .\experiments\full_scale_gcs.py` passed.
- Final LaTeX log has no undefined references, undefined citations, or overfull boxes.
- Link annotation inventory is green = 32, red = 15, cyan = 0, with one-point
  borders on all 47 link annotations.
- Rendered link pages 2, 3, 5, 6, 7, 16, 18, 20, and 23 were visually
  inspected.
- Local `paper/main.pdf` is absent.

Key findings:
- Family A eager GCS cost: 58.45.
- Family A replan-on-failure cost: 92.51.
- Family A linear default cost: 312.54.
- Family A eager GCS nodes: 293,649.
- Family A no-sharing GCS nodes: 79.10 billion.
- Probe cost 6.0 makes eager GCS worse than replan by 48.53.
- 100% guard error makes eager GCS worse than replan by 35.34.

Next:
- Commit and push Paper26 v3 final full-scale.
- Verify clean worktree and `HEAD == @{u}`.
- Only then proceed to Paper27.

End time: 2026-06-15 05:32:44 +01:00

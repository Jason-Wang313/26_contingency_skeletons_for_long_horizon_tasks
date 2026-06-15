# Child Status

Stage: v3 final full-scale complete; ready for commit and push.

Latest actions:
- Wrote `docs/full_scale_execution_plan.md` before substantive v3 work.
- Added RAM-light full-scale runner `experiments/full_scale_gcs.py`.
- Ran the v3 suite to completion: 79,305 rows, 10,135 cases, seed 26026, zero plot failures.
- Rewrote and expanded `paper/main.tex` into a 25-page final manuscript with main results, ablations, stress tests, negative controls, counterexamples, limitations, and reproducibility detail.
- Built the final PDF with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied the verified final PDF to `C:/Users/wangz/Downloads/26.pdf`.
- Removed local `paper/main.pdf` after canonical export.

Verification:
- Downloads PDF exists: true.
- Downloads PDF pages: 25.
- Downloads PDF bytes: 371778.
- Downloads PDF SHA256: `A36A75140750716A0D4E61DD4D59A7251AF27F6780FC0DDC5FA522AF61D8AAB9`.
- Required PDF text markers found: `v3 final full-scale`, `79,305`, `10,135`, `probe cost 6.0`, `100% guard error`, and `does not claim real-robot`.
- `python -m py_compile .\experiments\full_scale_gcs.py` passed.
- Final LaTeX log has no undefined references, undefined citations, or overfull boxes.
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

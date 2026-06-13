# Reproducibility Checklist

- [x] Main simulator is `src/guarded_skeletons.py`.
- [x] Main experiment script is `experiments/run_guarded_skeletons.py`.
- [x] Build script is `scripts/build_paper.ps1`.
- [x] Main outputs are `results/episodes.csv`, `results/summary.csv`, and `results/evidence_table.tex`.
- [x] V2 outputs are `results/guard_assumption_stress.csv`, `results/guard_assumption_stress_summary.csv`, and `results/guard_assumption_stress_table.tex`.
- [x] Figures are in `paper/figures/`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical PDF path is `C:/Users/wangz/Downloads/26.pdf`.
- [x] Local `paper/main.pdf` is removed after canonical copy.
- [x] Visible Desktop PDF copies are absent.

Recommended verification commands:

```powershell
python experiments\run_guarded_skeletons.py
powershell -ExecutionPolicy Bypass -File scripts\build_paper.ps1
```

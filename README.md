# Guarded Contingency Skeletons for Long-Horizon Robot Tasks

Anonymous research artifact for paper 26 in the robotics/embodied-intelligence batch.

## Contents

- `docs/related_work_matrix.csv`: 5147-paper landscape sweep.
- `docs/literature_map.md`: field map, hidden assumptions, candidate directions, and chosen thesis.
- `docs/hostile_prior_work.md`: 100-paper hostile prior-work set.
- `src/guarded_skeletons.py`: toy guarded contingency skeleton domain and baselines.
- `experiments/run_guarded_skeletons.py`: reproducible synthetic evidence.
- `results/summary.csv`: aggregate experiment results.
- `results/guard_assumption_stress_summary.csv`: v2 guard-cost and guard-error stress summary.
- `paper/main.tex`: anonymous ICLR-style manuscript.

## Reproduce

Run the experiment:

```powershell
python experiments/run_guarded_skeletons.py
```

Build the paper and copy the final PDF to `C:/Users/wangz/Downloads/26.pdf`:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
```

The plotting step uses `matplotlib` when available. If it is missing, the CSV and LaTeX table still build, but figures are not regenerated. The build script copies the canonical PDF to `C:/Users/wangz/Downloads/26.pdf` and removes local `paper/main.pdf` after the copy.

## V2 Hardening

- Added guard-assumption stress tests for expensive guard probes and noisy guard observations.
- At probe cost 6.00, GCS cost is 158.60, which is 14.79 worse than replan-on-failure.
- With 100% flipped guard observations, noisy GCS cost is 148.46, which is 4.66 worse than replan-on-failure.
- The manuscript now narrows the claim to cheap, calibrated, safe-to-test guards.

# Experiment Status

- Synthetic guard-deterministic TAMP abstraction completed.
- At horizon 64 / reuse 0.55, guarded skeleton cost 65.26 vs replan-on-failure 143.81.
- At horizon 64 / reuse 0.55, guarded skeleton nodes 273 vs relevant unshared tree 3820748.
- V2 probe-cost stress: when probe cost is 6.00, GCS cost 158.60, delta vs replan +14.79.
- V2 guard-error stress: when guards are always flipped, noisy GCS cost 148.46, delta vs replan +4.66.
- Outputs: `results/episodes.csv`, `results/summary.csv`, `results/evidence_table.tex`, and `paper/figures/*.pdf` if matplotlib is available.
- V2 outputs: `results/guard_assumption_stress.csv`, `results/guard_assumption_stress_summary.csv`, and `results/guard_assumption_stress_table.tex`.

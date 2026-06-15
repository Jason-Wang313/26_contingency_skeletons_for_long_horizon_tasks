# Experiment Report

## Run

- Script: `experiments/full_scale_gcs.py`.
- Seed: 26026.
- Elapsed time: 491.519 seconds.
- Total rows: 79,305.
- Total cases: 10,135.
- Plot failures: 0.
- Output root: `results/full_scale/`.

## Families

| Family | Rows | Cases | Runtime seconds |
|---|---:|---:|---:|
| A | 34,560 | 4,320 | 187.247 |
| B | 9,600 | 1,600 | 52.558 |
| C | 5,400 | 1,080 | 39.600 |
| D | 18,225 | 1,215 | 130.066 |
| E | 3,600 | 600 | 22.016 |
| F | 2,520 | 420 | 22.258 |
| G | 5,400 | 900 | 28.354 |

## Positive Result

Family A shows that, with cheap reliable guards, eager GCS reduces failed execution:

- Eager GCS cost: 58.45.
- Lazy GCS cost: 58.45.
- Replan-on-failure cost: 92.51.
- Linear default cost: 312.54.
- Oracle assignment cost: 57.33.

Family A also supports the representation claim:

- Eager GCS nodes: 293,649.
- No-sharing GCS nodes: 79.10 billion.
- Probe-all tree nodes: 93.33 billion.

## Boundaries

- Probe economics: at probe cost 6.0, eager GCS costs 157.60 and loses to replan by 48.53.
- Guard reliability: at 100% guard error, eager GCS costs 149.26 and loses to replan by 35.34.
- Coverage: missing relevant guards produce many failures and invalidate the formal coverage guarantee.
- Dense dependencies: GCS node count grows sharply when local action certificates depend on large guard subsets.

## Final Interpretation

The experiment supports GCS as a compact conditional-skeleton mechanism for known, cheap, safe, calibrated, locally sparse physical guards. It does not establish hardware readiness, learned guard discovery, production TAMP superiority, POMDP optimality, or safety certification.

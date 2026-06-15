# Full-Scale Evidence Summary

- Stage: complete.
- Seed: 26026.
- Rows: 79,305.
- Cases: 10,135.
- Plot failures: 0.
- Elapsed experiment time: 491.519 seconds.
- Final PDF: `C:/Users/wangz/Downloads/26.pdf`.
- Final PDF pages: 25.
- Final PDF bytes: 371778.
- Final PDF SHA256: `A36A75140750716A0D4E61DD4D59A7251AF27F6780FC0DDC5FA522AF61D8AAB9`.

## Family Inventory

| Family | Rows | Cases | Purpose |
|---|---:|---:|---|
| A | 34,560 | 4,320 | Horizon, topology, dependency width, reuse, and main methods. |
| B | 9,600 | 1,600 | Probe cost, failure penalty, irreversibility, and guard economics. |
| C | 5,400 | 1,080 | Guard error, confidence calibration, thresholds, and robust policies. |
| D | 18,225 | 1,215 | Baselines and ablations. |
| E | 3,600 | 600 | Missing guards, spurious guards, and coverage failures. |
| F | 2,520 | 420 | Negative controls. |
| G | 5,400 | 900 | Counterexample library. |

## Headline Numbers

- Family A linear-default cost: 312.54.
- Family A replan-on-failure cost: 92.51.
- Family A GCS eager cost: 58.45.
- Family A lazy GCS cost: 58.45.
- Family A no-sharing GCS nodes: 79.10 billion.
- Family A GCS eager nodes: 293,649.
- Family B probe cost 6.0: eager GCS cost 157.60, 48.53 worse than replan.
- Family C 100% guard-error: eager GCS cost 149.26, 35.34 worse than replan.
- Family E missing relevant guards: many failures, so formal coverage no longer applies.

## Scope

These results support a synthetic representation mechanism for long-horizon guard-deterministic TAMP abstractions. They do not establish real-robot safety, learned guard discovery, production TAMP superiority, general POMDP optimality, or safety certification.

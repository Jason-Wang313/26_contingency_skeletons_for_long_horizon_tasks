# Experiment Rigor Checklist

- [x] Detailed v3 plan written before substantive v3 edits: `docs/full_scale_execution_plan.md`.
- [x] RAM-light full-scale runner exists: `experiments/full_scale_gcs.py`.
- [x] Runner compiles with `python -m py_compile .\experiments\full_scale_gcs.py`.
- [x] Full-scale suite completed: 79,305 rows over 10,135 cases.
- [x] Metadata records seed 26026 and zero plot failures.
- [x] Family A covers horizons 8, 16, 32, 64, 96, and 128.
- [x] Family A covers clustered, banded, uniform-sparse, dense, and suffix-unique topologies.
- [x] Main methods include linear default, replan-on-failure, probe-all tree, relevant unshared tree, eager GCS, lazy GCS, no-sharing GCS, and oracle assignment.
- [x] Family B attacks probe cost, failure penalty, and irreversibility.
- [x] Family C attacks guard noise, confidence calibration, thresholds, and robust testing.
- [x] Family D includes broad baselines and ablations including behavior-tree fallback and delayed GCS.
- [x] Family E attacks missing and spurious guard coverage.
- [x] Family F/G include negative controls and counterexample mining.
- [x] Final manuscript is 25 pages and includes generated tables/figures.
- [x] Canonical PDF exported to `C:/Users/wangz/Downloads/26.pdf`.
- [ ] No real robot validation.
- [ ] No mature TAMP backend integration.
- [ ] No learned guard discovery.
- [ ] No general belief-space/POMDP baseline.

Decision: final synthetic mechanism paper under the current batch standard. The claim remains scoped to known, cheap, safe, calibrated, locally sparse physical guards.

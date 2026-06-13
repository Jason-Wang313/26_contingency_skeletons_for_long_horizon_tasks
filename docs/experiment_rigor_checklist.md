# Experiment Rigor Checklist

- [x] Main synthetic suite regenerates from `experiments/run_guarded_skeletons.py`.
- [x] Main sweep covers horizons 8, 16, 32, 48, and 64.
- [x] Main sweep uses 30 seeds and 200 assignments per seed.
- [x] Main baselines include linear default, replan-on-failure, probe-all tree, relevant unshared tree, and GCS.
- [x] V2 probe-cost stress attacks the cheap-guard assumption.
- [x] V2 noisy-guard stress attacks the reliable-guard assumption.
- [x] Negative boundary is explicit: GCS loses to replan at probe cost 6.00 and at 100% flipped guards.
- [ ] No real robot validation.
- [ ] No production TAMP integration.
- [ ] No learned guard discovery.
- [ ] No probabilistic belief-space baseline.

Decision: mechanism evidence only; terminal state is workshop-only / strong-revise.

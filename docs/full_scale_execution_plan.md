# Paper 26 Full-Scale Execution Plan

## Current Claim

The current v2 paper proposes Guarded Contingency Skeletons (GCS): compact decision DAGs for long-horizon task-and-motion planning where internal branch nodes are measurable physical guard predicates and leaves/fragments are task-motion skeleton pieces. The core thesis is that some long-horizon robot tasks should not commit to one linear symbolic skeleton and repair geometric failures late. Instead, the planning artifact should carry a compact set of physical contingencies when the branch conditions are cheap and safe to test.

The v2 evidence is promising but still narrow:

- Main synthetic suite: horizons 8, 16, 32, 48, 64; reuse biases 0.25, 0.55, 0.85; 30 seeds; 200 guard assignments per seed.
- Baselines: linear default, replan-on-failure, probe-all tree, relevant unshared tree, and GCS.
- Main result at horizon 64 / reuse 0.55: GCS expected cost 65.26 versus replan-on-failure 143.81, and GCS uses 273 nodes versus 3.82 million nodes for the relevant unshared tree.
- V2 stress: at probe cost 6.00, GCS cost becomes 158.60, which is 14.79 worse than replan. With 100% flipped guards, noisy GCS cost becomes 148.46, which is 4.66 worse than replan.
- Current manuscript is short and still judged workshop-only / strong-revise because evidence is synthetic, guard models are simple, and no broad stress/ablation matrix exists.

The v3 target is a final full-scale synthetic mechanism paper of at least 25 pages with much larger scope: richer guard regimes, broader baselines, cost/noise/safety stress, sparse-to-dense dependency sweeps, negative controls, counterexamples, and reproducibility artifacts.

## Main Gaps To Close

1. **Scale gap:** The current run has only a small grid and a few thousand rows. V3 should exceed 75,000 rows and preferably produce a six-figure row count while staying RAM-light.
2. **Dependency gap:** The compactness claim depends on sparse and reused guard dependencies. V3 must sweep sparse, banded, clustered, dense, adversarial, and suffix-unique dependency patterns.
3. **Baseline gap:** Current baselines are simple. V3 should add lazy guard testing, thresholded GCS, batched probe-all-local, myopic value-of-information, robust/noisy GCS, delayed-guard GCS, behavior-tree fallback proxy, belief-cost proxy, and oracle references.
4. **Robustness gap:** Current stress tests only probe cost and guard flips at one setting. V3 should test guard cost, guard noise, false positives/false negatives separately, irreversible action rate, repair cost, guard-test safety risk, missing guards, delayed observations, and dense dependencies.
5. **Ablation gap:** GCS mixes guard placement, suffix sharing, dominance pruning, early testing, and certification. Each component needs to be separated.
6. **Negative-control gap:** The paper must show where GCS should not help: zero failure penalty, dense dependencies, expensive/unsafe guards, random irrelevant guards, no reuse, all guards needed upfront, and missing coverage.
7. **Writing gap:** The final manuscript needs a deeper method section, algorithm pseudocode, proof detail, result ledgers, failure taxonomy, deployment guardrails, and a real-robot protocol that is explicitly not claimed.

## V3 Method Upgrade

Keep GCS as the central representation, but add scoped variants:

- **Eager GCS:** current policy, probes every needed guard before the first dependent action.
- **Lazy GCS:** delays guard tests until the local expected failure penalty exceeds probe cost.
- **Thresholded GCS:** tests guards only when guard confidence and expected value pass thresholds.
- **Robust GCS:** uses repeated guard tests or conservative fallback under noisy observations.
- **Delayed GCS ablation:** intentionally tests guards after first dependency to show late discovery cost.
- **No-sharing GCS ablation:** preserves guard testing but removes DAG suffix sharing.
- **No-dominance GCS ablation:** disables dominance pruning.
- **Probe-all-local baseline:** probes all relevant guards upfront.
- **Myopic VOI baseline:** probes the guard with largest immediate expected failure reduction.
- **Behavior-tree fallback proxy:** executes default skeleton with ordered condition/fallback checks.
- **Belief-cost proxy:** uses known guard probabilities to choose expected-cost actions without full GCS sharing.
- **Oracle assignment reference:** knows the full guard assignment and uses minimal correct skeleton cost.

The paper should not claim a complete TAMP solver, guard discovery from raw perception, real robot safety, POMDP optimality, or superiority over production planning stacks.

## Experiment Families

### Family A: Full Horizon/Dependency Sweep

Purpose: scale the main result across long horizons and guard dependency structures.

Variables:

- Horizons: 8, 16, 32, 48, 64, 96, 128.
- Reuse bias: 0.0, 0.25, 0.55, 0.85, 1.0.
- Dependency width: 1, 2, 3, 4.
- Dependency topology: clustered, banded, uniform sparse, dense, adversarial suffix-unique.
- Guard probability entropy: low, medium, high.

Expected honest outcome:

- GCS should be strongest in sparse/reused regimes.
- Dense and suffix-unique regimes should shrink or remove compactness gains.

### Family B: Guard Cost, Failure Cost, and Irreversibility

Purpose: map the economics of probing versus failing.

Variables:

- Probe cost from nearly free to more expensive than failure.
- Failure penalty and repair penalty.
- Irreversible action rate.
- Catastrophic failure multiplier.

Expected honest outcome:

- Early guards help when failures are expensive or irreversible.
- Replanning can beat GCS when probes are expensive and failures are cheap/reversible.

### Family C: Guard Reliability and Calibration

Purpose: expand the v2 noisy-guard stress.

Variables:

- Symmetric guard error.
- False-positive and false-negative asymmetry.
- Confidence calibration: calibrated, overconfident, underconfident, adversarial.
- Repeated-test policies and fallback thresholds.

Expected honest outcome:

- Uncalibrated or adversarial guards can make GCS worse than replan.
- Repeated tests reduce error but can lose when probe cost is high.

### Family D: Baselines and Ablations

Purpose: isolate what makes GCS work.

Baselines/ablations:

- Linear default.
- Replan-on-failure.
- Probe-all tree.
- Relevant unshared tree.
- Probe-all-local.
- Myopic VOI.
- Behavior-tree fallback proxy.
- Belief-cost proxy.
- Eager GCS.
- Lazy GCS.
- Robust GCS.
- Delayed GCS.
- No-sharing GCS.
- No-dominance GCS.
- Oracle assignment reference.

Expected honest outcome:

- Guard placement reduces failures.
- DAG sharing reduces representation size.
- Dominance pruning may matter mostly in redundant regimes.

### Family E: Missing Guards and Coverage Failures

Purpose: stress the finite-candidate coverage assumption.

Variables:

- Fraction of missing relevant guards.
- Spurious irrelevant guards.
- Guard regions that do not cover all assignments.
- Hidden guard interactions not represented by local dependencies.

Expected honest outcome:

- Missing relevant guards cause failures even with GCS.
- Spurious guards increase cost/size without reducing failures.

### Family F: Negative Controls

Purpose: prevent overclaiming.

Controls:

- Zero failure penalty.
- Probe cost greater than any failure penalty.
- Dense all-guard dependencies.
- No guard reuse.
- All guards needed at first step.
- Perfectly reversible failures.
- Already-known assignment.

Expected honest outcome:

- GCS advantage should vanish or reverse when early testing is not valuable or sharing is impossible.

### Family G: Counterexample and Failure Library

Purpose: create concrete reviewer-facing cases.

Outputs:

- Expensive probes worse than replan.
- Wrong guards worse than replan.
- Dense dependency representation explosion.
- Missing guard coverage failure.
- Lazy guard delay failure.
- Spurious guard cost waste.
- No-reuse regime where GCS is not compact.

## RAM-Light Execution Strategy

- Run families sequentially.
- Stream row-level CSVs to `results/full_scale/`.
- Keep only aggregate counters, small examples, and summaries in memory.
- Save `progress.json` after each family.
- Generate compact summary CSVs and TeX tables after row streaming.
- Generate figures from summaries, not from all rows.
- Use deterministic seed 26026 with family-specific offsets.
- Avoid high-dimensional state enumeration except for representation-size formulas; never materialize exponential trees.

## Required Figures And Tables

Figures:

- Main cost by method.
- Representation size versus horizon.
- Cost versus probe cost and failure penalty.
- Guard error/calibration curves.
- Dependency density compactness curve.
- Negative control outcomes.

Tables:

- Full-scale main benchmark.
- Dependency topology table.
- Guard economics table.
- Guard reliability table.
- Baseline/ablation table.
- Missing-coverage table.
- Negative-control table.
- Claim-to-evidence table.

## Manuscript Expansion Strategy

The final paper should reach at least 25 pages from real content:

- Core: abstract, introduction, related work, problem setup, GCS definition, synthesis algorithm, formal propositions, baselines, full-scale experiments, results, limitations, conclusion.
- Appendices: proof detail, simulator specification, dependency topologies, guard economics, noisy/calibrated guards, baseline definitions, ablations, negative controls, counterexamples, deployment guardrails, real-robot protocol, reproducibility, artifact manifest, validation report.

## Final Acceptance Checklist

Before moving to Paper 27:

- This plan exists and was written before v3 substantive edits.
- Full-scale experiment suite completes with deterministic metadata.
- Results include at least 75,000 rows.
- Manuscript builds locally to at least 25 pages.
- PDF text contains `v3 final full-scale`, row/case counts, headline cost/size values, guard failure boundaries, and no-real-robot limitation.
- Final PDF is copied to `C:/Users/wangz/Downloads/26.pdf`.
- Local `paper/main.pdf` is removed after export.
- Final PDF page count, byte count, and SHA256 are recorded in docs.
- README, child status, claims, evidence summary, experiment report, rigor checklist, final audit, hostile response, reproducibility checklist, reviewer attacks, attack log, readiness decision, version log, and validation report are updated.
- Repo is committed, pushed, clean, and `HEAD == @{u}` before Paper 27 begins.

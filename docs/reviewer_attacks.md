# Reviewer Attacks

## Attack 1: Is this just contingent planning?
No for the claimed boundary: contingent planning supplies symbolic observation policy machinery; GCS contributes physical guard lifting and skeleton sharing for TAMP alternatives. The paper must cite contingent planning as prior art and avoid first-policy language.

## Attack 2: Is this just a behavior tree?
Behavior trees are an execution representation. GCS is a compilation target with guard placement and dominance derived from candidate skeleton feasibility dependencies.

## Attack 3: Where do guards come from?
In this paper they are assumed or extracted from synthetic feasibility dependencies. This is a weakness; learned/raw-perception guard discovery is future work.

## Attack 4: Why no real robot?
The paper is workshop/revise strength: it demonstrates a mechanism and failure mode synthetically, not deployment readiness.

## Attack 5: Does the DAG become exponential?
Yes in worst case. The claim is conditional compactness under sparse or reused guard dependence, and experiments sweep regimes where this assumption varies.

## Attack 6: Could replanning solve it?
Only when failed attempts are cheap/reversible. The experiment explicitly varies irreversible failure penalties and shows the break-even condition.

## Attack 7: Could PDDLStream encode guards as predicates?
It could encode them if the designer already supplied symbolic tests. The novelty claim is the skeleton-level compilation and branch sharing, not representability in a language.

## Attack 8: Are probabilities ignored?
Coverage does not require probabilities; expected-cost evaluation can use them. The paper should not claim risk optimality.

## Attack 9: Is the literature sweep shallow?
The matrix is broad and metadata-driven; the hostile set extracts assumptions consistently but is not equivalent to reading 100 full PDFs. The audit must state this.

## Attack 10: Does the proof prove planning completeness?
No. It proves dispatch coverage for candidate skeletons under explicit guard assumptions.

## Attack 11: Is this only a new name?
The runnable artifact must show concrete data structures, dispatch, dominance/sharing, and baselines.

## Attack 12: Can physical guards be tested safely?
Only if the guard is cheap/reversible by domain design. The assumption is central and false in some domains.

## Attack 13: What if guard tests are expensive or wrong?
The v2 stress makes this a limitation, not a hidden premise. At probe cost 6.00, GCS is 14.79 cost units worse than replan-on-failure; with 100% flipped guard observations, noisy GCS is 4.66 worse. The paper must claim a compact representation for cheap calibrated guards, not a robust guard-learning system.

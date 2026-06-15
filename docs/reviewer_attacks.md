# Reviewer Attacks

## Attack 1: Is this just contingent planning?
No for the claimed boundary: contingent planning supplies symbolic observation policy machinery; GCS contributes physical guard lifting and skeleton sharing for TAMP alternatives. The paper cites contingent planning and avoids claiming to invent conditional policies.

## Attack 2: Is this just a behavior tree?
Behavior trees are a relevant execution representation. Family D explicitly includes a behavior-tree fallback proxy that can match clean execution cost. GCS is framed as a compilation target with guard placement, coverage assumptions, and shared skeleton fragments, not as the only way to write condition checks.

## Attack 3: Where do guards come from?
In this paper they are assumed or extracted from synthetic feasibility dependencies. This is a central weakness; learned/raw-perception guard discovery is future work.

## Attack 4: Why no real robot?
The paper is a synthetic mechanism paper, not a deployment paper. The manuscript explicitly says it does not claim real-robot readiness.

## Attack 5: Does the DAG become exponential?
Yes in dense or guard-unique cases. The compactness claim is conditional on sparse local guard dependence. Family A/D include dense cases to expose this boundary.

## Attack 6: Could replanning solve it?
Only when failed attempts are cheap/reversible or guard probes are expensive. Family B shows the break-even: at probe cost 6.0, eager GCS is 48.53 worse than replan.

## Attack 7: Could PDDLStream encode guards as predicates?
It could encode supplied symbolic tests. The novelty claim is not expressivity in a language; it is skeleton-level compilation and branch sharing under explicit guard dependencies.

## Attack 8: Are probabilities ignored?
Coverage does not require probabilities; expected-cost variants use simple probability proxies. The paper does not claim risk optimality or POMDP optimality.

## Attack 9: Is the literature sweep shallow?
The matrix is broad and metadata-driven; the hostile set extracts assumptions consistently but is not equivalent to reading 100 full PDFs end to end. The audit states this.

## Attack 10: Does the proof prove planning completeness?
No. It proves dispatch coverage for candidate skeletons under explicit guard assumptions. It does not prove candidate generation or arbitrary TAMP completeness.

## Attack 11: Is this only a new name?
The artifact includes concrete data structures, dispatch policies, sharing/size formulas, ablations, and counterexamples. The v3 suite makes the mechanism measurable.

## Attack 12: Can physical guards be tested safely?
Only if the domain supplies safe probes. The paper treats probe safety as an assumption and a required real-robot acceptance test.

## Attack 13: What if guard tests are expensive or wrong?
The v3 suite makes this a limitation, not a hidden premise. At probe cost 6.0, eager GCS is 48.53 worse than replan. At 100% guard error, eager GCS is 35.34 worse than replan.

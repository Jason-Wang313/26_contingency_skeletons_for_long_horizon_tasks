# Submission Attack Log

Updated: 2026-06-13 04:45:39 +01:00

## Attack Rounds

1. Closest-prior attack: TAMP, contingent planning, behavior trees, and belief-space planning already own broad conditional-policy territory. Response: keep novelty to guard-indexed skeleton DAG compilation with shared task-motion fragments.
2. Representation attack: compactness is conditional and can be exponential in dense guard-dependence cases. Response: the theorem and text state sparse local dependence explicitly.
3. Evidence attack: the main experiment gives GCS perfect, cheap, deterministic guards. Response: add v2 guard-assumption stress.
4. Robustness attack: wrong guard observations can route execution into the wrong skeleton. Response: add noisy-guard execution and quantify the failure boundary.
5. Cost attack: if guard probes are expensive, early tests may be worse than replanning. Response: add probe-cost stress.
6. Artifact attack: v1 left `paper/main.pdf` in the repo. Response: patch build script to copy only to Downloads and remove local PDF.

## V2 Outcome

The paper remains workshop-only / strong-revise. GCS is compelling as a representation mechanism under cheap, calibrated, safe-to-test guards, but v2 shows that high probe cost or systematically wrong guards can make it worse than replan-on-failure.

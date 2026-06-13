# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Why Not Submit-Ready

- Evidence is synthetic and uses an abstraction rather than a mature TAMP backend.
- Guards are assumed known and binary.
- V2 shows expensive probes and badly wrong guards can make GCS worse than replanning.
- There is no hardware validation, learned guard extraction, or noisy-belief handling.

## Why Not Kill

- The representation mechanism is crisp and distinct from simple linear skeleton repair.
- The compactness theorem is honest about sparse guard-dependence assumptions.
- The v2 stress makes the cheap/reliable-guard boundary explicit.

## Required Next Work

- Add calibrated guard confidence and fallback branches.
- Integrate with a real TAMP system such as PDDLStream or LGP.
- Evaluate on realistic manipulation/rearrangement domains with safe guard tests.
- Compare against behavior-tree synthesis and belief-space TAMP baselines.

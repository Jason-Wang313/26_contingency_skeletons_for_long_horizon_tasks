# Hostile Reviewer Response

## Likely Rejection

The work assumes the hard part: known, cheap, binary, deterministic, safe-to-test physical guards. Without those guards, the representation can route execution into the wrong branch or spend too much probing.

## Honest Response

We agree. GCS is not a complete TAMP solver, belief-space planner, or guard-learning system. It is a compact compilation target for candidate skeletons when physical feasibility dependencies can be exposed as reliable guards.

The v2 stress quantifies the boundary. At probe cost 6.00, GCS cost rises to 158.60, which is 14.79 worse than replan-on-failure. With 100% flipped guard observations, noisy GCS costs 148.46, which is 4.66 worse than replan-on-failure. The paper should claim only the cheap/calibrated-guard regime.

## Required Upgrade For Main-Track Submission

- Demonstrate guard extraction in a real or mature simulated TAMP domain.
- Add noisy guard confidence handling and fallback to replanning.
- Compare against PDDLStream, behavior-tree synthesis, and belief-space TAMP baselines.
- Show that guard tests are safe and cheaper than failed execution in realistic domains.

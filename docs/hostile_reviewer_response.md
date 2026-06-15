# Hostile Reviewer Response

## Likely Rejection

The work assumes the hard part: known, cheap, binary, deterministic, safe-to-test physical guards. Without those guards, the representation can route execution into the wrong branch, miss coverage, or spend too much probing. The evidence is synthetic rather than hardware or mature TAMP integration.

## Honest Response

We agree. GCS is not a complete TAMP solver, belief-space planner, or guard-learning system. It is a compact compilation target for candidate skeletons when physical feasibility dependencies can be exposed as reliable guards.

The v3 suite quantifies the boundary rather than hiding it. Across Family A, eager GCS costs 58.45 versus 92.51 for replan-on-failure. But at probe cost 6.0, eager GCS costs 157.60 and is 48.53 worse than replan. At 100% guard error, eager GCS costs 149.26 and is 35.34 worse than replan. Missing-guard Family E/G shows many failures and removes the formal coverage guarantee.

## What The Paper Can Claim

For synthetic guard-deterministic long-horizon TAMP abstractions with known, cheap, safe, calibrated, locally sparse physical guards, GCS can reduce failed execution relative to linear/replan strategies while remaining dramatically smaller than unshared contingency trees.

## What The Paper Must Not Claim

- Real-robot readiness.
- Learned guard discovery.
- Production TAMP superiority.
- General POMDP optimality.
- Safety certification.
- Universal advantage of eager testing.

## Required Upgrade For A Stronger Robotics Submission

- Demonstrate guard extraction in a real or mature simulated TAMP domain.
- Add calibrated guard confidence, independent guard checks, and fallback to replanning.
- Compare against PDDLStream, behavior-tree synthesis, and belief-space TAMP baselines.
- Show that guard tests are safe and cheaper than failed execution in realistic domains.

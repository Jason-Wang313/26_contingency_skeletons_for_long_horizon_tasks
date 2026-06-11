# Novelty Decision

## Decision
Proceed with **Guarded Contingency Skeletons for Long-Horizon Robot Tasks**.

## Thesis
Long-horizon task-and-motion planners often commit to a linear skeleton before the physical branch conditions that determine feasibility are measured. A guarded contingency skeleton instead compiles candidate skeletons into a compact decision DAG with branch nodes tied to measurable physical guards, allowing the robot to test cheap/reversible conditions before irreversible or high-penalty actions while sharing the rest of the plan.

## Why This Is Stronger Than The Seed
The seed suggested contingency skeletons with physical branching conditions. The literature sweep sharpened that into a representation mechanism: guard extraction, earliest-safe guard placement, and suffix/prefix sharing across guard-equivalent skeletons. The paper is not about adding uncertainty, a verifier, an LLM planner, or a benchmark; it is about moving the central planning object from one skeleton to a guard-indexed skeleton DAG.

## Rejected Directions
- Runtime TAMP repair tree: Too close to execution monitoring and behavior-tree fallback; central mechanism remains repair after failure.
- Belief-space TAMP with branch penalties: Would mainly add uncertainty/cost shaping, which prior POMDP and belief-space TAMP already cover.
- LLM-generated contingency plans: Falls into the forbidden weak move: using an LLM as planner without a new physical mechanism.

## Required Evidence
- Formalize guard-deterministic domains and skeleton DAG coverage.
- Prove compactness relative to unshared contingency trees under sparse guard dependence.
- Run a synthetic embodied TAMP abstraction showing when broken assumptions matter: failed execution and representation blow-up grow with horizon if branch conditions are not represented early.

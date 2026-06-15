# Claims

| Claim | Status | Support | Caveat |
|---|---|---|---|
| GCS is complete for a finite set of candidate skeletons in guard-deterministic domains with sound, exhaustive guards. | Formal conditional claim. | Proposition and proof in `paper/main.tex`. | Does not imply candidate generation, arbitrary TAMP completeness, noisy-guard correctness, or missing-guard coverage. |
| GCS can be much smaller than an unshared contingency tree under sparse local guard dependence. | Formal proposition plus v3 measurement. | Family A: eager GCS averages 293,649 nodes versus 79.10 billion for no-sharing GCS. | Dense dependencies inflate GCS size; compactness is conditional. |
| Early physical guard testing reduces failed execution in the synthetic abstraction when guards are cheap and reliable. | Empirical v3 claim. | Family A: eager GCS cost 58.45 versus replan 92.51 and linear default 312.54. | Synthetic only; not a real robot or production TAMP benchmark. |
| Eager GCS is not universally better than replan. | Empirical v3 boundary. | At probe cost 6.0, eager GCS cost 157.60 and is 48.53 worse than replan. At 100% guard error, eager GCS cost 149.26 and is 35.34 worse than replan. | Lazy, thresholded, and robust variants help in some regimes but do not remove the core assumptions. |
| The mechanism is not merely behavior trees. | Narrow novelty claim. | Family D explicitly includes behavior-tree fallback; it can match clean execution cost, while GCS contributes synthesized guard-dependency sharing and formal coverage boundaries. | Strong behavior-tree synthesis could narrow this distinction. |
| The mechanism is not general belief-space TAMP. | Scope claim. | GCS uses deterministic guard assignments and optional expected-cost policies; it does not optimize a POMDP. | Belief-space planning remains the right baseline for general partial observability. |

## Unsupported Claims That Must Not Be Made

- Real-robot transfer.
- Safety certification.
- Superiority over production TAMP solvers.
- Learned guard discovery from raw perception.
- General POMDP optimality.
- Complete coverage of all possible physical failures.
- Universal superiority of eager testing over replanning.

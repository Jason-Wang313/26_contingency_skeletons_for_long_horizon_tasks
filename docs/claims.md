# Claims

| Claim | Status | Support | Caveat |
|---|---|---|---|
| GCS is complete for a finite set of candidate skeletons in guard-deterministic domains with sound, exhaustive guards. | Formal claim with proof sketch in the paper. | Each guard assignment dispatches to a skeleton whose physical certificates cover that assignment. | Does not imply completeness for arbitrary TAMP domains or missing candidates. |
| GCS can be exponentially smaller than an unshared full contingency tree when actions depend on sparse/reused guard variables. | Formal representation-size proposition plus synthetic measurement. | A tree repeats suffixes for guard assignments; a DAG shares guard-equivalent suffixes. | Worst case can still be exponential if every suffix is guard-unique. |
| Early physical guards reduce failed irreversible actions compared with linear skeleton execution and replan-on-failure in the synthetic domain. | Empirical claim. | `experiments/run_guarded_skeletons.py` produces cost/failure tables. | Synthetic only; no real robot validation. |
| GCS depends on cheap and reliable guard tests. | Supported as a v2 limitation. | Probe-cost stress: cost 6.00 makes GCS 14.79 worse than replan. Guard-error stress: 100% flipped guards make noisy GCS 4.66 worse than replan. | Needs calibrated, safe-to-test guards or fallback to replanning/belief handling. |
| The mechanism is not just behavior trees. | Argumentative claim. | BTs provide execution syntax; GCS synthesizes branch placement from physical guard dependencies and skeleton dominance. | A strong BT synthesis paper could narrow this boundary. |
| The mechanism is not just belief-space TAMP. | Argumentative claim. | GCS requires guard coverage, not calibrated probabilities; probabilities are optional for expected cost. | Does not solve general partial observability. |

## Unsupported Claims That Must Not Be Made
- Real-robot transfer.
- Superiority over production TAMP solvers.
- Learned guard discovery from raw perception.
- General POMDP optimality.
- Complete coverage of all possible physical failures.

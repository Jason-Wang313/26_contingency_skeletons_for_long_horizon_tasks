# Final Audit

1. **Chosen thesis.** Long-horizon TAMP should sometimes plan over a compact family of physically conditioned skeletons rather than commit to one linear skeleton and repair after failure. Guarded Contingency Skeletons (GCS) compile candidate task-motion skeletons into a decision DAG whose branch nodes are measurable physical guard predicates.

2. **Field assumption broken.** The broken assumption is that geometric/sampling failure can be handled late by more sampling, optimization, behavior-tree fallback, or replanning. That assumption is false when the physical branch condition is cheap to test but expensive or irreversible to discover by failed execution.

3. **New central mechanism.** The central mechanism is a guard-indexed skeleton DAG: physical guard tests are placed before the first action certificate that depends on them, and guard-equivalent prefixes/suffixes are shared. This changes the planning artifact itself, not just the planner wrapped around it.

4. **Genuine novelty.** Prior TAMP covers symbolic-geometric integration, streams, samplers, and hybrid optimization; contingent planning covers symbolic conditional policies; behavior trees cover reactive fallback syntax; belief-space planning covers probabilistic information state. The narrower novelty here is lifting continuous physical feasibility dependencies into compact skeleton-level branch guards with shared task-motion fragments.

5. **Closest hostile prior work.** Closest hostile papers include FFRob, PDDLStream, integrated TAMP in belief space, logic-geometric programming, contingent planning via heuristic forward search, conformant planning via symbolic model checking, and behavior trees in robotics. The hostile set is documented in `docs/hostile_prior_work.md`.

6. **Literature coverage.** `docs/related_work_matrix.csv` contains 5147 data rows. The serious skim cut has 300 rows, the deep-read cut has 225 rows, and the hostile set has 100 rows. Some later OpenAlex queries hit HTTP 429 after enough rows were collected; this is recorded in `docs/literature_sweep_status.md`.

7. **Proof/formal-claim status.** The paper proves two conditional propositions: finite-candidate coverage for guard-deterministic domains with sound/exhaustive guards, and an exponential representation-size separation from unshared contingency trees when local guard dependence is sparse. It does not prove complete candidate generation, real-robot safety, noisy-guard correctness, or POMDP optimality.

8. **Strongest evidence.** The runnable synthetic embodied abstraction shows that at horizon 64 and reuse bias 0.55, GCS has expected cost 65.26 versus 143.81 for replan-on-failure, with 273 representation nodes versus 3,820,748 for a relevant unshared contingency tree.

9. **Biggest weaknesses.** Guards are assumed known, binary, deterministic, and safe to test. The experiment is synthetic. The method is a representation/compilation mechanism rather than a full TAMP solver. Real robot execution, learned guard discovery, and integration with production TAMP systems remain unsupported.

10. **Paper-readiness judgment.** Workshop or revise. The idea is coherent and runnable, but the evidence is too synthetic for a strong main-conference robotics claim without real domains or integration with a mature TAMP backend.

11. **Exact Downloads PDF path.** `C:/Users/wangz/Downloads/26.pdf`

12. **GitHub URL.** `https://github.com/Jason-Wang313/26_contingency_skeletons_for_long_horizon_tasks`

13. **Visible Desktop PDF status.** pending orchestrator copy

## Orchestrator Desktop Copy

Checked: 2026-06-11 20:28:45 +01:00
Downloads PDF: C:/Users/wangz/Downloads/26.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_26_20260611_202842.log

# Final Audit

1. **Chosen thesis.** Long-horizon TAMP should sometimes plan over a compact family of physically conditioned skeletons rather than commit to one linear skeleton and repair after failure. Guarded Contingency Skeletons (GCS) compile candidate task-motion skeletons into a decision DAG whose branch nodes are measurable physical guard predicates.

2. **Field assumption broken.** The broken assumption is that geometric/sampling failure can always be handled late by more sampling, optimization, behavior-tree fallback, or replanning. That assumption is false when the physical branch condition is cheap to test but expensive or irreversible to discover by failed execution.

3. **New central mechanism.** The central mechanism is a guard-indexed skeleton DAG: physical guard tests are placed before the first action certificate that depends on them, and guard-equivalent prefixes/suffixes are shared. This changes the planning artifact itself, not just the planner wrapped around it.

4. **Genuine novelty.** Prior TAMP covers symbolic-geometric integration, streams, samplers, and hybrid optimization; contingent planning covers symbolic conditional policies; behavior trees cover reactive fallback syntax; belief-space planning covers probabilistic information state. The narrower novelty here is lifting continuous physical feasibility dependencies into compact skeleton-level branch guards with shared task-motion fragments.

5. **Closest hostile prior work.** Closest hostile papers include FFRob, PDDLStream, integrated TAMP in belief space, logic-geometric programming, contingent planning via heuristic forward search, conformant planning via symbolic model checking, and behavior trees in robotics. The hostile set is documented in `docs/hostile_prior_work.md`.

6. **Literature coverage.** `docs/related_work_matrix.csv` contains 5147 data rows. The serious skim cut has 300 rows, the deep-read cut has 225 rows, and the hostile set has 100 rows. Some OpenAlex queries hit HTTP 429 after enough rows were collected; this is recorded in `docs/literature_sweep_status.md`.

7. **Proof/formal-claim status.** The paper proves two conditional propositions: finite-candidate coverage for guard-deterministic domains with sound/exhaustive guards, and an exponential representation-size separation from unshared contingency trees when local guard dependence is sparse. It does not prove complete candidate generation, real-robot safety, noisy-guard correctness, or POMDP optimality.

8. **Strongest evidence.** The v3 suite contains 79,305 method-condition rows over 10,135 deterministic cases. In Family A, eager GCS costs 58.45 versus 92.51 for replan-on-failure and 312.54 for linear default. Eager GCS averages 293,649 representation nodes versus 79.10 billion for no-sharing GCS.

9. **Boundary evidence.** At probe cost 6.0, eager GCS costs 157.60 and is 48.53 worse than replan. At 100% guard error, eager GCS costs 149.26 and is 35.34 worse than replan. Missing relevant guards produce many failures, so the formal coverage claim is inactive even when synthetic cost remains below replan.

10. **Biggest weaknesses.** Guards are assumed known, binary, cheap, calibrated, deterministic, and safe to test. The experiment is synthetic. The method is a representation/compilation mechanism rather than a full TAMP solver. Real robot execution, learned guard discovery, noisy-guard handling, and integration with production TAMP systems remain unsupported.

11. **Paper-readiness judgment.** Final under the current batch standard as a scoped synthetic mechanism paper. It is not a hardware-ready robotics systems paper.

12. **Exact Downloads PDF path.** `C:/Users/wangz/Downloads/26.pdf`

13. **Downloads PDF verification.** 25 pages, 371778 bytes, SHA256 `A36A75140750716A0D4E61DD4D59A7251AF27F6780FC0DDC5FA522AF61D8AAB9`.

14. **Visible Desktop PDF status.** absent (expected; canonical PDF stays in Downloads).

15. **Local repository PDF status.** `paper/main.pdf` absent after canonical copy.

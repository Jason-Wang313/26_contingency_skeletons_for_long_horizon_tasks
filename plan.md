# Paper 26 Execution Plan

## Objective
Produce a complete, runnable, anonymous ICLR-style robotics paper package for paper 26, ending with a compiled PDF at `C:/Users/wangz/Downloads/26.pdf`, a pushed public GitHub repository named `26_contingency_skeletons_for_long_horizon_tasks`, and a final audit.

## Safety And Recovery
- Treat all commands as fallible; prefer scripts for nontrivial parsing, scraping, experiments, plotting, and builds.
- Keep `child_status.md` compact and current after each stage, rewriting it from current facts when convenient.
- Reuse existing artifacts if present; do not delete caches unless they are unusable.
- Use explicit long timeouts for literature retrieval, experiments, and LaTeX builds.
- If optional network, bibliography, LaTeX, or GitHub operations fail, document the exact failure and continue to the strongest recoverable artifact.

## Stages
1. Initialize status and inspect the existing folder, tools, and git state safely.
2. Build literature tooling:
   - Query broad robotics, task-and-motion planning, contingency planning, behavior trees, HTN, PDDLStream, rearrangement, manipulation, and long-horizon planning literature.
   - Save at least 1000 rows to `docs/related_work_matrix.csv`.
   - Rank papers for a 300-paper serious skim, 200-250-paper deep read, and 100-paper hostile prior-work set.
3. Analyze novelty:
   - Extract mechanisms, assumptions, fixed variables, ignored failure modes, novelty pressure, and open gaps for important papers.
   - Write `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, and `docs/reviewer_attacks.md`.
4. Choose the strongest paper direction only after the sweep:
   - Define the field box.
   - Identify at least 20 falseable hidden assumptions.
   - Reject weak directions unless a genuinely new mechanism is present.
5. Implement runnable evidence:
   - Create a small reproducible task-and-motion planning simulation and algorithms that test the chosen mechanism.
   - Generate tables/figures into `results/` and paper-ready assets into `paper/figures/`.
6. Write the paper:
   - Obtain or recreate the latest official ICLR LaTeX template available at runtime.
   - Build an anonymous complete manuscript, BibTeX file, and reproducibility instructions.
   - Compile with direct `pdflatex`/`bibtex` passes and copy only the final PDF to `C:/Users/wangz/Downloads/26.pdf`.
7. Repository and audit:
   - Ensure the repo is runnable with clear commands.
   - Create/push public GitHub repo `26_contingency_skeletons_for_long_horizon_tasks` if credentials allow; otherwise document the blocker.
   - Write `docs/final_audit.md` with all required fields, including PDF path, GitHub URL or failure, and desktop-copy status.

## Done Criteria
- Required docs exist.
- Literature matrix has at least 1000 entries.
- Evidence code runs and outputs reproducible artifacts.
- Paper source and final PDF exist, or build failure is fully documented.
- GitHub push completed or failure documented.
- `docs/final_audit.md` exists and honestly characterizes readiness.

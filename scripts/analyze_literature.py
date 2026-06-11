#!/usr/bin/env python
"""Write novelty and prior-work analysis documents from the literature matrix."""

from __future__ import annotations

import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATRIX = DOCS / "related_work_matrix.csv"


ASSUMPTIONS = [
    ("Linear skeleton sufficiency", "A single task skeleton is enough until execution failure.", "Represent a set of branch-sharing skeletons before commitment."),
    ("Symbolic branch variables", "Contingencies can be named as discrete planner observations.", "Lift continuous clearance, friction, reachability, and contact tests into guard predicates."),
    ("Late failure is acceptable", "Discovering infeasibility by failed execution is a tolerable repair signal.", "Move branch tests before irreversible or high-penalty actions."),
    ("Sampler retry as repair", "More continuous samples will eventually repair the same high-level sequence.", "Let physical guards change the high-level sequence itself."),
    ("Mode sequence commitment", "The contact/mode sequence can be chosen before sensing the relevant regime.", "Delay only the choices whose feasibility depends on guard outcomes."),
    ("Cheap replanning", "Online replanning cost is negligible relative to execution.", "Compile a contingency object offline and execute by guard dispatch."),
    ("Stationary predicates", "Predicates mean the same thing across the whole horizon.", "Attach guards to physical tests at the action boundary where their truth is certified."),
    ("Manual fallbacks", "A designer can specify behavior-tree fallback order correctly.", "Synthesize fallback/branch order from candidate skeleton dominance."),
    ("Full belief necessity", "Uncertain physical tasks require a calibrated belief-space policy.", "Handle deterministic latent regimes with coverage guards instead of probabilities."),
    ("Independent failures", "Action failures can be treated as local exceptions.", "Model shared hidden guard causes that affect many later actions."),
    ("Fixed object affordances", "Object-action affordances are fixed during planning.", "Branch skeletons on measured affordance regimes."),
    ("Known contact regime", "Contact-rich actions expose no strategic branch point before contact.", "Probe guard conditions such as slip or clearance before committing to a contact sequence."),
    ("Geometry-only feasibility", "A geometric path certificate is enough for plan success.", "Track which physical condition made each certificate valid."),
    ("No irreversible side effects", "Trying an action and failing leaves the world unchanged.", "Separate reversible probe actions from irreversible task actions."),
    ("Complete observation alphabet", "The planner already contains all observations it may need.", "Derive observation tests from violated continuous preconditions."),
    ("Unshared contingency", "A conditional policy must enumerate complete future assignments.", "Use a skeleton DAG that shares suffixes across guard-equivalent branches."),
    ("Horizon-independent branching", "Branch count is independent of task length or can be hidden inside a planner.", "Measure representation growth with horizon and relevant guard count."),
    ("Benchmark abstraction fidelity", "Simulation predicates capture the same failures as physical execution.", "Make the paper's claims only for guard-deterministic abstractions and synthetic evidence."),
    ("Recovery locality", "A failed action can be repaired without changing earlier choices.", "Plan branch points at the earliest certificate boundary."),
    ("Planner owns all costs", "Cost lives in the symbolic/continuous planner objective only.", "Expose probe, failed-action, and irreversible penalties as separate planning costs."),
    ("No branch dominance", "Alternative skeletons must be searched independently.", "Prune alternatives whose guard regions and suffixes are dominated."),
    ("Outcome probabilities known", "Branch probabilities are required to plan contingencies.", "Guarantee coverage without assuming calibrated probabilities, then optionally score costs."),
]

CANDIDATES = [
    {
        "name": "Runtime TAMP repair tree",
        "breaks": "Late failure is acceptable.",
        "why_rejected": "Too close to execution monitoring and behavior-tree fallback; central mechanism remains repair after failure.",
    },
    {
        "name": "Belief-space TAMP with branch penalties",
        "breaks": "Full belief necessity.",
        "why_rejected": "Would mainly add uncertainty/cost shaping, which prior POMDP and belief-space TAMP already cover.",
    },
    {
        "name": "LLM-generated contingency plans",
        "breaks": "Manual fallbacks.",
        "why_rejected": "Falls into the forbidden weak move: using an LLM as planner without a new physical mechanism.",
    },
    {
        "name": "Guarded Contingency Skeletons",
        "breaks": "Linear skeleton sufficiency and symbolic branch-variable assumptions.",
        "why_rejected": "",
    },
]


def read_rows() -> list[dict[str, str]]:
    if not MATRIX.exists():
        return []
    with MATRIX.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def first_author(authors: str) -> str:
    if not authors:
        return "Unknown"
    return authors.split(";")[0].strip() or "Unknown"


def citeish(row: dict[str, str]) -> str:
    year = row.get("year") or "n.d."
    return f"{first_author(row.get('authors', ''))} et al., {year}, \"{row.get('title', '').strip()}\""


def top_by_cluster(rows: list[dict[str, str]], limit: int = 6) -> dict[str, list[dict[str, str]]]:
    clusters: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        clusters[row.get("cluster", "unknown")].append(row)
    return {cluster: vals[:limit] for cluster, vals in sorted(clusters.items())}


def write_literature_map(rows: list[dict[str, str]]) -> None:
    clusters = Counter(row.get("cluster", "unknown") for row in rows)
    years = [int(row["year"]) for row in rows if row.get("year", "").isdigit()]
    median_year = statistics.median(years) if years else "unknown"
    lines = [
        "# Literature Map",
        "",
        "## Field Box",
        "Task-and-motion planning for embodied robots, especially long-horizon manipulation and mobile manipulation where symbolic task choices, geometric feasibility, execution monitoring, and physical failure recovery interact.",
        "",
        "## Sweep Protocol",
        f"- Landscape sweep: {len(rows)} papers in `related_work_matrix.csv`.",
        f"- Serious skim: top 300 ranked papers in `serious_skim_300.csv`.",
        f"- Deep read: top 225 ranked papers in `deep_read_225.csv`.",
        f"- Hostile prior-work set: top 100 ranked papers in `hostile_prior_work_100.csv`.",
        f"- Median publication year among matrix rows: {median_year}.",
        "",
        "## Cluster Counts",
    ]
    for cluster, count in clusters.most_common():
        lines.append(f"- {cluster}: {count}")
    lines += ["", "## Representative Prior Work By Cluster"]
    for cluster, papers in top_by_cluster(rows[:300]).items():
        lines += ["", f"### {cluster}"]
        for row in papers:
            lines.append(f"- {citeish(row)}. Mechanism: {row.get('actual_mechanism_introduced','')}")
    lines += [
        "",
        "## Hidden Assumptions That May Be False",
    ]
    for idx, (name, assumption, direction) in enumerate(ASSUMPTIONS, 1):
        lines.append(f"{idx}. **{name}.** Assumption: {assumption} Paper direction: {direction}")
    lines += [
        "",
        "## Candidate Directions Considered",
    ]
    for candidate in CANDIDATES:
        verdict = "chosen" if candidate["name"] == "Guarded Contingency Skeletons" else f"rejected: {candidate['why_rejected']}"
        lines.append(f"- **{candidate['name']}** breaks `{candidate['breaks']}`; verdict: {verdict}")
    lines += [
        "",
        "## Chosen Direction",
        "Guarded Contingency Skeletons (GCS): compile many candidate task-motion skeletons into a decision DAG whose branch nodes are measurable physical guard predicates. The central object is not a bigger planner, learned verifier, or belief policy; it is a skeleton-level representation that delays exactly those high-level commitments whose continuous feasibility certificates depend on guard outcomes, while sharing prefixes and suffixes across guard-equivalent branches.",
    ]
    (DOCS / "literature_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_hostile(rows: list[dict[str, str]]) -> None:
    lines = [
        "# Hostile Prior Work Set",
        "",
        "This set is intentionally adversarial: each entry states what the paper makes less novel and which gap remains for guarded contingency skeletons.",
    ]
    for row in rows[:100]:
        lines += [
            "",
            f"## {row.get('hostile_rank') or row.get('rank')}. {row.get('title')}",
            f"- Citation handle: {citeish(row)}",
            f"- Problem claimed: {row.get('problem_claimed')}",
            f"- Actual mechanism introduced: {row.get('actual_mechanism_introduced')}",
            f"- Hidden assumptions: {row.get('hidden_assumptions')}",
            f"- Variables treated as fixed: {row.get('variables_treated_as_fixed')}",
            f"- Failure modes ignored: {row.get('failure_modes_ignored')}",
            f"- What it makes less novel: {row.get('what_it_makes_less_novel')}",
            f"- What it leaves open: {row.get('what_it_leaves_open')}",
        ]
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_novelty_boundary(rows: list[dict[str, str]]) -> None:
    lines = [
        "# Novelty Boundary Map",
        "",
        "| Boundary | Prior work already covers | This paper may claim | Must not claim |",
        "|---|---|---|---|",
        "| Sampling-based TAMP | Symbolic search over action skeletons coupled to continuous samplers, optimistic streams, and geometric certificates. | A branch-sharing skeleton DAG whose branch nodes are physical guards extracted from feasibility dependencies. | A generally better TAMP solver or sampler. |",
        "| Contingent planning | Conditional plans over discrete symbolic observations or nondeterministic effects. | Guard predicates grounded in continuous robot tests and attached to task-motion skeleton choices. | First conditional planning method. |",
        "| Behavior trees | Reactive sequence/fallback/condition execution patterns. | Automatic compilation of fallback structure from candidate skeleton guard regions and dominance. | First runtime fallback or first condition tree. |",
        "| Belief-space planning | Probabilistic policies, information gathering, and chance-aware planning. | Non-probabilistic coverage for deterministic latent physical regimes; probabilities only evaluate expected cost. | Solving general POMDP-TAMP. |",
        "| Robust/replanning systems | Replan after failure and repair local infeasibility. | Move selected branch tests before high-penalty/irreversible actions. | Eliminating all execution failures. |",
        "| Long-horizon manipulation benchmarks | Hard domains with many objects and interactions. | Evidence that guard sparsity changes representation size and failure cost in a controlled embodied abstraction. | Real-robot readiness or benchmark superiority. |",
        "",
        "## Strongest Novel Claim Boundary",
        "The defensible novelty is representation-level: GCS treats continuous physical feasibility conditions as first-class branch guards in a compact skeleton DAG. This is narrower than a new universal TAMP algorithm but stronger than a planner wrapper because the compiled object changes where commitment lives in the plan.",
        "",
        "## Closest Hostile Rows From The Matrix",
    ]
    for row in rows[:15]:
        lines.append(f"- {citeish(row)} [{row.get('cluster')}]: {row.get('what_it_makes_less_novel')}; open: {row.get('what_it_leaves_open')}")
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_decision() -> None:
    lines = [
        "# Novelty Decision",
        "",
        "## Decision",
        "Proceed with **Guarded Contingency Skeletons for Long-Horizon Robot Tasks**.",
        "",
        "## Thesis",
        "Long-horizon task-and-motion planners often commit to a linear skeleton before the physical branch conditions that determine feasibility are measured. A guarded contingency skeleton instead compiles candidate skeletons into a compact decision DAG with branch nodes tied to measurable physical guards, allowing the robot to test cheap/reversible conditions before irreversible or high-penalty actions while sharing the rest of the plan.",
        "",
        "## Why This Is Stronger Than The Seed",
        "The seed suggested contingency skeletons with physical branching conditions. The literature sweep sharpened that into a representation mechanism: guard extraction, earliest-safe guard placement, and suffix/prefix sharing across guard-equivalent skeletons. The paper is not about adding uncertainty, a verifier, an LLM planner, or a benchmark; it is about moving the central planning object from one skeleton to a guard-indexed skeleton DAG.",
        "",
        "## Rejected Directions",
    ]
    for candidate in CANDIDATES:
        if candidate["name"] != "Guarded Contingency Skeletons":
            lines.append(f"- {candidate['name']}: {candidate['why_rejected']}")
    lines += [
        "",
        "## Required Evidence",
        "- Formalize guard-deterministic domains and skeleton DAG coverage.",
        "- Prove compactness relative to unshared contingency trees under sparse guard dependence.",
        "- Run a synthetic embodied TAMP abstraction showing when broken assumptions matter: failed execution and representation blow-up grow with horizon if branch conditions are not represented early.",
    ]
    (DOCS / "novelty_decision.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_claims() -> None:
    lines = [
        "# Claims",
        "",
        "| Claim | Status | Support | Caveat |",
        "|---|---|---|---|",
        "| GCS is complete for a finite set of candidate skeletons in guard-deterministic domains with sound, exhaustive guards. | Formal claim with proof sketch in the paper. | Each guard assignment dispatches to a skeleton whose physical certificates cover that assignment. | Does not imply completeness for arbitrary TAMP domains or missing candidates. |",
        "| GCS can be exponentially smaller than an unshared full contingency tree when actions depend on sparse/reused guard variables. | Formal representation-size proposition plus synthetic measurement. | A tree repeats suffixes for guard assignments; a DAG shares guard-equivalent suffixes. | Worst case can still be exponential if every suffix is guard-unique. |",
        "| Early physical guards reduce failed irreversible actions compared with linear skeleton execution and replan-on-failure in the synthetic domain. | Empirical claim. | `experiments/run_guarded_skeletons.py` produces cost/failure tables. | Synthetic only; no real robot validation. |",
        "| The mechanism is not just behavior trees. | Argumentative claim. | BTs provide execution syntax; GCS synthesizes branch placement from physical guard dependencies and skeleton dominance. | A strong BT synthesis paper could narrow this boundary. |",
        "| The mechanism is not just belief-space TAMP. | Argumentative claim. | GCS requires guard coverage, not calibrated probabilities; probabilities are optional for expected cost. | Does not solve general partial observability. |",
        "",
        "## Unsupported Claims That Must Not Be Made",
        "- Real-robot transfer.",
        "- Superiority over production TAMP solvers.",
        "- Learned guard discovery from raw perception.",
        "- General POMDP optimality.",
        "- Complete coverage of all possible physical failures.",
    ]
    (DOCS / "claims.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_attacks() -> None:
    attacks = [
        ("Is this just contingent planning?", "No for the claimed boundary: contingent planning supplies symbolic observation policy machinery; GCS contributes physical guard lifting and skeleton sharing for TAMP alternatives. The paper must cite contingent planning as prior art and avoid first-policy language."),
        ("Is this just a behavior tree?", "Behavior trees are an execution representation. GCS is a compilation target with guard placement and dominance derived from candidate skeleton feasibility dependencies."),
        ("Where do guards come from?", "In this paper they are assumed or extracted from synthetic feasibility dependencies. This is a weakness; learned/raw-perception guard discovery is future work."),
        ("Why no real robot?", "The paper is workshop/revise strength: it demonstrates a mechanism and failure mode synthetically, not deployment readiness."),
        ("Does the DAG become exponential?", "Yes in worst case. The claim is conditional compactness under sparse or reused guard dependence, and experiments sweep regimes where this assumption varies."),
        ("Could replanning solve it?", "Only when failed attempts are cheap/reversible. The experiment explicitly varies irreversible failure penalties and shows the break-even condition."),
        ("Could PDDLStream encode guards as predicates?", "It could encode them if the designer already supplied symbolic tests. The novelty claim is the skeleton-level compilation and branch sharing, not representability in a language."),
        ("Are probabilities ignored?", "Coverage does not require probabilities; expected-cost evaluation can use them. The paper should not claim risk optimality."),
        ("Is the literature sweep shallow?", "The matrix is broad and metadata-driven; the hostile set extracts assumptions consistently but is not equivalent to reading 100 full PDFs. The audit must state this."),
        ("Does the proof prove planning completeness?", "No. It proves dispatch coverage for candidate skeletons under explicit guard assumptions."),
        ("Is this only a new name?", "The runnable artifact must show concrete data structures, dispatch, dominance/sharing, and baselines."),
        ("Can physical guards be tested safely?", "Only if the guard is cheap/reversible by domain design. The assumption is central and false in some domains."),
    ]
    lines = ["# Reviewer Attacks", ""]
    for idx, (attack, response) in enumerate(attacks, 1):
        lines += [f"## Attack {idx}: {attack}", response, ""]
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    rows = read_rows()
    write_literature_map(rows)
    write_hostile(rows)
    write_novelty_boundary(rows)
    write_decision()
    write_claims()
    write_attacks()
    print(f"Analyzed {len(rows)} literature rows into docs/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

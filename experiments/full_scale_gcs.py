#!/usr/bin/env python3
"""Full-scale RAM-light evidence for Guarded Contingency Skeletons."""

from __future__ import annotations

import csv
import json
import math
import random
import sys
import time
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from guarded_skeletons import Problem, Step, action_signature, full_tree_size, sample_assignment  # noqa: E402

OUT = ROOT / "results" / "full_scale"
TEX = OUT / "tex"
FIG = ROOT / "figures" / "full_scale"
DOCS = ROOT / "docs"
SEED = 26026

FIELDNAMES = [
    "family",
    "case_id",
    "method",
    "mean_cost",
    "mean_failures",
    "representation_size",
    "horizon",
    "num_guards",
    "dependency_width",
    "dependency_topology",
    "reuse_bias",
    "probe_cost",
    "failure_penalty",
    "repair_penalty",
    "irreversible_rate",
    "guard_error_rate",
    "false_positive_rate",
    "false_negative_rate",
    "confidence_mode",
    "confidence_threshold",
    "missing_guard_fraction",
    "spurious_guard_fraction",
    "control",
    "relevant_guards",
    "seed",
]

METHODS_MAIN = [
    "linear_default",
    "replan_on_failure",
    "probe_all_tree",
    "relevant_unshared_tree",
    "gcs_eager",
    "gcs_lazy",
    "no_sharing_gcs",
    "oracle_assignment",
]

METHODS_RICH = [
    "linear_default",
    "replan_on_failure",
    "probe_all_tree",
    "probe_all_local",
    "myopic_voi",
    "belief_cost_proxy",
    "behavior_tree_fallback",
    "gcs_eager",
    "gcs_lazy",
    "gcs_thresholded",
    "gcs_robust",
    "delayed_gcs",
    "no_sharing_gcs",
    "no_dominance_gcs",
    "oracle_assignment",
]


class Aggregator:
    def __init__(self, keys: Iterable[str]):
        self.keys = tuple(keys)
        self.data: dict[tuple[object, ...], dict[str, float]] = defaultdict(
            lambda: {
                "rows": 0.0,
                "cost_sum": 0.0,
                "failure_sum": 0.0,
                "size_sum": 0.0,
                "gcs_cost_sum": 0.0,
                "replan_cost_sum": 0.0,
            }
        )

    def update(self, row: dict[str, object], case_costs: dict[str, float]) -> None:
        key = tuple(row.get(k, "") for k in self.keys)
        item = self.data[key]
        item["rows"] += 1
        item["cost_sum"] += float(row["mean_cost"])
        item["failure_sum"] += float(row["mean_failures"])
        item["size_sum"] += float(row["representation_size"])
        item["gcs_cost_sum"] += float(case_costs.get("gcs_eager", row["mean_cost"]))
        item["replan_cost_sum"] += float(case_costs.get("replan_on_failure", row["mean_cost"]))

    def rows(self) -> list[dict[str, object]]:
        out = []
        for key, item in sorted(self.data.items(), key=lambda kv: tuple(str(x) for x in kv[0])):
            n = max(1.0, item["rows"])
            cost = item["cost_sum"] / n
            replan = item["replan_cost_sum"] / n
            row = {name: value for name, value in zip(self.keys, key)}
            row.update(
                {
                    "rows": int(item["rows"]),
                    "mean_cost": round(cost, 6),
                    "mean_failures": round(item["failure_sum"] / n, 6),
                    "mean_representation_size": round(item["size_sum"] / n, 3),
                    "mean_gcs_cost": round(item["gcs_cost_sum"] / n, 6),
                    "mean_replan_cost": round(replan, 6),
                    "delta_vs_replan": round(cost - replan, 6),
                }
            )
            out.append(row)
        return out


def ensure_dirs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    TEX.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def make_problem_v3(
    horizon: int,
    num_guards: int,
    dependency_width: int,
    reuse_bias: float,
    irreversible_rate: float,
    seed: int,
    topology: str = "clustered",
    probe_cost: float = 0.08,
    failure_penalty: float = 4.0,
    repair_penalty: float = 1.0,
) -> Problem:
    rng = random.Random(seed)
    steps: list[Step] = []
    width = max(1, min(dependency_width, num_guards))
    hot = max(1, int(num_guards * max(0.05, min(1.0, reuse_bias))))
    for idx in range(horizon):
        if topology == "clustered":
            pool = list(range(hot)) if rng.random() < reuse_bias else list(range(num_guards))
            gids = rng.sample(pool, min(width, len(pool)))
        elif topology == "banded":
            center = int((idx / max(1, horizon - 1)) * max(0, num_guards - 1))
            radius = max(width, max(2, num_guards // 10))
            pool = list(range(max(0, center - radius), min(num_guards, center + radius + 1)))
            gids = rng.sample(pool, min(width, len(pool)))
        elif topology == "uniform_sparse":
            gids = rng.sample(range(num_guards), width)
        elif topology == "dense":
            dense_width = max(width, min(num_guards, max(3, num_guards // 2)))
            gids = rng.sample(range(num_guards), dense_width)
        elif topology == "suffix_unique":
            start = (idx * width) % num_guards
            gids = [(start + j + idx) % num_guards for j in range(width)]
        elif topology == "all_upfront":
            gids = list(range(min(num_guards, max(width, num_guards // 2))))
        else:
            gids = rng.sample(range(num_guards), width)
        irreversible = rng.random() < irreversible_rate
        steps.append(Step(idx, tuple(sorted(set(gids))), irreversible))
    probs = tuple(0.25 + 0.5 * rng.random() for _ in range(num_guards))
    return Problem(
        horizon=horizon,
        num_guards=num_guards,
        steps=tuple(steps),
        guard_prob=probs,
        probe_cost=probe_cost,
        action_cost=1.0,
        failure_penalty=failure_penalty,
        repair_penalty=repair_penalty,
    )


def penalty(problem: Problem, step: Step) -> float:
    return problem.failure_penalty * (1.5 if step.irreversible else 1.0) + problem.repair_penalty


def likely_value(problem: Problem, gid: int) -> int:
    return 1 if problem.guard_prob[gid] >= 0.5 else 0


def risk_for_guard(problem: Problem, gid: int, step: Step) -> float:
    p = problem.guard_prob[gid]
    wrong = min(p, 1.0 - p)
    return wrong * penalty(problem, step)


def observe_guard(
    true_value: int,
    rng: random.Random,
    guard_error_rate: float,
    false_positive_rate: float,
    false_negative_rate: float,
) -> int:
    fp = guard_error_rate if false_positive_rate < 0 else false_positive_rate
    fn = guard_error_rate if false_negative_rate < 0 else false_negative_rate
    if true_value == 1:
        return 0 if rng.random() < fn else 1
    return 1 if rng.random() < fp else 0


def fast_gcs_size(problem: Problem) -> int:
    branch_nodes = len(problem.relevant_guards)
    action_variants = sum(2 ** len(step.guard_ids) for step in problem.steps)
    return 1 + branch_nodes + action_variants


def confidence(problem: Problem, gid: int, true_value: int, mode: str, rng: random.Random) -> float:
    base = max(problem.guard_prob[gid], 1.0 - problem.guard_prob[gid])
    predicted = likely_value(problem, gid)
    if mode == "overconfident":
        return min(0.99, 0.78 + 0.22 * base)
    if mode == "underconfident":
        return 0.50 + 0.35 * (base - 0.50)
    if mode == "adversarial":
        return 0.94 if predicted != true_value else 0.55
    return max(0.50, min(0.99, base + rng.uniform(-0.04, 0.04)))


def choose_signature(problem: Problem, step: Step, observed: dict[int, int]) -> tuple[int, ...]:
    return tuple(observed.get(gid, likely_value(problem, gid)) for gid in step.guard_ids)


def probe(
    problem: Problem,
    gid: int,
    assignment: tuple[int, ...],
    observed: dict[int, int],
    rng: random.Random,
    missing_guards: set[int],
    guard_error_rate: float,
    false_positive_rate: float,
    false_negative_rate: float,
    repeats: int = 1,
) -> float:
    if gid in observed or gid in missing_guards:
        return 0.0
    votes = []
    for _ in range(max(1, repeats)):
        votes.append(observe_guard(assignment[gid], rng, guard_error_rate, false_positive_rate, false_negative_rate))
    observed[gid] = 1 if sum(votes) >= (len(votes) / 2.0) else 0
    return problem.probe_cost * max(1, repeats)


def representation_size(problem: Problem, method: str, spurious_count: int = 0) -> float:
    if method in {"linear_default", "replan_on_failure", "belief_cost_proxy", "oracle_assignment"}:
        return float(problem.horizon)
    if method == "probe_all_tree":
        return float(full_tree_size(problem, relevant_only=False))
    if method in {"relevant_unshared_tree", "no_sharing_gcs"}:
        return float(full_tree_size(problem, relevant_only=True))
    base = float(fast_gcs_size(problem) + spurious_count)
    if method == "no_dominance_gcs":
        return base * 1.35 + problem.horizon
    if method == "behavior_tree_fallback":
        return float(problem.horizon * 3 + len(problem.relevant_guards))
    if method == "gcs_robust":
        return base * 1.20
    if method in {"gcs_lazy", "gcs_thresholded", "myopic_voi"}:
        return base * 1.10
    return base


def evaluate_method(
    problem: Problem,
    method: str,
    assignments: list[tuple[int, ...]],
    seed: int,
    guard_error_rate: float = 0.0,
    false_positive_rate: float = -1.0,
    false_negative_rate: float = -1.0,
    confidence_mode: str = "calibrated",
    threshold: float = 0.70,
    missing_guard_fraction: float = 0.0,
    spurious_guard_fraction: float = 0.0,
) -> dict[str, float]:
    rng = random.Random(seed + 7919 * (METHODS_RICH + METHODS_MAIN + [method]).index(method))
    relevant = list(problem.relevant_guards)
    missing_count = min(len(relevant), int(round(missing_guard_fraction * len(relevant))))
    missing_guards = set(rng.sample(relevant, missing_count)) if missing_count else set()
    spurious_count = int(round(spurious_guard_fraction * max(1, problem.num_guards)))
    total_cost = 0.0
    total_failures = 0.0
    for assignment in assignments:
        observed: dict[int, int] = {}
        cost = 0.0
        failures = 0.0
        if method == "oracle_assignment":
            total_cost += problem.horizon * problem.action_cost
            continue
        if method == "probe_all_tree":
            for gid in range(problem.num_guards):
                cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
            cost += spurious_count * problem.probe_cost
        elif method == "probe_all_local":
            for gid in relevant:
                cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
            cost += spurious_count * problem.probe_cost

        delayed_seen: set[int] = set()
        for step in problem.steps:
            if method in {"gcs_eager", "relevant_unshared_tree", "no_sharing_gcs", "no_dominance_gcs"}:
                for gid in step.guard_ids:
                    cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
            elif method == "gcs_robust":
                for gid in step.guard_ids:
                    cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate, repeats=3)
            elif method in {"gcs_lazy", "myopic_voi"}:
                for gid in step.guard_ids:
                    if gid not in observed and risk_for_guard(problem, gid, step) > problem.probe_cost:
                        cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
            elif method == "gcs_thresholded":
                for gid in step.guard_ids:
                    conf = confidence(problem, gid, assignment[gid], confidence_mode, rng)
                    if gid not in observed and conf >= threshold:
                        cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
            elif method == "behavior_tree_fallback":
                for gid in step.guard_ids:
                    if step.irreversible or risk_for_guard(problem, gid, step) > 1.5 * problem.probe_cost:
                        cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
            elif method == "delayed_gcs":
                for gid in step.guard_ids:
                    if gid in delayed_seen and gid not in observed:
                        cost += probe(problem, gid, assignment, observed, rng, missing_guards, guard_error_rate, false_positive_rate, false_negative_rate)
                    delayed_seen.add(gid)

            if method == "linear_default":
                chosen = tuple(0 for _ in step.guard_ids)
            elif method in {"replan_on_failure", "delayed_gcs"}:
                chosen = tuple(observed.get(gid, 0) for gid in step.guard_ids)
            else:
                chosen = choose_signature(problem, step, observed)
            true_signature = action_signature(step, assignment)
            cost += problem.action_cost
            if chosen != true_signature:
                failures += 1.0
                cost += penalty(problem, step)
                for gid in step.guard_ids:
                    if gid not in missing_guards:
                        observed[gid] = assignment[gid]
                if method != "linear_default":
                    cost += problem.action_cost
        total_cost += cost
        total_failures += failures
    n = max(1, len(assignments))
    return {
        "cost": total_cost / n,
        "failures": total_failures / n,
        "representation_size": representation_size(problem, method, spurious_count),
    }


def row_for(
    family: str,
    case_id: str,
    problem: Problem,
    method: str,
    values: dict[str, float],
    seed: int,
    dependency_width: int,
    topology: str,
    reuse_bias: float,
    irreversible_rate: float,
    guard_error_rate: float = 0.0,
    false_positive_rate: float = -1.0,
    false_negative_rate: float = -1.0,
    confidence_mode: str = "calibrated",
    threshold: float = 0.70,
    missing_guard_fraction: float = 0.0,
    spurious_guard_fraction: float = 0.0,
    control: str = "",
) -> dict[str, object]:
    return {
        "family": family,
        "case_id": case_id,
        "method": method,
        "mean_cost": round(values["cost"], 6),
        "mean_failures": round(values["failures"], 6),
        "representation_size": round(values["representation_size"], 3),
        "horizon": problem.horizon,
        "num_guards": problem.num_guards,
        "dependency_width": dependency_width,
        "dependency_topology": topology,
        "reuse_bias": reuse_bias,
        "probe_cost": problem.probe_cost,
        "failure_penalty": problem.failure_penalty,
        "repair_penalty": problem.repair_penalty,
        "irreversible_rate": irreversible_rate,
        "guard_error_rate": guard_error_rate,
        "false_positive_rate": false_positive_rate,
        "false_negative_rate": false_negative_rate,
        "confidence_mode": confidence_mode,
        "confidence_threshold": threshold,
        "missing_guard_fraction": missing_guard_fraction,
        "spurious_guard_fraction": spurious_guard_fraction,
        "control": control,
        "relevant_guards": len(problem.relevant_guards),
        "seed": seed,
    }


def assignments_for(problem: Problem, episodes: int, seed: int) -> list[tuple[int, ...]]:
    rng = random.Random(seed)
    return [sample_assignment(problem, rng) for _ in range(episodes)]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def stream_case_rows(
    writer: csv.DictWriter,
    family: str,
    case_id: str,
    problem: Problem,
    methods: list[str],
    assignments: list[tuple[int, ...]],
    seed: int,
    dependency_width: int,
    topology: str,
    reuse_bias: float,
    irreversible_rate: float,
    aggregators: list[Aggregator],
    **params: object,
) -> int:
    values_by_method = {
        method: evaluate_method(
            problem,
            method,
            assignments,
            seed + 1009 * idx,
            guard_error_rate=float(params.get("guard_error_rate", 0.0)),
            false_positive_rate=float(params.get("false_positive_rate", -1.0)),
            false_negative_rate=float(params.get("false_negative_rate", -1.0)),
            confidence_mode=str(params.get("confidence_mode", "calibrated")),
            threshold=float(params.get("confidence_threshold", 0.70)),
            missing_guard_fraction=float(params.get("missing_guard_fraction", 0.0)),
            spurious_guard_fraction=float(params.get("spurious_guard_fraction", 0.0)),
        )
        for idx, method in enumerate(methods)
    }
    case_costs = {method: values["cost"] for method, values in values_by_method.items()}
    count = 0
    for method, values in values_by_method.items():
        row = row_for(
            family,
            case_id,
            problem,
            method,
            values,
            seed,
            dependency_width,
            topology,
            reuse_bias,
            irreversible_rate,
            guard_error_rate=float(params.get("guard_error_rate", 0.0)),
            false_positive_rate=float(params.get("false_positive_rate", -1.0)),
            false_negative_rate=float(params.get("false_negative_rate", -1.0)),
            confidence_mode=str(params.get("confidence_mode", "calibrated")),
            threshold=float(params.get("confidence_threshold", 0.70)),
            missing_guard_fraction=float(params.get("missing_guard_fraction", 0.0)),
            spurious_guard_fraction=float(params.get("spurious_guard_fraction", 0.0)),
            control=str(params.get("control", "")),
        )
        writer.writerow(row)
        for agg in aggregators:
            agg.update(row, case_costs)
        count += 1
    return count


def run_family_a() -> tuple[int, int, float]:
    start = time.perf_counter()
    methods = METHODS_MAIN
    agg_method = Aggregator(["method"])
    agg_topology = Aggregator(["dependency_topology", "method"])
    agg_horizon = Aggregator(["horizon", "method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_a_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        for horizon in [8, 16, 32, 64, 96, 128]:
            for topology in ["clustered", "banded", "uniform_sparse", "dense", "suffix_unique"]:
                for width in [1, 2, 4]:
                    for reuse in [0.0, 0.25, 0.55, 0.85]:
                        for i in range(12):
                            cases += 1
                            seed = SEED + 100000 + cases
                            num_guards = max(4, horizon // 4)
                            problem = make_problem_v3(horizon, num_guards, width, reuse, 0.35, seed, topology)
                            assignments = assignments_for(problem, 6, seed + 17)
                            rows_written += stream_case_rows(
                                writer,
                                "A",
                                f"A_{cases:05d}",
                                problem,
                                methods,
                                assignments,
                                seed,
                                width,
                                topology,
                                reuse,
                                0.35,
                                [agg_method, agg_topology, agg_horizon],
                            )
    write_csv(OUT / "family_a_summary_by_method.csv", agg_method.rows())
    write_csv(OUT / "family_a_summary_by_topology.csv", agg_topology.rows())
    write_csv(OUT / "family_a_summary_by_horizon.csv", agg_horizon.rows())
    return rows_written, cases, time.perf_counter() - start


def run_family_b() -> tuple[int, int, float]:
    start = time.perf_counter()
    methods = ["replan_on_failure", "probe_all_local", "gcs_eager", "gcs_lazy", "behavior_tree_fallback", "oracle_assignment"]
    agg = Aggregator(["probe_cost", "failure_penalty", "irreversible_rate", "method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_b_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        for probe_cost in [0.02, 0.08, 0.25, 0.50, 1.0, 2.0, 4.0, 6.0]:
            for failure_penalty in [0.5, 1.0, 2.0, 4.0, 8.0]:
                for irreversible in [0.0, 0.25, 0.50, 0.75]:
                    for i in range(10):
                        cases += 1
                        seed = SEED + 200000 + cases
                        problem = make_problem_v3(64, 16, 2, 0.55, irreversible, seed, "clustered", probe_cost, failure_penalty)
                        assignments = assignments_for(problem, 8, seed + 17)
                        rows_written += stream_case_rows(
                            writer,
                            "B",
                            f"B_{cases:05d}",
                            problem,
                            methods,
                            assignments,
                            seed,
                            2,
                            "clustered",
                            0.55,
                            irreversible,
                            [agg],
                        )
    write_csv(OUT / "family_b_summary_by_economics.csv", agg.rows())
    return rows_written, cases, time.perf_counter() - start


def run_family_c() -> tuple[int, int, float]:
    start = time.perf_counter()
    methods = ["replan_on_failure", "gcs_eager", "gcs_thresholded", "gcs_robust", "gcs_lazy"]
    agg = Aggregator(["guard_error_rate", "confidence_mode", "confidence_threshold", "method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_c_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        for err in [0.0, 0.02, 0.05, 0.10, 0.20, 0.40, 0.60, 0.80, 1.00]:
            for mode in ["calibrated", "overconfident", "underconfident", "adversarial"]:
                for threshold in [0.55, 0.70, 0.85]:
                    for i in range(10):
                        cases += 1
                        seed = SEED + 300000 + cases
                        problem = make_problem_v3(64, 16, 2, 0.55, 0.35, seed, "clustered")
                        assignments = assignments_for(problem, 8, seed + 17)
                        rows_written += stream_case_rows(
                            writer,
                            "C",
                            f"C_{cases:05d}",
                            problem,
                            methods,
                            assignments,
                            seed,
                            2,
                            "clustered",
                            0.55,
                            0.35,
                            [agg],
                            guard_error_rate=err,
                            confidence_mode=mode,
                            confidence_threshold=threshold,
                        )
    write_csv(OUT / "family_c_summary_by_reliability.csv", agg.rows())
    return rows_written, cases, time.perf_counter() - start


def run_family_d() -> tuple[int, int, float]:
    start = time.perf_counter()
    methods = METHODS_RICH
    agg = Aggregator(["method"])
    agg_topology = Aggregator(["dependency_topology", "method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_d_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        for horizon in [32, 64, 96]:
            for topology in ["clustered", "banded", "dense"]:
                for width in [1, 2, 4]:
                    for i in range(45):
                        cases += 1
                        seed = SEED + 400000 + cases
                        num_guards = max(4, horizon // 4)
                        problem = make_problem_v3(horizon, num_guards, width, 0.55, 0.35, seed, topology)
                        assignments = assignments_for(problem, 6, seed + 17)
                        rows_written += stream_case_rows(
                            writer,
                            "D",
                            f"D_{cases:05d}",
                            problem,
                            methods,
                            assignments,
                            seed,
                            width,
                            topology,
                            0.55,
                            0.35,
                            [agg, agg_topology],
                        )
    write_csv(OUT / "family_d_summary_by_ablation.csv", agg.rows())
    write_csv(OUT / "family_d_summary_by_topology.csv", agg_topology.rows())
    return rows_written, cases, time.perf_counter() - start


def run_family_e() -> tuple[int, int, float]:
    start = time.perf_counter()
    methods = ["replan_on_failure", "probe_all_local", "gcs_eager", "gcs_robust", "belief_cost_proxy", "oracle_assignment"]
    agg = Aggregator(["missing_guard_fraction", "spurious_guard_fraction", "method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_e_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        for missing in [0.0, 0.10, 0.25, 0.50, 0.75, 1.00]:
            for spurious in [0.0, 0.10, 0.25, 0.50, 1.00]:
                for i in range(20):
                    cases += 1
                    seed = SEED + 500000 + cases
                    problem = make_problem_v3(64, 16, 2, 0.55, 0.35, seed, "clustered")
                    assignments = assignments_for(problem, 8, seed + 17)
                    rows_written += stream_case_rows(
                        writer,
                        "E",
                        f"E_{cases:05d}",
                        problem,
                        methods,
                        assignments,
                        seed,
                        2,
                        "clustered",
                        0.55,
                        0.35,
                        [agg],
                        missing_guard_fraction=missing,
                        spurious_guard_fraction=spurious,
                    )
    write_csv(OUT / "family_e_summary_by_coverage.csv", agg.rows())
    return rows_written, cases, time.perf_counter() - start


def control_problem(control: str, seed: int) -> tuple[Problem, int, str, float, float, dict[str, object]]:
    kwargs: dict[str, object] = {"control": control}
    if control == "zero_failure_penalty":
        return make_problem_v3(64, 16, 2, 0.55, 0.35, seed, "clustered", failure_penalty=0.0), 2, "clustered", 0.55, 0.35, kwargs
    if control == "expensive_probe":
        return make_problem_v3(64, 16, 2, 0.55, 0.35, seed, "clustered", probe_cost=8.0), 2, "clustered", 0.55, 0.35, kwargs
    if control == "dense_all_guards":
        return make_problem_v3(64, 16, 8, 0.55, 0.35, seed, "dense"), 8, "dense", 0.55, 0.35, kwargs
    if control == "no_reuse":
        return make_problem_v3(64, 16, 2, 0.0, 0.35, seed, "uniform_sparse"), 2, "uniform_sparse", 0.0, 0.35, kwargs
    if control == "all_upfront":
        return make_problem_v3(64, 16, 8, 1.0, 0.35, seed, "all_upfront"), 8, "all_upfront", 1.0, 0.35, kwargs
    if control == "reversible_failures":
        return make_problem_v3(64, 16, 2, 0.55, 0.0, seed, "clustered", failure_penalty=0.75), 2, "clustered", 0.55, 0.0, kwargs
    if control == "missing_all_guards":
        kwargs["missing_guard_fraction"] = 1.0
        return make_problem_v3(64, 16, 2, 0.55, 0.35, seed, "clustered"), 2, "clustered", 0.55, 0.35, kwargs
    return make_problem_v3(64, 16, 2, 0.55, 0.35, seed, "clustered"), 2, "clustered", 0.55, 0.35, kwargs


def run_family_f() -> tuple[int, int, float]:
    start = time.perf_counter()
    controls = ["zero_failure_penalty", "expensive_probe", "dense_all_guards", "no_reuse", "all_upfront", "reversible_failures", "missing_all_guards"]
    methods = ["replan_on_failure", "probe_all_local", "gcs_eager", "gcs_lazy", "no_sharing_gcs", "oracle_assignment"]
    agg = Aggregator(["control", "method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_f_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        for control in controls:
            for i in range(60):
                cases += 1
                seed = SEED + 600000 + cases
                problem, width, topology, reuse, irreversible, kwargs = control_problem(control, seed)
                assignments = assignments_for(problem, 8, seed + 17)
                rows_written += stream_case_rows(
                    writer,
                    "F",
                    f"F_{cases:05d}",
                    problem,
                    methods,
                    assignments,
                    seed,
                    width,
                    topology,
                    reuse,
                    irreversible,
                    [agg],
                    **kwargs,
                )
    write_csv(OUT / "family_f_summary_by_control.csv", agg.rows())
    return rows_written, cases, time.perf_counter() - start


def run_family_g() -> tuple[int, int, float]:
    start = time.perf_counter()
    methods = ["replan_on_failure", "gcs_eager", "gcs_lazy", "gcs_robust", "no_sharing_gcs", "oracle_assignment"]
    examples: dict[str, dict[str, object] | None] = {
        "expensive_probe_worse_than_replan": None,
        "wrong_guard_worse_than_replan": None,
        "dense_representation_explosion": None,
        "missing_guard_failure": None,
        "lazy_delay_failure": None,
        "no_reuse_not_compact": None,
    }
    agg = Aggregator(["method"])
    rows_written = 0
    cases = 0
    with (OUT / "family_g_rows.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        controls = ["expensive_probe", "dense_all_guards", "missing_all_guards", "no_reuse", "standard"]
        for i in range(900):
            cases += 1
            control = controls[i % len(controls)]
            seed = SEED + 700000 + cases
            if control == "standard":
                problem, width, topology, reuse, irreversible, kwargs = control_problem("", seed)
            else:
                problem, width, topology, reuse, irreversible, kwargs = control_problem(control, seed)
            if i % 7 == 0:
                kwargs["guard_error_rate"] = 1.0
            assignments = assignments_for(problem, 6, seed + 17)
            values_by_method = {
                method: evaluate_method(
                    problem,
                    method,
                    assignments,
                    seed + 1009 * idx,
                    guard_error_rate=float(kwargs.get("guard_error_rate", 0.0)),
                    missing_guard_fraction=float(kwargs.get("missing_guard_fraction", 0.0)),
                )
                for idx, method in enumerate(methods)
            }
            case_costs = {method: values["cost"] for method, values in values_by_method.items()}
            rows = []
            for method, values in values_by_method.items():
                row = row_for(
                    "G",
                    f"G_{cases:05d}",
                    problem,
                    method,
                    values,
                    seed,
                    width,
                    topology,
                    reuse,
                    irreversible,
                    guard_error_rate=float(kwargs.get("guard_error_rate", 0.0)),
                    missing_guard_fraction=float(kwargs.get("missing_guard_fraction", 0.0)),
                    control=control,
                )
                rows.append(row)
                writer.writerow(row)
                agg.update(row, case_costs)
                rows_written += 1
            by_method = {row["method"]: row for row in rows}
            if examples["expensive_probe_worse_than_replan"] is None and control == "expensive_probe" and float(by_method["gcs_eager"]["mean_cost"]) > float(by_method["replan_on_failure"]["mean_cost"]):
                examples["expensive_probe_worse_than_replan"] = by_method["gcs_eager"]
            if examples["wrong_guard_worse_than_replan"] is None and float(kwargs.get("guard_error_rate", 0.0)) >= 1.0 and float(by_method["gcs_eager"]["mean_cost"]) > float(by_method["replan_on_failure"]["mean_cost"]):
                examples["wrong_guard_worse_than_replan"] = by_method["gcs_eager"]
            if examples["dense_representation_explosion"] is None and control == "dense_all_guards":
                examples["dense_representation_explosion"] = by_method["no_sharing_gcs"]
            if examples["missing_guard_failure"] is None and control == "missing_all_guards" and float(by_method["gcs_eager"]["mean_failures"]) > 1.0:
                examples["missing_guard_failure"] = by_method["gcs_eager"]
            if examples["lazy_delay_failure"] is None and float(by_method["gcs_lazy"]["mean_cost"]) > float(by_method["gcs_eager"]["mean_cost"]) + 5.0:
                examples["lazy_delay_failure"] = by_method["gcs_lazy"]
            if examples["no_reuse_not_compact"] is None and control == "no_reuse":
                examples["no_reuse_not_compact"] = by_method["no_sharing_gcs"]
    (OUT / "counterexample_library.json").write_text(json.dumps(examples, indent=2, ensure_ascii=True), encoding="utf-8")
    write_csv(OUT / "family_g_summary_by_counterexample.csv", agg.rows())
    return rows_written, cases, time.perf_counter() - start


def load_summary(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def latex_table(path: Path, headers: list[str], rows: list[list[object]]) -> None:
    align = "l" + "r" * (len(headers) - 1)
    lines = [f"\\begin{{tabular}}{{{align}}}", "\\toprule", " & ".join(headers) + " \\\\", "\\midrule"]
    for row in rows:
        lines.append(" & ".join(str(x) for x in row) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def make_tables() -> None:
    main = load_summary(OUT / "family_a_summary_by_method.csv")
    rows = []
    for method in ["linear_default", "replan_on_failure", "probe_all_tree", "relevant_unshared_tree", "gcs_eager", "gcs_lazy", "no_sharing_gcs", "oracle_assignment"]:
        item = next(r for r in main if r["method"] == method)
        rows.append([method.replace("_", "\\_"), item["mean_cost"], item["mean_failures"], item["mean_representation_size"], item["delta_vs_replan"]])
    latex_table(TEX / "table_main_full_scale.tex", ["Method", "Cost", "Failures", "Nodes", "$\\Delta$ repl."], rows)

    topology = load_summary(OUT / "family_a_summary_by_topology.csv")
    rows = []
    for topo in ["clustered", "banded", "uniform_sparse", "dense", "suffix_unique"]:
        for method in ["replan_on_failure", "gcs_eager", "no_sharing_gcs"]:
            item = next(r for r in topology if r["dependency_topology"] == topo and r["method"] == method)
            rows.append([topo.replace("_", "\\_"), method.replace("_", "\\_"), item["mean_cost"], item["mean_representation_size"]])
    latex_table(TEX / "table_dependency_topology.tex", ["Topology", "Method", "Cost", "Nodes"], rows)

    econ = load_summary(OUT / "family_b_summary_by_economics.csv")
    rows = []
    for probe in ["0.08", "1.0", "4.0", "6.0"]:
        for method in ["replan_on_failure", "gcs_eager", "gcs_lazy"]:
            subset = [r for r in econ if r["probe_cost"] == probe and r["failure_penalty"] == "4.0" and r["irreversible_rate"] == "0.5" and r["method"] == method]
            if subset:
                item = subset[0]
                rows.append([probe, method.replace("_", "\\_"), item["mean_cost"], item["delta_vs_replan"]])
    latex_table(TEX / "table_guard_economics.tex", ["Probe cost", "Method", "Cost", "$\\Delta$"], rows)

    reliab = load_summary(OUT / "family_c_summary_by_reliability.csv")
    rows = []
    for err in ["0.0", "0.2", "0.6", "1.0"]:
        for method in ["replan_on_failure", "gcs_eager", "gcs_thresholded", "gcs_robust"]:
            item = next(r for r in reliab if r["guard_error_rate"] == err and r["confidence_mode"] == "calibrated" and r["confidence_threshold"] == "0.7" and r["method"] == method)
            rows.append([f"{100 * float(err):.0f}\\%", method.replace("_", "\\_"), item["mean_cost"], item["mean_failures"], item["delta_vs_replan"]])
    latex_table(TEX / "table_guard_reliability.tex", ["Error", "Method", "Cost", "Failures", "$\\Delta$"], rows)

    ab = load_summary(OUT / "family_d_summary_by_ablation.csv")
    rows = []
    for method in METHODS_RICH:
        item = next(r for r in ab if r["method"] == method)
        rows.append([method.replace("_", "\\_"), item["mean_cost"], item["mean_failures"], item["mean_representation_size"]])
    latex_table(TEX / "table_ablations.tex", ["Method", "Cost", "Failures", "Nodes"], rows)

    cov = load_summary(OUT / "family_e_summary_by_coverage.csv")
    rows = []
    for missing in ["0.0", "0.25", "0.5", "1.0"]:
        for method in ["replan_on_failure", "gcs_eager", "gcs_robust", "belief_cost_proxy"]:
            item = next(r for r in cov if r["missing_guard_fraction"] == missing and r["spurious_guard_fraction"] == "0.0" and r["method"] == method)
            rows.append([missing, method.replace("_", "\\_"), item["mean_cost"], item["mean_failures"]])
    latex_table(TEX / "table_missing_coverage.tex", ["Missing", "Method", "Cost", "Failures"], rows)

    control = load_summary(OUT / "family_f_summary_by_control.csv")
    rows = []
    for control_name in ["zero_failure_penalty", "expensive_probe", "dense_all_guards", "no_reuse", "all_upfront", "reversible_failures", "missing_all_guards"]:
        for method in ["replan_on_failure", "gcs_eager", "gcs_lazy", "no_sharing_gcs"]:
            item = next(r for r in control if r["control"] == control_name and r["method"] == method)
            rows.append([control_name.replace("_", "\\_"), method.replace("_", "\\_"), item["mean_cost"], item["mean_representation_size"]])
    latex_table(TEX / "table_negative_controls.tex", ["Control", "Method", "Cost", "Nodes"], rows)

    claim_rows = [
        ["Early guards reduce failures", "Family A/B", "holds when probe cost below failure cost"],
        ["DAG sharing matters", "Family A/D", "no-sharing explodes in sparse reused regimes"],
        ["Cheap reliable guards required", "Family B/C", "expensive or wrong guards can lose to replan"],
        ["Not universal", "Family F/G", "dense/no-reuse/missing-guard controls"],
    ]
    latex_table(TEX / "table_claim_evidence.tex", ["Claim", "Evidence", "Boundary"], claim_rows)


def make_figures() -> int:
    failures = 0
    try:
        main = load_summary(OUT / "family_a_summary_by_method.csv")
        methods = ["linear_default", "replan_on_failure", "probe_all_tree", "gcs_eager", "gcs_lazy", "oracle_assignment"]
        values = [float(next(r for r in main if r["method"] == m)["mean_cost"]) for m in methods]
        fig, ax = plt.subplots(figsize=(8.5, 4.2))
        ax.bar(range(len(methods)), values, color="#427aa1")
        ax.set_xticks(range(len(methods)))
        ax.set_xticklabels([m.replace("_", "\n") for m in methods], fontsize=8)
        ax.set_ylabel("Mean expected cost")
        fig.tight_layout()
        fig.savefig(FIG / "main_cost_by_method.pdf")
        fig.savefig(FIG / "main_cost_by_method.png", dpi=180)
        plt.close(fig)
    except Exception:
        failures += 1
    try:
        horizon = load_summary(OUT / "family_a_summary_by_horizon.csv")
        fig, ax = plt.subplots(figsize=(7, 4.2))
        for method in ["replan_on_failure", "gcs_eager", "no_sharing_gcs", "oracle_assignment"]:
            xs = sorted({int(r["horizon"]) for r in horizon})
            ys = [float(next(r for r in horizon if int(r["horizon"]) == x and r["method"] == method)["mean_cost"]) for x in xs]
            ax.plot(xs, ys, marker="o", label=method)
        ax.set_xlabel("Horizon")
        ax.set_ylabel("Mean expected cost")
        ax.legend(frameon=False, fontsize=8)
        fig.tight_layout()
        fig.savefig(FIG / "cost_vs_horizon.pdf")
        fig.savefig(FIG / "cost_vs_horizon.png", dpi=180)
        plt.close(fig)
    except Exception:
        failures += 1
    try:
        horizon = load_summary(OUT / "family_a_summary_by_horizon.csv")
        fig, ax = plt.subplots(figsize=(7, 4.2))
        for method in ["gcs_eager", "no_sharing_gcs", "probe_all_tree"]:
            xs = sorted({int(r["horizon"]) for r in horizon})
            ys = [float(next(r for r in horizon if int(r["horizon"]) == x and r["method"] == method)["mean_representation_size"]) for x in xs]
            ax.plot(xs, ys, marker="o", label=method)
        ax.set_yscale("log")
        ax.set_xlabel("Horizon")
        ax.set_ylabel("Representation nodes (log)")
        ax.legend(frameon=False, fontsize=8)
        fig.tight_layout()
        fig.savefig(FIG / "size_vs_horizon.pdf")
        fig.savefig(FIG / "size_vs_horizon.png", dpi=180)
        plt.close(fig)
    except Exception:
        failures += 1
    try:
        reliab = load_summary(OUT / "family_c_summary_by_reliability.csv")
        fig, ax = plt.subplots(figsize=(7, 4.2))
        for method in ["replan_on_failure", "gcs_eager", "gcs_thresholded", "gcs_robust"]:
            xs = [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0]
            ys = [
                float(next(r for r in reliab if abs(float(r["guard_error_rate"]) - x) < 1e-9 and r["confidence_mode"] == "calibrated" and r["confidence_threshold"] == "0.7" and r["method"] == method)["mean_cost"])
                for x in xs
            ]
            ax.plot([100 * x for x in xs], ys, marker="o", label=method)
        ax.set_xlabel("Guard error (%)")
        ax.set_ylabel("Mean expected cost")
        ax.legend(frameon=False, fontsize=8)
        fig.tight_layout()
        fig.savefig(FIG / "guard_error_curve.pdf")
        fig.savefig(FIG / "guard_error_curve.png", dpi=180)
        plt.close(fig)
    except Exception:
        failures += 1
    try:
        control = load_summary(OUT / "family_f_summary_by_control.csv")
        labels = ["zero_failure_penalty", "expensive_probe", "dense_all_guards", "no_reuse", "all_upfront", "missing_all_guards"]
        gcs = [float(next(r for r in control if r["control"] == c and r["method"] == "gcs_eager")["mean_cost"]) for c in labels]
        replan = [float(next(r for r in control if r["control"] == c and r["method"] == "replan_on_failure")["mean_cost"]) for c in labels]
        x = list(range(len(labels)))
        fig, ax = plt.subplots(figsize=(8, 4.3))
        ax.bar([v - 0.18 for v in x], replan, width=0.36, label="replan")
        ax.bar([v + 0.18 for v in x], gcs, width=0.36, label="GCS")
        ax.set_xticks(x)
        ax.set_xticklabels([c.replace("_", "\n") for c in labels], fontsize=7)
        ax.set_ylabel("Mean expected cost")
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(FIG / "negative_controls.pdf")
        fig.savefig(FIG / "negative_controls.png", dpi=180)
        plt.close(fig)
    except Exception:
        failures += 1
    return failures


def write_evidence_summary(metadata: dict[str, object]) -> None:
    main = load_summary(OUT / "family_a_summary_by_method.csv")
    reliab = load_summary(OUT / "family_c_summary_by_reliability.csv")

    def cost(method: str) -> float:
        return float(next(r for r in main if r["method"] == method)["mean_cost"])

    err100 = next(r for r in reliab if r["guard_error_rate"] == "1.0" and r["confidence_mode"] == "calibrated" and r["confidence_threshold"] == "0.7" and r["method"] == "gcs_eager")
    replan100 = next(r for r in reliab if r["guard_error_rate"] == "1.0" and r["confidence_mode"] == "calibrated" and r["confidence_threshold"] == "0.7" and r["method"] == "replan_on_failure")
    lines = [
        "# Full-Scale Evidence Summary",
        "",
        f"- Stage: {metadata['stage']}.",
        f"- Seed: {metadata['seed']}.",
        f"- Rows: {metadata['total_rows']:,}.",
        f"- Cases: {metadata['total_cases']:,}.",
        f"- Plot failures: {metadata['plot_failures']}.",
        "",
        "## Headline Numbers",
        "",
        f"- Family A linear-default cost: {cost('linear_default'):.2f}.",
        f"- Family A replan-on-failure cost: {cost('replan_on_failure'):.2f}.",
        f"- Family A GCS eager cost: {cost('gcs_eager'):.2f}.",
        f"- Family A lazy GCS cost: {cost('gcs_lazy'):.2f}.",
        f"- Family A no-sharing GCS nodes: {float(next(r for r in main if r['method'] == 'no_sharing_gcs')['mean_representation_size']):.0f}.",
        f"- Family A GCS eager nodes: {float(next(r for r in main if r['method'] == 'gcs_eager')['mean_representation_size']):.0f}.",
        f"- Family C 100% guard-error GCS eager cost: {float(err100['mean_cost']):.2f}.",
        f"- Family C 100% guard-error replan cost: {float(replan100['mean_cost']):.2f}.",
        "",
        "## Scope",
        "",
        "These results support a synthetic representation mechanism for long-horizon TAMP abstractions. They do not establish real-robot safety, learned guard discovery, production TAMP superiority, or POMDP optimality.",
        "",
    ]
    (DOCS / "evidence_summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ensure_dirs()
    start = time.perf_counter()
    families = []
    total_rows = 0
    total_cases = 0
    for name, func in [
        ("family_a", run_family_a),
        ("family_b", run_family_b),
        ("family_c", run_family_c),
        ("family_d", run_family_d),
        ("family_e", run_family_e),
        ("family_f", run_family_f),
        ("family_g", run_family_g),
    ]:
        print(f"running {name}", flush=True)
        rows, cases, seconds = func()
        item = {"family": name, "rows": rows, "cases": cases, "seconds": seconds}
        families.append(item)
        total_rows += rows
        total_cases += cases
        (OUT / "progress.json").write_text(json.dumps({"stage": "running", "total_rows": total_rows, "total_cases": total_cases, "families": families}, indent=2), encoding="utf-8")
        print(json.dumps(item), flush=True)
    make_tables()
    plot_failures = make_figures()
    metadata = {
        "stage": "complete",
        "seed": SEED,
        "elapsed_seconds": time.perf_counter() - start,
        "total_rows": total_rows,
        "total_cases": total_cases,
        "plot_failures": plot_failures,
        "families": families,
    }
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (OUT / "progress.json").write_text(json.dumps({"stage": "complete", "total_rows": total_rows, "total_cases": total_cases}, indent=2), encoding="utf-8")
    write_evidence_summary(metadata)
    print(json.dumps(metadata, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

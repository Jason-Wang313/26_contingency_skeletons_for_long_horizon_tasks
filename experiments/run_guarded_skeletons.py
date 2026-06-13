#!/usr/bin/env python
"""Run synthetic evidence for guarded contingency skeletons."""

from __future__ import annotations

import csv
from dataclasses import replace
import math
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from guarded_skeletons import evaluate_noisy_guarded, evaluate_problem, make_problem  # noqa: E402


RESULTS = ROOT / "results"
FIGS = ROOT / "paper" / "figures"
RESULTS.mkdir(exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)


def run() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    horizons = [8, 16, 32, 48, 64]
    reuse_biases = [0.25, 0.55, 0.85]
    seeds = list(range(30))
    for horizon in horizons:
        for reuse_bias in reuse_biases:
            for seed in seeds:
                num_guards = max(3, horizon // 4)
                problem = make_problem(
                    horizon=horizon,
                    num_guards=num_guards,
                    dependency_width=2,
                    reuse_bias=reuse_bias,
                    irreversible_rate=0.35,
                    seed=1000 * horizon + int(reuse_bias * 100) + seed,
                )
                result = evaluate_problem(problem, episodes=200, seed=seed + 17)
                for method, values in result.items():
                    rows.append(
                        {
                            "horizon": str(horizon),
                            "num_guards": str(num_guards),
                            "reuse_bias": f"{reuse_bias:.2f}",
                            "seed": str(seed),
                            "method": method,
                            "expected_cost": f"{values['cost']:.4f}",
                            "expected_failures": f"{values['failures']:.4f}",
                            "representation_size": f"{values['representation_size']:.1f}",
                            "relevant_guards": str(len(problem.relevant_guards)),
                        }
                    )
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "horizon",
        "num_guards",
        "reuse_bias",
        "seed",
        "method",
        "expected_cost",
        "expected_failures",
        "representation_size",
        "relevant_guards",
    ]
    with (RESULTS / "episodes.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["horizon"], row["reuse_bias"], row["method"])].append(row)
    summary: list[dict[str, str]] = []
    for (horizon, reuse_bias, method), vals in sorted(groups.items(), key=lambda x: (int(x[0][0]), x[0][1], x[0][2])):
        costs = [float(v["expected_cost"]) for v in vals]
        fails = [float(v["expected_failures"]) for v in vals]
        sizes = [float(v["representation_size"]) for v in vals]
        rel = [float(v["relevant_guards"]) for v in vals]
        summary.append(
            {
                "horizon": horizon,
                "reuse_bias": reuse_bias,
                "method": method,
                "mean_cost": f"{sum(costs) / len(costs):.4f}",
                "mean_failures": f"{sum(fails) / len(fails):.4f}",
                "mean_representation_size": f"{sum(sizes) / len(sizes):.2f}",
                "mean_relevant_guards": f"{sum(rel) / len(rel):.2f}",
            }
        )
    fields = [
        "horizon",
        "reuse_bias",
        "method",
        "mean_cost",
        "mean_failures",
        "mean_representation_size",
        "mean_relevant_guards",
    ]
    with (RESULTS / "summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary)
    return summary


def write_table(summary: list[dict[str, str]]) -> None:
    selected = [r for r in summary if r["reuse_bias"] == "0.55" and r["horizon"] in {"16", "32", "64"}]
    methods = ["linear_default", "replan_on_failure", "relevant_unshared_tree", "probe_all_tree", "guarded_skeleton"]
    by_key = {(r["horizon"], r["method"]): r for r in selected}
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "Horizon & Method & Cost & Failures & Nodes \\\\",
        "\\midrule",
    ]
    for horizon in ["16", "32", "64"]:
        for method in methods:
            row = by_key[(horizon, method)]
            pretty = method.replace("_", " ")
            lines.append(
                f"{horizon} & {pretty} & {float(row['mean_cost']):.2f} & "
                f"{float(row['mean_failures']):.2f} & {float(row['mean_representation_size']):.0f} \\\\"
            )
        lines.append("\\midrule")
    lines[-1] = "\\bottomrule"
    lines.append("\\end{tabular}")
    (RESULTS / "evidence_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_guard_assumption_stress() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    horizon = 64
    reuse_bias = 0.55
    episodes = 200
    seeds = list(range(30))
    for seed in seeds:
        problem = make_problem(
            horizon=horizon,
            num_guards=16,
            dependency_width=2,
            reuse_bias=reuse_bias,
            irreversible_rate=0.35,
            seed=1000 * horizon + int(reuse_bias * 100) + seed,
        )
        result = evaluate_problem(problem, episodes=episodes, seed=seed + 17)
        replan = result["replan_on_failure"]
        for probe_cost in [0.08, 0.50, 1.00, 2.00, 4.00, 6.00]:
            stressed = replace(problem, probe_cost=probe_cost)
            gcs_cost = stressed.horizon * stressed.action_cost + len(stressed.relevant_guards) * probe_cost
            rows.append(
                {
                    "stress": "probe_cost",
                    "level": f"{probe_cost:.2f}",
                    "seed": str(seed),
                    "gcs_cost": f"{gcs_cost:.4f}",
                    "gcs_failures": "0.0000",
                    "replan_cost": f"{replan['cost']:.4f}",
                    "delta_vs_replan": f"{gcs_cost - replan['cost']:.4f}",
                }
            )
        for guard_error_rate in [0.00, 0.05, 0.10, 0.20, 0.40, 0.80, 1.00]:
            noisy = evaluate_noisy_guarded(
                problem,
                episodes=episodes,
                seed=seed + 17,
                guard_error_rate=guard_error_rate,
            )
            rows.append(
                {
                    "stress": "guard_error",
                    "level": f"{guard_error_rate:.2f}",
                    "seed": str(seed),
                    "gcs_cost": f"{noisy['cost']:.4f}",
                    "gcs_failures": f"{noisy['failures']:.4f}",
                    "replan_cost": f"{replan['cost']:.4f}",
                    "delta_vs_replan": f"{noisy['cost'] - replan['cost']:.4f}",
                }
            )
    fields = ["stress", "level", "seed", "gcs_cost", "gcs_failures", "replan_cost", "delta_vs_replan"]
    with (RESULTS / "guard_assumption_stress.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def summarize_guard_assumption_stress(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["stress"], row["level"])].append(row)
    summary: list[dict[str, str]] = []
    for (stress, level), vals in sorted(groups.items(), key=lambda item: (item[0][0], float(item[0][1]))):
        costs = [float(v["gcs_cost"]) for v in vals]
        failures = [float(v["gcs_failures"]) for v in vals]
        replans = [float(v["replan_cost"]) for v in vals]
        deltas = [float(v["delta_vs_replan"]) for v in vals]
        summary.append(
            {
                "stress": stress,
                "level": level,
                "seeds": str(len(vals)),
                "mean_gcs_cost": f"{sum(costs) / len(costs):.4f}",
                "mean_gcs_failures": f"{sum(failures) / len(failures):.4f}",
                "mean_replan_cost": f"{sum(replans) / len(replans):.4f}",
                "mean_delta_vs_replan": f"{sum(deltas) / len(deltas):.4f}",
            }
        )
    fields = [
        "stress",
        "level",
        "seeds",
        "mean_gcs_cost",
        "mean_gcs_failures",
        "mean_replan_cost",
        "mean_delta_vs_replan",
    ]
    with (RESULTS / "guard_assumption_stress_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary)
    selected = [
        ("probe_cost", "0.08"),
        ("probe_cost", "4.00"),
        ("probe_cost", "6.00"),
        ("guard_error", "0.20"),
        ("guard_error", "0.80"),
        ("guard_error", "1.00"),
    ]
    by_key = {(row["stress"], row["level"]): row for row in summary}
    lines = [
        "\\begin{tabular}{llrrr}",
        "\\toprule",
        "Stress & Level & GCS cost & Failures & $\\Delta$ vs replan \\\\",
        "\\midrule",
    ]
    for stress, level in selected:
        row = by_key[(stress, level)]
        label = "probe cost" if stress == "probe_cost" else "guard error"
        display = f"{float(level):.2f}" if stress == "probe_cost" else f"{100 * float(level):.0f}\\%"
        lines.append(
            f"{label} & {display} & {float(row['mean_gcs_cost']):.2f} & "
            f"{float(row['mean_gcs_failures']):.2f} & {float(row['mean_delta_vs_replan']):+.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", ""])
    table = "\n".join(lines)
    (RESULTS / "guard_assumption_stress_table.tex").write_text(table, encoding="utf-8")
    return summary


def plot(summary: list[dict[str, str]]) -> None:
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        (RESULTS / "plot_status.txt").write_text(f"matplotlib unavailable: {exc}\n", encoding="utf-8")
        return
    methods = ["linear_default", "replan_on_failure", "relevant_unshared_tree", "probe_all_tree", "guarded_skeleton"]
    colors = {
        "linear_default": "#8c564b",
        "replan_on_failure": "#d62728",
        "relevant_unshared_tree": "#9467bd",
        "probe_all_tree": "#7f7f7f",
        "guarded_skeleton": "#1f77b4",
    }
    labels = {m: m.replace("_", " ") for m in methods}
    mid = [r for r in summary if r["reuse_bias"] == "0.55"]
    for metric, ylabel, filename, logy in [
        ("mean_cost", "expected execution cost", "cost_vs_horizon.pdf", False),
        ("mean_representation_size", "policy / skeleton nodes", "size_vs_horizon.pdf", True),
        ("mean_failures", "failed actions per episode", "failures_vs_horizon.pdf", False),
    ]:
        fig, ax = plt.subplots(figsize=(5.2, 3.1))
        for method in methods:
            vals = [r for r in mid if r["method"] == method]
            xs = [int(r["horizon"]) for r in vals]
            ys = [float(r[metric]) for r in vals]
            ax.plot(xs, ys, marker="o", linewidth=2, label=labels[method], color=colors[method])
        ax.set_xlabel("horizon")
        ax.set_ylabel(ylabel)
        if logy:
            ax.set_yscale("log")
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(FIGS / filename)
        fig.savefig(FIGS / filename.replace(".pdf", ".png"), dpi=180)
        plt.close(fig)


def write_status(summary: list[dict[str, str]], stress_summary: list[dict[str, str]]) -> None:
    gcs64 = next(r for r in summary if r["horizon"] == "64" and r["reuse_bias"] == "0.55" and r["method"] == "guarded_skeleton")
    replan64 = next(r for r in summary if r["horizon"] == "64" and r["reuse_bias"] == "0.55" and r["method"] == "replan_on_failure")
    tree64 = next(r for r in summary if r["horizon"] == "64" and r["reuse_bias"] == "0.55" and r["method"] == "relevant_unshared_tree")
    probe6 = next(r for r in stress_summary if r["stress"] == "probe_cost" and r["level"] == "6.00")
    error100 = next(r for r in stress_summary if r["stress"] == "guard_error" and r["level"] == "1.00")
    lines = [
        "# Experiment Status",
        "",
        "- Synthetic guard-deterministic TAMP abstraction completed.",
        f"- At horizon 64 / reuse 0.55, guarded skeleton cost {float(gcs64['mean_cost']):.2f} vs replan-on-failure {float(replan64['mean_cost']):.2f}.",
        f"- At horizon 64 / reuse 0.55, guarded skeleton nodes {float(gcs64['mean_representation_size']):.0f} vs relevant unshared tree {float(tree64['mean_representation_size']):.0f}.",
        f"- V2 probe-cost stress: when probe cost is 6.00, GCS cost {float(probe6['mean_gcs_cost']):.2f}, delta vs replan {float(probe6['mean_delta_vs_replan']):+.2f}.",
        f"- V2 guard-error stress: when guards are always flipped, noisy GCS cost {float(error100['mean_gcs_cost']):.2f}, delta vs replan {float(error100['mean_delta_vs_replan']):+.2f}.",
        "- Outputs: `results/episodes.csv`, `results/summary.csv`, `results/evidence_table.tex`, and `paper/figures/*.pdf` if matplotlib is available.",
        "- V2 outputs: `results/guard_assumption_stress.csv`, `results/guard_assumption_stress_summary.csv`, and `results/guard_assumption_stress_table.tex`.",
    ]
    (RESULTS / "experiment_status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = run()
    write_csv(rows)
    summary = summarize(rows)
    write_table(summary)
    stress_rows = run_guard_assumption_stress()
    stress_summary = summarize_guard_assumption_stress(stress_rows)
    plot(summary)
    write_status(summary, stress_summary)
    print(f"Wrote {len(rows)} episode aggregate rows, {len(summary)} summary rows, and {len(stress_rows)} stress rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

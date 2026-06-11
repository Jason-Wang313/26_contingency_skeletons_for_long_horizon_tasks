#!/usr/bin/env python
"""Run synthetic evidence for guarded contingency skeletons."""

from __future__ import annotations

import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from guarded_skeletons import evaluate_problem, make_problem  # noqa: E402


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


def write_status(summary: list[dict[str, str]]) -> None:
    gcs64 = next(r for r in summary if r["horizon"] == "64" and r["reuse_bias"] == "0.55" and r["method"] == "guarded_skeleton")
    replan64 = next(r for r in summary if r["horizon"] == "64" and r["reuse_bias"] == "0.55" and r["method"] == "replan_on_failure")
    tree64 = next(r for r in summary if r["horizon"] == "64" and r["reuse_bias"] == "0.55" and r["method"] == "relevant_unshared_tree")
    lines = [
        "# Experiment Status",
        "",
        "- Synthetic guard-deterministic TAMP abstraction completed.",
        f"- At horizon 64 / reuse 0.55, guarded skeleton cost {float(gcs64['mean_cost']):.2f} vs replan-on-failure {float(replan64['mean_cost']):.2f}.",
        f"- At horizon 64 / reuse 0.55, guarded skeleton nodes {float(gcs64['mean_representation_size']):.0f} vs relevant unshared tree {float(tree64['mean_representation_size']):.0f}.",
        "- Outputs: `results/episodes.csv`, `results/summary.csv`, `results/evidence_table.tex`, and `paper/figures/*.pdf` if matplotlib is available.",
    ]
    (RESULTS / "experiment_status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = run()
    write_csv(rows)
    summary = summarize(rows)
    write_table(summary)
    plot(summary)
    write_status(summary)
    print(f"Wrote {len(rows)} episode aggregate rows and {len(summary)} summary rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

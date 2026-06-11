"""Toy guarded contingency skeleton machinery for Paper 26.

The module models a finite long-horizon manipulation abstraction.  Hidden
binary physical guards stand for measurable regimes such as clearance, slip,
or reachability.  Each task step depends on a small subset of guards.  A
guarded contingency skeleton probes the guards it needs before the first action
that depends on them and dispatches to the corresponding action variant.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import random


@dataclass(frozen=True)
class Step:
    index: int
    guard_ids: tuple[int, ...]
    irreversible: bool


@dataclass(frozen=True)
class Problem:
    horizon: int
    num_guards: int
    steps: tuple[Step, ...]
    guard_prob: tuple[float, ...]
    probe_cost: float = 0.08
    action_cost: float = 1.0
    failure_penalty: float = 4.0
    repair_penalty: float = 1.0

    @property
    def relevant_guards(self) -> tuple[int, ...]:
        used = sorted({gid for step in self.steps for gid in step.guard_ids})
        return tuple(used)


def make_problem(
    horizon: int,
    num_guards: int,
    dependency_width: int,
    reuse_bias: float,
    irreversible_rate: float,
    seed: int,
) -> Problem:
    rng = random.Random(seed)
    hot = max(1, int(num_guards * max(0.05, min(0.95, reuse_bias))))
    steps = []
    for idx in range(horizon):
        width = max(1, min(dependency_width, num_guards))
        pool = list(range(hot)) if rng.random() < reuse_bias else list(range(num_guards))
        guard_ids = tuple(sorted(rng.sample(pool, min(width, len(pool)))))
        irreversible = rng.random() < irreversible_rate
        steps.append(Step(idx, guard_ids, irreversible))
    probs = tuple(0.25 + 0.5 * rng.random() for _ in range(num_guards))
    return Problem(horizon, num_guards, tuple(steps), probs)


def sample_assignment(problem: Problem, rng: random.Random) -> tuple[int, ...]:
    return tuple(1 if rng.random() < p else 0 for p in problem.guard_prob)


def action_signature(step: Step, assignment: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(assignment[gid] for gid in step.guard_ids)


def linear_default_episode(problem: Problem, assignment: tuple[int, ...], repair: bool) -> dict[str, float]:
    cost = 0.0
    failures = 0
    observed: set[int] = set()
    for step in problem.steps:
        cost += problem.action_cost
        required = action_signature(step, assignment)
        default = tuple(0 for _ in step.guard_ids)
        if required != default and not all(gid in observed for gid in step.guard_ids):
            failures += 1
            penalty = problem.failure_penalty * (1.5 if step.irreversible else 1.0)
            cost += penalty
            if repair:
                cost += problem.repair_penalty
                observed.update(step.guard_ids)
                cost += problem.action_cost
            else:
                observed.update(step.guard_ids)
    return {"cost": cost, "failures": float(failures)}


def guarded_episode(problem: Problem, assignment: tuple[int, ...], probe_all: bool = False) -> dict[str, float]:
    cost = 0.0
    failures = 0
    observed: set[int] = set()
    upfront = set(range(problem.num_guards)) if probe_all else set()
    cost += len(upfront) * problem.probe_cost
    observed.update(upfront)
    for step in problem.steps:
        missing = [gid for gid in step.guard_ids if gid not in observed]
        cost += len(missing) * problem.probe_cost
        observed.update(missing)
        cost += problem.action_cost
    return {"cost": cost, "failures": float(failures)}


def gcs_size(problem: Problem) -> int:
    branch_nodes = len(problem.relevant_guards)
    action_variants = 0
    seen_suffixes: set[tuple[int, tuple[int, ...]]] = set()
    for step in problem.steps:
        for values in product((0, 1), repeat=len(step.guard_ids)):
            seen_suffixes.add((step.index, values))
        action_variants += 2 ** len(step.guard_ids)
    return 1 + branch_nodes + min(action_variants, len(seen_suffixes))


def full_tree_size(problem: Problem, relevant_only: bool = False) -> int:
    guards = len(problem.relevant_guards) if relevant_only else problem.num_guards
    leaves = 2 ** guards
    branch_nodes = (2 ** (guards + 1)) - 1
    return branch_nodes + leaves * problem.horizon


def evaluate_problem(problem: Problem, episodes: int, seed: int) -> dict[str, dict[str, float]]:
    rng = random.Random(seed)
    totals = {
        "linear_default": {"cost": 0.0, "failures": 0.0},
        "replan_on_failure": {"cost": 0.0, "failures": 0.0},
        "probe_all_tree": {"cost": 0.0, "failures": 0.0},
        "guarded_skeleton": {"cost": 0.0, "failures": 0.0},
    }
    for _ in range(episodes):
        assignment = sample_assignment(problem, rng)
        results = {
            "linear_default": linear_default_episode(problem, assignment, repair=False),
            "replan_on_failure": linear_default_episode(problem, assignment, repair=True),
            "probe_all_tree": guarded_episode(problem, assignment, probe_all=True),
            "guarded_skeleton": guarded_episode(problem, assignment, probe_all=False),
        }
        for name, values in results.items():
            totals[name]["cost"] += values["cost"]
            totals[name]["failures"] += values["failures"]
    for values in totals.values():
        values["cost"] /= episodes
        values["failures"] /= episodes
    totals["linear_default"]["representation_size"] = float(problem.horizon)
    totals["replan_on_failure"]["representation_size"] = float(problem.horizon)
    totals["probe_all_tree"]["representation_size"] = float(full_tree_size(problem, relevant_only=False))
    totals["guarded_skeleton"]["representation_size"] = float(gcs_size(problem))
    totals["relevant_unshared_tree"] = {
        "cost": totals["guarded_skeleton"]["cost"],
        "failures": 0.0,
        "representation_size": float(full_tree_size(problem, relevant_only=True)),
    }
    return totals

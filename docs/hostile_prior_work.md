# Hostile Prior Work Set

This set is intentionally adversarial: each entry states what the paper makes less novel and which gap remains for guarded contingency skeletons.

## 1. FFRob: Leveraging symbolic planning for efficient task and motion planning
- Citation handle: Caelan Reed Garrett et al., 2017, "FFRob: Leveraging symbolic planning for efficient task and motion planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 2. Integrated task and motion planning in belief space
- Citation handle: Leslie Pack Kaelbling et al., 2013, "Integrated task and motion planning in belief space"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 3. Logic-geometric programming: an optimization-based approach to combined task and motion planning
- Citation handle: Marc Toussaint et al., 2015, "Logic-geometric programming: an optimization-based approach to combined task and motion planning"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 4. RHH-LGP: Receding Horizon And Heuristics-Based Logic-Geometric Programming For Task And Motion Planning
- Citation handle: Cornelius V. Braun et al., 2021, "RHH-LGP: Receding Horizon And Heuristics-Based Logic-Geometric Programming For Task And Motion Planning"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 5. PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning
- Citation handle: Caelan Reed Garrett et al., 2020, "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 6. Behavior Trees in Robotics and AI
- Citation handle: Michele Colledanchise et al., 2018, "Behavior Trees in Robotics and AI"
- Problem claimed: How to solve behavior trees and reactive execution problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Hidden assumptions: The tree structure and condition placement are supplied or locally learned rather than synthesized from TAMP alternatives. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Node library, condition tests, fallback order, and recovery semantics.
- Failure modes ignored: Global sharing and dominance among many long-horizon alternatives; geometric proof obligations.
- What it makes less novel: Reactive fallbacks and runtime condition checks as a representation pattern.
- What it leaves open: Automatic compilation of physical contingency skeletons from candidate task-motion plans.

## 7. Long-Horizon Multi-Robot Rearrangement Planning for Construction Assembly
- Citation handle: Valentin N. Hartmann et al., 2022, "Long-Horizon Multi-Robot Rearrangement Planning for Construction Assembly"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 8. STRIPStream: Integrating Symbolic Planners and Blackbox Samplers
- Citation handle: Caelan Reed Garrett et al., 2018, "STRIPStream: Integrating Symbolic Planners and Blackbox Samplers"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 9. Extended Tree Search for Robot Task and Motion Planning
- Citation handle: Tianyu Ren et al., 2021, "Extended Tree Search for Robot Task and Motion Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 10. Robust Task and Motion Planning for Long-Horizon Architectural Construction Planning
- Citation handle: Valentin N. Hartmann et al., 2020, "Robust Task and Motion Planning for Long-Horizon Architectural Construction Planning"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 11. A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches
- Citation handle: Zhigen Zhao et al., 2024, "A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: The field taxonomy and known limitation map.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 12. Synergistic Task and Motion Planning With Reinforcement Learning-Based Non-Prehensile Actions
- Citation handle: Gaoyuan Liu et al., 2023, "Synergistic Task and Motion Planning With Reinforcement Learning-Based Non-Prehensile Actions"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 13. Practical Task and Motion Planning for Robotic Food Preparation
- Citation handle: Jeremy Siburian et al., 2025, "Practical Task and Motion Planning for Robotic Food Preparation"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 14. R-LGP: A Reachability-guided Logic-geometric Programming Framework for Optimal Task and Motion Planning on Mobile Manipulators
- Citation handle: Kim Tien Ly et al., 2024, "R-LGP: A Reachability-guided Logic-geometric Programming Framework for Optimal Task and Motion Planning on Mobile Manipulators"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 15. Long-Horizon Manipulation of Unknown Objects via Task and Motion Planning with Estimated Affordances
- Citation handle: Aidan Curtis et al., 2022, "Long-Horizon Manipulation of Unknown Objects via Task and Motion Planning with Estimated Affordances"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 16. Learning to Search in Task and Motion Planning With Streams
- Citation handle: M. N. M. KHODEIR et al., 2023, "Learning to Search in Task and Motion Planning With Streams"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 17. SyDeBO: Symbolic-Decision-Embedded Bilevel Optimization for Long-Horizon Manipulation in Dynamic Environments
- Citation handle: Zhigen Zhao et al., 2021, "SyDeBO: Symbolic-Decision-Embedded Bilevel Optimization for Long-Horizon Manipulation in Dynamic Environments"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 18. Combining task and motion planning for mobile manipulators
- Citation handle: Aliakbar Akbari et al., 2020, "Combining task and motion planning for mobile manipulators"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 19. Extended Task and Motion Planning of Long-horizon Robot Manipulation.
- Citation handle: Tianyu Ren et al., 2021, "Extended Task and Motion Planning of Long-horizon Robot Manipulation."
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 20. Large language models for chemistry robotics
- Citation handle: Naruki Yoshikawa et al., 2023, "Large language models for chemistry robotics"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 21. Contingent Planning via Heuristic Forward Search with Implicit Belief States
- Citation handle: Jorg Hoffmann et al., 2005, "Contingent Planning via Heuristic Forward Search with Implicit Belief States"
- Problem claimed: How to solve contingent and nondeterministic planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Hidden assumptions: Branch variables are symbolic, enumerated, and available as planner observations.
- Variables treated as fixed: Observation alphabet, state abstraction, action outcomes, and sensing model.
- Failure modes ignored: Continuous geometric tests, contact/clearance regimes, and physical certificates produced by motion planning.
- What it makes less novel: Generic conditional policy construction over discrete observations.
- What it leaves open: Lifting continuous physical guard predicates into a skeleton-level object usable by TAMP.

## 22. LLM-GROP: Visually grounded robot task and motion planning with large language models
- Citation handle: Zhang, Xiaohan et al., 2025, "LLM-GROP: Visually grounded robot task and motion planning with large language models"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 23. LEAGUE: Guided Skill Learning and Abstraction for Long-Horizon Manipulation
- Citation handle: Shuo Cheng et al., 2023, "LEAGUE: Guided Skill Learning and Abstraction for Long-Horizon Manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 24. FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation
- Citation handle: Minho Heo et al., 2023, "FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 25. Optimistic Reinforcement Learning-Based Skill Insertions for Task and Motion Planning
- Citation handle: Gaoyuan Liu et al., 2024, "Optimistic Reinforcement Learning-Based Skill Insertions for Task and Motion Planning"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 26. Combined Task and Motion Planning for Mobile Manipulation
- Citation handle: Jason Wolfe et al., 2010, "Combined Task and Motion Planning for Mobile Manipulation"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 27. Fast and resilient manipulation planning for target retrieval in clutter
- Citation handle: Changjoo Nam et al., 2020, "Fast and resilient manipulation planning for target retrieval in clutter"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 28. Hierarchical Human-Motion Prediction and Logic-Geometric Programming for Minimal Interference Human-Robot Tasks
- Citation handle: An T. Le et al., 2021, "Hierarchical Human-Motion Prediction and Logic-Geometric Programming for Minimal Interference Human-Robot Tasks"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 29. Learning compositional models of robot skills for task and motion planning
- Citation handle: Zi Wang et al., 2020, "Learning compositional models of robot skills for task and motion planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 30. Differentiable GPU-Parallelized Task and Motion Planning
- Citation handle: William Shen et al., 2024, "Differentiable GPU-Parallelized Task and Motion Planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 31. AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers
- Citation handle: Yongchao Chen et al., 2023, "AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 32. D-LGP: Dynamic Logic-Geometric Program for Reactive Task and Motion Planning
- Citation handle: Teng Xue et al., 2023, "D-LGP: Dynamic Logic-Geometric Program for Reactive Task and Motion Planning"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 33. Anomaly? Weve got your back:A Bayesian Approach to Anomaly Handling through Task and Motion Planning
- Citation handle: Yazz Warsame et al., 2026, "Anomaly? Weve got your back:A Bayesian Approach to Anomaly Handling through Task and Motion Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 34. Continuous Optimization-Based Task and Motion Planning with Signal Temporal Logic Specifications for Sequential Manipulation
- Citation handle: Rin Takano et al., 2021, "Continuous Optimization-Based Task and Motion Planning with Signal Temporal Logic Specifications for Sequential Manipulation"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 35. Modular Multi-Level Replanning TAMP Framework for Dynamic Environment
- Citation handle: Tao Lin et al., 2023, "Modular Multi-Level Replanning TAMP Framework for Dynamic Environment"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 36. Increased Flexibility and Robustness of Mars Rovers
- Citation handle: L. J. Bresina et al., 1999, "Increased Flexibility and Robustness of Mars Rovers"
- Problem claimed: How to solve contingent and nondeterministic planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Hidden assumptions: Branch variables are symbolic, enumerated, and available as planner observations.
- Variables treated as fixed: Observation alphabet, state abstraction, action outcomes, and sensing model.
- Failure modes ignored: Continuous geometric tests, contact/clearance regimes, and physical certificates produced by motion planning.
- What it makes less novel: Generic conditional policy construction over discrete observations.
- What it leaves open: Lifting continuous physical guard predicates into a skeleton-level object usable by TAMP.

## 37. Guiding Long-Horizon Task and Motion Planning with Vision Language Models
- Citation handle: Zhutian Yang et al., 2024, "Guiding Long-Horizon Task and Motion Planning with Vision Language Models"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 38. Learning Symbolic Operators for Task and Motion Planning
- Citation handle: Tom Silver et al., 2021, "Learning Symbolic Operators for Task and Motion Planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 39. Recent Trends in Task and Motion Planning for Robotics: A Survey
- Citation handle: Huihui Guo et al., 2023, "Recent Trends in Task and Motion Planning for Robotics: A Survey"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: The field taxonomy and known limitation map.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 40. A Task and Motion Planning Framework for Partially Observable Household Manipulation Scenes
- Citation handle: MA Yu-hong et al., 2025, "A Task and Motion Planning Framework for Partially Observable Household Manipulation Scenes"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 41. Logic Learning from Demonstrations for Multi-step Manipulation Tasks in Dynamic Environments
- Citation handle: Yan Zhang et al., 2024, "Logic Learning from Demonstrations for Multi-step Manipulation Tasks in Dynamic Environments"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 42. Hierarchical task and motion planning in the now
- Citation handle: Leslie Pack Kaelbling et al., 2011, "Hierarchical task and motion planning in the now"
- Problem claimed: How to solve hierarchical task planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: General planning substrate, terminology, or benchmark context.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 43. A survey of Behavior Trees in robotics and AI
- Citation handle: Matteo Iovino et al., 2022, "A survey of Behavior Trees in robotics and AI"
- Problem claimed: How to solve behavior trees and reactive execution problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Hidden assumptions: The tree structure and condition placement are supplied or locally learned rather than synthesized from TAMP alternatives.
- Variables treated as fixed: Node library, condition tests, fallback order, and recovery semantics.
- Failure modes ignored: Global sharing and dominance among many long-horizon alternatives; geometric proof obligations.
- What it makes less novel: The field taxonomy and known limitation map.
- What it leaves open: Automatic compilation of physical contingency skeletons from candidate task-motion plans.

## 44. Accelerating Integrated Task and Motion Planning with Neural Feasibility Checking
- Citation handle: Lei Xu et al., 2022, "Accelerating Integrated Task and Motion Planning with Neural Feasibility Checking"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 45. Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness
- Citation handle: Aidan Curtis et al., 2024, "Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 46. A constraint-based method for solving sequential manipulation planning problems
- Citation handle: Tomas LozanoPerez et al., 2014, "A constraint-based method for solving sequential manipulation planning problems"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 47. Active model learning and diverse action sampling for task and motion planning
- Citation handle: Zi Wang et al., 2018, "Active model learning and diverse action sampling for task and motion planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 48. Guided Imitation of Task and Motion Planning
- Citation handle: Michael McDonald et al., 2021, "Guided Imitation of Task and Motion Planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 49. Versatile multicontact planning and control for legged loco-manipulation
- Citation handle: Jean-Pierre Sleiman et al., 2023, "Versatile multicontact planning and control for legged loco-manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 50. Object-Centric Task and Motion Planning in Dynamic Environments
- Citation handle: Toki Migimatsu et al., 2020, "Object-Centric Task and Motion Planning in Dynamic Environments"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 51. Planning Non-repetitive Robotic Assembly Processes with Task and Motion Planning (TAMP)
- Citation handle: Pok Yin Victor Leung et al., 2026, "Planning Non-repetitive Robotic Assembly Processes with Task and Motion Planning (TAMP)"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 52. PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via\n Optimistic Adaptive Planning
- Citation handle: Caelan Reed Garrett et al., 2018, "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via\n Optimistic Adaptive Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 53. Optimizing Trajectory-Trees in Belief Space: An Application from Model Predictive Control to Task and Motion Planning
- Citation handle: Camille Phiquepal et al., 2026, "Optimizing Trajectory-Trees in Belief Space: An Application from Model Predictive Control to Task and Motion Planning"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 54. Combining Task and Motion Planning: Challenges and Guidelines
- Citation handle: Masoumeh Mansouri et al., 2021, "Combining Task and Motion Planning: Challenges and Guidelines"
- Problem claimed: How to solve motion planning substrate problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: General planning substrate, terminology, or benchmark context.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 55. Robotic disassembly for end-of-life products focusing on task and motion planning: A comprehensive survey
- Citation handle: Mohammed Eesa Asif et al., 2024, "Robotic disassembly for end-of-life products focusing on task and motion planning: A comprehensive survey"
- Problem claimed: How to solve motion planning substrate problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: The field taxonomy and known limitation map.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 56. Sampling-based algorithms for optimal motion planning
- Citation handle: Sertac Karaman et al., 2011, "Sampling-based algorithms for optimal motion planning"
- Problem claimed: How to solve motion planning substrate problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: General planning substrate, terminology, or benchmark context.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 57. Anytime Integrated Task and Motion Policies for Stochastic Environments
- Citation handle: Naman Shah et al., 2020, "Anytime Integrated Task and Motion Policies for Stochastic Environments"
- Problem claimed: How to solve contingent and nondeterministic planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Hidden assumptions: Branch variables are symbolic, enumerated, and available as planner observations.
- Variables treated as fixed: Observation alphabet, state abstraction, action outcomes, and sensing model.
- Failure modes ignored: Continuous geometric tests, contact/clearance regimes, and physical certificates produced by motion planning.
- What it makes less novel: Generic conditional policy construction over discrete observations.
- What it leaves open: Lifting continuous physical guard predicates into a skeleton-level object usable by TAMP.

## 58. Robotic manipulation with pick and place task constructors
- Citation handle: Albert Llufriu Lopez et al., 2026, "Robotic manipulation with pick and place task constructors"
- Problem claimed: How to solve behavior trees and reactive execution problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Hidden assumptions: The tree structure and condition placement are supplied or locally learned rather than synthesized from TAMP alternatives.
- Variables treated as fixed: Node library, condition tests, fallback order, and recovery semantics.
- Failure modes ignored: Global sharing and dominance among many long-horizon alternatives; geometric proof obligations.
- What it makes less novel: Reactive fallbacks and runtime condition checks as a representation pattern.
- What it leaves open: Automatic compilation of physical contingency skeletons from candidate task-motion plans.

## 59. Conflict-Directed Diverse Planning for Logic-Geometric Programming
- Citation handle: Joaquim Ortiz-Haro et al., 2022, "Conflict-Directed Diverse Planning for Logic-Geometric Programming"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 60. Open-World Task and Motion Planning via Vision-Language Model Generated Constraints
- Citation handle: Nishanth Kumar et al., 2024, "Open-World Task and Motion Planning via Vision-Language Model Generated Constraints"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 61. FFRob: An Efficient Heuristic for Task and Motion Planning
- Citation handle: Caelan Reed Garrett et al., 2015, "FFRob: An Efficient Heuristic for Task and Motion Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 62. Contingent Task and Motion Planning under Uncertainty for HumanRobot Interactions
- Citation handle: Aliakbar Akbari et al., 2020, "Contingent Task and Motion Planning under Uncertainty for HumanRobot Interactions"
- Problem claimed: How to solve contingent and nondeterministic planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Hidden assumptions: Branch variables are symbolic, enumerated, and available as planner observations.
- Variables treated as fixed: Observation alphabet, state abstraction, action outcomes, and sensing model.
- Failure modes ignored: Continuous geometric tests, contact/clearance regimes, and physical certificates produced by motion planning.
- What it makes less novel: Generic conditional policy construction over discrete observations.
- What it leaves open: Lifting continuous physical guard predicates into a skeleton-level object usable by TAMP.

## 63. Primitive Action Based Combined Task and Motion Planning for the Service Robot
- Citation handle: Jeongmin Jeon et al., 2022, "Primitive Action Based Combined Task and Motion Planning for the Service Robot"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 64. Efficiently combining task and motion planning using geometric constraints
- Citation handle: Fabien Lagriffoul et al., 2014, "Efficiently combining task and motion planning using geometric constraints"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 65. PROTAMP-RRT: A Probabilistic Integrated Task and Motion Planner Based on RRT
- Citation handle: Alessio Saccuti et al., 2023, "PROTAMP-RRT: A Probabilistic Integrated Task and Motion Planner Based on RRT"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 66. Constraint Satisfaction for Motion Feasibility Checking
- Citation handle: Seok-Jun Lee et al., 2021, "Constraint Satisfaction for Motion Feasibility Checking"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 67. COAST: Constraints and Streams for Task and Motion Planning
- Citation handle: Brandon Vu et al., 2024, "COAST: Constraints and Streams for Task and Motion Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 68. Behavior Trees in Robotics and AI: An Introduction
- Citation handle: Michele Colledanchise et al., 2017, "Behavior Trees in Robotics and AI: An Introduction"
- Problem claimed: How to solve behavior trees and reactive execution problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Hidden assumptions: The tree structure and condition placement are supplied or locally learned rather than synthesized from TAMP alternatives. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Node library, condition tests, fallback order, and recovery semantics.
- Failure modes ignored: Global sharing and dominance among many long-horizon alternatives; geometric proof obligations.
- What it makes less novel: Reactive fallbacks and runtime condition checks as a representation pattern.
- What it leaves open: Automatic compilation of physical contingency skeletons from candidate task-motion plans.

## 69. Discovering State and Action Abstractions for Generalized Task and Motion Planning
- Citation handle: Aidan Curtis et al., 2022, "Discovering State and Action Abstractions for Generalized Task and Motion Planning"
- Problem claimed: How to solve motion planning substrate problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: General planning substrate, terminology, or benchmark context.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 70. Cooking Task Planning using LLM and Verified by Graph Network
- Citation handle: Ryunosuke Takebayashi et al., 2025, "Cooking Task Planning using LLM and Verified by Graph Network"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 71. Probabilistic roadmaps for path planning in high-dimensional configuration spaces
- Citation handle: Lydia E. Kavraki et al., 1996, "Probabilistic roadmaps for path planning in high-dimensional configuration spaces"
- Problem claimed: How to solve motion planning substrate problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: General planning substrate, terminology, or benchmark context.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 72. Integrated Task and Motion Planning for Multi-Robot Manipulation in Industry and Service Automation
- Citation handle: Ilknur Umay et al., 2025, "Integrated Task and Motion Planning for Multi-Robot Manipulation in Industry and Service Automation"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 73. Investigating strategies enabling novice users to teach plannable hierarchical tasks to robots
- Citation handle: Nina Moorman et al., 2024, "Investigating strategies enabling novice users to teach plannable hierarchical tasks to robots"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 74. Hierarchical Human-Motion Prediction and Logic-Geometric Programming for\n Minimal Interference Human-Robot Tasks
- Citation handle: An T. Le et al., 2021, "Hierarchical Human-Motion Prediction and Logic-Geometric Programming for\n Minimal Interference Human-Robot Tasks"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 75. Task and Motion Planning Using Infinite Completion Tree and Agnostic Skills
- Citation handle: Matan Sudry et al., 2025, "Task and Motion Planning Using Infinite Completion Tree and Agnostic Skills"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 76. Learning to combine primitive skills: A step towards versatile robotic manipulation
- Citation handle: Robin Strudel et al., 2020, "Learning to combine primitive skills: A step towards versatile robotic manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 77. TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation
- Citation handle: William Shen et al., 2026, "TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 78. Robot Planning and Situation Handling with Active Perception
- Citation handle: Austine Oloo et al., 2026, "Robot Planning and Situation Handling with Active Perception"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 79. An incremental constraint-based framework for task and motion planning
- Citation handle: Neil T. Dantam et al., 2018, "An incremental constraint-based framework for task and motion planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 80. Demonstration-guided Optimal Control for Long-term Non-prehensile Planar Manipulation
- Citation handle: Teng Xue et al., 2023, "Demonstration-guided Optimal Control for Long-term Non-prehensile Planar Manipulation"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 81. Automating Adaptive Execution Behaviors for Robot Manipulation
- Citation handle: Oriol Ruiz-Celada et al., 2022, "Automating Adaptive Execution Behaviors for Robot Manipulation"
- Problem claimed: How to solve behavior trees and reactive execution problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Hidden assumptions: The tree structure and condition placement are supplied or locally learned rather than synthesized from TAMP alternatives.
- Variables treated as fixed: Node library, condition tests, fallback order, and recovery semantics.
- Failure modes ignored: Global sharing and dominance among many long-horizon alternatives; geometric proof obligations.
- What it makes less novel: Reactive fallbacks and runtime condition checks as a representation pattern.
- What it leaves open: Automatic compilation of physical contingency skeletons from candidate task-motion plans.

## 82. SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation
- Citation handle: Zihan Zhou et al., 2024, "SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 83. Sampling-Based Robot Motion Planning: A Review
- Citation handle: Mohamed Elbanhawi et al., 2014, "Sampling-Based Robot Motion Planning: A Review"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: The field taxonomy and known limitation map.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 84. Large-Language-Model-Guided State Estimation for Partially Observable Task and Motion Planning
- Citation handle: Yoonwoo Kim et al., 2026, "Large-Language-Model-Guided State Estimation for Partially Observable Task and Motion Planning"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 85. FailRecOnt An Ontology-Based Framework for Failure Interpretation and Recovery in Planning and Execution
- Citation handle: Mohammed Diab et al., 2021, "FailRecOnt An Ontology-Based Framework for Failure Interpretation and Recovery in Planning and Execution"
- Problem claimed: How to solve contingent and nondeterministic planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Hidden assumptions: Branch variables are symbolic, enumerated, and available as planner observations.
- Variables treated as fixed: Observation alphabet, state abstraction, action outcomes, and sensing model.
- Failure modes ignored: Continuous geometric tests, contact/clearance regimes, and physical certificates produced by motion planning.
- What it makes less novel: Generic conditional policy construction over discrete observations.
- What it leaves open: Lifting continuous physical guard predicates into a skeleton-level object usable by TAMP.

## 86. Visually Grounded Task and Motion Planning for Mobile Manipulation
- Citation handle: Xiaohan Zhang et al., 2022, "Visually Grounded Task and Motion Planning for Mobile Manipulation"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 87. Chemistry Lab Automation via Constrained Task and Motion Planning
- Citation handle: Naruki Yoshikawa et al., 2022, "Chemistry Lab Automation via Constrained Task and Motion Planning"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 88. A Long Horizon Planning Framework for Manipulating Rigid Pointcloud\n Objects
- Citation handle: Anthony Simeonov et al., 2020, "A Long Horizon Planning Framework for Manipulating Rigid Pointcloud\n Objects"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 89. Online Replanning in Belief Space for Partially Observable Task and Motion Problems
- Citation handle: Caelan Reed Garrett et al., 2020, "Online Replanning in Belief Space for Partially Observable Task and Motion Problems"
- Problem claimed: How to solve belief-space and uncertain planning problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Hidden assumptions: Probabilistic models are calibrated and solving the belief policy is tractable for the horizon.
- Variables treated as fixed: Prior distributions, observation likelihoods, utility model, and state estimator.
- Failure modes ignored: Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization.
- What it makes less novel: Probabilistic formulations of uncertainty-aware TAMP.
- What it leaves open: Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks.

## 90. Imitating Task and Motion Planning with Visuomotor Transformers
- Citation handle: Murtaza Dalal et al., 2023, "Imitating Task and Motion Planning with Visuomotor Transformers"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 91. Long-Horizon Task and Motion Planning with Learning-Based Geometric Reasoning
- Citation handle: Ait Bouhsain, Smail et al., 2025, "Long-Horizon Task and Motion Planning with Learning-Based Geometric Reasoning"
- Problem claimed: How to solve optimization / geometric-constraint TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Hidden assumptions: The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Contact modes, constraint graph, objective weights, and observability of feasibility conditions.
- Failure modes ignored: Discrete physical branches that should alter the high-level skeleton before failure.
- What it makes less novel: Optimization over hybrid mode sequences and constraint-consistent trajectories.
- What it leaves open: Guarded sharing among alternative mode sequences driven by measurable branch conditions.

## 92. A Systematic Study of Large Language Models for Task and Motion Planning With PDDLStream
- Citation handle: Jorge Mendez-Mendez et al., 2025, "A Systematic Study of Large Language Models for Task and Motion Planning With PDDLStream"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 93. Hypergraph-Based Multi-robot Task and Motion Planning
- Citation handle: James Motes et al., 2023, "Hypergraph-Based Multi-robot Task and Motion Planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 94. STAMP: Differentiable Task and Motion Planning via Stein Variational Gradient Descent
- Citation handle: Yewon Lee et al., 2023, "STAMP: Differentiable Task and Motion Planning via Stein Variational Gradient Descent"
- Problem claimed: How to solve motion planning substrate problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hidden assumptions: The abstraction used by the planner is sufficiently faithful during execution.
- Variables treated as fixed: State variables, actions, observation model, and cost semantics.
- Failure modes ignored: Physical branch conditions not represented in the planning abstraction.
- What it makes less novel: General planning substrate, terminology, or benchmark context.
- What it leaves open: Physically grounded branch conditions embedded directly in task-motion skeletons.

## 95. Differentiable Physics and Stable Modes for Tool-Use and Manipulation Planning
- Citation handle: Marc Toussaint et al., 2018, "Differentiable Physics and Stable Modes for Tool-Use and Manipulation Planning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 96. A Software Architecture for Service Robots Manipulating Objects in Human Environments
- Citation handle: Changjoo Nam et al., 2020, "A Software Architecture for Service Robots Manipulating Objects in Human Environments"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 97. OceanChat: Piloting Autonomous Underwater Vehicles in Natural Language
- Citation handle: Ruochu Yang et al., 2023, "OceanChat: Piloting Autonomous Underwater Vehicles in Natural Language"
- Problem claimed: How to solve sampling-based TAMP problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Hidden assumptions: Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling.
- Variables treated as fixed: Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics.
- Failure modes ignored: Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment.
- What it makes less novel: Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search.
- What it leaves open: A compact representation of multiple physically conditioned skeletons without enumerating full belief policies.

## 98. A Long Horizon Planning Framework for Manipulating Rigid Pointcloud Objects
- Citation handle: Anthony Simeonov et al., 2020, "A Long Horizon Planning Framework for Manipulating Rigid Pointcloud Objects"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 99. Onto-LLM-TAMP: Knowledge-oriented Task and Motion Planning using Large Language Models
- Citation handle: Muhayy Ud Din et al., 2026, "Onto-LLM-TAMP: Knowledge-oriented Task and Motion Planning using Large Language Models"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

## 100. Human-in-the-Loop Task and Motion Planning for Imitation Learning
- Citation handle: Ajay Mandlekar et al., 2023, "Human-in-the-Loop Task and Motion Planning for Imitation Learning"
- Problem claimed: How to solve long-horizon manipulation and rearrangement problems for robot or embodied agents under long-horizon constraints.
- Actual mechanism introduced: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Hidden assumptions: Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction. Learned components are assumed to generalize over the branch regimes considered.
- Variables treated as fixed: Object set, support relations, manipulation primitives, and environment model.
- Failure modes ignored: Early physical branch tests that change which multi-step skeleton should be followed.
- What it makes less novel: Long-horizon domains and manipulation benchmarks as evidence settings.
- What it leaves open: A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space.

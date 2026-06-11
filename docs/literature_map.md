# Literature Map

## Field Box
Task-and-motion planning for embodied robots, especially long-horizon manipulation and mobile manipulation where symbolic task choices, geometric feasibility, execution monitoring, and physical failure recovery interact.

## Sweep Protocol
- Landscape sweep: 5147 papers in `related_work_matrix.csv`.
- Serious skim: top 300 ranked papers in `serious_skim_300.csv`.
- Deep read: top 225 ranked papers in `deep_read_225.csv`.
- Hostile prior-work set: top 100 ranked papers in `hostile_prior_work_100.csv`.
- Median publication year among matrix rows: 2019.

## Cluster Counts
- general robot / AI planning: 2783
- long-horizon manipulation and rearrangement: 801
- motion planning substrate: 698
- belief-space and uncertain planning: 252
- sampling-based TAMP: 197
- contingent and nondeterministic planning: 179
- hierarchical task planning: 128
- temporal-logic robot planning: 39
- optimization / geometric-constraint TAMP: 37
- behavior trees and reactive execution: 33

## Representative Prior Work By Cluster

### behavior trees and reactive execution
- Michele Colledanchise et al., 2018, "Behavior Trees in Robotics and AI". Mechanism: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Matteo Iovino et al., 2022, "A survey of Behavior Trees in robotics and AI". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Albert Llufriu Lopez et al., 2026, "Robotic manipulation with pick and place task constructors". Mechanism: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Michele Colledanchise et al., 2017, "Behavior Trees in Robotics and AI: An Introduction". Mechanism: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Oriol Ruiz-Celada et al., 2022, "Automating Adaptive Execution Behaviors for Robot Manipulation". Mechanism: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.
- Alessio De Luca et al., 2023, "Autonomous Navigation With Online Replanning and Recovery Behaviors for Wheeled-Legged Robots Using Behavior Trees". Mechanism: Composes fallback, sequence, and condition nodes to execute reactive robot behaviors.

### belief-space and uncertain planning
- Leslie Pack Kaelbling et al., 2013, "Integrated task and motion planning in belief space". Mechanism: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Gaoyuan Liu et al., 2024, "Optimistic Reinforcement Learning-Based Skill Insertions for Task and Motion Planning". Mechanism: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Jason Wolfe et al., 2010, "Combined Task and Motion Planning for Mobile Manipulation". Mechanism: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Aidan Curtis et al., 2024, "Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness". Mechanism: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Jeongmin Jeon et al., 2022, "Primitive Action Based Combined Task and Motion Planning for the Service Robot". Mechanism: Plans in belief or information space, often optimizing expected cost or chance constraints.
- Teng Xue et al., 2023, "Demonstration-guided Optimal Control for Long-term Non-prehensile Planar Manipulation". Mechanism: Plans in belief or information space, often optimizing expected cost or chance constraints.

### contingent and nondeterministic planning
- Jorg Hoffmann et al., 2005, "Contingent Planning via Heuristic Forward Search with Implicit Belief States". Mechanism: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- L. J. Bresina et al., 1999, "Increased Flexibility and Robustness of Mars Rovers". Mechanism: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Naman Shah et al., 2020, "Anytime Integrated Task and Motion Policies for Stochastic Environments". Mechanism: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Aliakbar Akbari et al., 2020, "Contingent Task and Motion Planning under Uncertainty for HumanRobot Interactions". Mechanism: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Mohammed Diab et al., 2021, "FailRecOnt An Ontology-Based Framework for Failure Interpretation and Recovery in Planning and Execution". Mechanism: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.
- Valerio Sanelli et al., 2017, "Short-Term Human-Robot Interaction through Conditional Planning and Execution". Mechanism: Builds conditional plans or policies over symbolic observations and nondeterministic outcomes.

### general robot / AI planning
- Stephanie Lowry et al., 2015, "Visual Place Recognition: A Survey". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Vincent Francois-Lavet et al., 2018, "An Introduction to Deep Reinforcement Learning". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Dylan P. Losey et al., 2018, "A Review of Intent Detection, Arbitration, and Communication Aspects of Shared Control for Physical HumanRobot Interaction". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Terrence Fong et al., 2003, "A survey of socially interactive robots". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Shansi Zhang et al., 2019, "Continuous control for robot based on deep reinforcement learning". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Wilko Schwarting et al., 2018, "Planning and Decision-Making for Autonomous Vehicles". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.

### hierarchical task planning
- Leslie Pack Kaelbling et al., 2011, "Hierarchical task and motion planning in the now". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Kanghyun Kim et al., 2023, "A Reachability Tree-Based Algorithm for Robot Task and Motion Planning". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.

### long-horizon manipulation and rearrangement
- Valentin N. Hartmann et al., 2022, "Long-Horizon Multi-Robot Rearrangement Planning for Construction Assembly". Mechanism: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Zhigen Zhao et al., 2024, "A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Zhigen Zhao et al., 2021, "SyDeBO: Symbolic-Decision-Embedded Bilevel Optimization for Long-Horizon Manipulation in Dynamic Environments". Mechanism: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Zhang, Xiaohan et al., 2025, "LLM-GROP: Visually grounded robot task and motion planning with large language models". Mechanism: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Shuo Cheng et al., 2023, "LEAGUE: Guided Skill Learning and Abstraction for Long-Horizon Manipulation". Mechanism: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.
- Minho Heo et al., 2023, "FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation". Mechanism: Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints.

### motion planning substrate
- Masoumeh Mansouri et al., 2021, "Combining Task and Motion Planning: Challenges and Guidelines". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Mohammed Eesa Asif et al., 2024, "Robotic disassembly for end-of-life products focusing on task and motion planning: A comprehensive survey". Mechanism: Organizes and categorizes prior methods rather than introducing one executable mechanism.
- Sertac Karaman et al., 2011, "Sampling-based algorithms for optimal motion planning". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Aidan Curtis et al., 2022, "Discovering State and Action Abstractions for Generalized Task and Motion Planning". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Lydia E. Kavraki et al., 1996, "Probabilistic roadmaps for path planning in high-dimensional configuration spaces". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Yewon Lee et al., 2023, "STAMP: Differentiable Task and Motion Planning via Stein Variational Gradient Descent". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.

### optimization / geometric-constraint TAMP
- Marc Toussaint et al., 2015, "Logic-geometric programming: an optimization-based approach to combined task and motion planning". Mechanism: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Cornelius V. Braun et al., 2021, "RHH-LGP: Receding Horizon And Heuristics-Based Logic-Geometric Programming For Task And Motion Planning". Mechanism: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Valentin N. Hartmann et al., 2020, "Robust Task and Motion Planning for Long-Horizon Architectural Construction Planning". Mechanism: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Kim Tien Ly et al., 2024, "R-LGP: A Reachability-guided Logic-geometric Programming Framework for Optimal Task and Motion Planning on Mobile Manipulators". Mechanism: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- Aliakbar Akbari et al., 2020, "Combining task and motion planning for mobile manipulators". Mechanism: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.
- An T. Le et al., 2021, "Hierarchical Human-Motion Prediction and Logic-Geometric Programming for Minimal Interference Human-Robot Tasks". Mechanism: Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure.

### sampling-based TAMP
- Caelan Reed Garrett et al., 2017, "FFRob: Leveraging symbolic planning for efficient task and motion planning". Mechanism: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Caelan Reed Garrett et al., 2020, "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning". Mechanism: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Caelan Reed Garrett et al., 2018, "STRIPStream: Integrating Symbolic Planners and Blackbox Samplers". Mechanism: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Tianyu Ren et al., 2021, "Extended Tree Search for Robot Task and Motion Planning". Mechanism: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Gaoyuan Liu et al., 2023, "Synergistic Task and Motion Planning With Reinforcement Learning-Based Non-Prehensile Actions". Mechanism: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.
- Jeremy Siburian et al., 2025, "Practical Task and Motion Planning for Robotic Food Preparation". Mechanism: Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates.

### temporal-logic robot planning
- Morteza Lahijanian et al., 2015, "This Time the Robot Settles for a Cost: A Quantitative Approach to Temporal Logic Planning with Partial Satisfaction". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.
- Hadas KressGazit et al., 2008, "Translating Structured English to Robot Controllers". Mechanism: Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making.

## Hidden Assumptions That May Be False
1. **Linear skeleton sufficiency.** Assumption: A single task skeleton is enough until execution failure. Paper direction: Represent a set of branch-sharing skeletons before commitment.
2. **Symbolic branch variables.** Assumption: Contingencies can be named as discrete planner observations. Paper direction: Lift continuous clearance, friction, reachability, and contact tests into guard predicates.
3. **Late failure is acceptable.** Assumption: Discovering infeasibility by failed execution is a tolerable repair signal. Paper direction: Move branch tests before irreversible or high-penalty actions.
4. **Sampler retry as repair.** Assumption: More continuous samples will eventually repair the same high-level sequence. Paper direction: Let physical guards change the high-level sequence itself.
5. **Mode sequence commitment.** Assumption: The contact/mode sequence can be chosen before sensing the relevant regime. Paper direction: Delay only the choices whose feasibility depends on guard outcomes.
6. **Cheap replanning.** Assumption: Online replanning cost is negligible relative to execution. Paper direction: Compile a contingency object offline and execute by guard dispatch.
7. **Stationary predicates.** Assumption: Predicates mean the same thing across the whole horizon. Paper direction: Attach guards to physical tests at the action boundary where their truth is certified.
8. **Manual fallbacks.** Assumption: A designer can specify behavior-tree fallback order correctly. Paper direction: Synthesize fallback/branch order from candidate skeleton dominance.
9. **Full belief necessity.** Assumption: Uncertain physical tasks require a calibrated belief-space policy. Paper direction: Handle deterministic latent regimes with coverage guards instead of probabilities.
10. **Independent failures.** Assumption: Action failures can be treated as local exceptions. Paper direction: Model shared hidden guard causes that affect many later actions.
11. **Fixed object affordances.** Assumption: Object-action affordances are fixed during planning. Paper direction: Branch skeletons on measured affordance regimes.
12. **Known contact regime.** Assumption: Contact-rich actions expose no strategic branch point before contact. Paper direction: Probe guard conditions such as slip or clearance before committing to a contact sequence.
13. **Geometry-only feasibility.** Assumption: A geometric path certificate is enough for plan success. Paper direction: Track which physical condition made each certificate valid.
14. **No irreversible side effects.** Assumption: Trying an action and failing leaves the world unchanged. Paper direction: Separate reversible probe actions from irreversible task actions.
15. **Complete observation alphabet.** Assumption: The planner already contains all observations it may need. Paper direction: Derive observation tests from violated continuous preconditions.
16. **Unshared contingency.** Assumption: A conditional policy must enumerate complete future assignments. Paper direction: Use a skeleton DAG that shares suffixes across guard-equivalent branches.
17. **Horizon-independent branching.** Assumption: Branch count is independent of task length or can be hidden inside a planner. Paper direction: Measure representation growth with horizon and relevant guard count.
18. **Benchmark abstraction fidelity.** Assumption: Simulation predicates capture the same failures as physical execution. Paper direction: Make the paper's claims only for guard-deterministic abstractions and synthetic evidence.
19. **Recovery locality.** Assumption: A failed action can be repaired without changing earlier choices. Paper direction: Plan branch points at the earliest certificate boundary.
20. **Planner owns all costs.** Assumption: Cost lives in the symbolic/continuous planner objective only. Paper direction: Expose probe, failed-action, and irreversible penalties as separate planning costs.
21. **No branch dominance.** Assumption: Alternative skeletons must be searched independently. Paper direction: Prune alternatives whose guard regions and suffixes are dominated.
22. **Outcome probabilities known.** Assumption: Branch probabilities are required to plan contingencies. Paper direction: Guarantee coverage without assuming calibrated probabilities, then optionally score costs.

## Candidate Directions Considered
- **Runtime TAMP repair tree** breaks `Late failure is acceptable.`; verdict: rejected: Too close to execution monitoring and behavior-tree fallback; central mechanism remains repair after failure.
- **Belief-space TAMP with branch penalties** breaks `Full belief necessity.`; verdict: rejected: Would mainly add uncertainty/cost shaping, which prior POMDP and belief-space TAMP already cover.
- **LLM-generated contingency plans** breaks `Manual fallbacks.`; verdict: rejected: Falls into the forbidden weak move: using an LLM as planner without a new physical mechanism.
- **Guarded Contingency Skeletons** breaks `Linear skeleton sufficiency and symbolic branch-variable assumptions.`; verdict: chosen

## Chosen Direction
Guarded Contingency Skeletons (GCS): compile many candidate task-motion skeletons into a decision DAG whose branch nodes are measurable physical guard predicates. The central object is not a bigger planner, learned verifier, or belief policy; it is a skeleton-level representation that delays exactly those high-level commitments whose continuous feasibility certificates depend on guard outcomes, while sharing prefixes and suffixes across guard-equivalent branches.

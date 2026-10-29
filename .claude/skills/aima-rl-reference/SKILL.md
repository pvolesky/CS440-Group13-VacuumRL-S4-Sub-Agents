---
name: aima-rl-reference
description: Map of relevant concepts from Russell & Norvig, Artificial Intelligence: A Modern Approach, to components of this project (agents, PEAS, MDPs, reinforcement learning, exploration). Load for conceptual grounding or when explaining design choices.
---
# AIMA concept map (pointers, not solutions)

Chapter numbers differ by edition: RL is Ch. 22 in the 4th edition and Ch. 21 in the 3rd. Verify against your copy.

| Project element | AIMA concept |
|---|---|
| Describing the robot's task | Task environment and PEAS (Ch. 2); environment properties (observability, determinism, episodic vs. sequential, discrete) |
| Gridworld layout, rewards | Sequential decision problems / MDPs (Ch. 16 in 4th ed., Ch. 17 in 3rd). The 4x3 world is the textbook analog |
| Unknown T and R | Reinforcement learning: model-free vs. model-based; passive vs. active learners |
| Q-learning | Temporal-difference methods; action-utility (Q) functions; off-policy learning |
| Epsilon / exploration decay | Exploration vs. exploitation; the GLIE idea (greedy in the limit with infinite exploration) |
| Discount and step cost | Utilities over time sequences; discounted rewards |
| Evaluating the result | Comparing learned policy utility to the optimal policy (only the evaluation side may know T and R) |

Use this to explain why a design choice exists. Do not paste textbook pseudocode into the repo.

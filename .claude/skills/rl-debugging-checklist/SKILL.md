---
name: rl-debugging-checklist
description: Ordered checklist for diagnosing failures in a tabular Q-learning vacuum robot (no convergence, wrong policy, oscillating values, agent walks into the wall repeatedly). Load when reviewing or debugging learning behavior.
---
# RL debugging checklist (check in order)

## 1. Boundary and environment
- Does any agent code read T, R, or environment internals?
- Do terminal cells actually end the episode? Is reset restoring the start state?
- Does bumping the obstacle or a border behave as documented in DECISIONS.md?
- Coordinates: (row, col) vs. (x, y) swaps; row 0 is the top.

## 2. Learning signal
- Are rewards reaching the agent at the right step (reward for the transition, not the previous one)?
- Terminal transitions: is the future-value term treated correctly at episode end?
- Is the Q-table updated for the state-action pair that was actually taken?

## 3. Exploration
- Does the agent still visit all reachable states late in training? Plot visit counts.
- Is exploration decayed too fast or never?

## 4. Hyperparameters
- Learning rate too high -> oscillation; too low -> stalls.
- Discount close to 1 with a small step cost -> long horizon, slow signal propagation.

## 5. Evaluation
- Evaluate with exploration off and across multiple seeds.
- A single lucky run is not evidence.

---
name: q-learning-procedure
description: Process guidance (not code) for designing and implementing a tabular Q-learning agent in this repo: components, order of work, decisions to settle first. Load when planning or implementing the agent.
---
# Q-learning working procedure

This skill describes process and design questions. It intentionally contains no solution code or update-rule listing; the user implements or explicitly requests implementation.

## Before writing anything
1. Confirm the Open decisions that affect the agent (D3 discounting, D4 stochasticity, D5 actions) in `docs/DECISIONS.md`.
2. Confirm state indexing with `gridworld-spec`. The Q-table shape follows from states x actions; decide how the obstacle cell is treated.

## Components to design (one at a time)
1. Q-table representation and initialization (what initial values encourage or discourage exploration?).
2. Action selection / exploration policy (separate module: `exploration.py`).
3. The learning update, driven only by observed experience tuples.
4. Terminal-state handling: what is the target value when the next state is terminal?
5. Hyperparameter schedule: learning rate, discount, exploration decay.
6. Policy extraction for evaluation.

## Order of work
Interface first, then the exploration policy, then the update, then terminal handling, then schedules. After each step, hand to `rl-reviewer`.

## Conceptual references
See `aima-rl-reference` for the textbook concepts behind each component.

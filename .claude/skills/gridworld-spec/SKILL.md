---
name: gridworld-spec
description: Specification of the 4x4 vacuum robot gridworld (layout, coordinates, terminals, PEAS description, agent/environment interface contract). Load when working on the environment, state/action indexing, or anything that depends on the grid.
---
# Gridworld specification

## Given layout (row 0 at top, coordinates are (row, col))
```
[ start, 0, 0,  0 ]
[ 0,     X, 0,  0 ]
[ 0,     0, 0,  0 ]
[ 0,    -1, 0, 10 ]
```
- start = (0,0)
- X = (1,1), obstacle (exact semantics: see D1 in docs/DECISIONS.md)
- -1 = (3,1), penalty cell
- 10 = (3,3), goal reward cell
- Whether -1 / 10 end the episode, step costs, discount, stochasticity, and action set are **Open** (docs/DECISIONS.md). Ask; do not assume.

## PEAS (AIMA Ch. 2)
- Performance: cumulative (discounted) reward; reaching the goal while avoiding the penalty cell.
- Environment: 4x4 discrete grid with one obstacle and two special cells.
- Actuators: movement actions (set is Open, D5).
- Sensors: current grid position only.

## Interface contract (agent-visible)
- `reset()` returns the initial observation.
- `step(action)` returns observation, reward, a termination signal, and an info dict.
- The info dict must NOT carry transition probabilities, the reward table, or any model internals.
- State representation for the agent = what `step`/`reset` return, nothing more.

## Why T and R are hidden
Because the agent does not know T or R, the problem is model-free RL (AIMA Ch. 22: active, model-free / temporal-difference learning), not planning with a known MDP.

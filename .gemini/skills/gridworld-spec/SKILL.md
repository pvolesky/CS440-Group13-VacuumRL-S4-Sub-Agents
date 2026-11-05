---
name: gridworld-spec
description: Specification of the 4x4 vacuum robot gridworld (layout, coordinates, terminals, interface contract).
---

# Gridworld Specification

## Layout (row 0 at top, coordinates (row, col))
```
[ (0,0) Start, (0,1),      (0,2), (0,3)      ]
[ (1,0),       (1,1) Wall, (1,2), (1,3)      ]
[ (2,0),       (2,1),      (2,2), (2,3)      ]
[ (3,0),       (3,1) -1,   (3,2), (3,3) +10  ]
```

- Start: `(0, 0)`
- Obstacle (Wall): `(1, 1)` (attempting to enter keeps the agent in place)
- Penalty: `(3, 1)` (-1.0 reward, terminal)
- Goal: `(3, 3)` (+10.0 reward, terminal)
- Living Reward: `-0.01` per step
- Actions: `["UP", "DOWN", "LEFT", "RIGHT"]`

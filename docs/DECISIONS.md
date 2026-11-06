# Design Decisions Log

| ID | Question | Status | Decision | Affects |
|---|---|---|---|---|
| D1 | What is `X`: impassable wall or something else? | Resolved | Impassable wall (collision keeps agent in place) | environment, tests |
| D2 | Do the `-1` and `10` cells end the episode? | Resolved | Both terminal (`done = True`) | environment, agent terminal handling |
| D3 | Hyperparameters & Epsilon Schedule | Resolved | Step cost -0.01, discount 0.9, learning rate 0.1, initial epsilon 1.0 with 0.99 decay | environment, hyperparameters |
| D4 | Is the simulator deterministic or stochastic? | Resolved | Deterministic gridworld transition model | environment, evaluation |
| D5 | Action set | Resolved | `["UP", "DOWN", "LEFT", "RIGHT"]` | environment, agent |
| D6 | Environment API shape | Resolved | Lightweight `reset()` and `step(action)` returning `(next_state, reward, done)` | environment, agent, train |
| D7 | Strategy 4 Implementation | Resolved | Complete model-free isolation via sub-agents and skills | all |
| D8 | Baseline | Resolved | Excluded from the repo | evaluation |

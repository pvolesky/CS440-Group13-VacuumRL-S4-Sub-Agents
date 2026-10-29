# Design decisions log

Agents must **ask** about anything marked Open and must not assume the proposed default. Only the repository owner resolves a decision.

| ID | Question | Status | Proposed default (not binding) | Affects |
|----|----------|--------|--------------------------------|---------|
| D1 | What is `X`: impassable wall (bump = stay in place) or something else? | Open | Wall | environment, tests |
| D2 | Do the `-1` and `10` cells end the episode? | Open | Both terminal | environment, agent terminal handling |
| D3 | Per-step cost and discount factor | Open | Step cost -0.04 (AIMA 4x3 world), discount 0.99 | environment, hyperparameters |
| D4 | Is the simulator deterministic or stochastic (e.g. AIMA 0.8/0.1/0.1)? | Open | Stochastic, hidden from agent | environment, evaluation |
| D5 | Action set | Open | Up/down/left/right | environment, agent |
| D6 | Environment API shape | Open | Gymnasium-style reset/step, no Gymnasium dependency | environment, agent, train |
| D7 | Who writes implementation code | Resolved | Owner writes it; agents explain, review, scaffold unless explicitly asked | all |
| D8 | Value-iteration / known-model baseline | Resolved | Excluded from the repo | evaluation |

## Resolved by the owner
- Source code: Python. Hook scripts: Bash (Linux).
- Skills may be used if they help and do not do the implementation for the owner.
- Q-learning is not implemented in this phase; files are stubs.

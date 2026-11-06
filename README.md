# Vacuum Robot RL (CS440 Lab)

Model-free tabular Q-learning for a vacuum robot navigating a 4x4 gridworld with hidden transition ($T$) and reward ($R$) models.

```
[ Start (0,0),  (0,1),        (0,2),  (0,3)      ]
[ (1,0),        (1,1) [X Wall],(1,2), (1,3)      ]
[ (2,0),        (2,1),        (2,2),  (2,3)      ]
[ (3,0),        (3,1) [-1],   (3,2),  (3,3) [+10]]
```

---

## Assignment Objectives & Context Engineering

This lab demonstrates **Context Engineering Strategy 4 (Isolate)**:
1. **Model-Free Isolation Boundary:**
   The learning agent (`QLearningAgent`) interacts strictly via `env.reset()` and `env.step(action)` tuples `(s, a, r, s', done)`. It has no knowledge of internal grid representations, wall coordinates, or transition probabilities.
2. **Sub-agents (`.gemini/agents/`):**
   - [`env-designer`](.gemini/agents/env-designer.md): Encapsulates grid physics, boundaries, and hidden $T, R$ dynamics in [`src/vacuum_rl/environment.py`](src/vacuum_rl/environment.py).
   - [`q-learning-implementer`](.gemini/agents/q-learning-implementer.md): Manages policy calculation, $\epsilon$-greedy action selection, and Bellman TD updates in [`src/vacuum_rl/agent.py`](src/vacuum_rl/agent.py).
   - [`experiment-runner`](.gemini/agents/experiment-runner.md): Manages training sweeps, logging, and evaluation metrics in [`src/vacuum_rl/train.py`](src/vacuum_rl/train.py) and [`src/vacuum_rl/evaluate.py`](src/vacuum_rl/evaluate.py).
3. **Skills (`.gemini/skills/`):**
   - [`q-update-rule`](.gemini/skills/q-update-rule/SKILL.md): Standardized mathematical procedure for model-free Q-learning updates.
   - [`gridworld-spec`](.gemini/skills/gridworld-spec/SKILL.md): Gridworld dimensions, coordinates, and terminal specs.

---

## Hyperparameter Configuration

Configured per `GEMINI.md`:
- **Living Reward ($R_{\text{living}}$):** `-0.01` (incentivizes shorter paths)
- **Discount Factor ($\gamma$):** `0.9`
- **Learning Rate ($\alpha$):** `0.1`
- **Epsilon Initial ($\epsilon_0$):** `1.0` (starts with full exploration)
- **Epsilon Decay ($\lambda$):** `0.99` (multiplicative decay per episode)
- **Epsilon Minimum ($\epsilon_{\min}$):** `0.01`

---

## Repository Structure

```
├── GEMINI.md                    # Lab instructions & hyperparameter specifications
├── README.md                    # Project overview & running instructions
├── docs/DECISIONS.md            # Architectural decisions log
├── .gemini/
│   ├── agents/                  # Isolated sub-agent definitions
│   │   ├── env-designer.md
│   │   ├── q-learning-implementer.md
│   │   └── experiment-runner.md
│   └── skills/                  # Procedural skills
│       ├── q-update-rule/
│       └── gridworld-spec/
├── src/
│   ├── vacuum_env.py            # Primary runner script
│   └── vacuum_rl/
│       ├── environment.py       # Isolated Gridworld environment (reset, step)
│       ├── agent.py             # Model-free QLearningAgent
│       ├── exploration.py       # Epsilon-greedy action selection
│       ├── train.py             # Training loop
│       └── evaluate.py          # Greedy policy evaluation & visualizer
├── tests/
│   ├── test_environment.py     # Environment mechanics & boundary tests
│   ├── test_agent.py           # TD update math & action selection tests
│   └── test_boundary.py        # Strategy 4 isolation boundary tests
└── experiments/
    └── results/                 # JSON logs of training sweeps and trajectory traces
```

---

## Execution

### Run Training and Evaluation
```bash
python3 src/vacuum_env.py
```
This trains the agent for 1,000 episodes, outputs the learned policy grid, and prints the step-by-step greedy trajectory from $(0, 0)$ to $(3, 3)$.

### Run Unit Tests
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```
All 12 unit tests verify environment bounds, TD update calculations, and strict architectural isolation boundaries.

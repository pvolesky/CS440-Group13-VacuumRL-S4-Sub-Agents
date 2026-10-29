# Vacuum Robot RL

Model-free RL (Q-learning) for a vacuum robot on a 4x4 gridworld. The agent does NOT know T or R.
Grid and details: `.claude/skills/gridworld-spec/`. Open design choices: `docs/DECISIONS.md`.

## Hard rules
1. **Boundary:** agent code may only use what `reset()`/`step()` return. It must never import or read the environment's transition/reward internals.
2. **Current phase = scaffolding.** Do not write implementation code (environment dynamics, Q-learning, training loops) unless the user explicitly asks in that message. Default to explaining, reviewing, and planning.
3. **Never assume an open decision.** If `docs/DECISIONS.md` marks something Open, ask the user.
4. **Isolation:** delegate to the sub-agents in `.claude/agents/`; expect short summaries back, not raw file dumps.

## Layout
`src/vacuum_rl/` source stubs | `tests/` | `experiments/` configs and results | `docs/` | `.claude/` context engineering

## Delegation
- Environment / T,R boundary -> `env-designer`
- Agent, exploration -> `q-learning-implementer`
- Training, sweeps, seeds -> `experiment-runner`
- Review (read-only) -> `rl-reviewer`
- README / docs -> `docs-writer`

## Commands
`pytest` | `ruff check .`

A hook injects short task-relevant hints per prompt; skills hold longer procedures. Load a skill only when needed.

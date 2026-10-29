# Vacuum Robot RL

A Q-learning vacuum robot on a 4x4 gridworld where the agent does not know the transition model (T) or reward function (R):

```
[start, 0, 0,  0]
[0,     X, 0,  0]
[0,     0, 0,  0]
[0,    -1, 0, 10]
```

**Status: scaffold only.** The source and test files are docstring stubs. This repository's main purpose right now is *context engineering* for Claude Code, using **isolation via sub-agents** combined with three supporting mechanisms.

## Structure

```
vacuum-rl/
├── CLAUDE.md                     # Small, always-loaded rules (boundary, phase, delegation)
├── README.md
├── pyproject.toml                # Python >=3.11, numpy; dev: pytest, ruff
├── .gitignore
├── .claude/
│   ├── settings.json             # Registers the UserPromptSubmit hook (committed, project-wide)
│   ├── agents/                   # Isolated sub-agents, each with its own tools, model, and file ownership
│   │   ├── env-designer.md           # simulator + hidden T/R boundary
│   │   ├── q-learning-implementer.md # agent + exploration
│   │   ├── experiment-runner.md      # training, sweeps, seeds, logging
│   │   ├── rl-reviewer.md            # read-only correctness review
│   │   └── docs-writer.md            # README + docs
│   ├── hooks/
│   │   ├── context_router.sh     # Bash; reads prompt JSON, emits matching snippets
│   │   ├── routes.tsv            # regex -> snippet mapping (edit this to change routing)
│   │   └── snippets/*.md         # 1-2 line hints
│   └── skills/                   # Longer procedures, loaded on demand
│       ├── gridworld-spec/
│       ├── q-learning-procedure/     # process only, no solution code
│       ├── aima-rl-reference/        # AIMA concept map
│       ├── rl-debugging-checklist/
│       └── experiment-protocol/
├── src/vacuum_rl/                # Stubs: environment, agent, exploration, train, evaluate
├── tests/                        # Stubs: environment, agent, boundary
├── experiments/                  # Configs; results/ is git-ignored
└── docs/DECISIONS.md             # Open and resolved design decisions
```

## How the context-engineering pieces fit together

| Mechanism | Size | Loaded | Purpose |
|---|---|---|---|
| `CLAUDE.md` | tiny | Always | Non-negotiable rules and a delegation map |
| `UserPromptSubmit` hook | 1-3 short snippets | Per prompt, by keyword | Nudges Claude toward the right sub-agent/skill and flags Open decisions |
| Skills | long | On demand | Procedures, checklists, specs, AIMA pointers |
| Sub-agents | separate context windows | When delegated | **Isolation**: noisy work (searching files, running sweeps) stays out of the main conversation; only a short summary returns |

### Isolation design
- **File ownership:** each sub-agent owns specific files, listed in its definition.
- **Least privilege:** `rl-reviewer` is read-only (Read, Grep, Glob); `docs-writer` has no Bash.
- **Model per role:** reviewer on a stronger model, docs on a cheaper one, others on a mid-tier model.
- **Summary contract:** each sub-agent returns a short, bounded summary rather than file dumps.
- **Boundary:** the agent/environment separation (agent never sees T or R) is enforced by CLAUDE.md, by the `env-designer` and `q-learning-implementer` scopes, and by the planned `tests/test_boundary.py`.

### AIMA grounding
The task is described via PEAS (Ch. 2), modeled as a sequential decision problem (MDP chapter), and solved as model-free active RL (RL chapter) with attention to exploration vs. exploitation. See `.claude/skills/aima-rl-reference/`.

## Using the hook
- Requires Bash and `grep`; uses `jq` if installed, otherwise matches against the raw JSON.
- Test it manually: `echo '{"prompt":"tune epsilon decay"}' | .claude/hooks/context_router.sh`
- Cap on snippets per prompt: `VACUUM_RL_MAX_SNIPPETS` (default 3).
- Add routing: append a `regex<TAB>snippet.md` line to `routes.tsv` and create the snippet.

## Policy on implementation
Claude Code is configured to explain, review, and scaffold, and not to write the environment dynamics or Q-learning code unless explicitly asked (see `CLAUDE.md` rule 2 and decision D7). To change this, edit that rule.

## Setup
```
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest && ruff check .
```

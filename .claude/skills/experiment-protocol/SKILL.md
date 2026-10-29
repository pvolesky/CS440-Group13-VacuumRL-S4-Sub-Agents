---
name: experiment-protocol
description: Protocol for running, logging, and reporting RL experiments in this repo (seeds, configs, metrics, result locations). Load before running sweeps or comparing hyperparameters.
---
# Experiment protocol

1. **Config first:** every run has a config file in `experiments/` (hyperparameters, episode count, seed).
2. **Seeds:** at least 5 seeds per configuration; report mean and spread, never a single run.
3. **Record:** seed, config, git commit, and date with every result under `experiments/results/` (git-ignored).
4. **Metrics:** episodic return (smoothed), success rate of reaching the goal, penalty-cell visits, steps per episode, greedy-policy return.
5. **Evaluation:** greedy policy with exploration disabled, run separately from training.
6. **Comparison:** change one variable at a time; state it in the report.
7. **Reporting to the parent agent:** a compact table only. Do not paste raw logs into the conversation.

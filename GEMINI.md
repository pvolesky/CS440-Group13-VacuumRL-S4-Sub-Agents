# Vacuum Robot Reinforcement Learning Lab

## Assignment Objectives
- Implement model-free Q-learning for a vacuum robot where transition ($T$) and reward ($R$) models are initially unknown.
- Apply Context Engineering **Strategy 4 (Isolate)** via sub-agents.
- Utilize 3 required code features: **Sub-agents** and **Skills**.

## RL Hyperparameters Configuration
- **Living Reward ($R_{living}$):** `-0.01` (Encourages efficiency/shorter paths)
- **Discount Factor ($\gamma$):** `0.9` (Values future rewards highly)
- **Learning Rate ($\alpha$):** `0.1` (Controls weight given to new experiences)
- **Epsilon ($\epsilon$):** `0.1` (Exploration vs. exploitation rate for $\epsilon$-greedypolicy)
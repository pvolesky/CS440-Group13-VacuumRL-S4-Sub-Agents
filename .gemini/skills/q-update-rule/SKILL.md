---
name: q-update-rule
description: Standardized procedure for executing model-free Q-learning updates based on empirical rewards.
---

# Q-Learning Update Skill

When processing an experience tuple $(s, a, r, s')$, apply the Bellman-style model-free update equation:

$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]$$

## Mandatory Hyperparameters:
- **Learning Rate ($\alpha$):** `0.1`
- **Discount Factor ($\gamma$):** `0.9`
- **Living Reward ($R_{living}$):** `-0.01`
- **Epsilon ($\epsilon$):** `0.1`
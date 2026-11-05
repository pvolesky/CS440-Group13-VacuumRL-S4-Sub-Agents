"""Exploration strategy for Q-learning.

Owner: q-learning-implementer sub-agent.
"""

import random

def epsilon_greedy(q_values, actions, epsilon=0.1):
    """Select action using epsilon-greedy policy.

    Args:
        q_values: dict mapping action -> float Q-value for the current state.
        actions: list of available action strings.
        epsilon: exploration probability (0.0 to 1.0).

    Returns:
        Chosen action string.
    """
    if random.random() < epsilon:
        return random.choice(actions)
    return max(actions, key=lambda a: q_values.get(a, 0.0))

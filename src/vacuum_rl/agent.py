"""Q-learning agent.

Owner: q-learning-implementer sub-agent.
Responsibility: Learn action values purely from observed (state, action, reward, next_state)
experience tuples. Adheres to Strategy 4 (Isolate) by never accessing environment internals.
"""

from vacuum_rl.exploration import epsilon_greedy

class QLearningAgent:
    """Model-free tabular Q-learning agent."""

    def __init__(self, actions=None, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.actions = actions if actions is not None else ["UP", "DOWN", "LEFT", "RIGHT"]
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q_values(self, state):
        """Retrieve Q-values dictionary for a state, initializing to 0.0 if unseen."""
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in self.actions}
        return self.q_table[state]

    def select_action(self, state, greedy=False):
        """Select an action using epsilon-greedy policy (or purely greedy when greedy=True)."""
        eps = 0.0 if greedy else self.epsilon
        q_vals = self.get_q_values(state)
        return epsilon_greedy(q_vals, self.actions, epsilon=eps)

    def update(self, state, action, reward, next_state, done):
        """Update Q-value for experience tuple (s, a, r, s') using Bellman TD update rule.

        Equation:
            Q(s, a) <- Q(s, a) + alpha * [r + gamma * max_a'(Q(s', a')) - Q(s, a)]
        """
        q_s = self.get_q_values(state)
        current_q = q_s[action]

        max_next_q = 0.0
        if not done:
            next_q_vals = self.get_q_values(next_state)
            max_next_q = max(next_q_vals.values())

        # Target value
        td_target = reward + self.gamma * max_next_q
        td_error = td_target - current_q

        # Q-update
        q_s[action] = current_q + self.alpha * td_error
        return q_s[action]

    def get_best_action(self, state):
        """Return the greedy action with highest Q-value for given state."""
        q_vals = self.get_q_values(state)
        return max(self.actions, key=lambda a: q_vals[a])

"""Gridworld simulator for the vacuum robot.

Owner: env-designer sub-agent.
Responsibility: hold the hidden transition model T and reward function R and expose only
reset() and step() to the outside world, adhering to Strategy 4 (Isolate).
"""

class VacuumEnvironment:
    """4x4 Discrete Gridworld simulator for the vacuum robot."""

    def __init__(self, living_reward=-0.01):
        self.rows = 4
        self.cols = 4
        self.living_reward = living_reward
        self.start_pos = (0, 0)
        self.agent_pos = self.start_pos
        self.obstacle = (1, 1)
        self.penalty_pos = (3, 1)
        self.goal_pos = (3, 3)
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT"]

    def reset(self):
        """Reset environment to initial state."""
        self.agent_pos = self.start_pos
        return self.agent_pos

    def step(self, action):
        """Execute action and return (observation, reward, done).

        Transition model T and reward model R are encapsulated here.
        """
        r, c = self.agent_pos
        new_r, new_c = r, c

        if action == "UP":
            new_r = max(0, r - 1)
        elif action == "DOWN":
            new_r = min(self.rows - 1, r + 1)
        elif action == "LEFT":
            new_c = max(0, c - 1)
        elif action == "RIGHT":
            new_c = min(self.cols - 1, c + 1)

        # Check collision with obstacle: bump causes robot to stay in place
        if (new_r, new_c) == self.obstacle:
            new_r, new_c = r, c

        self.agent_pos = (new_r, new_c)

        # Reward structure: living reward plus terminal bonus/penalty
        reward = self.living_reward
        done = False

        if self.agent_pos == self.goal_pos:
            reward += 10.0
            done = True
        elif self.agent_pos == self.penalty_pos:
            reward += -1.0
            done = True

        return self.agent_pos, reward, done

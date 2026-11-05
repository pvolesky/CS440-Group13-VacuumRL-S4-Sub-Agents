"""Boundary verification tests for Strategy 4 (Isolate).

Ensures that QLearningAgent never accesses or stores environment internals
(grid maps, obstacle coordinates, or transition/reward probability tables).
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from vacuum_rl.environment import VacuumEnvironment
from vacuum_rl.agent import QLearningAgent

class TestStrategy4Boundary(unittest.TestCase):
    def test_agent_has_no_environment_internals(self):
        agent = QLearningAgent()

        # Forbidden attributes that would break model-free isolation
        forbidden_attributes = [
            "grid", "cleaned_grid", "obstacle", "obstacles",
            "penalty_pos", "goal_pos", "transition_model", "reward_model",
            "T", "R"
        ]

        for attr in forbidden_attributes:
            self.assertFalse(
                hasattr(agent, attr),
                f"Agent violates Strategy 4 boundary by containing '{attr}'"
            )

    def test_interaction_strictly_via_reset_and_step(self):
        env = VacuumEnvironment()
        agent = QLearningAgent()

        # Step 1: Agent receives state strictly as a return value of reset()
        state = env.reset()
        self.assertIsInstance(state, tuple)

        # Step 2: Agent selects action strictly from state observation
        action = agent.select_action(state)
        self.assertIn(action, agent.actions)

        # Step 3: Agent interacts with environment strictly via step()
        next_state, reward, done = env.step(action)
        self.assertIsInstance(next_state, tuple)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(done, bool)

        # Step 4: Agent updates value function purely from experience tuple
        agent.update(state, action, reward, next_state, done)
        self.assertIn(state, agent.q_table)

if __name__ == "__main__":
    unittest.main()

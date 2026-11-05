"""Unit tests for VacuumEnvironment."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from vacuum_rl.environment import VacuumEnvironment

class TestVacuumEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = VacuumEnvironment(living_reward=-0.01)

    def test_reset(self):
        start_state = self.env.reset()
        self.assertEqual(start_state, (0, 0))
        self.assertEqual(self.env.agent_pos, (0, 0))

    def test_boundaries(self):
        self.env.reset()
        next_state, reward, done = self.env.step("UP")
        self.assertEqual(next_state, (0, 0))
        self.assertEqual(reward, -0.01)
        self.assertFalse(done)

        next_state, reward, done = self.env.step("LEFT")
        self.assertEqual(next_state, (0, 0))
        self.assertEqual(reward, -0.01)
        self.assertFalse(done)

    def test_obstacle_collision(self):
        self.env.reset()
        # Move to (0, 1)
        self.env.step("RIGHT")
        self.assertEqual(self.env.agent_pos, (0, 1))

        # Attempt to move DOWN into obstacle (1, 1)
        next_state, reward, done = self.env.step("DOWN")
        # Agent should bump and remain at (0, 1)
        self.assertEqual(next_state, (0, 1))
        self.assertEqual(reward, -0.01)
        self.assertFalse(done)

    def test_goal_terminal(self):
        self.env.reset()
        self.env.agent_pos = (2, 3)
        next_state, reward, done = self.env.step("DOWN")
        self.assertEqual(next_state, (3, 3))
        self.assertAlmostEqual(reward, 9.99, places=3)
        self.assertTrue(done)

    def test_penalty_terminal(self):
        self.env.reset()
        self.env.agent_pos = (2, 1)
        next_state, reward, done = self.env.step("DOWN")
        self.assertEqual(next_state, (3, 1))
        self.assertAlmostEqual(reward, -1.01, places=3)
        self.assertTrue(done)

if __name__ == "__main__":
    unittest.main()

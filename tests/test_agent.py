"""Unit tests for QLearningAgent."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from vacuum_rl.agent import QLearningAgent

class TestQLearningAgent(unittest.TestCase):
    def setUp(self):
        self.agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.99)

    def test_init_hyperparameters(self):
        self.assertEqual(self.agent.alpha, 0.1)
        self.assertEqual(self.agent.gamma, 0.9)
        self.assertEqual(self.agent.epsilon, 1.0)
        self.assertEqual(self.agent.epsilon_decay, 0.99)
        self.assertEqual(self.agent.actions, ["UP", "DOWN", "LEFT", "RIGHT"])

    def test_epsilon_decay(self):
        self.assertEqual(self.agent.epsilon, 1.0)
        self.agent.decay_epsilon()
        self.assertAlmostEqual(self.agent.epsilon, 0.99, places=4)
        for _ in range(600):
            self.agent.decay_epsilon()
        self.assertGreaterEqual(self.agent.epsilon, 0.01)

    def test_unseen_state_initialization(self):
        q_vals = self.agent.get_q_values((0, 0))
        self.assertEqual(q_vals, {"UP": 0.0, "DOWN": 0.0, "LEFT": 0.0, "RIGHT": 0.0})

    def test_q_update_terminal(self):
        # Initial Q = 0.0, terminal transition with reward +10.0
        # Q(s, a) <- 0.0 + 0.1 * [10.0 + 0.9 * 0.0 - 0.0] = 1.0
        new_q = self.agent.update(
            state=(2, 3),
            action="DOWN",
            reward=10.0,
            next_state=(3, 3),
            done=True
        )
        self.assertAlmostEqual(new_q, 1.0, places=4)
        self.assertAlmostEqual(self.agent.get_q_values((2, 3))["DOWN"], 1.0, places=4)

    def test_q_update_non_terminal(self):
        # Set next_state max Q
        self.agent.get_q_values((1, 2))["RIGHT"] = 5.0
        # Transition: state (0, 2) -> next_state (1, 2), reward -0.01
        # Target = -0.01 + 0.9 * 5.0 = 4.49
        # Q <- 0.0 + 0.1 * (4.49 - 0.0) = 0.449
        new_q = self.agent.update(
            state=(0, 2),
            action="DOWN",
            reward=-0.01,
            next_state=(1, 2),
            done=False
        )
        self.assertAlmostEqual(new_q, 0.449, places=4)

    def test_greedy_action_selection(self):
        self.agent.get_q_values((0, 0))["RIGHT"] = 2.5
        self.agent.get_q_values((0, 0))["DOWN"] = 1.2
        selected = self.agent.select_action((0, 0), greedy=True)
        self.assertEqual(selected, "RIGHT")

if __name__ == "__main__":
    unittest.main()

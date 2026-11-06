"""Vacuum robot reinforcement learning runner.

Entrypoint for running the isolated environment and Q-learning agent with decaying epsilon.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from vacuum_rl.environment import VacuumEnvironment
from vacuum_rl.agent import QLearningAgent
from vacuum_rl.train import train_agent
from vacuum_rl.evaluate import evaluate_agent, print_policy_grid, print_q_table

def run_simulation(episodes=1000):
    """Run full training, output Q-table, display policy grid, and evaluate greedy trace."""
    print("=" * 82)
    print("         VACUUM ROBOT REINFORCEMENT LEARNING LAB (Q-LEARNING)")
    print("=" * 82)
    print(" Hyperparameters:")
    print("   - Living Reward:   -0.01")
    print("   - Epsilon Initial: 1.0 (decay: 0.99, min: 0.01)")
    print("   - Learning Rate:   0.1")
    print("   - Discount Factor: 0.9")
    print("=" * 82)

    # Initialize environment and agent with requested hyperparameters
    env = VacuumEnvironment(living_reward=-0.01)
    agent = QLearningAgent(
        alpha=0.1,              # learning rate = 0.1
        gamma=0.9,              # discount factor = 0.9
        epsilon=1.0,            # epsilon initial = 1.0
        epsilon_decay=0.99,     # epsilon decay = 0.99
        epsilon_min=0.01
    )

    # 1. Train agent
    train_agent(env, agent, episodes=episodes)

    # 2. Output full learned Q-table
    print_q_table(agent)

    # 3. Display learned greedy policy grid
    print_policy_grid(agent)

    # 4. Evaluate greedy policy step-by-step
    evaluate_agent(env, agent)

    return env, agent

if __name__ == "__main__":
    run_simulation()

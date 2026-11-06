"""Vacuum robot reinforcement learning runner.

Entrypoint for running the isolated environment and Q-learning agent with decaying epsilon.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from vacuum_rl.environment import VacuumEnvironment
from vacuum_rl.agent import QLearningAgent
from vacuum_rl.train import train_agent
from vacuum_rl.evaluate import evaluate_agent, print_policy_grid

def main():
    # Initialize environment and agent with requested hyperparameters
    env = VacuumEnvironment(living_reward=-0.01)
    agent = QLearningAgent(
        alpha=0.1,              # learning rate = 0.1
        gamma=0.9,              # discount factor = 0.9
        epsilon=1.0,            # epsilon initial = 1.0
        epsilon_decay=0.99,     # epsilon decay = 0.99
        epsilon_min=0.01
    )

    # Train
    train_agent(env, agent, episodes=1000)

    # Display learned greedy policy
    print_policy_grid(agent)

    # Evaluate greedy policy step-by-step
    evaluate_agent(env, agent)

if __name__ == "__main__":
    main()

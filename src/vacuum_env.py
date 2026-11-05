"""Vacuum robot reinforcement learning runner.

Entrypoint for running the isolated environment and Q-learning agent.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from vacuum_rl.environment import VacuumEnvironment
from vacuum_rl.agent import QLearningAgent
from vacuum_rl.train import train_agent
from vacuum_rl.evaluate import evaluate_agent, print_policy_grid

def main():
    # Initialize isolated environment and agent with required hyperparameters
    env = VacuumEnvironment(living_reward=-0.01)
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.1)

    # Train
    train_agent(env, agent, episodes=1000)

    # Display policy
    print_policy_grid(agent)

    # Evaluate greedy policy step-by-step
    evaluate_agent(env, agent)

if __name__ == "__main__":
    main()

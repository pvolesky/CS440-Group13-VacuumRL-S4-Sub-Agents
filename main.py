"""Main entry point for Vacuum Robot Reinforcement Learning.

Run this file directly (e.g. click 'Play' in your IDE or run `python3 main.py`)
to train the agent, display the full Q-table, visualize the policy grid,
and trace the optimal step-by-step evaluation path.
"""

import sys
import os

# Add src directory to search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from vacuum_env import run_simulation

if __name__ == "__main__":
    run_simulation(episodes=1000)

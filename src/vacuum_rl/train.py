"""Training loop / episode runner.

Owner: experiment-runner sub-agent.
Responsibility: Connect the isolated environment and agent via the reset/step boundary.
"""

def train_agent(env, agent, episodes=1000, max_steps_per_episode=200, verbose=True):
    """Train Q-learning agent on the environment.

    Args:
        env: VacuumEnvironment instance exposing reset() and step().
        agent: QLearningAgent instance exposing select_action(), update(), and decay_epsilon().
        episodes: Number of training episodes.
        max_steps_per_episode: Safety step cap per episode.
        verbose: Whether to print progress summary.

    Returns:
        List of dicts containing per-episode metrics.
    """
    if verbose:
        print(f"Starting Q-learning training for {episodes} episodes...")

    history = []
    total_steps = 0

    for ep in range(episodes):
        state = env.reset()
        done = False
        ep_reward = 0.0
        steps = 0

        while not done and steps < max_steps_per_episode:
            action = agent.select_action(state, greedy=False)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state, done)

            ep_reward += reward
            steps += 1
            total_steps += 1
            state = next_state

        # Epsilon decay schedule per episode
        if hasattr(agent, "decay_epsilon"):
            agent.decay_epsilon()

        history.append({
            "episode": ep + 1,
            "steps": steps,
            "reward": ep_reward,
            "epsilon": getattr(agent, "epsilon", None),
            "reached_goal": (state == getattr(env, "goal_pos", (3, 3)))
        })

    if verbose:
        final_eps = getattr(agent, 'epsilon', 0.0)
        print(f"Training completed successfully in {total_steps} total steps. Final epsilon: {final_eps:.4f}")

    return history

"""Evaluation of learned policies.

Owner: experiment-runner sub-agent.
"""

def evaluate_agent(env, agent, max_steps=20, verbose=True):
    """Execute greedy policy and trace step-by-step performance.

    Returns:
        tuple (step_log, total_return, goal_reached)
    """
    state = env.reset()
    done = False
    total_reward = 0.0
    step_log = []

    if verbose:
        print("\n--- Step-by-Step Greedy Policy Evaluation ---")
        print(f"Initial State: {state}")

    for step_num in range(1, max_steps + 1):
        action = agent.select_action(state, greedy=True)
        next_state, reward, done = env.step(action)
        total_reward += reward

        record = {
            "step": step_num,
            "state": state,
            "action": action,
            "next_state": next_state,
            "reward": reward,
            "cumulative_reward": total_reward,
            "done": done
        }
        step_log.append(record)

        if verbose:
            print(f"Step {step_num}: State={state} -> Action={action:<5} -> NextState={next_state} | Reward={reward:+.2f} | CumReward={total_reward:+.2f} | Done={done}")

        state = next_state
        if done:
            break

    goal_reached = (state == getattr(env, "goal_pos", (3, 3)))
    if verbose:
        status = "Goal reached" if goal_reached else "Terminated"
        print(f"{status} in {len(step_log)} steps with total return: {total_reward:.2f}")

    return step_log, total_reward, goal_reached


def print_policy_grid(agent, rows=4, cols=4, obstacle=(1, 1), penalty=(3, 1), goal=(3, 3)):
    """Print 2D grid visual of the greedy policy."""
    print("\nLearned Policy Actions:")
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            pos = (r, c)
            if pos == obstacle:
                row_str += " [ X ] "
            elif pos == goal:
                row_str += " [ G ] "
            elif pos == penalty:
                row_str += " [ -1] "
            else:
                best_action = agent.get_best_action(pos)
                row_str += f" [{best_action[0]}] "
        print(row_str)

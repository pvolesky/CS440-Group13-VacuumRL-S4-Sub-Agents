"""Evaluation of learned policies and Q-table visualization.

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
        print("\n" + "=" * 78)
        print("                 STEP-BY-STEP GREEDY POLICY EVALUATION")
        print("=" * 78)
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
    print("\n" + "=" * 78)
    print("                         LEARNED POLICY GRID")
    print("=" * 78)
    for r in range(rows):
        row_str = "  "
        for c in range(cols):
            pos = (r, c)
            if pos == obstacle:
                row_str += " [  X  ] "
            elif pos == goal:
                row_str += " [  G  ] "
            elif pos == penalty:
                row_str += " [ -1  ] "
            else:
                best_action = agent.get_best_action(pos)
                row_str += f" [ {best_action[0]}   ] "
        print(row_str)
    print("  Legend: [R]=Right, [D]=Down, [U]=Up, [L]=Left, [X]=Obstacle, [G]=Goal (+10), [-1]=Penalty")


def print_q_table(agent, rows=4, cols=4, obstacle=(1, 1), penalty=(3, 1), goal=(3, 3)):
    """Print a clean, formatted tabular breakdown of all Q-values across states."""
    print("\n" + "=" * 82)
    print("                                LEARNED Q-TABLE")
    print("=" * 82)
    print(f" {'State (r,c)':<13} | {'UP':>9} | {'DOWN':>9} | {'LEFT':>9} | {'RIGHT':>9} | {'Best':<5} | {'Max Q':>8}")
    print("-" * 82)

    for r in range(rows):
        for c in range(cols):
            state = (r, c)
            label = f"({r}, {c})"
            if state == obstacle:
                label += " [X]"
                print(f" {label:<13} | {'--':>9} | {'--':>9} | {'--':>9} | {'--':>9} | {'N/A':<5} | {'--':>8}")
                continue
            elif state == goal:
                label += " [G]"
            elif state == penalty:
                label += " [-1]"
            elif state == (0, 0):
                label += " [Start]"

            q_vals = agent.get_q_values(state)
            up_s = f"{q_vals.get('UP', 0.0):.4f}"
            down_s = f"{q_vals.get('DOWN', 0.0):.4f}"
            left_s = f"{q_vals.get('LEFT', 0.0):.4f}"
            right_s = f"{q_vals.get('RIGHT', 0.0):.4f}"

            best_a = agent.get_best_action(state)
            max_q_s = f"{q_vals.get(best_a, 0.0):.4f}"

            print(f" {label:<13} | {up_s:>9} | {down_s:>9} | {left_s:>9} | {right_s:>9} | {best_a:<5} | {max_q_s:>8}")
    print("=" * 82)

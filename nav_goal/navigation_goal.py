# navigation_goal.py

import numpy as np

def move_to_goal(current_position, goal_position, step_size=0.5):
    """
    Move the robot towards the goal using a simple step-based approach.
    """
    direction = np.array(goal_position) - np.array(current_position)
    direction_norm = direction / np.linalg.norm(direction)
    new_position = np.array(current_position) + direction_norm * step_size
    return new_position

if __name__ == "__main__":
    current = [2, 3]
    goal = [10, 10]
    new_pos = move_to_goal(current, goal)
    print("New Position:", new_pos)

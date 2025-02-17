# goal_navigation.py

import numpy as np

def navigate_to_goal(current_position, goal_position, speed=1.0):
    """
    Move towards the goal using simple proportional control.
    """
    direction = np.array(goal_position) - np.array(current_position)
    direction_norm = direction / np.linalg.norm(direction)
    new_position = np.array(current_position) + direction_norm * speed
    return new_position

if __name__ == "__main__":
    current_pos = [0, 0]
    goal_pos = [10, 10]
    new_pos = navigate_to_goal(current_pos, goal_pos)
    print("New Position:", new_pos)

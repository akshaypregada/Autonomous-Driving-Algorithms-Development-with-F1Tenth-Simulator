# pure_pursuit.py

import numpy as np

def pure_pursuit(target, current, lookahead_distance):
    """
    Implements the Pure Pursuit algorithm for path tracking.
    """
    direction = np.array(target) - np.array(current)
    direction = direction / np.linalg.norm(direction)
    pursuit_point = np.array(current) + direction * lookahead_distance
    return pursuit_point

if __name__ == "__main__":
    current_position = [2, 2]
    target_position = [10, 10]
    lookahead = 3.0
    next_point = pure_pursuit(target_position, current_position, lookahead)
    print("Next Pursuit Point:", next_point)

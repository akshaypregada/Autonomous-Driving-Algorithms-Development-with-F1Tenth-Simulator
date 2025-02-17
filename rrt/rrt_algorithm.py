# rrt_algorithm.py

import numpy as np

def rrt_planning(start, goal, obstacles):
    """
    Basic Rapidly-exploring Random Tree (RRT) path planning.
    """
    path = [start]
    while np.linalg.norm(np.array(path[-1]) - np.array(goal)) > 1.0:
        new_point = path[-1] + np.random.uniform(-1, 1, size=2)
        if not any(np.linalg.norm(new_point - obs) < 1.0 for obs in obstacles):
            path.append(new_point)
    path.append(goal)
    return path

if __name__ == "__main__":
    start_pos = [0, 0]
    goal_pos = [10, 10]
    obstacles_list = [[5, 5], [6, 6]]
    planned_path = rrt_planning(start_pos, goal_pos, obstacles_list)
    print("Planned Path:", planned_path)

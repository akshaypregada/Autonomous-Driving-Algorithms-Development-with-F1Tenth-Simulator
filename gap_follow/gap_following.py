# gap_following.py

import numpy as np

def find_gap(lidar_scan):
    """
    Identify the largest gap in LiDAR scan data.
    """
    gaps = np.where(lidar_scan > 1.0)[0]
    if len(gaps) == 0:
        return None
    return gaps[np.argmax(np.diff(gaps))]

if __name__ == "__main__":
    lidar_sample = np.random.uniform(0, 2, 100)
    best_gap = find_gap(lidar_sample)
    print("Best Gap Index:", best_gap)

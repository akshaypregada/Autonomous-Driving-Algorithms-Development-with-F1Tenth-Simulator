# lidar_processing.py

import numpy as np

def process_lidar_data(lidar_points):
    """
    Process LiDAR point cloud data.
    """
    filtered_points = [point for point in lidar_points if point[2] > 0]
    return np.array(filtered_points)

if __name__ == "__main__":
    sample_data = np.random.rand(100, 3) * 10
    processed_data = process_lidar_data(sample_data)
    print("Processed LiDAR Data:", processed_data)

# slam.py

import numpy as np

def slam_update(map_data, sensor_readings, motion_model):
    """
    Perform SLAM update with sensor readings and motion model.
    """
    updated_map = map_data + sensor_readings - motion_model
    return np.clip(updated_map, 0, 1)

if __name__ == "__main__":
    map_data = np.zeros((10, 10))
    sensor_readings = np.random.rand(10, 10) * 0.5
    motion_model = np.random.rand(10, 10) * 0.2
    updated_map = slam_update(map_data, sensor_readings, motion_model)
    print("Updated Map:")
    print(updated_map)

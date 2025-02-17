# sensor_fusion.py

import numpy as np

def fuse_sensors(lidar_data, imu_data):
    """
    Fuse LiDAR and IMU sensor data.
    """
    fused_data = (lidar_data + imu_data) / 2
    return fused_data

if __name__ == "__main__":
    lidar_sample = np.random.rand(10, 3)
    imu_sample = np.random.rand(10, 3)
    fused_output = fuse_sensors(lidar_sample, imu_sample)
    print("Fused Sensor Data:", fused_output)

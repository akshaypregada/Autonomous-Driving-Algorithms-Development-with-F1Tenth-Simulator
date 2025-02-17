# occupancy_grid.py

import numpy as np

def generate_occupancy_grid(sensor_data, grid_size=(10, 10)):
    """
    Generate an occupancy grid from sensor readings.
    """
    grid = np.zeros(grid_size)
    for x, y in sensor_data:
        if 0 <= x < grid_size[0] and 0 <= y < grid_size[1]:
            grid[int(x)][int(y)] = 1
    return grid

if __name__ == "__main__":
    sensor_sample = np.random.randint(0, 10, (15, 2))
    occupancy_grid = generate_occupancy_grid(sensor_sample)
    print("Occupancy Grid:")
    print(occupancy_grid)

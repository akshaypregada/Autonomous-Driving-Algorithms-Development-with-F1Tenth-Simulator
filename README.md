# Autonomous Driving Algorithms Development with F1Tenth Simulator

## Project Overview
This project focuses on developing and simulating autonomous driving algorithms for vehicle navigation and obstacle avoidance in a racing environment using the F1Tenth simulator.

## Skills & Tools Used
- **Programming:** Python
- **Robotics Framework:** ROS
- **Perception:** LiDAR Processing, OpenCV
- **Machine Learning:** Pytorch, TensorFlow
- **Control Systems:** PID Control, Pure Pursuit
- **Path Planning:** RRT/RRT*, A*
- **Localization:** Bayesian Estimation, Particle Filters

## Key Features
- Designed and implemented autonomous driving algorithms such as:
  - **Bicycle Kinematics** for motion modeling
  - **PID Control, Pure Pursuit** for trajectory following
  - **RRT/RRT*, A*** for global path planning
- Advanced obstacle avoidance using **LiDAR-based gap-following methods (Bug Algorithm, VFH+)**
- **Sensor Fusion:** Integrated stereo visual odometry, LiDAR & IMU using RANSAC for accurate localization
- Developed **local occupancy grids** and applied probabilistic localization techniques for dynamic environments
- Integrated **machine learning-based obstacle detection** to enhance real-time navigation
- Secured **2nd place** in the F1Tenth Grand Prix virtual race

## Repository Structure
```
.
├── src
│   ├── perception
│   │   ├── lidar_processing.py
│   │   ├── object_detection.py
│   │   └── sensor_fusion.py
│   ├── planning
│   │   ├── path_planning_rrt.py
│   │   ├── path_planning_a_star.py
│   │   ├── gap_following.py
│   │   └── local_occupancy_grid.py
│   ├── control
│   │   ├── pid_control.py
│   │   ├── pure_pursuit.py
│   │   └── motion_model.py
│   ├── localization
│   │   ├── bayesian_estimation.py
│   │   ├── particle_filter.py
│   │   └── slam.py
│   ├── svo
│   │   ├── svo_algorithm.py
│   ├── turtlesim
│   │   ├── turtlesim_control.py
│   ├── graph_planning
│   │   ├── graph_planning.py
│   ├── point_cloud_depth
│   │   ├── depth_estimation.py
│   ├── goto_goal
│   │   ├── goal_navigation.py
│   ├── ros_basics
│   │   ├── ros_basics.py
│   ├── gap_follow
│   │   ├── gap_following.py
│   ├── nav_goal
│   │   ├── navigation_goal.py
│   ├── detect_align
│   │   ├── object_alignment.py
│   ├── bayesian_estimation
│   │   ├── bayesian_filter.py
│   ├── bicycle_kinematics
│   │   ├── kinematics_model.py
│   ├── rrt
│   │   ├── rrt_algorithm.py
│   ├── local_occupancy
│   │   ├── occupancy_grid.py
│   ├── particle_filter
│   │   ├── particle_filter_localization.py
│   └── main.py
├── README.md
├── requirements.txt
└── LICENSE
```

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/ub-cse4568-sp24/f1tenth_autonomous.git
   ```
2. Navigate to the project folder:
   ```sh
   cd f1tenth_autonomous
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the simulation:
   ```sh
   python src/main.py
   ```

## References
- [F1Tenth Simulator](https://f1tenth.org/)
- [ROS (Robot Operating System)](https://www.ros.org/)

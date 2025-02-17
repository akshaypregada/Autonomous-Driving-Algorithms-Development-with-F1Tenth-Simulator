# main.py

from nav_goal.navigation_goal import move_to_goal
from detect_align.object_alignment import align_object
from bayesian_estimation.bayesian_filter import bayesian_update
from bicycle_kinematics.kinematics_model import bicycle_kinematics
from rrt.rrt_algorithm import rrt_planning
from local_occupancy.occupancy_grid import generate_occupancy_grid
from particle_filter.particle_filter_localization import particle_filter_update

if __name__ == "__main__":
    # Navigation Goal
    print("Navigation Goal:")
    new_pos = move_to_goal([2, 3], [10, 10])
    print(new_pos)

    # Object Alignment
    print("\nObject Alignment:")
    aligned = align_object([5, 5], [10, 10])
    print(aligned)

    # Bayesian Filter Update
    print("\nBayesian Filter:")
    updated_posterior = bayesian_update([0.2, 0.5, 0.3], [0.8, 0.6, 0.4])
    print(updated_posterior)

    # Bicycle Kinematics Model
    print("\nBicycle Kinematics:")
    new_state = bicycle_kinematics([0, 0, 0], [1.0, 0.1], 0.1)
    print(new_state)

    # RRT Planning
    print("\nRRT Path Planning:")
    planned_path = rrt_planning([0, 0], [10, 10], [[5, 5], [6, 6]])
    print(planned_path)

    # Occupancy Grid
    print("\nOccupancy Grid:")
    occupancy_grid = generate_occupancy_grid([[2, 3], [5, 6], [7, 8]])
    print(occupancy_grid)

    # Particle Filter
    print("\nParticle Filter Update:")
    updated_particles, updated_weights = particle_filter_update([[2, 3], [5, 6]], [0.5, 0.5], [0.1, 0.1], 0.05)
    print(updated_particles)

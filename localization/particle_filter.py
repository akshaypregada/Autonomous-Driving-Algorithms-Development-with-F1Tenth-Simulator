# particle_filter.py

import numpy as np

def particle_filter_update(particles, weights, motion, noise):
    """
    Updates the particles based on motion model and reweights.
    """
    particles += motion + np.random.normal(0, noise, particles.shape)
    weights /= np.sum(weights)
    
    return particles, weights

if __name__ == "__main__":
    num_particles = 1000
    particles = np.random.rand(num_particles, 2) * 10
    weights = np.ones(num_particles) / num_particles
    motion = np.array([0.5, 0.5])
    noise = 0.1
    updated_particles, updated_weights = particle_filter_update(particles, weights, motion, noise)
    print("Updated Particles:", updated_particles)

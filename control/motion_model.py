# motion_model.py

import numpy as np

def bicycle_model(state, control, dt):
    """
    Implements a simple bicycle motion model.
    """
    x, y, theta = state
    v, delta = control
    L = 2.0  # Wheelbase length
    
    x_new = x + v * np.cos(theta) * dt
    y_new = y + v * np.sin(theta) * dt
    theta_new = theta + (v / L) * np.tan(delta) * dt
    
    return np.array([x_new, y_new, theta_new])

if __name__ == "__main__":
    state = np.array([0, 0, 0])
    control = np.array([1.0, 0.1])
    dt = 0.1
    new_state = bicycle_model(state, control, dt)
    print("New State:", new_state)

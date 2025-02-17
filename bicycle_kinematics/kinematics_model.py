# kinematics_model.py

import numpy as np

def bicycle_kinematics(state, control, dt):
    """
    Bicycle model kinematics.
    """
    x, y, theta = state
    v, delta = control
    L = 2.0  # Wheelbase length
    
    x_new = x + v * np.cos(theta) * dt
    y_new = y + v * np.sin(theta) * dt
    theta_new = theta + (v / L) * np.tan(delta) * dt
    
    return np.array([x_new, y_new, theta_new])

if __name__ == "__main__":
    state = [0, 0, 0]
    control = [1.0, 0.1]
    new_state = bicycle_kinematics(state, control, 0.1)
    print("New State:", new_state)

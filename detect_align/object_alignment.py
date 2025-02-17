# object_alignment.py

import numpy as np

def align_object(detected_position, target_position):
    """
    Adjust object position to align with the target.
    """
    correction = np.array(target_position) - np.array(detected_position)
    aligned_position = np.array(detected_position) + correction * 0.5
    return aligned_position

if __name__ == "__main__":
    detected = [5, 5]
    target = [10, 10]
    aligned = align_object(detected, target)
    print("Aligned Position:", aligned)

# object_detection.py

import cv2
import numpy as np

def detect_objects(image):
    """
    Perform basic object detection using edge detection.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return edges

if __name__ == "__main__":
    sample_image = np.zeros((500, 500, 3), dtype=np.uint8)
    detected_edges = detect_objects(sample_image)
    cv2.imshow("Detected Edges", detected_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

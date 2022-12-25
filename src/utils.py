
import numpy as np

def get4corners(center, size):
    left = center + np.array([0, -size])
    right = center + np.array([0, size])
    up = center + np.array([ -size, 0 ])
    down = center + np.array([size, 0])

    return np.array([right, up, left, down])

import numpy as np

def get4corners(center, size):
    left = center + np.array([0, -size])
    right = center + np.array([0, size])
    up = center + np.array([ -size, 0 ])
    down = center + np.array([size, 0])

    return np.array([right, up, left, down])

def neighboors(matrix, x,y, range=1):
    return matrix[x-range:x+range+1, y-range:y+range+1]

def neighbors_present(matrix, center):
    if matrix[center[0], center[1]]:
        submatrix = neighboors(matrix, *center)
        right = submatrix[1,2]
        up = submatrix[0,1]
        left = submatrix[1,0]
        down = submatrix[2,1]
        return np.array([right, up, left, down])    
    else:
        return np.zeros(4)
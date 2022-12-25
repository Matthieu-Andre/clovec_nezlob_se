
import numpy as np

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

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


def cell_centers(cell_map, used_cells):
    used_cells_centers = [] 
    for cell, mask in zip(cell_map, used_cells):
        if mask:
            used_cells_centers.append(cell)
    return np.array(used_cells_centers)


def xy(point):
    return point[0],point[1]


def map2path(map_mask, start):

    map_mask = np.pad(map_mask, 1)
    print(map_mask)
    path_list = [] 
    current = start + np.array([1,1])
    neigh = neighbors_present(map_mask, start )
    print(map_mask[xy(current)])
    while neigh.sum() > 0:
        path_list.append(current)
        map_mask[xy(current)] = 0
        if neigh[RIGHT]:
            current = start + np.array([1,0])
        elif neigh[UP]:
            current = start + np.array([0,-1])
        elif neigh[LEFT]:
            current = start + np.array([-1,0])
        elif neigh[DOWN]:
            current = start + np.array([0,1])
        
        neigh = neighbors_present(map_mask, current)
        print(neigh)

    return np.array(path_list) - 1
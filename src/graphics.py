import pygame
import numpy as np
from utils import get4corners, neighbors_present

def drawGrid(screen, window_width, window_height, color, blockSize, offset):
     #Set the size of the grid block
    for x in range(offset, window_width - 2 * offset, blockSize):
        for y in range(offset, window_height - 2 * offset, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 1)

def draw_playing_circle(screen, center, size, color, border_size):
    pygame.draw.circle(screen, (0, 0, 0), center, size + border_size, border_size)
    pygame.draw.circle(screen, color, center, size )


def get_grid(dimension, size, offset):
    axis_vals = [offset + x * size for x in range(dimension) ]
    xv, yv = np.meshgrid(axis_vals, axis_vals)
    xv = xv.reshape(dimension,dimension,1)
    yv = yv.reshape(dimension,dimension,1)

    centers = np.concatenate((xv, yv), axis=2)
    return centers.reshape((dimension**2, 2))


def get_map_mask(dimensions):
    map_mask = np.zeros((dimensions,dimensions))

    length = dimensions//2
    map_mask[length-1, 0:length] = 1
    map_mask[0:length, length-1] = 1
    map_mask[length, 0] = 1
    map_mask[0, length] = 1

    map_mask = map_mask +np.flip(map_mask, axis=0)
    map_mask = map_mask +np.flip(map_mask, axis=1)

    map_mask[map_mask > 1 ] = 1

    return map_mask


def get_connection_coords(centers, cells_radius, cell_size):
    start_segments = []
    end_segments = []
    
    dimensions = int(np.sqrt(centers.shape[0]))

    for center in centers:
        start_segments.append( get4corners(center, cells_radius))
        end_segments.append( get4corners(center, cell_size))
    
    start_segments = np.array(start_segments)
    end_segments = np.array(end_segments)

    segments = np.concatenate((start_segments, end_segments), axis=2)
    segments = segments.reshape((dimensions*dimensions, 4, 2, 2))

    return segments


def get_segment_mask(cell_mask):
    
    padded_cell_mask = np.pad(cell_mask, 1)
    size = cell_mask.shape[0]

    segment_mask = np.zeros((size,size,4)) 

    for x in range(1,size+1):
        for y in range(1,size+1):
            segment_mask[x-1,y-1] = neighbors_present(padded_cell_mask, [y,x])

    return segment_mask
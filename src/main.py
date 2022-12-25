# Simple pygame program

# 900 / ( 4/3 * 60) = 11.25

# Import and initialize the pygame library
import pygame
from graphics import drawGrid, draw_playing_circle, get_grid, get_map_mask, get_connection_coords, get_segment_mask

pygame.init()


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

GRID_DIM = 11
# colors 
grid_color = (0,0,0)
play_tiles_color = (255,255,255)

# graphic elements sizes
BLOCK_SIZE = 82
PLAY_TILE_RADIUS = 30
BORDER_SIZE = 5
LINE_LENGTH = 12
GRID_START_OFFSET = 51
cell_radius = PLAY_TILE_RADIUS + BORDER_SIZE


temp = LINE_LENGTH//2 + BORDER_SIZE + PLAY_TILE_RADIUS
cells_grid = get_grid(GRID_DIM, BLOCK_SIZE, GRID_START_OFFSET + temp)
segments_grid = get_connection_coords(cells_grid, BLOCK_SIZE//2, cell_radius)
map_mask = get_map_mask(GRID_DIM)
segment_mask = get_segment_mask(map_mask).reshape((GRID_DIM**2,4))
map_mask = map_mask.reshape(GRID_DIM**2)

x_coord_00 = GRID_START_OFFSET + temp
coord_00 = [x_coord_00, x_coord_00] 

# coordinates of the play tiles
tiles_pos = [( coord_00[0], coord_00[1]+ int(70 + LINE_LENGTH)*x) for x in range(11)]
lines_pos = [[(coord_00[0], coord_00[1] + 35 + int(70 + LINE_LENGTH)*x  ), (coord_00[0], coord_00[1] + 35  + int(70 + LINE_LENGTH)*x + LINE_LENGTH ) ] for x in range(10)]


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

    # Fill the background with white
    screen.fill((255, 255, 200))

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50, 5)
    # drawGrid(screen, SCREEN_WIDTH,  SCREEN_HEIGHT, grid_color, BLOCK_SIZE, GRID_START_OFFSET)
        

    for center, mask in zip(cells_grid, map_mask):
        if mask :
            draw_playing_circle(screen, center, PLAY_TILE_RADIUS, play_tiles_color, BORDER_SIZE)
    # for tile in tiles_pos:
    #     draw_playing_circle(screen, tile, PLAY_TILE_RADIUS, play_tiles_color, BORDER_SIZE)
    
    for cell, cell_mask in zip(segments_grid, segment_mask):
        for segment, mask in zip(cell, cell_mask):
            if mask:
                pygame.draw.line(screen, grid_color, segment[0], segment[1], 5)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
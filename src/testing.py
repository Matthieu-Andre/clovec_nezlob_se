from graphics import get_grid, get_map_mask, get_connection_coords, get_segment_mask

GRID_DIM = 11




# print(get_grid(11, 82,48))
# print(get_map_mask(11))
# print( get_connection_coords( get_grid(11, 82,48), 41, 6))
print( get_segment_mask( get_map_mask(GRID_DIM)))
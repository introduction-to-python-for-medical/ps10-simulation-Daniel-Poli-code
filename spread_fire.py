import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                # Check neighbors
                neighbors = [grid[i-1][j] if i > 0 else 0, 
                             grid[i+1][j] if i < grid_size-1 else 0, 
                             grid[i][j-1] if j > 0 else 0, 
                             grid[i][j+1] if j < grid_size-1 else 0]
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid


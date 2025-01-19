import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size-1):
        for j in range(grid_size-1):
            if grid[i][j] == 1:
                # Check neighbors
                neighbors = [grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2

    # Now handle the rightmost column (last column)
    for i in range(grid_size-1):
        if grid[i][grid_size-1] == 1:
            neighbors = [grid[i-1][grid_size-1], grid[i+1][grid_size-1], grid[i][grid_size-2]]
            if 2 in neighbors:
                update_grid[i][grid_size-1] = 2

    # Now handle the bottom row (last row)
    for j in range(grid_size-1):
        if grid[grid_size-1][j] == 1:
            neighbors = [grid[grid_size-2][j], grid[grid_size-1][j-1], grid[grid_size-1][j+1]]
            if 2 in neighbors:
                update_grid[grid_size-1][j] = 2

    return update_grid



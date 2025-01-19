import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)

    # Loop through the grid except for the last row and column
    for i in range(grid_size-1):
        for j in range(grid_size-1):
            if grid[i][j] == 1:
                # Check the four neighboring cells (top, bottom, left, right)
                neighbors = []
                if i > 0:  # Top
                    neighbors.append(grid[i-1][j])
                if i < grid_size-1:  # Bottom
                    neighbors.append(grid[i+1][j])
                if j > 0:  # Left
                    neighbors.append(grid[i][j-1])
                if j < grid_size-1:  # Right
                    neighbors.append(grid[i][j+1])

                # If any neighbor is on fire (2), set the current tree on fire
                if 2 in neighbors:
                    update_grid[i][j] = 2

    # Handle the last row separately
    for j in range(grid_size-1):
        if grid[grid_size-1][j] == 1:
            neighbors = [grid[grid_size-2][j], grid[grid_size-1][j-1], grid[grid_size-1][j+1]]
            if 2 in neighbors:
                update_grid[grid_size-1][j] = 2

    # Handle the last column separately
    for i in range(grid_size-1):
        if grid[i][grid_size-1] == 1:
            neighbors = [grid[i-1][grid_size-1], grid[i+1][grid_size-1], grid[i][grid_size-2]]
            if 2 in neighbors:
                update_grid[i][grid_size-1] = 2

    return update_grid




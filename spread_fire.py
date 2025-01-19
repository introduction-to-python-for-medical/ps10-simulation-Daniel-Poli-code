import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    
    # Loop through all the cells
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # Check if there is a tree
                # Check for fire in neighboring cells (up, down, left, right)
                neighbors = []
                
                if i > 0 and grid[i-1][j] == 2:  # Check top
                    neighbors.append(True)
                if i < grid_size-1 and grid[i+1][j] == 2:  # Check bottom
                    neighbors.append(True)
                if j > 0 and grid[i][j-1] == 2:  # Check left
                    neighbors.append(True)
                if j < grid_size-1 and grid[i][j+1] == 2:  # Check right
                    neighbors.append(True)

                # If fire is in any of the neighbors, set the tree on fire
                if any(neighbors):
                    update_grid[i][j] = 2

    return update_grid





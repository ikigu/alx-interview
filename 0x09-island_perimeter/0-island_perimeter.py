#!/usr/bin/python3


"""
Finds the perimeter of an island, grid.
"""


def island_perimeter(grid):
    """
    Finds the perimeter of an island, grid

    Args:
            grid: a 2D array

    Returns:
            The perimeter of grid
    """

    perimeter = 0

    if type(grid) is not list:
        return perimeter

    if len(grid) == 0:
        return perimeter

    grid_height = len(grid)
    grid_width = len(grid[0])

    for i in range(0, grid_height):
        for j in range(0, grid_width):

            if grid[i][j] == 1:

                # Check above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Check below
                if i == grid_height - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # Check right
                if j == grid_width - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

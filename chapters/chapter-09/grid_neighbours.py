"""Starter code for Week 3 Lab 2: grid neighbours.

Copy this into your week-3 folder as grid_neighbours.py.
"""

import numpy as np


def in_bounds(grid, position):
    row, column = position
    rows, columns = grid.shape
    return 0 <= row < rows and 0 <= column < columns


def is_passable(grid, position):
    row, column = position
    return grid[row, column] == 0


def get_neighbours(grid, position):
    """Return valid up, down, left and right neighbours for position."""
    row, column = position
    possible_moves = [
        (row - 1, column),
        (row + 1, column),
        (row, column - 1),
        (row, column + 1),
    ]

    neighbours = []

    # TODO: for each possible move, check that it is in bounds and passable.
    # Add valid moves to neighbours.

    return neighbours


if __name__ == "__main__":
    sample_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ])

    print(get_neighbours(sample_grid, (0, 0)))
    print(get_neighbours(sample_grid, (2, 2)))

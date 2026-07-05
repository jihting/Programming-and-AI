"""Week 3 Lab 3 starter: BFS and DFS on grid mazes.

Copy this file into your own week-3 folder and rename it to grid_search.py.
Complete bfs(), dfs(), and dfs_recursive() during the lab.
"""

from collections import deque
from pathlib import Path


WALL = "#"
OPEN = "."
START = "S"
GOAL = "G"


class Grid:
    def __init__(self, rows):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0]) if rows else 0
        self.start = self.find_symbol(START)
        self.goal = self.find_symbol(GOAL)

    @classmethod
    def from_file(cls, filename):
        text = Path(filename).read_text().splitlines()
        rows = [list(line.rstrip("\n")) for line in text if line.strip()]
        return cls(rows)

    def find_symbol(self, symbol):
        for row_index, row in enumerate(self.rows):
            for column_index, value in enumerate(row):
                if value == symbol:
                    return (row_index, column_index)
        raise ValueError(f"Missing symbol: {symbol}")

    def in_bounds(self, position):
        row, column = position
        return 0 <= row < self.height and 0 <= column < self.width

    def passable(self, position):
        row, column = position
        return self.rows[row][column] != WALL

    def neighbours(self, position):
        row, column = position
        possible = [
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ]
        return [p for p in possible if self.in_bounds(p) and self.passable(p)]

    def show(self, path=None):
        path = set(path or [])
        for row_index, row in enumerate(self.rows):
            displayed = []
            for column_index, value in enumerate(row):
                position = (row_index, column_index)
                if position in path and value not in (START, GOAL):
                    displayed.append("*")
                else:
                    displayed.append(value)
            print("".join(displayed))


def reconstruct_path(came_from, start, goal):
    if goal not in came_from and goal != start:
        return []

    current = goal
    path = [current]

    while current != start:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def bfs(grid):
    """Return (path, explored_count) using breadth-first search."""
    # TODO: create a deque frontier, visited set, and came_from dictionary.
    # Use frontier.popleft() to explore in queue order.
    return [], 0


def dfs(grid):
    """Return (path, explored_count) using iterative depth-first search."""
    # TODO: create a list frontier, visited set, and came_from dictionary.
    # Use frontier.pop() to explore in stack order.
    return [], 0


def dfs_recursive(grid):
    """Return (path, explored_count) using recursive depth-first search."""
    visited = set()
    explored_count = 0

    def visit(current):
        nonlocal explored_count
        # TODO: implement recursive DFS.
        return None

    path = visit(grid.start)
    return path or [], explored_count


def run_algorithm(name, algorithm, grid):
    path, explored = algorithm(grid)
    print(f"\n{name}")
    print("Path found:", bool(path))
    print("Path length:", len(path) if path else 0)
    print("Explored nodes:", explored)
    if path:
        grid.show(path)


if __name__ == "__main__":
    maze_file = "maze_simple.txt"
    grid = Grid.from_file(maze_file)

    print("Maze:")
    grid.show()
    print("Start:", grid.start)
    print("Goal:", grid.goal)

    run_algorithm("BFS", bfs, grid)
    run_algorithm("DFS", dfs, grid)
    run_algorithm("Recursive DFS", dfs_recursive, grid)

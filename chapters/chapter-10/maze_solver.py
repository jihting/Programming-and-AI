"""Week 4 Maze Solver skeleton.

Complete bfs(), dfs(), and a_star() as directed in the workbook.
"""

from collections import deque
import heapq
from pathlib import Path

WALL = "#"
START = "S"
GOAL = "G"


class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.start = self.find_cell(START)
        self.goal = self.find_cell(GOAL)

    @classmethod
    def from_file(cls, path):
        lines = Path(path).read_text(encoding="utf-8").splitlines()
        grid = [list(line) for line in lines if line.strip()]
        return cls(grid)

    def find_cell(self, symbol):
        for r, row in enumerate(self.grid):
            for c, value in enumerate(row):
                if value == symbol:
                    return (r, c)
        raise ValueError(f"Maze does not contain {symbol!r}")

    def in_bounds(self, position):
        r, c = position
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])

    def passable(self, position):
        r, c = position
        return self.grid[r][c] != WALL

    def cost(self, position):
        r, c = position
        value = self.grid[r][c]
        if value in (START, GOAL, "."):
            return 1
        if value.isdigit():
            return int(value)
        raise ValueError(f"Unknown cell value: {value!r}")

    def neighbours(self, position):
        r, c = position
        candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        return [p for p in candidates if self.in_bounds(p) and self.passable(p)]

    def draw(self, path=None, explored=None):
        path = set(path or [])
        explored = set(explored or [])
        lines = []
        for r, row in enumerate(self.grid):
            line = []
            for c, value in enumerate(row):
                pos = (r, c)
                if value in (START, GOAL, WALL):
                    line.append(value)
                elif pos in path:
                    line.append("*")
                elif pos in explored:
                    line.append("+")
                else:
                    line.append(value)
            lines.append("".join(line))
        return "\n".join(lines)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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


def bfs(maze):
    """Return (path, explored_order) using queue-based BFS."""
    # TODO 1: create a deque frontier containing maze.start
    # TODO 2: create came_from and visited structures
    # TODO 3: repeatedly popleft(), check the goal, add unvisited neighbours
    # TODO 4: return reconstruct_path(...) and explored_order
    raise NotImplementedError("Complete bfs() in Lab 2")


def dfs(maze):
    """Return (path, explored_order) using stack-based DFS."""
    # TODO: use the same structure as BFS, but use a list stack and pop()
    raise NotImplementedError("Complete dfs() in Lab 2")


def a_star(maze, heuristic=manhattan_distance):
    """Return (path, explored_order) using A* and heapq."""
    # TODO 1: create a priority queue frontier using heapq
    # TODO 2: track came_from and cost_so_far
    # TODO 3: priority = new_cost + heuristic(next_position, maze.goal)
    # TODO 4: return reconstruct_path(...) and explored_order
    raise NotImplementedError("Complete a_star() in Lab 2")


def run_algorithm(name, function, maze):
    print("=" * 60)
    print(name)
    path, explored = function(maze)
    print("Path length:", len(path) if path else "no path")
    print("Explored nodes:", len(explored))
    print(maze.draw(path, explored))


if __name__ == "__main__":
    maze = Maze.from_file(Path(__file__).with_name("maze_01_simple.txt"))
    print(maze.draw())
    # Uncomment each line as you complete the functions.
    # run_algorithm("BFS", bfs, maze)
    # run_algorithm("DFS", dfs, maze)
    # run_algorithm("A*", a_star, maze)

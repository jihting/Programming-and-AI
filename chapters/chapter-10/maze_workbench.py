"""Week 4 maze search workbench.

Run this file to compare BFS, DFS, Dijkstra, greedy best-first search and A*.
The code is intentionally readable rather than clever.
"""

from collections import deque
import heapq
from pathlib import Path

WALL = "#"
START = "S"
GOAL = "G"


def load_maze(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    grid = [list(line.rstrip("\n")) for line in lines if line.strip()]
    start = None
    goal = None
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == START:
                start = (r, c)
            elif value == GOAL:
                goal = (r, c)
    if start is None or goal is None:
        raise ValueError("Maze must contain S and G")
    return grid, start, goal


def terrain_cost(value):
    if value in (START, GOAL, "."):
        return 1
    if value.isdigit():
        return int(value)
    raise ValueError(f"Unknown maze cell: {value!r}")


def neighbours(grid, position):
    r, c = position
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != WALL:
                yield (nr, nc)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def zero_heuristic(a, b):
    return 0


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


def path_cost(grid, path):
    if not path:
        return None
    return sum(terrain_cost(grid[r][c]) for r, c in path[1:])


def bfs(grid, start, goal):
    frontier = deque([start])
    came_from = {}
    visited = {start}
    explored_order = []
    while frontier:
        current = frontier.popleft()
        explored_order.append(current)
        if current == goal:
            break
        for nxt in neighbours(grid, current):
            if nxt not in visited:
                visited.add(nxt)
                came_from[nxt] = current
                frontier.append(nxt)
    path = reconstruct_path(came_from, start, goal)
    return {"path": path, "explored": explored_order, "cost": path_cost(grid, path)}


def dfs(grid, start, goal):
    frontier = [start]
    came_from = {}
    visited = {start}
    explored_order = []
    while frontier:
        current = frontier.pop()
        explored_order.append(current)
        if current == goal:
            break
        for nxt in neighbours(grid, current):
            if nxt not in visited:
                visited.add(nxt)
                came_from[nxt] = current
                frontier.append(nxt)
    path = reconstruct_path(came_from, start, goal)
    return {"path": path, "explored": explored_order, "cost": path_cost(grid, path)}


def dijkstra(grid, start, goal):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    explored_order = []
    explored_set = set()
    while frontier:
        current_cost, current = heapq.heappop(frontier)
        if current in explored_set:
            continue
        explored_set.add(current)
        explored_order.append(current)
        if current == goal:
            break
        for nxt in neighbours(grid, current):
            r, c = nxt
            new_cost = current_cost + terrain_cost(grid[r][c])
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                came_from[nxt] = current
                heapq.heappush(frontier, (new_cost, nxt))
    path = reconstruct_path(came_from, start, goal)
    return {"path": path, "explored": explored_order, "cost": path_cost(grid, path)}


def greedy_best_first(grid, start, goal, heuristic=manhattan):
    frontier = [(heuristic(start, goal), start)]
    came_from = {}
    visited = {start}
    explored_order = []
    while frontier:
        _, current = heapq.heappop(frontier)
        explored_order.append(current)
        if current == goal:
            break
        for nxt in neighbours(grid, current):
            if nxt not in visited:
                visited.add(nxt)
                came_from[nxt] = current
                heapq.heappush(frontier, (heuristic(nxt, goal), nxt))
    path = reconstruct_path(came_from, start, goal)
    return {"path": path, "explored": explored_order, "cost": path_cost(grid, path)}


def a_star(grid, start, goal, heuristic=manhattan):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    explored_order = []
    explored_set = set()
    while frontier:
        _, current = heapq.heappop(frontier)
        if current in explored_set:
            continue
        explored_set.add(current)
        explored_order.append(current)
        if current == goal:
            break
        for nxt in neighbours(grid, current):
            r, c = nxt
            new_cost = cost_so_far[current] + terrain_cost(grid[r][c])
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(nxt, goal)
                came_from[nxt] = current
                heapq.heappush(frontier, (priority, nxt))
    path = reconstruct_path(came_from, start, goal)
    return {"path": path, "explored": explored_order, "cost": path_cost(grid, path)}


def draw_maze(grid, path=None, explored=None):
    path = set(path or [])
    explored = set(explored or [])
    output = []
    for r, row in enumerate(grid):
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
        output.append("".join(line))
    return "\n".join(output)


def run_all(maze_path):
    grid, start, goal = load_maze(maze_path)
    algorithms = [
        ("BFS", bfs(grid, start, goal)),
        ("DFS", dfs(grid, start, goal)),
        ("Dijkstra", dijkstra(grid, start, goal)),
        ("Greedy", greedy_best_first(grid, start, goal)),
        ("A*", a_star(grid, start, goal)),
    ]
    for name, result in algorithms:
        print("=" * 60)
        print(name)
        print("Path length:", len(result["path"]) if result["path"] else "no path")
        print("Path cost:", result["cost"])
        print("Explored nodes:", len(result["explored"]))
        print(draw_maze(grid, result["path"], result["explored"]))


if __name__ == "__main__":
    run_all(Path(__file__).with_name("maze_01_simple.txt"))

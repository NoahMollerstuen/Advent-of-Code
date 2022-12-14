from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""")

inp = h.get_input_grid()

start = None
dest = None

for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == "S":
            inp[y][x] = 'a'
            start = (y, x)
        elif inp[y][x] == 'E':
            inp[y][x] = 'z'
            dest = (y, x)


def bfs(grid: t.List[t.List[t.Any]], start_y: int, start_x: int,
        allow_diagonals: bool = False, backtracking: bool = False) -> t.List[t.List[t.Optional[int]]]:
    """
    Perform a breadth first search to find the shortest path to each cell in a grid

    :param grid: a 2d list representing the grid
    :param start_y: the y (first) index for the source cell
    :param start_x: the x (second) index for the source cell
    :param obstacles: a list or string containing each value which is impassable
    :param passables: a list or string containing each value which is passable. Overrides obstacles.
    :param allow_diagonals: Whether a diagonal move on the grid is allowed. If True, it is considered one step.
    :param backtracking: If true, return the shortest path to each cell
    :return: a 2d list with the same shape as the input. Each cell is the minimum number of steps to reach that cell
    or None for no path.
    """
    directions = Grid.DIR8 if allow_diagonals else Grid.DIR4

    cell_queue = [(start_y, start_x)]
    distance_grid: t.List[t.List[t.Optional[int]]] = [[None for _ in row] for row in grid]
    distance_grid[start_y][start_x] = 0
    paths_grid: t.List[t.List[t.Optional[t.Tuple[int, int]]]] = [[None for _ in row] for row in grid]
    paths_grid[start_y][start_x] = []

    while len(cell_queue) > 0:
        cell = cell_queue.pop(0)
        cell_val = Grid.get(distance_grid, cell)
        neighbors = [(cell[0] + direction[0], cell[1] + direction[1]) for direction in directions]
        for n in neighbors:
            n_val = Grid.get(grid, n)
            if n_val is not None and Grid.get(distance_grid, n) is None and \
                    (ord(n_val) - ord(Grid.get(grid, cell)) <= 1):
                distance_grid[n[0]][n[1]] = cell_val + 1
                if backtracking:
                    paths_grid[n[0]][n[1]] = paths_grid[cell[0]][cell[1]] + [n]
                cell_queue.append(n)

    if backtracking:
        return distance_grid, paths_grid  # TODO fix return typing
    return distance_grid


path_lens = []
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if Grid.get(inp, (y, x)) == 'a':
            distances = bfs(inp, y, x, allow_diagonals=False)
            path_lens.append(distances[dest[0]][dest[1]])
print(path_lens)
h.submit(min(*[p for p in path_lens if p is not None]))

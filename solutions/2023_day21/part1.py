from queue import Queue

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""")


def flood_fill(grid, start_pos, max_depth):
    queue = Queue()
    queue.put((start_pos, max_depth))
    visited = set()
    while not queue.empty():
        p, depth = queue.get(block=False)
        for d in Grid.DIR4:
            new_p = (p[0] + d[0], p[1] + d[1])
            if new_p not in visited and Grid.get(grid, new_p) == '.':
                visited.add(new_p)
                if depth > 1:
                    queue.put((new_p, depth - 1))
    return visited


inp = h.get_input_grid()

starting_pos = None
for y, row in enumerate(inp):
    if 'S' in row:
        starting_pos = (y, row.index('S'))
        inp[y][starting_pos[1]] = '.'


filled_cells = flood_fill(inp, starting_pos, max_depth=64)
valid_moves = [c for c in filled_cells if (starting_pos[0] + starting_pos[1] + c[0] + c[1]) % 2 == 0]

h.submit(len(valid_moves))

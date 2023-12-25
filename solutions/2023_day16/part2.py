from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input=r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""")

FORWARD_SLASH_DIR_MAP = {
    (1, 0): (0, -1),
    (-1, 0): (0, 1),
    (0, 1): (-1, 0),
    (0, -1): (1, 0),
}

BACK_SLASH_DIR_MAP = {
    (1, 0): (0, 1),
    (-1, 0): (0, -1),
    (0, 1): (1, 0),
    (0, -1): (-1, 0),
}

inp = h.get_input_grid()
Grid.print(inp)


def energize_tiles(tiles, energy_grid, visited_states_grid, pos, start_dir):
    d = start_dir
    while True:
        c = Grid.get(tiles, pos)
        if c is None:
            return energy_grid

        if d in visited_states_grid[pos[0]][pos[1]]:
            return energy_grid

        energy_grid[pos[0]][pos[1]] += 1
        visited_states_grid[pos[0]][pos[1]].append(d)

        if c == '/':
            d = FORWARD_SLASH_DIR_MAP[d]
        elif c == '\\':
            d = BACK_SLASH_DIR_MAP[d]
        elif c == '|':
            if d[1] != 0:
                energize_tiles(tiles, energy_grid, visited_states_grid, (pos[0] + 1, pos[1]), (1, 0))
                energize_tiles(tiles, energy_grid, visited_states_grid, (pos[0] - 1, pos[1]), (-1, 0))
                return energy_grid
        elif c == '-':
            if d[0] != 0:
                energize_tiles(tiles, energy_grid, visited_states_grid, (pos[0], pos[1] + 1), (0, 1))
                energize_tiles(tiles, energy_grid, visited_states_grid, (pos[0], pos[1] - 1), (0, -1))
                return energy_grid

        pos = (pos[0] + d[0], pos[1] + d[1])


max_tiles = 0

for s_dir, i in it.product(Grid.DIR4, range(len(inp))):
    start_pos = None
    if s_dir == (0, 1):
        start_pos = (i, 0)
    elif s_dir == (0, -1):
        start_pos = (i, len(inp) - 1)
    elif s_dir == (1, 0):
        start_pos = (0, i)
    elif s_dir == (-1, 0):
        start_pos = (len(inp) - 1, i)

    energized_tiles = [list(0 for _ in range(len(row))) for row in inp]
    visited = [list([] for _ in range(len(row))) for row in inp]

    energize_tiles(inp, energized_tiles, visited, start_pos, s_dir)

    max_tiles = max(max_tiles, sum(len(list(n for n in row if n > 0)) for row in energized_tiles))

h.submit(max_tiles)

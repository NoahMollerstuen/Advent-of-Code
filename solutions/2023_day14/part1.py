import copy

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""")


def tilt_north(grid):
    new_grid = copy.deepcopy(grid)
    Grid.print(new_grid)

    for x, column in enumerate(zip(*grid)):
        obstacle_y = -1
        for y, c in enumerate(column):
            if c == "#":
                obstacle_y = y
            elif c == "O":
                new_grid[y][x] = "."
                obstacle_y += 1
                new_grid[obstacle_y][x] = "O"
    return new_grid


inp = h.get_input_grid()

res = tilt_north(inp)

h.submit(sum((len(res) - y) * row.count("O") for y, row in enumerate(res)))

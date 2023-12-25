import copy
from collections import defaultdict

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


def tilt_south(grid):
    return list(reversed(tilt_north(list(reversed(grid)))))


def tilt_west(grid):
    return list(map(list, zip(*tilt_north(list(map(list, zip(*grid)))))))


def tilt_east(grid):
    return list(map(lambda l: list(reversed(l)), tilt_west(list(map(lambda l: list(reversed(l)), grid)))))


inp = h.get_input_grid()

visited_states = defaultdict(lambda: 0)

spin_cycle = (tilt_north, tilt_west, tilt_south, tilt_east)

cycle_start = None
cycle_len = None
cycle_states = []

for step in range(1000000000):
    key = tuple(map(tuple, inp))
    prev_visits = visited_states[key]
    if prev_visits == 1:
        if cycle_start is None:
            cycle_start = step
        cycle_states.append(copy.deepcopy(inp))
    elif prev_visits == 2:
        cycle_len = step - cycle_start
        break

    visited_states[key] = prev_visits + 1

    for tilt in spin_cycle:
        inp = tilt(inp)

last_state = cycle_states[(1000000000 - cycle_start) % cycle_len]

h.submit(sum((len(last_state) - y) * row.count("O") for y, row in enumerate(last_state)))

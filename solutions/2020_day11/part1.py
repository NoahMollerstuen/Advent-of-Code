import copy

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=11)

inp = h.get_input_grid()

grd = inp
while True:
    new_grid = copy.deepcopy(grd)
    changed = False
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            cur = grd[y][x]
            if cur == ".":
                new_grid[y][x] = "."
                continue
            occupied = 0
            for d in Grid.DIR8:
                if Grid.get(grd, (y + d[0], x + d[1]), "L") == "#":
                    occupied += 1
            if (cur == "L" and occupied == 0) or (cur == "#" and occupied < 4):
                new_grid[y][x] = "#"
            else:
                new_grid[y][x] = "L"
            if grd[y][x] != new_grid[y][x]:
                changed = True

    if not changed:
        h.submit(sum([len([c for c in row if c == "#"]) for row in new_grid]))
        break
    grd = copy.deepcopy(new_grid)

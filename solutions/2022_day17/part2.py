import math

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
""")

inp = h.get_input_raw()

shapes = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((2, 2), (1, 2), (0, 0), (0, 1), (0, 2)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
]

heights = {shape: max([p[0] for p in shape]) + 1 for shape in shapes}
widths = {shape: max([p[1] for p in shape]) + 1 for shape in shapes}

shapes_indx = 0
jets_indx = 0

grid = []
max_height = -1


def verify_pos(shape, pos):
    for point in shape:
        if g.get(grid, (pos[0] + point[0], pos[1] + point[1]), default="#") == "#":
            return False
    return True


indicies = []
last_10s = []
height_skipped = None

tick = 0
while tick < 1000000000000:
    shape = shapes[shapes_indx]
    shapes_indx = (shapes_indx + 1) % len(shapes)

    shape_pos = (max_height + 4, 2)

    for _ in range(shape_pos[0] + heights[shape] - len(grid)):
        grid.append(["."] * 7)

    while True:
        new_pos = (shape_pos[0], shape_pos[1] + (1 if inp[jets_indx] == '>' else -1))
        jets_indx = (jets_indx + 1) % len(inp)
        if verify_pos(shape, new_pos):
            shape_pos = new_pos

        new_pos = (shape_pos[0] - 1, shape_pos[1])
        if verify_pos(shape, new_pos):
            shape_pos = new_pos
        else:
            for point in shape:
                y = shape_pos[0] + point[0]
                x = shape_pos[1] + point[1]
                grid[y][x] = "#"
                max_height = max(max_height, y)

            if height_skipped is None and len(indicies) > 0 and jets_indx < indicies[-1][1]:
                # Jet rollover
                if indicies[-10:] in [l[0] for l in last_10s]:
                    # Pattern found
                    ticks_diff = tick - last_10s[-1][1]
                    height_diff = max_height - last_10s[-1][2]

                    cycles_skipped = (1000000000000 - tick) // ticks_diff
                    print(height_diff, ticks_diff, cycles_skipped)
                    tick += cycles_skipped * ticks_diff
                    print(tick)
                    height_skipped = cycles_skipped * height_diff

                last_10s.append((indicies[-10:], tick, max_height))

            indicies.append((shapes_indx, jets_indx))
            break

    tick += 1
    # g.print(list(reversed(grid)))

h.submit(max_height + height_skipped + 1)

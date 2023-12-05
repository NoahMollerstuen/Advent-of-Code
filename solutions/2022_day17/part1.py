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

shapes_iter = it.cycle(shapes)
jets_iter = it.cycle(inp)

grid = []
max_height = -1


def verify_pos(shape, pos):
    for point in shape:
        if g.get(grid, (pos[0] + point[0], pos[1] + point[1]), default="#") == "#":
            return False
    return True


for i in range(2022):
    shape = next(shapes_iter)

    shape_pos = (max_height + 4, 2)

    for _ in range(shape_pos[0] + heights[shape] - len(grid)):
        grid.append(["."] * 7)

    while True:
        new_pos = (shape_pos[0], shape_pos[1] + (1 if next(jets_iter) == '>' else -1))
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
            break

    # g.print(list(reversed(grid)), f"Tick {i}")

h.submit(max_height + 1)

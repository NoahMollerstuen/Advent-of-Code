from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""")

PIPES = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
    ".": []
}


def follow_pipe(grd, pos, prev_pos):
    last_dir = (pos[0] - prev_pos[0], pos[1] - prev_pos[1])
    for d in PIPES[Grid.get(grd, pos)]:
        if not (d[0] == -last_dir[0] and d[1] == -last_dir[1]):
            return pos[0] + d[0], pos[1] + d[1]


inp = h.get_input_grid()

starting_pos = None
for y, row in enumerate(inp):
    for x, c in enumerate(row):
        if c == "S":
            starting_pos = (y, x)
            break

second_pos = None
for first_dir in Grid.DIR4:
    next_pos = (starting_pos[0] + first_dir[0], starting_pos[1] + first_dir[1])
    if Grid.get(inp, next_pos) is None:
        continue
    for d in PIPES[Grid.get(inp, next_pos)]:
        if d[0] == -first_dir[0] and d[1] == -first_dir[1]:
            second_pos = next_pos
            break

print(starting_pos, second_pos)

cur_pos = second_pos
last_pos = starting_pos
step = 1
while Grid.get(inp, cur_pos) != 'S':
    new_pos = follow_pipe(inp, cur_pos, last_pos)
    print(new_pos)
    last_pos = cur_pos
    cur_pos = new_pos
    step += 1

h.submit(step // 2)

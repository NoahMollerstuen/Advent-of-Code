from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""")

inp = h.get_input_grid()

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

visited = [starting_pos, second_pos]

cur_pos = second_pos
last_pos = starting_pos
while Grid.get(inp, cur_pos) != 'S':
    new_pos = follow_pipe(inp, cur_pos, last_pos)
    visited.append(new_pos)
    last_pos = cur_pos
    cur_pos = new_pos

enclosed_count = 0
for y, row in enumerate(inp):
    a = 0
    for x, c in enumerate(row):
        if (y, x) not in visited:
            enclosed_count += a % 2
            print("I" if a % 2 > 0 else c, end='')
            continue
        elif (y, x) in visited and c not in "-F7":
            a += 1
        print(c if (y, x) in visited else ' ', end='')
    print()

h.submit(enclosed_count)

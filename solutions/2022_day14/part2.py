from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""")

inp = h.get_input_list()

paths = [[[int(n) for n in pair.split(",")] for pair in line.split(" -> ")] for line in inp]
paths = [[(pair[1], pair[0] - 300) for pair in path] for path in paths]

grd = [["."] * 400 for _ in range(200)]
print(paths)

y_max = 0
for path in paths:
    for pair in path:
        y_max = max(y_max, pair[0])
print(y_max)


for path in paths:
    for p1, p2 in it.pairwise(path):
        if p1[0] == p2[0]:
            for x in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                grd[p1[0]][x] = "#"
        elif p1[1] == p2[1]:
            for y in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                grd[y][p1[1]] = "#"
        else:
            raise ValueError

rest = 0
while True:
    x = 200
    y = 0
    if grd[y][x] == "o":
        break

    while True:
        if y == y_max + 1:
            grd[y][x] = "o"
            rest += 1
            break
        if grd[y + 1][x] == ".":
            y += 1
        elif grd[y + 1][x - 1] == ".":
            y += 1
            x -= 1
        elif grd[y + 1][x + 1] == ".":
            y += 1
            x += 1
        else:
            grd[y][x] = "o"
            rest += 1
            break
    # print("\n\n\n\n\n")
    # g.print(grd)

h.submit(rest)

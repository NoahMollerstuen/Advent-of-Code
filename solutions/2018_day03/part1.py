from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(3, year=2018)

inp = h.get_input_list()

grid = [[0] * 1000 for i in range(1000)]

claims = []
for line in inp:
    split = line.split(' ')
    pos = split[2].strip(":").split(",")
    pos = [int(pos[0]), int(pos[1])]
    sides = split[3].split("x")
    sides = [int(sides[0]), int(sides[1])]

    claims.append([pos[0], pos[1], sides[0], sides[1]])
    for x in range(pos[0], pos[0]+sides[0]):
        for y in range(pos[1], pos[1]+sides[1]):
            grid[y][x] += 1
print(claims)

for row in grid:
    print("".join([str(c) for c in row]))


conflicted_cells = sum([sum([e > 1 for e in row]) for row in grid])
h.submit(conflicted_cells)

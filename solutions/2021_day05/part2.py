from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(5)

inp = h.get_input_list()

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in inp:
    s = line.split(" -> ")
    coords = [(int(c.split(",")[0]), int(c.split(",")[1])) for c in s]
    print(coords)

    if coords[0][0] == coords[1][0]:
        for i in range(min(coords[0][1], coords[1][1]), max(coords[0][1], coords[1][1]) + 1):
            grid[coords[0][0]][i] += 1
    elif coords[0][1] == coords[1][1]:
        for i in range(min(coords[0][0], coords[1][0]), max(coords[0][0], coords[1][0]) + 1):
            grid[i][coords[0][1]] += 1
    elif coords[0][0] - coords[1][0] == coords[0][1] - coords[1][1]:
        for i in range(min(coords[0][0], coords[1][0]), max(coords[0][0], coords[1][0]) + 1):
            grid[i][i + coords[0][1] - coords[0][0]] += 1
    elif coords[0][0] - coords[1][0] == -coords[0][1] + coords[1][1]:
        for i in range(min(coords[0][0], coords[1][0]), max(coords[0][0], coords[1][0]) + 1):
            grid[i][coords[0][0] + coords[0][1] - i] += 1
            print(i, coords[0][0] + coords[0][1] - i)


for row in grid:
    print("".join([str(c) for c in row]))

a = [len([c for c in row if c > 1]) for row in grid]
print(a)
h.submit(sum(a))


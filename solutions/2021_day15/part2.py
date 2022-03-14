from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(15)

inp = h.get_input_grid()

inp1 = []
for row in inp:
    new_row = []
    for i in range(5):
        for r in row:
            new_row.append((r + i - 1) % 9 + 1)
    inp1.append(new_row)

inp2 = []
for i in range(5):
    for row in inp1:
        new_row = []
        for r in row:
            new_row.append((r + i - 1) % 9 + 1)
        inp2.append(new_row)

inp = inp2
g.print(inp)

# op = [(0, 0)]
# closed = []
# while len(op) > 0:
#

dists = [[1e10 for v in row] for row in inp]

q = [((0, 0), 0)]

while len(q) > 0:
    # print(q)
    q.sort(key=lambda v: v[1], reverse=True)
    tup = q.pop()
    cell = tup[0]
    dist = tup[1]

    if cell == (len(inp) - 1, len(inp[0]) - 1):
        print(cell)
        h.submit(dist)
    if dist < dists[cell[0]][cell[1]]:
        dists[cell[0]][cell[1]] = dist
        for d in g.DIR4:
            y1 = cell[0] + d[0]
            x1 = cell[1] + d[1]
            if 0 <= y1 < len(inp) and 0 <= x1 < len(inp[y1]):
                q.append(((y1, x1), dist + inp[y1][x1]))

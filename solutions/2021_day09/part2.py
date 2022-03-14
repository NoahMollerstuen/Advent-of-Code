from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(9)

inp = h.get_input_grid()

lowpoints = []
for y in range(len(inp)):
    for x in range(len(inp[y])):
        if all(g.get(inp, (y + d[0], x + d[1])) is None or g.get(inp, (y + d[0], x + d[1])) > g.get(inp, (y, x)) for d in g.DIR4):
            lowpoints.append((y,x))

basins = {}
for p in lowpoints:
    basins[p] = 0

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if g.get(inp, (y, x)) == 9:
            continue

        yy = y
        xx = x
        while (yy, xx) not in lowpoints:
            for d in g.DIR4:
                n = g.get(inp, (yy + d[0], xx + d[1]))
                if n is not None and n < g.get(inp, (yy, xx)):
                    yy += d[0]
                    xx += d[1]
                    break
        basins[(yy, xx)] += 1

s = sorted(basins.keys(), key=lambda k: basins[k], reverse=True)
for b in s:
    print(b, basins[b])

h.submit(basins[s[0]] * basins[s[1]] * basins[s[2]])

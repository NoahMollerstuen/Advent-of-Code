from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(9)

inp = h.get_input_grid()

risks = []
for y in range(len(inp)):
    for x in range(len(inp[y])):
        height = g.get(inp, (y, x))
        lowpoint = True
        for d in g.DIR4:
            ht = g.get(inp, (y + d[0], x + d[1]))
            if y==32:
                print(x, height, d, (y + d[0], x + d[1]), g.get(inp, (y + d[0], x + d[1])))
            if ht is None:
                continue
            if not height < ht:
                lowpoint = False
                break
        if lowpoint:
            # if all(g.get(inp, (y + d[0], x + d[1])) is None or g.get(inp, (y + d[0], x + d[1])) > g.get(inp, (y, x)) for d in g.DIR4):
            # print(y, x, g.get(inp, (y, x)))
            risks.append(1 + g.get(inp, (y, x)))

h.submit(sum(risks))

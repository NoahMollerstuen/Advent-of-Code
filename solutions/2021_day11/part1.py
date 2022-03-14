from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(11)

inp = h.get_input_grid()

total_flashes = 0


def do_step(gr):
    flashes = 0

    for y in range(len(gr)):
        for x in range(len(gr[y])):
            gr[y][x] += 1

    done = False
    while not done:
        done = True
        for y in range(len(gr)):
            for x in range(len(gr[y])):
                v = g.get(gr, (y, x))
                if v > 9:
                    gr[y][x] = -1e9
                    done = False
                    flashes += 1
                    for d in g.DIR8:
                        c = g.get(gr, (y + d[0], x + d[1]))
                        if c is not None:
                            gr[y + d[0]][x + d[1]] += 1

    for y in range(len(gr)):
        for x in range(len(gr[y])):
            if g.get(gr, (y, x)) < 0:
                gr[y][x] = 0
    return flashes


for i in range(100):
    total_flashes += do_step(inp)
    for row in inp:
        print("".join(str(c) for c in row))
    print()

h.submit(total_flashes)

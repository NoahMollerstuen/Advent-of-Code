from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""")

inp = h.get_input_grid()

y = 0
while y < len(inp):
    if all(c == '.' for c in inp[y]):
        inp = inp[:y] + [inp[y]] + inp[y:]
        y += 1
    y += 1

inp = list(zip(*inp))

y = 0
while y < len(inp):
    if all(c == '.' for c in inp[y]):
        inp = inp[:y] + [inp[y]] + inp[y:]
        y += 1
    y += 1

inp = list(zip(*inp))

galaxies = []
for y, row in enumerate(inp):
    for x, c in enumerate(row):
        if c == "#":
            galaxies.append((x, y))

total_dist = 0
for g1, g2 in it.combinations(galaxies, 2):
    total_dist += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

h.submit(total_dist)
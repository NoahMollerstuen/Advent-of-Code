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

EXPANSION = 1000000

expansions_x = []
expansions_y = []

y = 0
while y < len(inp):
    if all(c == '.' for c in inp[y]):
        expansions_y.append(y)
    y += 1

inp = list(zip(*inp))

x = 0
while x < len(inp):
    if all(c == '.' for c in inp[x]):
        expansions_x.append(x)
    x += 1

inp = list(zip(*inp))

galaxies = []
for y, row in enumerate(inp):
    for x, c in enumerate(row):
        if c == "#":
            galaxies.append((y, x))

total_dist = 0
print(galaxies)
print(expansions_y)
print(expansions_x)
for g1, g2 in it.combinations(galaxies, 2):
    total_dist += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    total_dist += len(list(e for e in expansions_y if min(g1[0], g2[0]) < e < max(g1[0], g2[0]))) * (EXPANSION - 1)
    total_dist += len(list(e for e in expansions_x if min(g1[1], g2[1]) < e < max(g1[1], g2[1]))) * (EXPANSION - 1)

h.submit(total_dist)

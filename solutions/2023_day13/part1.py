from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(day=13, test_mode=False, test_input="""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""")

inp = h.get_input_list_2d()


def get_mirrors(grid):
    mirrors = []

    for y in range(1, len(grid)):
        if y <= len(grid) / 2:
            if grid[0:y] == list(reversed(grid[y:2*y])):
                mirrors.append(y)
        else:
            if grid[len(grid)-2*(len(grid)-y):y] == list(reversed(grid[y:])):
                mirrors.append(y)
    return mirrors


total_sum = 0
for mat in inp:
    total_sum += 100 * sum(get_mirrors(mat))
    total_sum += sum(get_mirrors(list(zip(*mat))))

# print()
h.submit(total_sum)

import copy

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


def comp_list(l1, l2):
    return sum(sum(c1 != c2 for c1, c2 in zip(r1, r2)) for r1, r2 in zip(l1, l2))


def make_equal(l1, l2):
    for r1, r2 in zip(l1, l2):
        for i, v in enumerate(r2):
            r1[i] = v


def correct_smudge(grid):
    grid = copy.deepcopy(grid)
    for y in range(1, len(grid)):
        if y <= len(grid) / 2:
            if comp_list(grid[0:y], list(reversed(grid[y:2 * y]))) == 1:
                make_equal(grid[0:y], list(reversed(grid[y:2 * y])))
                return True, grid, y
        else:
            if comp_list(grid[len(grid) - 2 * (len(grid) - y):y], list(reversed(grid[y:]))) == 1:
                make_equal(grid[len(grid) - 2 * (len(grid) - y):y], list(reversed(grid[y:])))
                return True, grid, y
    return False, grid, None


total_sum = 0
for str_list in inp:
    mat = list(map(list, str_list))
    print()
    Grid.print(mat)

    was_corrected, mat, value = correct_smudge(mat)
    if was_corrected:
        total_sum += 100 * value
    else:
        was_corrected, flipped_mat, value = correct_smudge(list(map(list, zip(*mat))))
        mat = list(zip(*flipped_mat))
        total_sum += value

    if not was_corrected:
        raise ValueError

    print(value)
    Grid.print(mat)

h.submit(total_sum)

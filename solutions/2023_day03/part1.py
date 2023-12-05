from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""")

inp = h.get_input_grid()
print(inp)


def to_int(s):
    try:
        return int(s)
    except Exception:
        return None


part_nums = []


for y, r in enumerate(inp):
    for x, c in enumerate(r):
        c = to_int(c)
        if c is None:
            continue

        if to_int(Grid.get(inp, (y, x-1))) is not None:
            continue

        tempx = x

        n = 0
        is_part_num = False
        while True:
            for dx, dy in Grid.DIR8:
                a = Grid.get(inp, (y + dy, tempx + dx))
                if a not in (None, '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    is_part_num = True

            n *= 10
            n += to_int(Grid.get(inp, (y, tempx)))

            tempx += 1

            if to_int(Grid.get(inp, (y, tempx))) is None:
                break

        print(n, is_part_num)
        if is_part_num:
            part_nums.append(n)

h.submit(sum(part_nums))

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


star_numbers = {}

for y, r in enumerate(inp):
    for x, c in enumerate(r):
        c = to_int(c)
        if c is None:
            continue

        if to_int(Grid.get(inp, (y, x-1))) is not None:
            continue

        tempx = x

        n = 0
        neighbor_stars = set()

        while True:
            for dx, dy in Grid.DIR8:
                a = Grid.get(inp, (y + dy, tempx + dx))
                if a == '*':
                    neighbor_stars.add((y + dy, tempx + dx))

            n *= 10
            n += to_int(Grid.get(inp, (y, tempx)))

            tempx += 1

            if to_int(Grid.get(inp, (y, tempx))) is None:
                break

        for star in neighbor_stars:
            if star not in star_numbers.keys():
                star_numbers[star] = []
            star_numbers[star].append(n)

print(star_numbers)

ratio_sum = 0
for star, nums in star_numbers.items():
    if len(nums) == 2:
        ratio_sum += nums[0] * nums[1]

h.submit(ratio_sum)

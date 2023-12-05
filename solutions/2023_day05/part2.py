from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""")


def lookup_in_map(mp, ranges):
    output_ranges = []
    for m in mp:
        new_ranges = []
        for r in ranges:
            if r[0] + r[1] <= m[1] or r[0] >= m[1] + m[2]:
                new_ranges.append(r)
                continue
            overlap = (max(r[0], m[1]), min(r[0] + r[1], m[1] + m[2]) - max(r[0], m[1]))
            if overlap[0] != r[0]:
                new_ranges.append((r[0], overlap[0] - r[0]))
            if overlap[0] + overlap[1] != r[0] + r[1]:
                new_ranges.append((overlap[0] + overlap[1], (overlap[0] + overlap[1]) - (r[0] + r[1])))

            output_ranges.append((overlap[0] - m[1] + m[0], overlap[1]))
        ranges = new_ranges
    for r in ranges:
        output_ranges.append(r)
    return output_ranges


def get_final_value(maps, in_ranges):
    for mp in maps:
        in_ranges = lookup_in_map(mp, in_ranges)
        print(in_ranges)
    return in_ranges


inp = h.get_input_list_2d()

print(inp)

initial_ranges = [int(n) for n in inp[0][0].split(" ")[1:]]
print(initial_ranges)

initial_seeds = []
for i in range(0, len(initial_ranges), 2):
    initial_seeds.append((initial_ranges[i], initial_ranges[i + 1]))

maps = []
for group in inp[1:]:
    m = []
    for line in group[1:]:
        m.append([int(n) for n in line.split(" ")])
    maps.append(m)

locs = get_final_value(maps, initial_seeds)

h.submit(min(l[0] for l in locs))

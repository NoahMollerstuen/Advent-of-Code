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


def lookup_in_map(mp, in_num):
    for mapping in mp:
        if mapping[1] <= in_num < mapping[1] + mapping[2]:
            return in_num - mapping[1] + mapping[0]
    return in_num


def get_final_value(maps, in_num):
    for mp in maps:
        in_num = lookup_in_map(mp, in_num)
    return in_num

inp = h.get_input_list_2d()

print(inp)

initial_seeds = [int(n) for n in inp[0][0].split(" ")[1:]]
print(initial_seeds)

maps = []
for group in inp[1:]:
    m = []
    for line in group[1:]:
        m.append([int(n) for n in line.split(" ")])
    maps.append(m)

locs = []
for seed in initial_seeds:
    locs.append(get_final_value(maps, seed))

h.submit(min(locs))

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np

h = Helper(year=2018, day=6)

inp = h.get_input_list()

coords = [(int(line.split(", ")[0]), int(line.split(", ")[1])) for line in inp]
print(coords)


def closest_coord(y, x, coords):
    min_dist = 1e10
    best_c = None
    for c in coords:
        dist = abs(y - c[1]) + abs(x - c[0])
        if dist < min_dist:
            min_dist = dist
            best_c = c
        elif dist == min_dist:
            best_c = None
    return best_c


bad_coords = set()
for x in range(1000):
    bad_coords.add(closest_coord(0, x, coords))
    bad_coords.add(closest_coord(1000, x, coords))

for y in range(1000):
    bad_coords.add(closest_coord(y, 0, coords))
    bad_coords.add(closest_coord(y, 1000, coords))

area = {}
for y in range(1000):
    for x in range(1000):
        coord = closest_coord(y, x, coords)
        if coord is None or coord in bad_coords:
            continue
        area[coord] = area.get(coord, 0) + 1

print(area)
h.submit(max(area.values()))

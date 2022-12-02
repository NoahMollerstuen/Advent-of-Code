from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np

h = Helper(year=2018, day=6)

inp = h.get_input_list()

coords = [(int(line.split(", ")[0]), int(line.split(", ")[1])) for line in inp]
print(coords)

count = 0
for y in range(1000):
    for x in range(1000):
        tot_dist = 0
        for c in coords:
            tot_dist += abs(y - c[1]) + abs(x - c[0])
        if tot_dist < 10000:
            count += 1

h.submit(count)
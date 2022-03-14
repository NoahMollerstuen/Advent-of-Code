from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(6)

inp = h.get_input_list()

fish = [int(f) for f in inp[0].split(",")]
print(fish)


def day(f):
    to_add = []
    for i, ff in enumerate(f):
        if ff == 0:
            f[i] = 6
            to_add.append(8)
        else:
            f[i] -= 1
    for ff in to_add:
        f.append(ff)


for i in range(80):
    day(fish)

h.submit(len(fish))

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(6)

inp = h.get_input_list()

ages = [0] * 9
fish = [int(f) for f in inp[0].split(",")]
print(fish)

for f in fish:
    ages[f] += 1


def day(f):
    new_f = [0] * 9
    new_f[8] = f[0]
    new_f[6] += f[0]
    for i in range(8):
        new_f[i] += f[i+1]
    return new_f


for i in range(256):
    ages = day(ages)

h.submit(sum(ages))

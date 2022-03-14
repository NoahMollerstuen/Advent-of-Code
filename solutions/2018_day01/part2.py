from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(1, year=2018)

inp = h.get_input_list()

sums = []
s = 0
for n in inp:
    s = s + n
    sums.append(s)

ss = sum(inp)
for c in range(1, 100000):
    for s in sums:
        if s + c * ss in sums:
            print(s, c, ss)
            h.submit(s + c * ss)
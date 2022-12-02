from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=10)

inp = h.get_input_list()
inp.append(0)
inp.append(max(inp) + 3)

diffs = np.diff(sorted(inp))

print(diffs.tolist())
chains = "".join([str(n) for n in diffs.tolist()]).split("3")

p = 1
for c in chains:
    if len(c) == 2:
        p *= 2
    if len(c) == 3:
        p *= 4
    if len(c) == 4:
        p *= 7
h.submit(p)

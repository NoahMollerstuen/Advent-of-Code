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

ones = len([n for n in diffs if n == 1])
threes = len([n for n in diffs if n == 3])
print(ones, threes)
h.submit(ones * threes)

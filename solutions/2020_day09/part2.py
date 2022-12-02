from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=9)

inp = h.get_input_list()

for i in range(25, len(inp)):
    prev_numbs = inp[i-25:i]
    numb = inp[i]
    valid = False
    for comb in it.combinations(prev_numbs, 2):
        if sum(comb) == numb:
            valid = True
            break
    if not valid:
        invalid_numb = numb

for i in range(len(inp)):
    for j in range(i, len(inp)):
        if sum(inp[i:j]) == invalid_numb:
            h.submit(min(inp[i:j]) + max(inp[i:j]))

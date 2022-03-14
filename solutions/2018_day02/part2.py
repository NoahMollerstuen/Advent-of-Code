from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(2, year=2018)

inp = h.get_input_list()

for line in inp:
    for line2 in inp:
        if len([i for i, c in enumerate(line) if line2[i] != c]) == 1:
            chars = [c for i, c in enumerate(line) if line2[i] == c]
            s = ""
            for c in chars:
                s = s + c
            h.submit(s)

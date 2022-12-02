from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np

h = Helper(year=2018, day=8, test_input="2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", test_mode=False)

inp = [int(c) for c in h.get_input_raw().split(" ")]


def get_meta_sum(s):
    children = s[0]
    meta = s[1]
    tot = 0
    s = s[2:]
    for i in range(children):
        s, m = get_meta_sum(s)
        tot += m
    for i in range(meta):
        tot += s[i]
    s = s[meta:]
    return s, tot


h.submit(get_meta_sum(inp)[1])

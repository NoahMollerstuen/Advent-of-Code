from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np

h = Helper(year=2018, day=8, test_input="2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", test_mode=False)

inp = [int(c) for c in h.get_input_raw().split(" ")]


def get_value(s):
    children = s[0]
    meta = s[1]
    s = s[2:]
    vals = []
    for i in range(children):
        s, v = get_value(s)
        vals.append(v)

    if children == 0:
        tot = 0
        for i in range(meta):
            tot += s[i]
        s = s[meta:]
        return s, tot

    tot = 0
    print(vals)
    for i in range(meta):
        # print(s[i])
        try:
            if s[i] < 0:
                continue
            tot += vals[s[i]-1]
        except IndexError:
            pass

    s = s[meta:]
    return s, tot


h.submit(get_value(inp)[1])

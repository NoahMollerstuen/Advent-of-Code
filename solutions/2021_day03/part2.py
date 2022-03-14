from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(3)

inp = h.get_input_raw().split("\n")

bi = 0
while len(inp) > 1:
    s = 0
    to_remove = []
    for n in inp:
        s += int(n[bi])
    for op in inp:
        if s == len(inp) / 2:
            if op[bi] == "1":
                to_remove.append(op)
            continue
        if (op[bi] == "1") == (s > len(inp) / 2):
            to_remove.append(op)
    print(bi, inp, s, s > len(inp) / 2)

    for op in to_remove:
        inp.remove(op)
    bi += 1

print(inp[0])
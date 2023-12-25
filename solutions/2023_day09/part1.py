from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""")

inp = h.get_input_list()

total = 0
for line in inp:
    seq = [int(c) for c in line.split(" ")]
    seqs = [seq]
    while any(n != 0 for n in seq):
        seq = [b - a for a, b in it.pairwise(seq)]
        seqs.append(seq)

    seqs.reverse()
    seqs[0].append(0)
    prev_val = 0
    for seq in seqs[1:]:
        val = seq[-1] + prev_val
        prev_val = val
        seq.append(val)
    total += prev_val

h.submit(total)

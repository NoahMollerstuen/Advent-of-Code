import math

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=13, test_mode=False, test_input="""939
1789,37,47,1889""")

inp = h.get_input_list()

depart = int(inp[0])
busses = inp[1].split(",")

busses = [(int(b), i) for i, b in enumerate(busses) if b != "x"]


def get_first_overlap(seq1, seq2):
    if seq2[0] > seq1[0]:
        seq1, seq2 = (seq2, seq1)

    tick = seq1[1]
    while True:
        if tick % seq2[0] == seq2[1]:
            return tick
        tick += seq1[0]


cycle = 1
offset = 0

for id, off in busses:
    print(cycle, offset, id, off)
    offset = get_first_overlap((cycle, offset), (id, (id - off) % id))
    cycle = math.lcm(cycle, id)

h.submit(offset)
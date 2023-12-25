import math

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""")

inp = h.get_input_list()

dir_string = inp[0]
nodes = {l.split(" = ")[0]: {"L": l.split(" = ")[1][1:4], "R": l.split(" = ")[1][6:9]} for l in inp[2:]}

cur_nodes = [k for k in nodes.keys() if k[-1] == "A"]
step = 0
cycle_lens = [None] * len(cur_nodes)

for d in it.cycle(dir_string):
    # print(cur_nodes)
    cur_nodes = [nodes[n][d] for n in cur_nodes]
    step += 1

    for i, n in enumerate(cur_nodes):
        if n[-1] == "Z":
            if cycle_lens[i] is None:
                cycle_lens[i] = step
            if None not in cycle_lens:
                print(cycle_lens)
                h.submit(math.lcm(*cycle_lens))

h.submit(step)

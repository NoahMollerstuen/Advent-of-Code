from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""")

inp = h.get_input_list()

dir_string = inp[0]
nodes = {l.split(" = ")[0]: {"L": l.split(" = ")[1][1:4], "R": l.split(" = ")[1][6:9]} for l in inp[2:]}

cur_node = "AAA"
step = 0
for d in it.cycle(dir_string):
    print(cur_node)
    cur_node = nodes[cur_node][d]
    step += 1
    if cur_node == "ZZZ":
        break

h.submit(step)

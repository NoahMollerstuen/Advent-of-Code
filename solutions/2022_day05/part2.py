from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_mode=False, test_input="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""")

inp = h.get_input_raw()

crates = zip(*[it.compress(s, it.cycle((0, 1, 0, 0))) for s in inp.split("\n\n")[0].split("\n")[:-1]])
crates = [list(reversed([c for c in stack if c != " "])) for stack in crates]
print(crates)

insts = inp.split("\n\n")[1].split("\n")
matches = [re.match(r"move (\d+) from (\d+) to (\d+)", i) for i in insts]
commands = [(int(m.groups()[0]), int(m.groups()[1]), int(m.groups()[2])) for m in matches]

for c in commands:
    count = c[0]
    frm = c[1] - 1
    to = c[2] - 1
    moving = crates[frm][-count:]
    crates[to].extend(moving)
    for _ in range(count):
        crates[frm].pop()

h.submit("".join([stack[-1] for stack in crates]))

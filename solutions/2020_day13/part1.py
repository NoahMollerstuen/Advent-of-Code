from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=13, test_mode=False, test_input="""939
7,13,x,x,59,x,31,19""")

inp = h.get_input_list()

depart = int(inp[0])
busses = inp[1].split(",")

busses = [int(b) for b in busses if b != "x"]
print(depart)
print(busses)

waits = [id - (depart % id) for id in busses]

best_id = busses[waits.index(min(waits))]

print(best_id)
h.submit(best_id * min(waits))

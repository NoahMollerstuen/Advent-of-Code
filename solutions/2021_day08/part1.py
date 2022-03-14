from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(8)

inp = h.get_input_list()

outputs = []
for line in inp:
    out = line.split(" | ")[1].split(" ")
    outputs.append(out)

h.submit(sum(len([d for d in o if len(d) in [2, 4, 3, 7]]) for o in outputs))

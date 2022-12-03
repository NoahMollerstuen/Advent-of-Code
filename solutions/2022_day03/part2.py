from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_mode=False, test_input="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""")

inp = h.get_input_list()

chars = []
for i in range(0, len(inp), 3):
    chars.append(set(inp[i]).intersection(set(inp[i+1])).intersection(set(inp[i+2])).pop())

priorities = [ord(c) - 96 if c.lower() == c else ord(c) - 38 for c in chars]

h.submit(sum(priorities))

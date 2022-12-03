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
for sack in inp:
    half1 = set(sack[:len(sack) // 2])
    half2 = set(sack[len(sack) // 2:])
    c = half1.intersection(half2).pop()
    chars.append(c)
    print(c)

priorities = [ord(c) - 96 if c.lower() == c else ord(c) - 38 for c in chars]

h.submit(sum(priorities))

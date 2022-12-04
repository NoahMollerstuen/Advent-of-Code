from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_mode=False, test_input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""")

inp = h.get_input_list()

overlaps = 0
for pair in inp:
    ranges = pair.split(',')
    ids = [list(map(int, r.split('-'))) for r in ranges]
    print(ids)
    if not (ids[0][1] < ids[1][0] or ids[1][1] < ids[0][0]):
        overlaps += 1
        print("succeeded")

h.submit(overlaps)

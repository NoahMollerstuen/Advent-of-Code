from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_mode=False, test_input="""mjqjpqmgbljsphdztnvjfqwrcgsmlb""")

inp = h.get_input_raw()

for i in range(len(inp)):
    if len(set(inp[i:i+14])) == 14:
        h.submit(i + 14)
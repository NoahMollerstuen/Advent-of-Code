from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper()

inp = h.get_input_list()

m = 0
acc = 0
for i in inp:
    if i == "":
        if acc > m:
            m = acc
        acc = 0
    else:
        acc += int(i)

h.submit(m)
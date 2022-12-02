from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2018, day=5)

inp = h.get_input_raw()

s = inp
i = 0
last_s = ""
while True:
    try:
        if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
            s = s[:i] + s[i+2:]
        else:
            i += 1
    except IndexError:
        if last_s == s:
            break
        i = 0
        # print(s)
        last_s = s
h.submit(len(s))

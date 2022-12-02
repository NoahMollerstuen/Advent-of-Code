from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2018, day=5)

inp = h.get_input_raw()

min_len = 1e10
for c in ALPHABET:
    s = inp
    s = s.replace(c, "")
    s = s.replace(c.upper(), "")

    last_s = ""
    while True:
        for c2 in ALPHABET:
            s = s.replace(c2.upper() + c2, "").replace(c2 + c2.upper(), "")
        if last_s == s:
            break
        last_s = s
    if len(s) < min_len:
        min_len = len(s)
h.submit(min_len)

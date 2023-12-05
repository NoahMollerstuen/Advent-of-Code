from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""

""")

inp = h.get_input_list()

calibrations = []

for line in inp:
    chars = []
    print(line)
    for c in line:
        try:
            chars.append(int(c))
        except Exception:
            pass

    print(chars)
    calibrations.append(10 * chars[0] + chars[-1])

h.submit(sum(calibrations))

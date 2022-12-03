from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=12, test_mode=False)

inp = h.get_input_list()

x = 0
y = 0
facing = 270
for command in inp:
    code = command[0]
    arg = int(command[1:])
    if code == "N" or (code == "F" and facing == 0):
        y += arg
    elif code == "S" or (code == "F" and facing == 180):
        y -= arg
    elif code == "E" or (code == "F" and facing == 270):
        x += arg
    elif code == "W" or (code == "F" and facing == 90):
        x -= arg
    elif code == "R":
        facing = (facing - arg) % 360
    elif code == "L":
        facing = (facing + arg) % 360
    else:
        raise ValueError(code)

h.submit(abs(x) + abs(y))




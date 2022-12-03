from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=12, test_mode=False, test_input="""F10
N3
F7
R90
F11""")

inp = h.get_input_list()

x = 0
y = 0
w_x = 10
w_y = 1

for command in inp:
    code = command[0]
    arg = int(command[1:])
    if code == "N":
        w_y += arg
    elif code == "S":
        w_y -= arg
    elif code == "E":
        w_x += arg
    elif code == "W":
        w_x -= arg
    elif code == "R":
        for i in range(arg // 90):
            w_x, w_y = (w_y, -w_x)
    elif code == "L":
        for i in range(arg // 90):
            w_x, w_y = (-w_y, w_x)
    elif code == "F":
        x += w_x * arg
        y += w_y * arg
    else:
        raise ValueError(code)
    print(x, y)

h.submit(abs(x) + abs(y))




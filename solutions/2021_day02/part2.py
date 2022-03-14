from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(2)

inp = h.get_input_list()

x=0
d = 0
a = 0
for line in inp:
    s = line.split(" ")
    if s[0] == "forward":
        x += int(s[1])
        d += a * int(s[1])
    elif s[0] == "up":
        a -= int(s[1])
    elif s[0] == "down":
        a += int(s[1])
    else:
        print("WARN")

h.submit(x * d)
from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(7)

inp = h.get_input_list()

inp = [int(i) for i in inp[0].split(",")]

srt = sorted(inp)
print(srt)
median = srt[int(len(inp) / 2)]
print(median)

dist = [abs(median - v) for v in inp]

h.submit(sum(dist))

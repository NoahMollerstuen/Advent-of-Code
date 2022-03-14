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


def get_cost(s, d):
    n = abs(s - d)
    return n * (n + 1) / 2


def get_total_cost(l, d):
    return sum(get_cost(v, d) for v in l)


costs = [get_total_cost(inp, i) for i in range(1500)]

dist = [abs(median - v) for v in inp]

h.submit(min(costs))

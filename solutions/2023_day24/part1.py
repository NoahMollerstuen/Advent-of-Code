from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""")

inp = h.get_input_list()

TEST_MIN = 200000000000000
TEST_MAX = 400000000000000

hails = []

for line in inp:
    line_split = line.split(' @ ')
    pos = tuple(int(n) for n in line_split[0].split(', '))
    vel = tuple(int(n) for n in line_split[1].split(', '))
    hails.append((pos, vel))

total = 0
for h1, h2 in it.combinations(hails, 2):
    # print(h1, h2)
    dx = h2[0][0] - h1[0][0]
    dy = h2[0][1] - h1[0][1]
    det = h2[1][0] * h1[1][1] - h2[1][1] * h1[1][0]
    if det == 0:
        continue
    u = (dy * h2[1][0] - dx * h2[1][1]) / det
    v = (dy * h1[1][0] - dx * h1[1][1]) / det

    total += u >= 0 and v >= 0 and \
        TEST_MIN <= h1[0][0] + h1[1][0] * u <= TEST_MAX and \
        TEST_MIN <= h1[0][1] + h1[1][1] * u <= TEST_MAX


h.submit(total)

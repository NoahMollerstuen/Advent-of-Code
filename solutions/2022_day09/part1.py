import math

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_mode=False, test_input="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""")

inp = h.get_input_list()

head = [0, 0]
tail = [0, 0]

DIRS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

visited = {(0, 0)}

for inst in inp:
    d = DIRS[inst[0]]
    length = int(inst[2:])
    for _ in range(length):
        head[0] += d[0]
        head[1] += d[1]
        if math.dist(head, tail) >= 2:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -= 1
        visited.add(tuple(tail))

h.submit(len(visited))

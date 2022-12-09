import math

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""")


inp = h.get_input_list()

knots = [[0, 0] for i in range(10)]

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
        knots[0][0] += d[0]
        knots[0][1] += d[1]
        for leader, follower in it.pairwise(knots):

            if math.dist(leader, follower) >= 2:
                if leader[0] > follower[0]:
                    follower[0] += 1
                elif leader[0] < follower[0]:
                    follower[0] -= 1
                if leader[1] > follower[1]:
                    follower[1] += 1
                elif leader[1] < follower[1]:
                    follower[1] -= 1
        visited.add(tuple(knots[-1]))
    # print(knots)

h.submit(len(visited))

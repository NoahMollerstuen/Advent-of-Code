from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np
from collections import defaultdict


h = Helper(22)

inp = h.get_input_list()

instructions = []
for line in inp:
    m = re.match(r"(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
    instruction = [m[1] == "on"]
    for i in range(2, 8):
        instruction.append(int(m[i]) + i % 2)
    print(instruction)
    instructions.append(instruction)


def subtract_prisms(p1, p2):
    # print("args:", p1, p2)
    subprisms = (
        (p1[0], (p1[1][0], p1[1][1], p2[0][2])),
        ((p1[0][0], p1[0][1], p2[1][2]), p1[1]),
        ((p1[0][0], p1[0][1], p2[0][2]), (p1[1][0], p2[0][1], p2[1][2])),
        ((p1[0][0], p2[1][1], p2[0][2]), (p1[1][0], p1[1][1], p2[1][2])),
        ((p1[0][0], p2[0][1], p2[0][2]), (p2[0][0], p2[1][1], p2[1][2])),
        ((p2[1][0], p2[0][1], p2[0][2]), (p1[1][0], p2[1][1], p2[1][2]))
    )

    clamped_prisms = [
        (
            tuple([max(p1[0][i], p[0][i]) for i in range(3)]),
            tuple([min(p1[1][i], p[1][i]) for i in range(3)]),
        )
        for p in subprisms
    ]
    valid_prisms = [p for p in clamped_prisms if all(p[1][i] > p[0][i] for i in range(3))]
    return valid_prisms


prisms = []
for i, inst in enumerate(instructions):
    new_p = ((inst[1], inst[3], inst[5]), (inst[2], inst[4], inst[6]))
    print(i, len(prisms), inst)
    new_prisms = []
    for p in prisms:
        results = subtract_prisms(p, new_p)
        for r in results:
            new_prisms.append(r)
    if inst[0]:
        new_prisms.append(new_p)
    prisms = new_prisms

volumes = [(p[1][0] - p[0][0]) * (p[1][1] - p[0][1]) * (p[1][2] - p[0][2]) for p in prisms]
h.submit(sum(volumes))

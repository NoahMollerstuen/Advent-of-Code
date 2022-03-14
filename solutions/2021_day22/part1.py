from util import *
from util import Grid as g
from packets import *
import itertools as it
import re
import numpy as np


h = Helper(22)

inp = h.get_input_list()

instructions = []
for line in inp:
    m = re.match(r"(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
    instruction = [m[1] == "on"]
    for i in range(2, 8):
        instruction.append(int(m[i]) + 50)
    print(instruction)
    instructions.append(instruction)


grid = [[[False for i in range(101)] for j in range(101)] for k in range(101)]
for inst in instructions:
    for x in range(max(0, inst[1]), min(100, inst[2]) + 1):
        for y in range(max(0, inst[3]), min(100, inst[4]) + 1):
            for z in range(max(0, inst[5]), min(100, inst[6]) + 1):
                grid[x][y][z] = inst[0]

total = sum(sum(sum(val for val in row) for row in slice) for slice in grid)

h.submit(total)

import enum
import math

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np

h = Helper(24)

inp = h.get_input_list()


class InstructionType(enum.Enum):
    inp = 0
    add = 1
    mul = 2
    div = 3
    mod = 4
    eql = 5

    def __repr__(self):
        return self.name


instructions = []
inp_count = 0
for line in inp:
    spl = line.split(" ")
    inst = [InstructionType[spl[0]], ord(spl[1]) - ord('w')]
    if len(spl) > 2:
        try:
            inst.append(int(spl[2]))
            inst.append(True)
        except ValueError:
            inst.append(ord(spl[2]) - ord('w'))
            inst.append(False)
    else:
        inst.append(inp_count)
        inp_count += 1
        inst.append(None)
    instructions.append(inst)

parts = []
part = None
for inst in instructions:
    if inst[0] == InstructionType.inp:
        if part is not None:
            parts.append(part)
        part = []
    part.append(inst)
parts.append(part)

parts_simple = []
for part in parts:
    parts_simple.append((part[5][2], part[15][2], part[4][2] == 26))
    print(parts_simple[-1])


def int_div(a, b):
    return (abs(a) // b) * int(math.copysign(1, a))


def do_op(tp, v1, v2):
    if tp == InstructionType.add:
        return v1 + v2
    elif tp == InstructionType.mul:
        return v1 * v2
    elif tp == InstructionType.div:
        return int_div(v1, v2)
    elif tp == InstructionType.mod:
        return v1 % v2
    elif tp == InstructionType.eql:
        return int(v1 == v2)
    else:
        raise ValueError(tp)


def do_part(z: int, inp: int, c1: int, c2: int, do_z_div: bool):
    x = z % 26 + c1
    if do_z_div:
        z = int_div(z, 26)

    if x != inp:
        z *= 26
        z += inp + c2
        return z, True

    return z, False


max_dist = []
for i in range(13):
    remaining = parts_simple[i + 1:]
    dist = 0
    for part in remaining:
        if part[2]:
            dist += 1
        else:
            dist -= 1
    max_dist.append(dist)

inps = [int(c) for c in "13474238124685"]
while True:
    print("".join([str(c) for c in inps]))
    z = 0
    inc_index = None
    for i in range(14):
        z, exploded = do_part(z, inps[i], *parts_simple[i])
        dist = math.floor(math.log(z, 26)) if z > 0 else -1
        if i != 13 and dist > max_dist[i]:
            inc_index = i
            break

    if i == 13 and z == 0:
        print(z)
        h.submit("".join([str(c) for c in inps]), confirm_answer=False)
        break
    else:
        inc_index = inc_index or 13
        j = inc_index
        while j > 0 and inps[j] == 9:
            j -= 1
        inps[j] += 1
        for k in range(j + 1, 14):
            inps[k] = 1

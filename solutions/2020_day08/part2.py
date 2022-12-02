import copy

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2020, day=8)

inp = h.get_input_list()

instructions = [[row.split(' ')[0][0], int(row.split(' ')[1])] for row in inp]

for corrupt in range(len(instructions)):
    if instructions[corrupt][0] == 'a':
        continue
    inst = copy.deepcopy(instructions)
    if inst[corrupt][0] == 'j':
        inst[corrupt][0] = 'n'
    else:
        inst[corrupt][0] = 'j'

    accessed = [False] * len(instructions)

    pc = 0
    acc = 0
    looped = False
    while 0 <= pc < len(instructions):
        current_inst = inst[pc]
        if accessed[pc]:
            looped = True
            break
        accessed[pc] = True
        if current_inst[0] == 'a':
            acc += current_inst[1]
        elif current_inst[0] == 'j':
            pc += current_inst[1]
            continue
        pc += 1

    if pc == len(instructions):
        h.submit(acc, part=2)

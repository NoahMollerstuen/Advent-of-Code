import copy

from util import *
from util import Grid as g
from packets import *
import itertools as it
import re
import numpy as np


h = Helper(25)

grd = h.get_input_grid()
height = len(grd)
width = len(grd[0])

step = 0
while True:
    new_grd = copy.deepcopy(grd)
    for y, row in enumerate(grd):
        for x, cell in enumerate(row):
            if cell == '>' and g.get(grd, (y, (x + 1) % width)) == '.':
                new_grd[y][x] = '.'
                new_grd[y][(x + 1) % width] = '>'

    new_new_grd = copy.deepcopy(new_grd)
    for y, row in enumerate(new_grd):
        for x, cell in enumerate(row):
            if cell == 'v' and g.get(new_grd, ((y + 1) % height, x)) == '.':
                new_new_grd[y][x] = '.'
                new_new_grd[(y + 1) % height][x] = 'v'

    step += 1
    # g.print(new_grd, str(step))
    print(step)
    if new_new_grd == grd:
        h.submit(step)
        break

    grd = new_new_grd

from util import *
from util import Grid as g
from packets import *
import itertools as it
import re
import numpy as np

h = Helper(21)

inp = h.get_input_list()

last_roll = 0


def roll_die():
    global last_roll
    last_roll += 1
    if last_roll > 100:
        last_roll = 1
    return last_roll


scores = [0, 0]
spaces = [int(line[-1]) - 1 for line in inp]

turn = 0
rolls = 0
while True:
    roll = sum(roll_die() for i in range(3))
    rolls += 3

    spaces[turn] += roll
    spaces[turn] = spaces[turn] % 10

    scores[turn] += spaces[turn] + 1
    print(spaces[turn] + 1, scores[turn])

    if scores[turn] >= 1000:
        break

    turn = (turn + 1) % 2

print(min(scores), rolls)
h.submit(min(scores) * rolls)

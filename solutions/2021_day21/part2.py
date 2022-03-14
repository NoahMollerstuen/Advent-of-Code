from util import *
from util import Grid as g
from packets import *
import itertools as it
import re
import numpy as np

h = Helper(21)

inp = h.get_input_list()

scores = [0, 0]
spaces = [int(line[-1]) - 1 for line in inp]

weights = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


def count_wins(spaces, scores, turn):
    wins = [0, 0]
    new_turn = (turn + 1) % 2
    for roll in weights.keys():
        sp = spaces.copy()
        sp[turn] = (sp[turn] + roll) % 10
        sc = scores.copy()
        sc[turn] += sp[turn] + 1

        if sc[turn] >= 21:
            wins[turn] += weights[roll]
        else:
            results = count_wins(sp, sc, new_turn)
            wins[0] += results[0] * weights[roll]
            wins[1] += results[1] * weights[roll]
    return wins


total_wins = count_wins(spaces, scores, 0)
print(total_wins)

h.submit(max(total_wins))
from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_input="""A Y
B X
C Z""", test_mode=False)

inp = h.get_input_list()

scores = []
for round in inp:
    op = ord(round[0]) - 65
    goal = ord(round[2]) - 88

    you = (op + goal - 1) % 3
    if goal == 2:
        score = 6
    elif goal == 1:
        score = 3
    else:
        score = 0
    score += you + 1
    print(op, you, score)
    scores.append(score)

h.submit(sum(scores))

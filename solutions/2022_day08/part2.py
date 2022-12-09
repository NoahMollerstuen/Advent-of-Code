from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(test_mode=False, test_input="""30373
25512
65332
33549
35390""")

inp = h.get_input_grid()

scores = []

for y in range(len(inp)):
    for x in range(len(inp[0])):
        height = inp[y][x]
        score = 1
        for d in Grid.DIR4:
            t_y = y
            t_x = x
            dir_score = 0
            while True:
                t_y += d[0]
                t_x += d[1]
                tree = Grid.get(inp, (t_y, t_x))
                if tree is None:
                    break
                dir_score += 1
                if tree >= height:
                    break
            score *= dir_score

        scores.append(score)

        # print((y, x), height, visible)

h.submit(max(scores))

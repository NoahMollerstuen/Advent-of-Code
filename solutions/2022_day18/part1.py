from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""")

inp = h.get_input_list()

points = [tuple(int(n) for n in p.split(",")) for p in inp]

ADJ = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0),)

surface = 0
for p in points:
    print(p)
    for side in ADJ:
        side_coord = (p[0] + side[0], p[1] + side[1], p[2] + side[2])
        if side_coord not in points:
            surface += 1

h.submit(surface)

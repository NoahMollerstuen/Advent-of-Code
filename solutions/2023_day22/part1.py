import copy

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""")


def do_bricks_intersect(b1, b2):
    for a in range(3):
        b1_max = max(b1[0][a], b1[1][a])
        b1_min = min(b1[0][a], b1[1][a])
        b2_max = max(b2[0][a], b2[1][a])
        b2_min = min(b2[0][a], b2[1][a])
        if not (b1_min <= b2_max and b2_min <= b1_max):
            return False
    return True


inp = h.get_input_list()


falling_bricks = []

for line in inp:
    raw_coords = line.split('~')
    coords = [[int(n) for n in c.split(',')] for c in raw_coords]
    falling_bricks.append(coords)


falling_bricks.sort(key=lambda b: min(b[0][2], b[1][2]))
print(falling_bricks)

resting_bricks = []
would_cause_fall = []

for falling_brick in falling_bricks:
    while True:
        if min(falling_brick[0][2], falling_brick[1][2]) == 1:
            resting_bricks.append(falling_brick)
            break

        next_pos = copy.deepcopy(falling_brick)
        next_pos[0][2] -= 1
        next_pos[1][2] -= 1

        supporting_bricks = []
        for resting_brick in reversed(resting_bricks):
            if do_bricks_intersect(resting_brick, next_pos):
                supporting_bricks.append(resting_brick)

        if supporting_bricks:
            resting_bricks.append(falling_brick)
            if len(supporting_bricks) == 1 and supporting_bricks[0] not in would_cause_fall:
                would_cause_fall.append(supporting_bricks[0])
            break

        falling_brick = next_pos


print(resting_bricks)
print(would_cause_fall)

h.submit(len(resting_bricks) - len(would_cause_fall))

from util import *
from util import Grid as g
import itertools as it
import re
from queue import PriorityQueue


h = Helper(test_mode=False, test_input="""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""")

inp = h.get_input_grid()


def get_successors(state):
    pos = state[0]
    curr_dir = state[1]
    straight_line_steps = state[2]

    successors = []

    # Turning left or right
    for d in ((1, 0), (-1, 0)) if curr_dir[0] == 0 else ((0, 1), (0, -1)):
        successors.append(((pos[0] + d[0], pos[1] + d[1]), d, 1))

    if straight_line_steps < 3:
        successors.append(((pos[0] + curr_dir[0], pos[1] + curr_dir[1]), curr_dir, straight_line_steps + 1))

    return successors


q = PriorityQueue()
q.put((0, ((0, 0), (0, 1), 0)))

goal_pos = (len(inp) - 1, len(inp[0]) - 1)
visited = set()

while True:
    curr_cost, curr_state = q.get(block=False)

    if curr_state in visited:
        continue

    # print(curr_state)
    if curr_state == ((11, 7), (0, -1), 3):
        pass
    visited.add(curr_state)

    if curr_state[0] == goal_pos:
        h.submit(curr_cost)
        break

    for successor in get_successors(curr_state):
        if successor not in visited and (cost := Grid.get(inp, successor[0])) is not None:
            q.put(((curr_cost + int(cost)), successor))

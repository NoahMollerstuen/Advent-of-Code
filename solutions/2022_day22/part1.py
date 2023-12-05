from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""")

inp = h.get_input_raw()

board_raw, directions_raw = inp.split("\n\n")

board = [list(row) for row in board_raw.split("\n")]


FACING_MAP = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}


facing = 0
pos = [0, board[0].index('.')]

numbs = [int(n) for n in re.split(r"[RL]", directions_raw)]
turns = re.findall("[RL]", directions_raw)
directions = it.chain.from_iterable(it.zip_longest(numbs, turns))

for d in directions:
    print(d)
    if d is None:
        break

    if d == "R":
        facing = (facing + 1) % 4
    elif d == "L":
        facing = (facing - 1) % 4
    else:
        for _ in range(d):
            facing_tup = FACING_MAP[facing]

            first_move = True
            npos = pos.copy()
            while g.get(board, npos, ' ') == ' ' or first_move:
                first_move = False
                npos[0] = (npos[0] + facing_tup[0]) % len(board)
                npos[1] = (npos[1] + facing_tup[1]) % len(board[0])

            if g.get(board, npos) == '.':
                pos = npos

            print(pos)


h.submit(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing)

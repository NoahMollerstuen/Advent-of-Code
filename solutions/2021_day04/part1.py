import random

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(4)

inp = h.get_input_list()

draws = inp[0].split(",")
draws = [int(v) for v in draws]

inp = inp[2:]
# print(draws)
boards_raw = "\n".join(inp).split("\n\n")
# print(boards_raw[0])
boards = []
for b in boards_raw:
    rows = []
    for row in b.split("\n"):
        m = re.search(r"\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*", row)
        rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))])
    boards.append(rows)


def has_won(board, draws):
    pulled = [[board[i][j] in draws for i in range(5)] for j in range(5)]
    if any(all(row) for row in pulled):
        return True
    if any(all(row) for row in zip(*pulled)):
        return True

def get_score(board, draws):
    unmarked_score = sum([sum([v for v in r if v not in draws]) for r in board])
    return unmarked_score * draws[-1]

test_draws = []
for d in draws:
    test_draws.append(d)
    for board in boards:
        if has_won(board, test_draws):
            print(board)
            print(test_draws)
            h.submit(get_score(board, test_draws))

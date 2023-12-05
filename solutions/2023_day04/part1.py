from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""")

inp = h.get_input_list()

scratches = []
for line in inp:
    card_num = int(line.split(':')[0].lstrip("Card "))

    your_nums = [int(n) for n in line.split(':')[1].split(" | ")[0].strip(" ").split(" ") if len(n)]
    win_nums = [int(n) for n in line.split(':')[1].split(" | ")[1].strip(" ").split(" ") if len(n)]

    scratches.append((card_num, your_nums, win_nums))


score = 0
for scratch in scratches:
    # print(scratch)
    your_win_nums = [n for n in scratch[1] if n in scratch[2]]
    if your_win_nums:
        score += 2 ** (len(your_win_nums) - 1)
        print(score)

h.submit(score)

import operator

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
Time:      7  15   30
Distance:  9  40  200
""")

inp = h.get_input_list()

time = int(inp[0].split(":")[1].replace(' ', ''))
dist = int(inp[1].split(":")[1].replace(' ', ''))


def get_race_distance(total_time, hold_time):
    return (total_time - hold_time) * hold_time


def count_winning_times(max_time, dist_to_beat):
    c = 0
    for ht in range(max_time):
        if get_race_distance(max_time, ht) > dist_to_beat:
            c += 1
    return c


h.submit(count_winning_times(time, dist))

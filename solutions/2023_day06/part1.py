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


def get_race_distance(total_time, hold_time):
    return (total_time - hold_time) * hold_time


def count_winning_times(max_time, dist_to_beat):
    c = 0
    for ht in range(max_time):
        if get_race_distance(max_time, ht) > dist_to_beat:
            c += 1
    return c


times = [int(n) for n in inp[0].split(" ")[1:] if n]
distances = [int(n) for n in inp[1].split(" ")[1:] if n]


races = list(zip(times, distances))


h.submit(list(it.accumulate((count_winning_times(*r) for r in races), operator.mul))[-1])



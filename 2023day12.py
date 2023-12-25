import functools

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(day=12, test_mode=True, test_input="""
??? 1
""")

inp = h.get_input_list()


@functools.cache
def check_record_consistency(springs, groups):
    springs = list(springs)
    group_len = 0
    group_index = -1
    in_group = False
    for c in springs + ["."]:
        if c == '?':
            return True
        if in_group:
            if c == "#":
                group_len += 1
                if group_len > groups[group_index]:
                    return False
            else:
                if groups[group_index] != group_len:
                    return False
                in_group = False
        else:
            if c == "#":
                group_index += 1
                if group_index >= len(groups):
                    return False
                in_group = True
                group_len = 1

    return group_index == len(groups) - 1


def count_valid_combinations(springs, groups):
    springs = list(springs)
    if '?' not in springs:
        return 1

    question_index = springs.index('?')

    total_options = 0

    for c in ".#":
        springs[question_index] = c
        if check_record_consistency(tuple(springs), groups):
            total_options += count_valid_combinations(tuple(springs), groups)

    return total_options


records = []

for line in inp:
    records.append((
        list("?".join(it.repeat(line.split(" ")[0], 5))),
        list(it.chain.from_iterable(it.repeat(list(int(d) for d in line.split(" ")[1].split(",")), 5)))
    ))
    # print(records[-1])
    # print("".join(records[-1][0]))
    # print(records[-1][1])


options_sum = 0
for record in records:
    print("".join(record[0]), ",".join(str(n) for n in record[1]))
    options = count_valid_combinations(tuple(record[0]), tuple(record[1]))
    print(options)
    options_sum += options

h.submit(options_sum)

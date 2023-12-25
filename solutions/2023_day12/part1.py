from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""")

inp = h.get_input_list()


def check_record_consistency(springs, groups):
    group_len = 0
    group_index = -1
    in_group = False
    for c in springs + ["."]:
        if c == '?':
            return True
        if in_group:
            if c == "#":
                group_len += 1
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
    if '?' not in springs:
        return 1

    question_index = springs.index('?')

    total_options = 0

    for c in ".#":
        springs[question_index] = c
        if check_record_consistency(springs, groups):
            total_options += count_valid_combinations(springs.copy(), groups)

    return total_options


records = []

for line in inp:
    records.append((list(line.split(" ")[0]), tuple(int(d) for d in line.split(" ")[1].split(","))))


options_sum = 0
for record in records:
    options = count_valid_combinations(record[0].copy(), record[1])
    options_sum += options

h.submit(options_sum)

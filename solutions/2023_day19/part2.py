import copy
import functools
import operator

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""")


def count_accepted_parts(name, flows, ranges):
    print(name, ranges)
    if name == 'A':
        return functools.reduce(operator.mul, (v2 - v1 for v2, v1 in ranges.values()))

    if name == 'R':
        return 0

    flow = flows[name]
    ranges = {k: copy.copy(v) for k, v in ranges.items()}

    total_accepted = 0
    for cond in flow[0]:
        if cond[3] == '>':
            if not ranges[cond[1]][1] - 1 > cond[2]:
                continue
            if ranges[cond[1]][0] > cond[2]:
                return count_accepted_parts(cond[0], flows, ranges)

            new_ranges = {k: copy.copy(v) for k, v in ranges.items()}
            new_ranges[cond[1]][0] = cond[2] + 1
            total_accepted += count_accepted_parts(cond[0], flows, new_ranges)
            ranges[cond[1]][1] = cond[2] + 1
        else:
            if not ranges[cond[1]][0] < cond[2]:
                continue
            if ranges[cond[1]][1] - 1 < cond[2]:
                return count_accepted_parts(cond[0], flows, ranges)
            new_ranges = {k: copy.copy(v) for k, v in ranges.items()}
            new_ranges[cond[1]][1] = cond[2]
            total_accepted += count_accepted_parts(cond[0], flows, new_ranges)
            ranges[cond[1]][0] = cond[2]
    return total_accepted + count_accepted_parts(flow[1], flows, ranges)


inp = h.get_input_list_2d()

workflows = {}
for line in inp[0]:
    m = re.fullmatch(r"(\w+)\{((?:[xmas][><]\d+:\w+,)+)(\w+)}", line)
    name = m.group(1)
    flows_raw = m.group(2)
    default = m.group(3)

    flows = []
    for f in flows_raw.strip(',').split(','):
        var = f[0]
        op = f[1]
        thresh = int(f.split(':')[0][2:])
        next_name = f.split(':')[1]
        if op in '<>':
            flows.append((next_name, var, thresh, op))
        else:
            raise ValueError(op)

    workflows[name] = (flows, default)


h.submit(count_accepted_parts("in", workflows, {k: [1, 4001] for k in 'xmas'}))

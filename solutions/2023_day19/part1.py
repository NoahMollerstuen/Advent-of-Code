import functools

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
        if op == '>':
            flows.append((functools.partial(lambda v, th, p: p[v] > th, var, thresh), next_name))
        elif op == '<':
            flows.append((functools.partial(lambda v, th, p: p[v] < th, var, thresh), next_name))
        else:
            raise ValueError(op)

    workflows[name] = (flows, default)


parts = []
for line in inp[1]:
    parts.append({v[0]: int(v[2:]) for v in line.strip('{}').split(',')})


total_rating = 0
for part in parts:
    print(part)
    flow_name = "in"

    while True:
        flow = workflows[flow_name]

        for cond in flow[0]:
            if cond[0](part):
                flow_name = cond[1]
                break
        else:
            flow_name = flow[1]

        if flow_name == 'R':
            print('R')
            break

        if flow_name == 'A':
            print('A')
            total_rating += sum(part.values())
            break

h.submit(total_rating)

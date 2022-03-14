from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(12)

inp = h.get_input_list()

edges = {}
for line in inp:
    # print(line)
    rm1, rm2 = line.split("-")
    if rm1 not in edges.keys():
        edges[rm1] = []
    if rm2 not in edges.keys():
        edges[rm2] = []
    edges[rm1].append(rm2)
    edges[rm2].append(rm1)

print(edges)


def count_paths(start, end, egs, visited):
    visited = visited.copy()
    if start == start.lower():
        visited.append(start)

    total_paths = 0
    for e in egs[start]:
        if e in visited:
            continue
        if e == end:
            total_paths += 1
        else:
            total_paths += count_paths(e, end, egs, visited)
    return total_paths


h.submit(count_paths("start", "end", edges, []))

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np


h = Helper(year=2018, day=7)

inp = h.get_input_list()

deps = []

for step in inp:
    m = re.match(r"Step (\S) must be finished before step (\S) can begin\.", step)
    deps.append(m.groups())

completed_steps = []

tick = 0
workers = [None] * 5
time_left = [None] * 5
while True:
    for i in range(5):
        if workers[i] is not None:
            if time_left[i] > 0:
                time_left[i] -= 1
            else:
                completed_steps.append(workers[i])
                workers[i] = None

    for i in range(5):
        if workers[i] is not None:
            continue
        not_ready = set()
        for dep in deps:
            if dep[0] not in completed_steps:
                not_ready.add(dep[1])
        for c in ALPHABET.upper():
            if c not in completed_steps and c not in not_ready and c not in workers:
                workers[i] = c
                time_left[i] = 60 + 1 + ALPHABET.index(c.lower()) - 1
                print(tick, workers)
                break

    if len(completed_steps) == 26:
        h.submit(tick)
        break

    tick += 1

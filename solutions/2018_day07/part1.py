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

while True:
    not_ready = set()
    for dep in deps:
        if dep[0] not in completed_steps:
            not_ready.add(dep[1])
    for c in ALPHABET.upper():
        if c not in completed_steps and c not in not_ready:
            completed_steps.append(c)
            break

    if len(completed_steps) == 26:
        h.submit("".join(completed_steps))

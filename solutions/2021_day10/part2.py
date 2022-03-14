from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(10)

inp = h.get_input_list()

incomplete = []
for line in inp:
    stack = []
    corrupted = False
    for c in line:
        if c in ("<", "(", "[", "{"):
            stack.append(c)
        elif c == ")":
            if stack.pop() != "(":
                corrupted = True
                break
        elif c == "]":
            if stack.pop() != "[":
                corrupted = True
                break
        elif c == "}":
            if stack.pop() != "{":
                corrupted = True
                break
        elif c == ">":
            if stack.pop() != "<":
                corrupted = True
                break
    if not corrupted:
        incomplete.append(line)

print(incomplete)

VALUES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

scores = []
for line in incomplete:
    stack = []
    for c in line:
        if c in ("<", "(", "[", "{"):
            stack.append(c)
        else:
            stack.pop()
    print(stack)
    score = 0
    while len(stack) > 0:
        c = stack.pop()
        score = score * 5
        score += VALUES[c]
    scores.append(score)
    print(score)

scores.sort()
print(len(scores))

h.submit(scores[int((len(scores) - 1) / 2)])

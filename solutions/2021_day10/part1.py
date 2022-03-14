from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(10)

inp = h.get_input_list()

score = 0
for line in inp:
    stack = []
    for c in line:
        print(stack)
        if c in ("<", "(", "[", "{"):
            stack.append(c)
        elif c == ")":
            if stack.pop() != "(":
                score += 3
                break
        elif c == "]":
            if stack.pop() != "[":
                score += 57
                break
        elif c == "}":
            if stack.pop() != "{":
                score += 1197
                break
        elif c == ">":
            if stack.pop() != "<":
                score += 25137
                break

h.submit(score)

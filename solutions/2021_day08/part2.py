from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(8)

inp = h.get_input_list()

COMBS = [
    (0, 1, 2, 4, 5, 6),
    (2, 5),
    (0, 2, 3, 4, 6),
    (0, 2, 3, 5, 6),
    (1, 2, 3, 5),
    (0, 1, 3, 5, 6),
    (0, 1, 3, 4, 5, 6),
    (0, 2, 5),
    (0, 1, 2, 3, 4, 5, 6),
    (0, 1, 2, 3, 5, 6)
]

displays = []
outputs = []
for line in inp:
    displays.append(line.split(" | ")[0].split(" "))
    out = line.split(" | ")[1].split(" ")
    outputs.append(out)

print(displays)


def letter_to_int(l):
    return ord(l) - ord("a")


def check_perm(d, p):
    # print(d, p)
    for digit in d:
        # print(tuple(p[letter_to_int(c)] for c in digit))
        if tuple(sorted(p[letter_to_int(c)] for c in digit)) not in COMBS:
            return False
    return True

total = 0
for output, display in zip(outputs, displays):
    for permutation in it.permutations(range(7)):
        if check_perm(display, permutation):
            print("WORKED: " + str(permutation))
            pv = 1000
            s = 0
            for digit in output:
                s += COMBS.index(tuple(sorted(permutation[letter_to_int(c)] for c in digit))) * pv
                pv /= 10
            print(s)
            total += s
            break
h.submit(int(total))

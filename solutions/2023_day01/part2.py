from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
nineight
""")

inp = h.get_input_list()

calibrations = []

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

s = "(?=(" + "|".join(DIGITS.keys())+r"|\d" + "))"
print(s)


for line in inp:
    cals = []
    f = [m[1] for m in (re.finditer(s, line))]
    print(f)
    for m in f:
        print(m)
        try:
            cals.append(int(m))
        except ValueError:
            cals.append(DIGITS[m])
    print(line)
    print(cals)
    calibrations.append(int(str(cals[0]) + str(cals[-1])))
    print(calibrations[-1])

print(len(calibrations), max(calibrations), min(calibrations))
h.submit(sum(calibrations))

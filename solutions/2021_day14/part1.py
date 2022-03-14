from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(14)

inp = h.get_input_list()

s = inp[0]
inp = inp[2:]


replacements = {}
for line in inp:
    split = line.split(" -> ")
    replacements[split[0]] = split[1]


for _ in range(10):
    i = 0
    while i + 1 < len(s):
        if s[i:i + 2] in replacements.keys():
            s = s[:i+1] + replacements[s[i:i + 2]] + s[i+1:]
            i += 1
        i += 1

chars = {}
for c in s:
    if c not in chars.keys():
        chars[c] = 0
    chars[c] += 1

h.submit(max(chars.values()) - min(chars.values()))


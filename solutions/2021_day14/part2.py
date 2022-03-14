from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(14)

inp = h.get_input_list()

s = inp[0]
inp = inp[2:]


insertions = {}
for line in inp:
    split = line.split(" -> ")
    insertions[split[0]] = split[1]


pairs = {}
for r in insertions.keys():
    pairs[r] = 0

for i in range(len(s) - 1):
    if s[i:i + 2] in pairs.keys():
        pairs[s[i:i + 2]] += 1

print(pairs)

new_pairs = {}
for _ in range(40):
    for r in insertions.keys():
        new_pairs[r] = 0

    for p in pairs.keys():
        insert = insertions[p]
        p1 = p[0] + insert
        p2 = insert + p[1]
        if p1 in pairs.keys():
            new_pairs[p1] += pairs[p]
        if p2 in pairs.keys():
            new_pairs[p2] += pairs[p]
        pairs[p] = 0

    for k, v in new_pairs.items():
        pairs[k] += v


chars = {}
for pair in pairs.keys():
    for c in pair:
        if c not in chars.keys():
            chars[c] = 0
        chars[c] += pairs[pair]

chars[s[0]] += 1
chars[s[-1]] += 1

print(s)
for k, v in chars.items():
    if v % 2 == 1:
        print(k)
    chars[k] = int(v / 2)


h.submit(max(chars.values()) - min(chars.values()))

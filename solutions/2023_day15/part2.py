from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""")

inp = h.get_input_raw()
inp = inp.replace("\n", "")
inp = inp.split(",")


def ascii_hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val


hashmap = [[] for _ in range(256)]

for code in inp:
    if code[-1] == "-":
        hsh = ascii_hash(code[:-1])
        for lens in hashmap[hsh]:
            if lens[0] == code[:-1]:
                hashmap[hsh].remove(lens)
    else:
        hsh = ascii_hash(code[:-2])
        focus = code[-1]
        for lens in hashmap[hsh]:
            if lens[0] == code[:-2]:
                lens[1] = focus
                break
        else:
            hashmap[hsh].append([code[:-2], focus])


print(hashmap)

total = 0
for i, box in enumerate(hashmap):
    for j, lens in enumerate(box):
        total += (1 + i) * (1 + j) * int(lens[1])

h.submit(total)

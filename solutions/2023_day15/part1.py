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


total = 0
for code in inp:
    print(ascii_hash(code))
    total += ascii_hash(code)

h.submit(total)

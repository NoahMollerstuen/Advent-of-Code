import functools

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""")

inp = h.get_input_raw()

packets = [eval(line) for line in inp.split("\n") if line != ""]
packets.append([[2]])
packets.append([[6]])

def compare(left, right):
    t_left = type(left)
    t_right = type(right)
    if t_left == int and t_right == int:
        if left < right:
            return True, False
        if left > right:
            return False, True
        else:
            return False, False
    elif t_left == list and t_right == list:
        for i in it.count():
            if i == len(left) and i == len(right):
                return False, False
            if i == len(left):
                return True, False
            if i == len(right):
                return False, True
            r, w = compare(left[i], right[i])
            if r or w:
                return r, w

    else:
        if t_left == list:
            return compare(left, [right])
        else:
            return compare([left], right)


s = sorted(packets, key=functools.cmp_to_key(lambda x, y: -1 if compare(x, y)[0] else 1))
for p in s:
    print(p)

decoders = []
for i, p in enumerate(s):
    if str(p) in ("[[2]]", "[[6]]"):
        decoders.append(i + 1)

print(decoders)
h.submit(decoders[0] * decoders[1])

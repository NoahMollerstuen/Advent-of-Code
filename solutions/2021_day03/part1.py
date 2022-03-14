from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(3)

inp = h.get_input_raw().split("\n")

b = [0 for i in inp[0]]
for n in inp:
    for i, bit in enumerate(n):
        print(bit, i)
        b[i] += int(bit)

print(b)
epsilon = [bit > len(inp) / 2 for bit in b]
gamma = [bit < len(inp) / 2 for bit in b]
print(epsilon)
print(gamma)

d = 1
e = 0
g = 0
epsilon.reverse()
gamma.reverse()
for i in range(len(gamma)):
    e += epsilon[i] * d
    g += gamma[i] * d
    d = d * 2
h.submit(e*g)

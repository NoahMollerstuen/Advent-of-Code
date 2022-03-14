from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(2, year=2018)

inp = h.get_input_list()

twos = 0
threes = 0

for line in inp:
    for c in "qwertyuiopasdfghjklzxcvbnm":
        count = len([i for i in line if i == c])
        if count == 2:
            twos += 1
            break

for line in inp:
    for c in "qwertyuiopasdfghjklzxcvbnm":
        count = len([i for i in line if i == c])
        if count == 3:
            threes += 1
            break


print(twos, threes)
h.submit(twos * threes)
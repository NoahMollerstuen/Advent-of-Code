from util import Helper
import itertools as it
import re

h = Helper(1)

inp = h.get_input_list()

h.submit(len([i for i in range(len(inp) - 1) if inp[i + 1] > inp[i]]))

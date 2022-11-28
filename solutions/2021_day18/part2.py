import copy
import math

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(18)

inp = h.get_input_list()


def parse_numb(s):
    s = s.strip(" ")

    depth = 0
    for i, c in enumerate(s):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif depth == 1 and c == ",":
            s = s[:i] + "#" + s[i + 1:]
    s = s[1:-1]
    elements = s.split("#")

    out = []
    for element in elements:
        try:
            out.append(int(element))
        except ValueError:
            out.append(parse_numb(element))
    return out


def add_nums(n1, n2):
    out = [copy.deepcopy(n1), copy.deepcopy(n2)]

    while True:
        exploded = True
        while exploded:
            _, _, exploded = handle_explosion(out, 0)

        if not handle_split(out):
            break

    return out


def handle_explosion(arr: list, depth):
    prop_l, prop_r = None, None
    exploded = False
    i = 0
    for i, element in enumerate(arr):
        if type(element) == list:
            if depth == 3:
                arr[i] = 0
                prop_l, prop_r = element[0], element[1]
                exploded = True
                break
            else:
                prop_l, prop_r, exploded = handle_explosion(element, depth + 1)
                if exploded:
                    break

    if prop_l is not None:
        if i - 1 >= 0:
            if type(arr[i - 1]) is int:
                arr[i - 1] += prop_l
                prop_l = None
            else:
                prop_arr = arr[i - 1]
                while True:
                    if type(prop_arr[1]) is int:
                        prop_arr[1] += prop_l
                        prop_l = None
                        break
                    prop_arr = prop_arr[i]

    if prop_r is not None and i + 1 < len(arr):
        if type(arr[i + 1]) is int:
            arr[i + 1] += prop_r
            prop_r = None
        else:
            prop_arr = arr[i + 1]
            while True:
                if type(prop_arr[0]) is int:
                    prop_arr[0] += prop_r
                    prop_r = None
                    break
                prop_arr = prop_arr[0]

    return prop_l, prop_r, exploded


def handle_split(arr):
    for i, e in enumerate(arr):
        if type(e) is int:
            if e > 9:
                arr[i] = [math.floor(e / 2), math.ceil(e / 2)]
                return True
        else:
            if handle_split(e):
                return True
    return False


def get_magnitude(arr):
    mag = 0

    weights = (3, 2)
    for i, e in enumerate(arr):
        if type(e) is int:
            mag += weights[i] * e
        else:
            mag += weights[i] * get_magnitude(e)
    return mag


max_mag = 0
for comb in it.permutations([parse_numb(s) for s in inp], 2):
    max_mag = max(max_mag, get_magnitude(add_nums(comb[0], comb[1])))


h.submit(max_mag)

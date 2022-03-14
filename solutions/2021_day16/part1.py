from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(16)

inp = h.get_input_raw()

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def bin_to_int(b):
    i = len(b) - 1
    v = 1
    s = 0
    while i >= 0:
        s += int(b[i]) * v
        i -= 1
        v *= 2
    return s


bin_str = ""
for c in inp:
    bin_str += hex_to_bin[c]


def get_total_version(bit_string):
    total_version = bin_to_int(bit_string[:3])
    packet_type = bin_to_int(bit_string[3:6])

    if packet_type == 4:
        # Literal
        i = 6
        while bit_string[i] == "1":
            i += 5
        i += 5
        return total_version, i

    else:
        # Operator
        length_type = int(bit_string[6])
        if length_type == 0:
            subpackets_len = bin_to_int(bit_string[7:22])
            total_len = 22 + subpackets_len
            i = 22
            while i < total_len:
                rets = get_total_version(bit_string[i:total_len])
                total_version += rets[0]
                i += rets[1]
            return total_version, total_len

        num_subpackets = bin_to_int(bit_string[7:18])
        i = 18
        for _ in range(num_subpackets):
            rets = get_total_version(bit_string[i:])
            total_version += rets[0]
            i += rets[1]
        return total_version, i


h.submit(get_total_version(bin_str)[0])

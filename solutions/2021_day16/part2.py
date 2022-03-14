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


def eval_packet(bit_string):
    packet_type = bin_to_int(bit_string[3:6])

    if packet_type == 4:
        # Literal
        i = 6
        literal_str = ""
        done = False
        while not done:
            done = bit_string[i] == "0"
            literal_str += bit_string[i + 1:i + 5]
            i += 5
        return bin_to_int(literal_str), i

    else:
        # Operator
        sub_values = []

        length_type = int(bit_string[6])
        if length_type == 0:
            subpackets_len = bin_to_int(bit_string[7:22])
            total_len = 22 + subpackets_len
            i = 22
            while i < total_len:
                rets = eval_packet(bit_string[i:total_len])
                sub_values.append(rets[0])
                i += rets[1]
        else:
            num_subpackets = bin_to_int(bit_string[7:18])
            i = 18
            for _ in range(num_subpackets):
                rets = eval_packet(bit_string[i:])
                sub_values.append(rets[0])
                i += rets[1]

        if packet_type == 0:
            return sum(sub_values), i
        if packet_type == 1:
            p = 1
            for v in sub_values:
                p *= v
            return p, i
        if packet_type == 2:
            return min(sub_values), i
        if packet_type == 3:
            return max(sub_values), i
        if packet_type == 5:
            return int(sub_values[0] > sub_values[1]), i
        if packet_type == 6:
            return int(sub_values[0] < sub_values[1]), i
        if packet_type == 7:
            return int(sub_values[0] == sub_values[1]), i


h.submit(eval_packet(bin_str)[0])

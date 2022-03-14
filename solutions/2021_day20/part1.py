import numpy as np

from util import *
from util import Grid as g
from packets import *
import itertools as it
import re

h = Helper(20)
# h = Helper(20, test_input="""..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###""")

inp = h.get_input_list()

algo = [int(c == "#") for c in inp[0]]
print(algo, "\n")

mp = np.pad(np.array([[int(c == "#") for c in row] for row in inp[2:]], int), 10, constant_values=0)


def do_step(mat):
    new_mat = mat.copy()

    for i in range(mat.shape[0] - 2):
        for j in range(mat.shape[1] - 2):
            region = mat[i:i+3, j:j+3]
            bits = "".join([str(n) for n in region.flatten()])
            index = bin_to_int(bits)
            new_mat[i + 1][j + 1] = algo[index]
    return new_mat


mp = do_step(mp)
mp = do_step(mp)

mp = mp[3:-3,3:-3]

for row in mp:
    print("".join([str(n) for n in row]))

h.submit(np.sum(mp))

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(13)

inp = h.get_input_raw()
s = inp.split("\n\n")
dots = [(int(r.split(",")[1]), int(r.split(",")[0])) for r in s[0].split("\n")]
folds = [r.split(" ")[2] for r in s[1].split("\n")]


def do_fold(dts, fold):
    ax = fold.split("=")[0]
    val = int(fold.split("=")[1])

    new_dots = []

    for d in dts:
        if ax == "x":
            if d[1] > val:
                new_d = (d[0], 2 * val - d[1])
            else:
                new_d = d
        else:
            if d[0] > val:
                new_d = (2 * val - d[0], d[1])
            else:
                new_d = d
        if new_d not in new_dots:
            new_dots.append(new_d)
    return new_dots


for fold in folds:
    dots = do_fold(dots, fold)


height = max(pos[0] for pos in dots) + 1
width = max(pos[1] for pos in dots) + 1

grd = [[" " for i in range(width)] for j in range(height)]

for d in dots:
    grd[d[0]][d[1]] = "#"

g.print(grd)

# Grid.print from util file:
@staticmethod
def print(grid: t.List[t.List[t.Any]], name="unnamed grid", crush=True):
    print(f"{name} printout, crush={crush}")
    for row in grid:
        print("".join([str(c)[0] if crush else str(c) for c in row]))
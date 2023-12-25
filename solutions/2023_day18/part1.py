from collections import defaultdict

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""")

inp = h.get_input_list()


DIR_NAMES = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}


vertical_edges = []
horizontal_edges = []
pos = (0, 0)

for line in inp:
    m = re.match(r"(\w) (\d+) \(#(.{6})\)", line)

    d = DIR_NAMES[m.group(1)]
    length = int(m.group(2))

    new_pos = (pos[0] + d[0] * length, pos[1] + d[1] * length)

    (vertical_edges if d[1] == 0 else horizontal_edges).append((pos, new_pos, m.group(3)))

    pos = new_pos

y_bounds = (min(min(e[0][0], e[1][0]) for e in vertical_edges), max(max(e[0][0], e[1][0]) for e in vertical_edges))

area = 0
for y in range(y_bounds[0], y_bounds[1] + 1):
    intersecting_edges = []
    for e in vertical_edges:
        p1 = e[0]
        p2 = e[1]
        max_y = max(p1[0], p2[0])
        min_y = min(p1[0], p2[0])

        if min_y <= y <= max_y:
            intersecting_edges.append(e)

    interior = False
    on_edge = False
    last_x = 0
    last_was_dug = False

    for e in sorted(intersecting_edges, key=lambda e: e[0][1]):
        p1 = e[0]
        p2 = e[1]
        max_y = max(p1[0], p2[0])
        min_y = min(p1[0], p2[0])

        x = p1[1]
        if on_edge or interior:
            area += x - last_x

        last_x = x

        if y == max_y:
            on_edge = not on_edge
        elif y == min_y:
            on_edge = not on_edge
            interior = not interior
        else:
            interior = not interior

        if not last_was_dug and (interior or on_edge):
            area += 1
        last_was_dug = interior or on_edge

    assert not on_edge
    assert not interior

h.submit(area)

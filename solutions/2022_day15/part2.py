from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""")

inp = h.get_input_list()

sensors = []
beacons = []
dists = []
for line in inp:
    m = re.findall(r"[\d|-]+", line)
    sensors.append((int(m[0]), int(m[1])))
    beacons.append((int(m[2]), int(m[3])))
    dists.append(abs(sensors[-1][0] - beacons[-1][0]) + abs(sensors[-1][1] - beacons[-1][1]))


def check_cell(x, y):
    for i, s in enumerate(sensors):
        d = dists[i]
        if abs(s[0] - x) + abs(s[1] - y) <= d:
            return
    h.submit(x * 4000000 + y)


for i, s in enumerate(sensors):
    d = dists[i]
    print(d)
    for x in range(s[0] - d - 1, s[0] + d + 2):
        if not 0 <= x <= 4000000:
            continue
        y1 = s[1] - (d - abs(s[0] - x) + 1)
        y2 = s[1] - (d - abs(s[0] - x) + 1)
        if 0 <= y1 <= 4000000:
            check_cell(x, y1)
        if 0 <= y2 <= 4000000:
            check_cell(x, y2)

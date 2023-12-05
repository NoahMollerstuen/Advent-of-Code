from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""

""")

inp = h.get_input_list()

sensors = []
beacons = []
dists = []
for line in inp:
    m = re.findall(r"\d+", line)
    sensors.append((int(m[0]), int(m[1])))
    beacons.append((int(m[2]), int(m[3])))
    dists.append(abs(sensors[-1][0] - beacons[-1][0]) + abs(sensors[-1][1] - beacons[-1][1]))


def merge_if_needed(seg1, seg2):
    if seg1[1] < seg2[0] or seg2[1] < seg1[0]:
        return None
    return min(seg1[0], seg2[0]), max(seg1[1], seg2[1])


segments = []
for i, s in enumerate(sensors):
    print(s)
    b = beacons[i]
    d = dists[i]
    dist_from_line = abs(s[1] - 2000000)
    if dist_from_line > d:
        continue
    seg = (s[0] - (d - dist_from_line), s[0] + (d - dist_from_line) + 1)

    new_segments = []
    for old_seg in segments:
        merge = merge_if_needed(old_seg, seg)
        if merge is None:
            new_segments.append(old_seg)
        else:
            seg = merge
    new_segments.append(seg)
    segments = new_segments

tot = sum(s[1] - s[0] for s in segments)
tot -= len(set(b for b in beacons if b[1] == 2000000))

h.submit(tot)

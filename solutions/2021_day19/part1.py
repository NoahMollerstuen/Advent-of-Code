import numpy.linalg

from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np
from collections import defaultdict

h = Helper(19)

inp = h.get_input_raw()
scanners_raw = inp.split("\n\n")
scanners_lists = []
for sc in scanners_raw:
    sc_list = []
    for coord in sc.split("\n")[1:]:
        sc_list.append([int(n) for n in coord.split(",")])
    scanners_lists.append(sc_list)

scanner_mats = [np.array(sc) for sc in scanners_lists]

all_rotations = []
for perm in it.permutations(range(3), 3):
    for invs in it.product((-1, 1), (-1, 1), (-1, 1)):
        mat = np.zeros((3, 3), int)
        for i in range(3):
            mat[i][perm[i]] = invs[i]
        if np.linalg.det(mat) > 0:
            all_rotations.append(mat)

matched_offsets = {0: np.array((0, 0, 0), int)}
matched_rotations = {0: np.identity(3, int)}

scanner_queue = [0]
to_process = list(range(len(scanner_mats)))
to_process.remove(0)

while len(to_process) > 0:
    sc_id = scanner_queue.pop(0)
    sc = scanner_mats[sc_id]

    matched = []
    for check_scanner_id in to_process:
        check_scanner = scanner_mats[check_scanner_id]

        for rot in all_rotations:
            offsets = defaultdict(lambda: 0)
            transformed_coords = check_scanner.dot(rot)
            for c1, c2 in it.product(tuple(sc), tuple(transformed_coords)):
                offsets[tuple(c1 - c2)] += 1
            matches = [of for of, v in offsets.items() if v >= 12]
            if len(matches) > 0:
                # Match found
                print("Matched", check_scanner_id)
                offset = matches[0]
                matched_offsets[check_scanner_id] = matched_offsets[sc_id] + \
                                                    np.array(offset, int).dot(matched_rotations[sc_id])
                matched_rotations[check_scanner_id] = rot.dot(matched_rotations[sc_id])

                matched.append(check_scanner_id)
                scanner_queue.append(check_scanner_id)
                break
    for m in matched:
        to_process.remove(m)

all_beacons = set()
for i, sc in enumerate(scanner_mats):
    for coord in sc:
        all_beacons.add(tuple(coord.dot(matched_rotations[i]) + matched_offsets[i]))

for b in all_beacons:
    print(b)

h.submit(len(all_beacons))
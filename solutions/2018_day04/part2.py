from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(4, year=2018)

inp = h.get_input_list()

records = []
id = 0
for line in inp:
    m = re.search(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)] (.*)", line)
    records.append([m, int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))])

print("Sorting")
records.sort(key=lambda r: r[1] * 1000 * 24 * 3600 + r[2] * 100 * 24 * 3600 + r[3] * 24 * 3600 + r[4] * 3600 + r[5] * 60)

# for r in records:
#     print(r[0].group(0))

id = 0
mins_asleep = {}
sleep_time = 0
for r in records:
    m = r[0]
    msg = m.group(6)
    if "begins shift" in msg:
        id = int(msg.split(" ")[1].strip("#"))
        if id not in mins_asleep.keys():
            mins_asleep[id] = 0
    else:
        if "falls asleep" in msg:
            sleep_time = r[5]
        if "wakes" in msg:
            mins_asleep[id] += r[5] - sleep_time

max_mins = max(mins_asleep.values())
id_choice = [k for k, v in mins_asleep.items() if v == max_mins][0]

max_asleep_by_id = {}
min_choice_by_id = {}
for id_choice in mins_asleep.keys():
    asleep_count = [0]*60
    id = 0
    for r in records:
        m = r[0]
        msg = m.group(6)
        if "begins shift" in msg:
            id = int(msg.split(" ")[1].strip("#"))
        elif id == id_choice:
            if "falls asleep" in msg:
                sleep_time = r[5]
            if "wakes" in msg:
                for i in range(sleep_time, r[5]):
                    asleep_count[i] += 1

    max_asleep = max(asleep_count)
    min_choice = [i for i, c in enumerate(asleep_count) if c == max_asleep][0]
    max_asleep_by_id[id_choice] = [max_asleep]
    min_choice_by_id[id_choice] = min_choice

max_max_asleep = max(max_asleep_by_id.values())
print(max_asleep_by_id)
final_choice = [k for k, v in max_asleep_by_id.items() if v == max_max_asleep][0]
min_choice = min_choice_by_id[final_choice]

print(min_choice)
h.submit(final_choice * min_choice)
from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""")

inp = h.get_input_list()

adj_list = {}
flow_rates = {}
for line in inp:
    m = re.match(r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)", line)
    flow_rates[m[1]] = int(m[2])
    adj_list[m[1]] = m[3].split(", ") or m[3]

print(adj_list)

q = [('AA', {k: False for k in adj_list.keys()}, 0, 0)]
final_states = []
while len(q) > 0:
    room, valve_states, tick, score = q.pop(0)
    if tick == 30:
        final_states.append((room, valve_states, tick, score))
        continue

    new_states = []
    if not valve_states[room] and flow_rates[room] > 0:
        new_valves = {k: True if k == room else v for k, v in valve_states.items()}
        new_states.append((room, new_valves, tick + 1, score + (29 - tick) * flow_rates[room]))
    for neighbor in adj_list[room]:
        new_states.append((neighbor, valve_states, tick + 1, score))

    for state in new_states:
        redundant = False

        for s in q:
            if state[0] == s[0] and state[3] <= s[3]:
                redundant = True
                break

        if not redundant:
            q.append(state)

print(final_states)
h.submit(max(s[3] for s in final_states))

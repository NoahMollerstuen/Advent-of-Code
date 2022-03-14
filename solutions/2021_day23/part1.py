import copy

from util import *
from util import Grid as g
from packets import *
import itertools as it
import re
import numpy as np
import heapq

INTERSECTIONS = [2, 4, 6, 8]

h = Helper(23)

inp = h.get_input_list()


class QueueElement:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, QueueElement(item, priority))

    def get(self):
        el = heapq.heappop(self.elements)
        return el.priority, el.item


class State:
    def __init__(self, burrows, hall=None):
        self.burrows = burrows
        self.hall = hall or [None] * 11

    def __eq__(self, other):
        return self.burrows == other.burrows and self.hall == other.hall

    def to_tuple(self):
        return tuple([tuple(b) for b in self.burrows]), tuple(self.hall)

    def __hash__(self):
        return self.to_tuple().__hash__()

    def copy(self):
        return State(copy.deepcopy(self.burrows), copy.copy(self.hall))

    def __str__(self):
        return f"State: burrows={self.burrows}, hall={self.hall}"

    def get_moves(self):
        possible_states = []
        for pos, tp in enumerate(self.hall):
            if tp is None:
                continue
            if all(self.burrows[tp][i] in (None, tp) for i in range(2)):
                goal = INTERSECTIONS[tp]
                if (pos < goal and all(self.hall[i] is None for i in range(pos + 1, goal))) or \
                        (pos > goal and all(self.hall[i] is None for i in range(goal, pos))):
                    next_state = self.copy()
                    moves = abs(pos - goal) + 1
                    next_state.hall[pos] = None
                    if self.burrows[tp][1] is None:
                        next_state.burrows[tp][1] = tp
                        moves += 1
                    else:
                        next_state.burrows[tp][0] = tp
                    possible_states.append((next_state, moves * 10 ** tp))

        for i, burrow in enumerate(self.burrows):
            depth = None
            tp = None
            for depth in range(2):
                if burrow[depth] is not None:
                    tp = burrow[depth]
                    break
            if tp is None:
                continue

            start = INTERSECTIONS[i]
            for j in range(start + 1, len(self.hall)):
                if self.hall[j] is not None:
                    break
                if j in INTERSECTIONS:
                    continue
                next_state = self.copy()
                next_state.burrows[i][depth] = None
                next_state.hall[j] = tp
                moves = depth + 1 + j - start
                possible_states.append((next_state, moves * 10 ** tp))

            for j in range(start - 1, -1, -1):
                if self.hall[j] is not None:
                    break
                if j in INTERSECTIONS:
                    continue
                next_state = self.copy()
                next_state.burrows[i][depth] = None
                next_state.hall[j] = tp
                moves = depth + 1 + start - j
                possible_states.append((next_state, moves * 10 ** tp))

        return possible_states


b = [[] for i in range(4)]
for line in inp[2:4]:
    for i, c in enumerate(line.strip(" ").strip("#").split("#")):
        b[i].append(ord(c) - ord('A'))

start_state = State(b)
end_state = State([[i, i] for i in range(4)])

frontier = PriorityQueue()
frontier.put(start_state, 0)
cost_so_far = {start_state: 0}

print(start_state)
print()
# for state, cost in start_state.get_moves():
#     print(cost, state)

while not frontier.empty():
    priority, current = frontier.get()
    if current == end_state:
        break

    for new_state, cost in current.get_moves():
        new_cost = cost_so_far[current] + cost
        if new_state not in cost_so_far or new_cost < cost_so_far[new_state]:
            cost_so_far[new_state] = new_cost
            priority = new_cost
            frontier.put(new_state, priority)

h.submit(cost_so_far[end_state])

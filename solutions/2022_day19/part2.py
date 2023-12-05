import collections
import dataclasses
import enum
import math

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
""")

inp = h.get_input_list()

END_TICK = 32


class Resource(enum.Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


blueprints = []
for line in inp[:3]:
    m = [int(n) for n in re.findall(r"\d+", line)]
    blueprints.append({
        Resource.ORE: {Resource.ORE: m[1]},
        Resource.CLAY: {Resource.ORE: m[2]},
        Resource.OBSIDIAN: {Resource.ORE: m[3], Resource.CLAY: m[4]},
        Resource.GEODE: {Resource.ORE: m[5], Resource.OBSIDIAN: m[6]}
    })


@dataclasses.dataclass
class State:
    resources: t.Dict[Resource, int]
    rates: t.Dict[Resource, int]
    tick: int


scores = []

for blueprint_numb, blueprint in enumerate(blueprints):
    print(blueprint_numb, blueprint)
    max_robots = {r: max(blueprint[r2].get(r) or 0 for r2 in Resource) for r in Resource}
    max_robots[Resource.GEODE] = END_TICK
    print(max_robots)

    max_end_score = 0
    q = collections.deque([State({r: 0 for r in Resource}, {Resource.ORE: 1, Resource.CLAY: 0, Resource.OBSIDIAN: 0, Resource.GEODE: 0},
               0)])

    while len(q) > 0:
        state = q.popleft()
        next_buys = [r for r in Resource if state.rates[r] < max_robots[r] and all(state.rates[cost] > 0 for cost in blueprint[r].keys() if cost != r)]
        for buy in next_buys:
            time_to_completion = max(
                math.ceil((blueprint[buy][ingredient] - state.resources[ingredient]) / state.rates[ingredient])
                for ingredient in blueprint[buy].keys()) + 1
            time_to_completion = max(time_to_completion, 1)

            if state.tick + time_to_completion >= END_TICK:
                continue
            if buy == Resource.CLAY and (blueprint[Resource.GEODE][Resource.OBSIDIAN] - state.rates[Resource.OBSIDIAN]) * blueprint[Resource.OBSIDIAN][Resource.CLAY] <= state.resources[Resource.CLAY]:
                continue

            new_state = State(
                {r: state.resources[r] + state.rates[r] * time_to_completion - (blueprint[buy].get(r) or 0) for r in Resource},
                {r: state.rates[r] + 1 if r == buy else state.rates[r] for r in Resource},
                state.tick + time_to_completion
            )


            q.append(new_state)

        time_left = END_TICK - state.tick
        max_end_score = max(max_end_score, state.resources[Resource.GEODE] + state.rates[Resource.GEODE] * time_left)

    scores.append(max_end_score)

print(scores)
h.submit(scores[0] * scores[1] * scores[2], confirm_answer=False)

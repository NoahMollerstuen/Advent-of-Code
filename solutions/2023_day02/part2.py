import dataclasses

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""")

inp = h.get_input_list()


@dataclasses.dataclass
class Game:
    id: int
    reds: list
    blues: list
    greens: list


games = []

for line in inp:
    m = re.match(r"Game (\d+)", line)
    id = int(m.group(1))

    reds = [int(n) for n in re.findall(r"(\d+) red", line)]
    blues = [int(n) for n in re.findall(r"(\d+) blue", line)]
    greens = [int(n) for n in re.findall(r"(\d+) green", line)]

    games.append(Game(id, reds, blues, greens))

s = 0
for g in games:
    s += max(g.reds) * max(g.blues) * max(g.greens)

h.submit(s)
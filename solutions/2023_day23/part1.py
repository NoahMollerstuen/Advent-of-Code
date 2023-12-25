import dataclasses
import queue

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""")


SLOPE_DIR = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}


@dataclasses.dataclass
class State:
    pos: t.Tuple[int, int]
    visited: set[t.Tuple[int, int]]


inp = h.get_input_grid()

starting_pos = (0, inp[0].index('.'))
ending_pos = (len(inp) - 1, inp[-1].index('.'))

q = queue.Queue()
q.put(State(starting_pos, set()))

longest_path = 0
while not q.empty():
    s: State = q.get()
    if s.pos == ending_pos:
        longest_path = max(longest_path, len(s.visited))
        continue

    for d in Grid.DIR4:
        new_pos = (s.pos[0] + d[0], s.pos[1] + d[1])
        c = Grid.get(inp, new_pos)
        if c == '#' or new_pos in s.visited:
            continue
        if c == '.':
            new_visited = s.visited.copy()
            new_visited.add(new_pos)
            q.put(State(new_pos, new_visited))
        if c in SLOPE_DIR.keys():
            slope_dir = SLOPE_DIR[c]
            if slope_dir[0] != -d[0] or slope_dir[1] != - d[1]:
                new_new_pos = (new_pos[0] + slope_dir[0], new_pos[1] + slope_dir[1])
                new_visited = s.visited.copy()
                new_visited.add(new_pos)
                new_visited.add(new_new_pos)
                q.put(State(new_new_pos, new_visited))

h.submit(longest_path)

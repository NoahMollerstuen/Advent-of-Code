import queue
from collections import defaultdict

from pyvis.network import Network

from util import *
from util import Grid as g
import itertools as it
import re


h = Helper(test_mode=False, test_input="""

""")

inp = h.get_input_list()

components = set()
edges = []
for line in inp:
    comp = line.split(': ')[0]
    connections = line.split(': ')[1].split(' ')
    components.add(comp)
    for c in connections:
        components.add(c)
        edges.append((comp, c))

# net = Network()
#
# for comp in components:
#     net.add_node(comp, comp)
#
# for e in edges:
#     net.add_edge(*e)
#
# net.show('mygraph.html', notebook=False)


IGNORED_EDGES = [("lxt", "lsv"), ("dhn", "xvh"), ("ptj", "qmr")]


q = queue.Queue()
q.put(components.copy().pop())
visited = set()

edges_dict = defaultdict(lambda: [])

for e in edges:
    if e in IGNORED_EDGES or (e[1], e[0]) in IGNORED_EDGES:
        print(e)
        continue
    edges_dict[e[0]].append(e[1])
    edges_dict[e[1]].append(e[0])

while not q.empty():
    comp = q.get()
    if comp in visited:
        continue
    visited.add(comp)
    for c in edges_dict[comp]:
        q.put(c)

group_size = len(visited)
other_size = len(components) - group_size
print(group_size, other_size)
h.submit(group_size * other_size)

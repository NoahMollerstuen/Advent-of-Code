from util import *
from util import Grid as g
import itertools as it
import re
import numpy as np

h = Helper(test_mode=False, test_input="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""")

inp = h.get_input_raw()
blocks = inp.strip("$").strip(" ").split("\n$ ")


all_nodes = []


class Node:
    def __init__(self, parent, size=0, is_file=False):
        all_nodes.append(self)
        self.children = {}
        self.parent = parent
        self.size = size
        self.is_file = is_file

    def get_size(self):
        tot = self.size
        for child in self.children.values():
            tot += child.get_size()
        return tot


root_node = Node(parent=Node)
cur_node = root_node

for block in blocks:
    command = block[:2]
    if command == "cd":
        arg = block.split(" ")[1]
        if arg == "/":
            cur_node = root_node
        elif arg == "..":
            cur_node = cur_node.parent
        else:
            if arg not in cur_node.children.keys():
                cur_node.children[arg] = Node(cur_node)
            cur_node = cur_node.children[arg]
    elif command == "ls":
        for line in block.split("\n")[1:]:
            size, name = line.split(" ")
            if size == "dir":
                cur_node.children[name] = Node(cur_node)
            else:
                cur_node.children[name] = Node(cur_node, int(size), is_file=True)
    else:
        raise ValueError(command)

need_to_free = 30000000 - (70000000 - root_node.get_size())
nodes_by_size = sorted([n for n in all_nodes if not n.is_file], key=lambda n: n.get_size())
for n in nodes_by_size:
    if n.get_size() >= need_to_free:
        h.submit(n.get_size())

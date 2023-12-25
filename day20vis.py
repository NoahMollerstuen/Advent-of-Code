from pyvis.network import Network

from util import Helper

net = Network(directed=True)

h = Helper(test_mode=False)

inp = h.get_input_list()

modules = {}

for line in inp:
    type_code = line[0]
    name = line.split(' -> ')[0].strip('%&')
    links = line.split(' -> ')[1].split(', ')
    modules[name] = (type_code, name, links)
    if type_code == '&':
        net.add_node(name, name, shape="box")
    else:
        net.add_node(name, name)

net.add_node("rx", "rx")
net.add_node("button", "button")
modules["button"] = ("but", "button", ["broadcaster"])

for m in modules.values():
    for n in m[2]:
        net.add_edge(m[1], n)

net.show('mygraph.html', notebook=False)

import queue
from collections import defaultdict

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""")


# pulses_queue = queue.Queue()
#
#
# class SolutionFoundException(Exception):
#     pass
#
#
# class Module:
#     def __init__(self, name: str, link_strs: t.List[str]):
#         self.name: str = name
#         self.link_strs: t.List[str] = link_strs
#         self.link_objects: t.List[Module] = []
#
#     def init_link_objects(self, all_modules):
#         for li in self.link_strs:
#             try:
#                 self.link_objects.append(all_modules[li])
#             except KeyError:
#                 pass
#
#     def send_pulse(self, is_high_pulse: bool):
#         global pulses_queue
#
#         for li in self.link_objects:
#             if li.name == "kj" and is_high_pulse:
#                 raise SolutionFoundException
#             pulses_queue.put((li, is_high_pulse, self.name))
#
#     def activate(self, is_high_pulse: bool, activator_name: str):
#         raise NotImplemented()
#
#
# class FlipFlop(Module):
#     def __init__(self, name: str, link_strs: t.List[str]):
#         super().__init__(name, link_strs)
#         self.state = False
#
#     def activate(self, is_high_pulse: bool, activator_name):
#         if is_high_pulse:
#             return
#
#         self.state = not self.state
#         self.send_pulse(self.state)
#
#
# class Conjunction(Module):
#     def __init__(self, name: str, link_strs: t.List[str]):
#         super().__init__(name, link_strs)
#         self.input_states = {}
#
#     def init_link_objects(self, all_modules):
#         super().init_link_objects(all_modules)
#         for mod in all_modules.values():
#             if self.name in mod.link_strs:
#                 self.input_states[mod.name] = False
#
#     def activate(self, is_high_pulse: bool, activator_name: str):
#         self.input_states[activator_name] = is_high_pulse
#         self.send_pulse(not all(self.input_states.values()))
#
#
# class Broadcast(Module):
#     def activate(self, is_high_pulse: bool, activator_name: str):
#         self.send_pulse(is_high_pulse)
#
#
# class Button(Module):
#     def activate(self, is_high_pulse: bool, activator_name: str):
#         self.send_pulse(False)
#
#
# TYPE_CODES = {
#     '%': FlipFlop,
#     '&': Conjunction,
#     'b': Broadcast,
# }
#
# inp = h.get_input_list()
#
# modules: t.Dict[str, Module] = {}
#
# for line in inp:
#     type_code = line[0]
#     module_type = TYPE_CODES[type_code]
#     name = line.split(' -> ')[0].strip('%&')
#     links = line.split(' -> ')[1].split(', ')
#     modules[name] = module_type(name, links)
#
# modules["button"] = (Button("button", ["broadcaster"]))
#
# for m in modules.values():
#     m.init_link_objects(modules)
#
# step = 0
# last_high = 0
#
# while True:
#     states = [str(int(m.state)) for m in modules.values() if isinstance(m, FlipFlop)]
#     # print("".join(states))
#
#     step += 1
#     modules["pd"].activate(False, "")
#
#     while not pulses_queue.empty():
#         pulse = pulses_queue.get(block=False)
#         # print(pulse, pulse[0].name)
#         try:
#             pulse[0].activate(pulse[1], pulse[2])
#         except SolutionFoundException:
#             print(step, step - last_high)
#             last_high = step
#             break

high_steps = defaultdict(lambda: 0)

steps = [
    4003,
    3989,
    3863,
    3943,
]

periods = [
    3910,
    3882,
    3630,
    3790,
]

"""
kt: goes high on step 4003 and 4004, repeats for 2 steps with period 3910 steps
xv: goes high on step 3989 and 3990, repeats for 2 steps with period 3882 steps
rg: goes high on step 3863 and 3864, repeats for 2 steps with period 3630 steps
pd: goes high on step 3943 and 3944, repeats for 2 steps with period 3790 steps
"""


while True:
    for i, p in enumerate(periods):
        s = steps[i]
        high_steps[s] += 1
        if high_steps[s] == 4:
            h.submit(s)

        high_steps[s + 1] += 1
        if high_steps[s + 1] == 4:
            h.submit(s + 1)

        steps[i] += p

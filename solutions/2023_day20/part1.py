import queue

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


pulses_queue = queue.Queue()


class Module:
    def __init__(self, name: str, link_strs: t.List[str]):
        self.name: str = name
        self.link_strs: t.List[str] = link_strs
        self.link_objects: t.List[Module] = []

        self.low_pulses_sent = 0
        self.high_pulses_sent = 0

    def init_link_objects(self, all_modules):
        for li in self.link_strs:
            try:
                self.link_objects.append(all_modules[li])
            except KeyError:
                pass

    def send_pulse(self, is_high_pulse: bool):
        global pulses_queue

        if is_high_pulse:
            self.high_pulses_sent += len(self.link_strs)
        else:
            self.low_pulses_sent += len(self.link_strs)

        for li in self.link_objects:
            pulses_queue.put((li, is_high_pulse, self.name))

    def activate(self, is_high_pulse: bool, activator_name: str):
        raise NotImplemented()


class FlipFlop(Module):
    def __init__(self, name: str, link_strs: t.List[str]):
        super().__init__(name, link_strs)
        self.state = False

    def activate(self, is_high_pulse: bool, activator_name):
        if is_high_pulse:
            return

        self.state = not self.state
        self.send_pulse(self.state)


class Conjunction(Module):
    def __init__(self, name: str, link_strs: t.List[str]):
        super().__init__(name, link_strs)
        self.input_states = {}

    def init_link_objects(self, all_modules):
        super().init_link_objects(all_modules)
        for mod in all_modules.values():
            if self.name in mod.link_strs:
                self.input_states[mod.name] = False

    def activate(self, is_high_pulse: bool, activator_name: str):
        self.input_states[activator_name] = is_high_pulse
        self.send_pulse(not all(self.input_states.values()))


class Broadcast(Module):
    def activate(self, is_high_pulse: bool, activator_name: str):
        self.send_pulse(is_high_pulse)


class Button(Module):
    def activate(self, is_high_pulse: bool, activator_name: str):
        self.send_pulse(False)


TYPE_CODES = {
    '%': FlipFlop,
    '&': Conjunction,
    'b': Broadcast,
}

inp = h.get_input_list()

modules: t.Dict[str, Module] = {}

for line in inp:
    type_code = line[0]
    module_type = TYPE_CODES[type_code]
    name = line.split(' -> ')[0].strip('%&')
    links = line.split(' -> ')[1].split(', ')
    modules[name] = module_type(name, links)

modules["button"] = (Button("button", ["broadcaster"]))

for m in modules.values():
    m.init_link_objects(modules)

for _ in range(1000):
    modules["button"].activate(False, "")

    while not pulses_queue.empty():
        pulse = pulses_queue.get(block=False)
        # print(pulse, pulse[0].name)
        pulse[0].activate(pulse[1], pulse[2])

total_low_pulses = sum(m.low_pulses_sent for m in modules.values())
total_high_pulses = sum(m.high_pulses_sent for m in modules.values())
print(total_low_pulses)
print(total_high_pulses)

h.submit(total_low_pulses * total_high_pulses)

import functools

from util import Helper
import itertools as it
import re

h = Helper(7, year=2020)

inp = h.get_input_list()

rules_dict = {}
for line in inp:
    m = re.search(r"([\w| ]+) bags contain (.+).", line)

    rules = m.group(2).split(", ")

    rules_dict[m.group(1)] = [re.findall(r"(\d+) (.*) bags?", rule)[0] for rule in rules if "no other bags" not in rule]

print(rules_dict)


@functools.cache
def count_inside(bag):
    return sum((count_inside(b[1]) + 1) * int(b[0]) for b in rules_dict[bag])


h.submit(count_inside("shiny gold"))

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


def contains_gold(bag):
    if bag == "shiny gold":
        return True
    return any(contains_gold(b[1]) for b in rules_dict[bag])


c = 0
for k in rules_dict.keys():
    c += contains_gold(k)

h.submit(c-1)

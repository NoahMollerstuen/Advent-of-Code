from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""")

inp = h.get_input_raw()


class Monkey:
    def __init__(self, starting_items, operation, test, true_throw, false_throw):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspection_count = 0

    def do_inspections(self):
        self.inspection_count += len(self.items)

        for item in self.items:
            op = self.operation.replace("old", str(item))
            new_item = eval(op) // 3

            monkeys[self.true_throw if new_item % self.test == 0 else self.false_throw].items.append(new_item)
        self.items = []


monkeys_raw = inp.split("\n\n")
monkeys = []

for monkey in monkeys_raw:
    lines = monkey.split("\n")
    monkeys.append(Monkey(
        [int(item) for item in lines[1].split(": ")[1].split(", ")],
        " ".join(lines[2].split(" ")[5:]),
        int(lines[3].split(" ")[-1]),
        int(lines[4].split(" ")[-1]),
        int(lines[5].split(" ")[-1])
    ))

for tick in range(20):
    for monkey in monkeys:
        monkey.do_inspections()
    # print([m.items for m in monkeys])


busiest = sorted([m.inspection_count for m in monkeys])[-2:]
h.submit(busiest[0] * busiest[1])
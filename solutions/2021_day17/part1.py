from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(17)

inp = h.get_input_raw()

numbs = re.findall(r"-?\d+", inp)

x_range = (int(numbs[0]), int(numbs[1]))
y_range = (int(numbs[2]), int(numbs[3]))
print(x_range, y_range)

vy0 = -min(y_range) - 1
vx0 = 1

while True:
    while True:
        x_vel = vx0
        y_vel = vy0
        x = y = 0
        max_y = 0
        peak_x = None
        while y >= min(y_range):
            x += x_vel
            y += y_vel
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1
            max_y = max(y, max_y)
            if peak_x is None and max_y != y:
                peak_x = x
                print(vx0, peak_x)

            if x in range(min(x_range), max(x_range) + 1) and y in range(min(y_range), max(y_range) + 1):
                h.submit(max_y)

        if peak_x > max(x_range):
            break

        vx0 += 1

    print("Decreasing vy0", vy0)
    vy0 -= 1

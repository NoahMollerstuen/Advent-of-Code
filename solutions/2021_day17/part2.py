from util import *
from util import Grid as g
from packets import *
import itertools as it
import re

h = Helper(17)

inp = h.get_input_raw()

numbs = re.findall(r"-?\d+", inp)

x_range = (int(numbs[0]), int(numbs[1]))
y_range = (int(numbs[2]), int(numbs[3]))
print(x_range, y_range)

vy0 = -min(y_range) - 1


trajectories = []

while True:
    vx0 = 1
    while True:
        print(vx0, vy0)
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

            if x in range(min(x_range), max(x_range) + 1) and y in range(min(y_range), max(y_range) + 1):
                trajectories.append((vx0,  vy0))
                break

        if peak_x > max(x_range):
            break

        vx0 += 1

    if vy0 < min(y_range):
        break

    vy0 -= 1

print(trajectories)
h.submit(len(trajectories))

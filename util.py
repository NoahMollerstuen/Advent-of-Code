import inspect
import json
import os
import shutil
import time
import datetime

import requests
from bs4 import BeautifulSoup
import typing as t

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class Helper:
    def __init__(self, day=None, year=None, test_input=None):
        self.day = day if day is not None else (datetime.date.today() + datetime.timedelta(minutes=1)).day
        self.year = year if day is not None else datetime.date.today().year
        self.raw_input = test_input or self.load_input()
        self.raw_input = self.raw_input.strip("\n")

    def load_input(self):
        filename = f"{self.year}_day{self.day:02d}.txt"
        if filename not in os.listdir("puzzle_inputs"):
            print("Fetching puzzle input")
            with open("secrets.json") as f:
                secrets = json.load(f)
            cookies = {
                "session": secrets["session"]
            }
            while True:
                response = requests.get(
                    f"https://adventofcode.com/{self.year}/day/{self.day}/input",
                    cookies=cookies
                )
                raw_input = response.text.strip("\n")
                print(raw_input)

                if response.status_code != 504:
                    break
                time.sleep(2)

            if response.status_code == 200:
                with open(f"puzzle_inputs/{filename}", "w") as file:
                    file.write(raw_input)
        else:
            with open(f"puzzle_inputs/{filename}", "r") as file:
                raw_input = file.read()
        return raw_input

    def get_input_raw(self):
        return self.raw_input

    def get_input_list(self):
        raw_text = self.raw_input
        split_text = raw_text.split("\n")

        int_list = []
        try:
            for line in split_text:
                int_list.append(int(line))
            return int_list
        except ValueError:
            return split_text

    def get_input_grid(self):
        rows = self.raw_input.split("\n")
        grid = [[c for c in row] for row in rows]
        try:
            grid = [[int(c) for c in row] for row in rows]
        except ValueError:
            pass
        return grid

    def submit(self, answer=None, part=None, confirm_answer=True):
        if answer is None:
            return

        solutions_dir = f"solutions/{self.year}_day{self.day:02d}"
        if part is None:
            part = 2 if os.path.exists(f"{solutions_dir}/part1.py") else 1

        if confirm_answer:
            print(f"Submit {answer}?")
            user_input = input('>')
            if user_input not in ['y', 'yes', 'Y']:
                print("Answer not submitted")
                return

        # Retry request on 504
        while True:
            with open("secrets.json") as f:
                secrets = json.load(f)
            cookies = {
                "session": secrets["session"]
            }
            response = requests.post(
                f"https://adventofcode.com/{self.year}/day/{self.day}/answer",
                data={"level": part, "answer": answer},
                cookies=cookies
            )
            if response.status_code != 504:
                break
            print("504 error, retrying...")
            time.sleep(2)

        parsed_response = BeautifulSoup(response.text, features="html.parser")
        text = parsed_response.main.get_text().strip("\n")
        print(text)

        if "That's the right answer!" in text:
            if not os.path.exists(solutions_dir):
                os.makedirs(solutions_dir)

            source_file = inspect.stack()[-1].filename
            shutil.copy(source_file, f"{solutions_dir}/part{part}.py")


class Grid:
    DIR4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
    DIR8 = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    @staticmethod
    def get(grid: t.List[t.List[t.Any]], pos: t.Tuple[int, int], default: t.Any = None):
        if pos[0] < 0 or pos[1] < 0:
            return default
        try:
            return grid[pos[0]][pos[1]]
        except IndexError:
            return default

    @staticmethod
    def bfs(grid: t.List[t.List[t.Any]], start_y: int, start_x: int, obstacles: t.Union[t.List[t.Any], str] = "",
            passables: t.Optional[t.Union[t.List[t.Any], str]] = None,
            allow_diagonals: bool = False, backtracking: bool = False) -> t.List[t.List[t.Optional[int]]]:
        """
        Perform a breadth first search to find the shortest path to each cell in a grid
        
        :param grid: a 2d list representing the grid
        :param start_y: the y (first) index for the source cell
        :param start_x: the x (second) index for the source cell
        :param obstacles: a list or string containing each value which is impassable
        :param passables: a list or string containing each value which is passable. Overrides obstacles.
        :param allow_diagonals: Whether a diagonal move on the grid is allowed. If True, it is considered one step.
        :param backtracking: If true, return the shortest path to each cell
        :return: a 2d list with the same shape as the input. Each cell is the minimum number of steps to reach that cell
        or None for no path.
        """
        directions = Grid.DIR8 if allow_diagonals else Grid.DIR4

        cell_queue = [(start_y, start_x)]
        distance_grid: t.List[t.List[t.Optional[int]]] = [[None for _ in row] for row in grid]
        distance_grid[start_y][start_x] = 0
        paths_grid: t.List[t.List[t.Optional[t.Tuple[int, int]]]] = [[None for _ in row] for row in grid]
        paths_grid[start_y][start_x] = []

        while len(cell_queue) > 0:
            cell = cell_queue.pop(0)
            cell_val = Grid.get(distance_grid, cell)
            neighbors = [(cell[0] + direction[0], cell[1] + direction[1]) for direction in directions]
            for n in neighbors:
                n_val = Grid.get(grid, n)
                if n_val is not None and Grid.get(distance_grid, n) is None and \
                        (n_val not in obstacles if passables is None else n_val in passables):
                    distance_grid[n[0]][n[1]] = cell_val + 1
                    if backtracking:
                        paths_grid[n[0]][n[1]] = paths_grid[cell[0]][cell[1]] + [n]
                    cell_queue.append(n)

        if backtracking:
            return distance_grid, paths_grid  # TODO fix return typing
        return distance_grid

    @staticmethod
    def print(grid: t.List[t.List[t.Any]], name="unnamed grid", crush=True):
        print(f"{name} printout, crush={crush}")
        for row in grid:
            print("".join([str(c)[0] if crush else str(c) for c in row]))

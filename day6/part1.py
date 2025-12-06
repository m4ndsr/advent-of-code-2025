import operator
from typing import Literal
from pydantic import BaseModel
import re
from functools import reduce

OperationSign = Literal["+", "*"]


class Problem(BaseModel):
    numbers: list[int]
    operator: OperationSign

    def solve(self) -> int:
        if self.operator == "+":
            return sum(self.numbers)
        elif self.operator == "*":
            return reduce(operator.mul, self.numbers, 1)


def part1(file_name: str) -> int:
    grid = _convert_file_to_grid(file_name)
    problems = _get_problems(grid)
    return _get_grand_total(problems)


def _convert_file_to_grid(file_name: str) -> list[list[str]]:
    grid = []
    with open(file_name, "r") as file:
        for line in file:
            row = re.split("\s+", line.strip())
            grid.append(row)
    return grid


def _get_problems(grid: list[list[str]]) -> list[Problem]:
    transposed_grid = list(zip(*grid))
    return [
        Problem(numbers=map(int, row[:-1]), operator=row[-1]) for row in transposed_grid
    ]


def _get_grand_total(problems: list[Problem]) -> int:
    return sum([problem.solve() for problem in problems])


# ------------------------------------------------
# Example
# ------------------------------------------------

file = "example.txt"

assert part1(file) == 4277556

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

file = "input.txt"

assert part1(file) == 5873191732773

print("Puzzle input: Successful")

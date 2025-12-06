from functools import reduce
import operator
from typing import Literal

from pydantic import BaseModel


OperationSign = Literal["+", "*"]


class Problem(BaseModel):
    numbers: list[int]
    operator_sign: OperationSign

    def solve(self) -> int:
        if self.operator_sign == "+":
            return sum(self.numbers)
        elif self.operator_sign == "*":
            return reduce(operator.mul, self.numbers, 1)


def part2(file_name: str) -> int:
    lines = _get_input_lines(file_name)
    problems = _get_problems(lines)
    return sum([problem.solve() for problem in problems])


def _get_input_lines(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        return [line.strip("\n") for line in file.readlines()]


def _get_problems(lines: list[str]) -> list[Problem]:
    problems = []

    current_numbers = []
    current_operator_sign = ""

    line_length = len(lines[0])
    for i in range(line_length - 1, -1, -1):
        current_number = ""
        for line in lines:
            part = line[i]
            if part in ("+", "*"):
                current_operator_sign = part
            else:
                current_number += part

        current_number_is_empty = current_number.strip() == ""
        save_and_reset_problem = (
            current_number_is_empty and len(current_numbers) > 0
        ) or (i == 0)

        if not current_number_is_empty:
            current_numbers.append(int(current_number))

        if save_and_reset_problem:
            problems.append(
                Problem(numbers=current_numbers, operator_sign=current_operator_sign)
            )
            current_numbers = []

    return problems


# ------------------------------------------------
# Example
# ------------------------------------------------

file = "example.txt"

assert part2(file) == 3263827

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

file = "input.txt"

assert part2(file) == 11386445308378

print("Puzzle input: Successful")

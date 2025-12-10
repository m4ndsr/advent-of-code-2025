from itertools import combinations_with_replacement
import re
from z3 import IntVector, Optimize, Sum, sat


class MachineLogic:
    indicator_light_diagram: list[bool] = []
    button_wiring_schematics: list[tuple] = []
    joltage_requirements: list[int] = []

    def __init__(self, line: str):
        self.indicator_light_diagram = _get_indicator_light_diagram(line)
        self.button_wiring_schematics = _get_button_wiring_schematics(line)
        self.joltage_requirements = _get_joltage_requirements(line)

    def get_fewest_presses_for_light_diagram(self, max_presses: int = 1) -> int:
        for combination in combinations_with_replacement(
            self.button_wiring_schematics, max_presses
        ):
            state = [False] * len(self.indicator_light_diagram)

            for button in combination:
                for button_idx in button:
                    state[button_idx] = not state[button_idx]

            is_correct_state = state == self.indicator_light_diagram
            if is_correct_state:
                return max_presses

        return self.get_fewest_presses_for_light_diagram(max_presses + 1)

    def get_fewest_presses_for_joltage(self) -> int:
        joltage_length = len(self.joltage_requirements)
        number_of_buttons = len(self.button_wiring_schematics)

        button_presses = IntVector("x", number_of_buttons)
        optimizer = Optimize()
        for press_count in button_presses:
            # Add non-negativity constraint
            optimizer.add(press_count >= 0)

        button_matrix = []
        for button in self.button_wiring_schematics:
            row = [
                1 if joltage_idx in button else 0
                for joltage_idx in range(joltage_length)
            ]
            button_matrix.append(row)

        for joltage_idx in range(joltage_length):
            # Add constraint for each joltage requirement
            optimizer.add(
                Sum(
                    button_presses[button_idx] * button_matrix[button_idx][joltage_idx]
                    for button_idx in range(number_of_buttons)
                )
                == self.joltage_requirements[joltage_idx]
            )

        # Look for the solution with the fewest total button presses
        optimizer.minimize(Sum(button_presses))

        if optimizer.check() == sat:
            solution = optimizer.model()
            return sum(solution[var].as_long() for var in solution)


def part1(file_name: str) -> int:
    presses = 0
    for machine_logic in _get_all_machine_logic(file_name):
        presses += machine_logic.get_fewest_presses_for_light_diagram(1)
    return presses


def part2(file_name: str) -> int:
    presses = 0
    for machine_logic in _get_all_machine_logic(file_name):
        presses += machine_logic.get_fewest_presses_for_joltage()
    return presses


def _get_all_machine_logic(file_name: str) -> list[MachineLogic]:
    with open(file_name, "r") as file:
        return [MachineLogic(line.strip()) for line in file.readlines()]


def _get_indicator_light_diagram(line: str) -> list[bool]:
    return [x == "#" for x in re.match(r"\[(.*)\]", line).group(1)]


def _get_button_wiring_schematics(line: str) -> list[tuple]:
    return [
        tuple(int(x) for x in match[0].split(",") if x)
        for match in re.findall(r"\((\d(\,\d)*)\)", line)
    ]


def _get_joltage_requirements(line: str) -> list[int]:
    match = re.search(r"\{(.*)\}", line).group(1)
    return [int(x) for x in match.split(",") if x]


assert part1("example.txt") == 7
assert part2("example.txt") == 33

print("Example: Successful")

assert part1("input.txt") == 507
assert part2("input.txt") == 18981

print("Puzzle input: Successful")

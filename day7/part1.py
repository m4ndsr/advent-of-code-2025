def part1(file_name: str) -> int:
    lines = _get_lines(file_name)
    beams = []
    n_hit_splits = 0

    for line in lines:
        new_beams, hit_splits = _get_new_beams(line, beams)
        beams = new_beams
        n_hit_splits += hit_splits

    return n_hit_splits


def _get_lines(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]


def _get_new_beams(line: str, previous_beams: list[int]) -> tuple[set[int], int]:
    new_beams = set()
    n_hit_splits = 0

    for position, item in enumerate(line):
        if item == "S":
            new_beams.add(position)

        elif item == "^" and position in previous_beams:
            left_position = position - 1
            if line[left_position] == ".":
                new_beams.add(left_position)

            right_position = position + 1
            if line[right_position] == ".":
                new_beams.add(right_position)

            n_hit_splits += 1

        elif item == "." and position in previous_beams:
            new_beams.add(position)

    return new_beams, n_hit_splits


assert part1("example.txt") == 21
print("Example: Successful")

assert part1("input.txt") == 1717
print("Puzzle Input: Successful")

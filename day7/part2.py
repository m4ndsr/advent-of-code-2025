def part2(file_name: str) -> int:
    lines = _get_lines(file_name)

    paths = {}
    for line in lines:
        paths = _find_next_paths(line, paths)

    total_paths = sum(paths.values())
    return total_paths


def _get_lines(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]


def _find_next_paths(line: str, paths: dict) -> dict:
    for position, item in enumerate(line):
        if item == "S":
            paths = {position: 1}

        elif item == "^" and position in paths:
            current_paths = paths.get(position)
            paths.pop(position)
            _split_position(position - 1, line, paths, current_paths)
            _split_position(position + 1, line, paths, current_paths)

        elif item == "." and position in paths:
            paths[position] = paths.get(position, 0)

    return paths


def _split_position(
    new_position: int,
    line: str,
    paths: dict,
    current_paths: int,
) -> None:
    if line[new_position] == ".":
        paths[new_position] = paths.get(new_position, 0) + current_paths


assert part2("example.txt") == 40
print("Example: Successful")

assert part2("input.txt") == 231507396180012
print("Puzzle Input: Successful")

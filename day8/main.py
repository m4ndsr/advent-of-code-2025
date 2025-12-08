from functools import reduce
from math import dist
import operator


def part1(file_name: str, limit: int, top_largest: int = 3) -> int:
    boxes = _get_boxes(file_name)
    connections = _get_all_connections(boxes)
    selected_connections = sorted(connections)[:limit]

    circuits = []
    for _, pair in selected_connections:
        circuits = _create_next_circuits(pair, circuits)

    circuit_sizes = [len(circuit) for circuit in circuits]
    sorted_sizes = sorted(circuit_sizes, reverse=True)
    return reduce(operator.mul, sorted_sizes[:top_largest], 1)


def part2(file_name: str) -> int:
    boxes = _get_boxes(file_name)
    connections = _get_all_connections(boxes)
    circuits = []
    for _, pair in sorted(connections):
        circuits = _create_next_circuits(pair, circuits)
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            return reduce(operator.mul, [point[0] for point in pair], 1)


def _get_boxes(
    file_name: str,
) -> tuple[int, int, int]:
    with open(file_name, "r") as file:
        return [tuple(map(int, line.strip().split(","))) for line in file.readlines()]


def _get_all_connections(
    boxes: tuple[int, int, int],
) -> list[tuple[float, set[tuple[int, int, int]]]]:
    connections = []

    for i, box in enumerate(boxes[:-1], 1):
        for box2 in boxes[i:]:
            distance = dist(box, box2)
            connections.append((distance, {box, box2}))

    return connections


def _create_next_circuits(
    pair: set[tuple[int, int, int]],
    current_circuits: list[set[tuple[int, int, int]]],
) -> list[set[tuple[int, int, int]]]:
    circuit_matches = []
    for i, circuit in enumerate(current_circuits):
        if circuit.intersection(pair):
            circuit_matches.append(i)

    new_circuits = current_circuits

    if len(circuit_matches) == 1:  # Only one circuit overlaps, add pair to it
        new_circuits[circuit_matches[0]].update(pair)

    elif len(circuit_matches) > 1:  # Multiple circuits overlap, merge them
        combined_circuit = pair.union(*(current_circuits[i] for i in circuit_matches))

        remaining_circuits = []
        for i, circuit in enumerate(current_circuits):
            if i not in circuit_matches:
                remaining_circuits.append(circuit)

        new_circuits = remaining_circuits
        new_circuits.append(combined_circuit)

    else:  # No circuits overlap, create a new one
        new_circuits.append(pair)

    return new_circuits


assert part1("example.txt", 10) == 40
assert part2("example.txt") == 25272
print("Example: Successful")

assert part1("input.txt", 1000) == 57970
assert part2("input.txt") == 8520040659
print("Puzzle Input: Successful")

from itertools import permutations
from math import prod


class Server:
    device_outputs: dict[str, list[str]]
    cached_paths: dict[tuple[str, str], int]

    def __init__(self, device_outputs: dict[str, list[str]]) -> None:
        self.device_outputs = device_outputs
        self.cached_paths = {}

    def count_paths(
        self,
        from_device: str,
        to_device: str,
    ) -> int:
        key = (from_device, to_device)

        if key in self.cached_paths:
            return self.cached_paths[key]

        if from_device == to_device:
            return 1

        n_paths = sum(
            self.count_paths(device, to_device)
            for device in self.device_outputs.get(from_device, [])
        )
        self.cached_paths[key] = n_paths

        return n_paths

    def count_paths_with_connectors(
        self,
        from_device: str,
        to_device: str,
        connectors: list[str],
    ) -> int:
        n_paths = 0

        # Get all possible paths based on connectors
        for connector_permutation in permutations(connectors):
            full_path = [from_device] + list(connector_permutation) + [to_device]

            pairs = zip(full_path, full_path[1:])

            pair_counts = [
                self.count_paths(from_device, to_device)
                for from_device, to_device in pairs
            ]

            n_paths += prod(pair_counts)

        return n_paths


def part1(file_name: str) -> int:
    device_outputs = _get_device_outputs(file_name)
    server = Server(device_outputs)
    return server.count_paths(
        from_device="you",
        to_device="out",
    )


def part2(file_name: str) -> int:
    device_outputs = _get_device_outputs(file_name)
    server = Server(device_outputs)
    return server.count_paths_with_connectors(
        from_device="svr",
        to_device="out",
        connectors=["dac", "fft"],
    )


def _get_device_outputs(file_name: str) -> dict[str, list[str]]:
    device_outputs = {}
    with open(file_name, "r") as file:
        for line in file.readlines():
            device, output = line.strip().split(":", 1)
            device_outputs[device] = output.strip().split(" ")
    return device_outputs


assert part1("example.txt") == 5
assert part2("example2.txt") == 2

print("Example: Successful")

assert part1("input.txt") == 477
assert part2("input.txt") == 383307150903216

print("Puzzle input: Successful")

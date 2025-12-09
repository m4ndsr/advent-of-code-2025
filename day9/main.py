from shapely import box
from shapely.geometry import Polygon
from shapely.prepared import prep


def part1(file_name: str) -> int:
    coords = _get_tile_coords(file_name)
    combinations = _get_all_combinations_of_coords_with_surface(coords)
    sorted_combinations = sorted(combinations, reverse=True)
    surface, _ = sorted_combinations[0]
    return surface


def part2(file_name: str) -> int:
    coords = _get_tile_coords(file_name)
    combinations = _get_all_combinations_of_coords_with_surface(coords)
    sorted_combinations = sorted(combinations, reverse=True)
    polygon = _get_polygon(coords)
    largest_valid_combination = _get_largest_rectangle_within_polygon(
        sorted_combinations, polygon
    )
    surface, _ = largest_valid_combination
    return surface


def _get_tile_coords(file_name: str) -> list[tuple[int, int]]:
    with open(file_name, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        return [tuple(map(int, line.split(","))) for line in lines]


def _get_all_combinations_of_coords_with_surface(
    coords: list[tuple[int, int]],
) -> list[tuple[int, tuple[tuple[int, int], tuple[int, int]]]]:
    combinations = []

    for i, coord in enumerate(coords, 1):
        for coord2 in coords[i:]:
            surface = _calculate_surface(coord, coord2)
            combinations.append((surface, (coord, coord2)))

    return combinations


def _calculate_surface(coord1: tuple[int, int], coord2: tuple[int, int]) -> int:
    x1, y1 = coord1
    x2, y2 = coord2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def _get_polygon(coords: list[tuple[int, int]]) -> Polygon:
    return Polygon(coords)


def _get_largest_rectangle_within_polygon(
    combinations: list[tuple[int, tuple[tuple[int, int], tuple[int, int]]]],
    polygon: Polygon,
) -> tuple[int, tuple[tuple[int, int], tuple[int, int]]]:
    poly = prep(polygon)
    for combination in combinations:
        _, coords = combination
        (x1, y1), (x2, y2) = coords
        rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if poly.contains(rectangle):
            return combination
    raise ValueError("No rectangle found within polygon")


assert part1("example.txt") == 50
assert part2("example.txt") == 24

print("Example: Successful")

assert part1("input.txt") == 4767418746
assert part2("input.txt") == 1461987144

print("Puzzle input: Successful")

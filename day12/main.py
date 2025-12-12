class Shape:
    width: int
    height: int
    matrix: list[list[int]]

    def __init__(self, input: str) -> None:
        rows = input.strip().split("\n")[1:]
        self.height = len(rows)
        self.width = len(rows[0])
        self.matrix = [[1 if x == "#" else 0 for x in row] for row in rows]

    def get_area_of_shapes(self) -> int:
        return sum(sum(row) for row in self.matrix)


class Region:
    width: int
    height: int
    shapes: list[Shape]
    _constraints: list[int]

    def __init__(self, input: str, all_shapes: list[Shape]) -> None:
        parts = input.split(":")
        self.height, self.width = map(int, parts[0].split("x"))
        self._constraints = [int(n) for n in parts[1].strip().split(" ")]
        self.shapes = self._get_shapes(all_shapes)

    def _get_shapes(self, all_shapes: list[Shape]) -> list[Shape]:
        shapes = []
        for i, amount in enumerate(self._constraints):
            shapes.extend([all_shapes[i]] * amount)
        return shapes

    def _max_area(self) -> int:
        return self.width * self.height

    def _required_area_for_shapes(self) -> int:
        return sum(shape.get_area_of_shapes() for shape in self.shapes)

    def fits(self) -> bool:
        return self._required_area_for_shapes() <= self._max_area()


def part1(filename: str) -> int:
    components = _get_components(filename)
    shapes = _get_shapes(components)
    regions = _get_regions(components, shapes)

    n = 0
    for region in regions:
        if region.fits():
            n += 1

    return n


def _get_components(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().split("\n\n")


def _get_shapes(components: list[str]) -> list[Shape]:
    return [Shape(shape) for shape in components[:-1]]


def _get_regions(components: list[str], shapes: list[Shape]) -> list[Region]:
    return [Region(region, shapes) for region in components[-1].split("\n")]


assert part1("example.txt") == 2

print("Example: Successful")

assert part1("input.txt") == 579

print("Puzzle input: Successful")

import copy

def part1(grid: list[list[int]]) -> int:
    accessible_count, _ = _get_accessible_rolls_in_grid(grid)
    return accessible_count

def part2(grid: list[list[int]]) -> int:
    last_accessible, new_grid = _get_accessible_rolls_in_grid(grid)
    total_accessible = last_accessible
    
    while last_accessible > 0:
        last_accessible, new_grid = _get_accessible_rolls_in_grid(new_grid)
        total_accessible += last_accessible

    return total_accessible

def _get_accessible_rolls_in_grid(grid: list[list[int]]) -> tuple[int, list[list[int]]]:
    accessible_count = 0
    new_grid = copy.deepcopy(grid)
    
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y]:    
                roll_count = _get_rolls_from_adjecent_positions(grid, x, y)
    
                if roll_count < 4:
                    accessible_count += 1
                    new_grid[x][y] = 0

    return accessible_count, new_grid


def _get_grid(file_name: str) -> list[list]:
    grid = []
    
    with open(file_name, "r") as file:
        for line in file:
            grid.append([1 if x == "@" else 0 for x in line.strip()])
    
    return grid


def _get_rolls_from_adjecent_positions(grid: list[list[int]], x: int, y: int) -> int:
    values = []

    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for neighbor in neighbors:
        nx, ny = x + neighbor[0], y + neighbor[1]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            values.append(grid[nx][ny])
                
    return sum(values)


# ------------------------------------------------
# Example 
# ------------------------------------------------

grid = _get_grid("example.txt")

assert part1(grid) == 13
assert part2(grid) == 43

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

grid = _get_grid("input.txt")

assert part1(grid) == 1564
assert part2(grid) == 9401

print("Puzzle input: Successful")

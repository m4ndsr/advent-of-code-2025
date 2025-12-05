def part1(fresh_ranges: list[tuple[int, int]], ids_to_check: set[int]) -> int:
    fresh_ids = set()

    for id in ids_to_check:
        for start, end in fresh_ranges:
            if start <= id <= end:
                fresh_ids.add(id)

    return len(fresh_ids)


def part2(fresh_ranges: list[tuple[int, int]]) -> int:
    total_fresh_ids = 0

    fresh_ranges = sorted(fresh_ranges)
    merged_ranges = []

    for start, end in fresh_ranges:
        if len(merged_ranges) == 0:
            merged_ranges.append((start, end))
            continue

        last_start, last_end = merged_ranges[-1]

        if last_start <= start <= last_end:
            merged_ranges = merged_ranges[:-1]
            merged_ranges.append((last_start, max(last_end, end)))
        else:
            merged_ranges.append((start, end))

    for start, end in merged_ranges:
        total_fresh_ids += end - start + 1

    return total_fresh_ids
    


def _get_fresh_ranges_and_ids_to_check(file_name: str) -> tuple[list[tuple[int, int]], set[int]]:
    fresh_ranges = []
    ids_to_check = set()
    
    with open(file_name, "r") as file:
        is_ranges = True

        for line in file:
            line = line.strip()
            
            if line == "":
                is_ranges = False
                continue

            if is_ranges:
                start, end = map(int, line.split("-"))
                fresh_ranges.append((start, end))
            else:
                id = int(line)
                ids_to_check.add(id)
    
    return fresh_ranges, ids_to_check


# ------------------------------------------------
# Example 
# ------------------------------------------------

fresh_ranges, ids_to_check = _get_fresh_ranges_and_ids_to_check("example.txt")

assert part1(fresh_ranges, ids_to_check) == 3
assert part2(fresh_ranges) == 14

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

fresh_ranges, ids_to_check = _get_fresh_ranges_and_ids_to_check("input.txt")

assert part1(fresh_ranges, ids_to_check) == 773
assert part2(fresh_ranges) == 332067203034711

print("Puzzle input: Successful")
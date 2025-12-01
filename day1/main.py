def part1(rotations: list[str], dial: int = 50) -> int:
    """ Returns amount of times we ended at 0 """
    result = 0
    for rotation in rotations:
        # get rotation
        is_add = rotation[0] == "R"
        count = int(rotation[1:])

        # add/subtract rotation
        rest = count % 100
        dial += rest if is_add else -rest

        # correct if out of bound
        dial = (dial + 100) % 100

        # check if ended at 0
        if dial == 0:
            result += 1

    return result

def part2(rotations: list[str], dial: int = 50) -> int:
    """ Returns amount of times we crossed 0 """
    result = 0
    for rotation in rotations:
        # get rotation
        is_add = rotation[0] == "R"
        count = int(rotation[1:])

        # check for complete cycles
        result += count // 100

        # add/subtract rotation (ignore complete cycles)
        rest = count % 100
        new_dial = dial + (rest if is_add else -rest)

        # check if 0 was crossed
        if (is_add and new_dial >= 100) or (new_dial < 1 and dial != 0): # if we are at 0 and subtract, we don't pass 0 again
            result += 1

        # correct if out of bound
        dial = (new_dial + 100) % 100
    
    return result
        

# ------------------------------------------------
# Example 
# ------------------------------------------------

rotations = []
with open("example.txt", "r") as file:
    for line in file:
        rotations.append(line.strip())

assert part1(rotations) == 3
assert part2(rotations) == 6

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

rotations = []
with open("input.txt", "r") as file:
    for line in file:
        rotations.append(line.strip())

assert part1(rotations) == 984
assert part2(rotations) == 5657

print("Puzzle input: Successful")

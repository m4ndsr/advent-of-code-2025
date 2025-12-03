def part1(banks: list[str]) -> int:
    biggest_joltages = []
    
    for bank in banks:
        n1 = _get_biggest_number(bank[:-1])
        start_idx_n2 = bank.index(n1) + 1
        n2 = _get_biggest_number(bank[start_idx_n2:])
        biggest_joltages.append(int(n1 + n2))

    return sum(biggest_joltages)

def part2(banks: list[str], total_length: int = 12) -> int:
    biggest_joltages = []
    
    for bank in banks:
        joltage = ""
        last_idx = 0
        
        min_extra_len = total_length - 1
        while len(joltage) != total_length:
            new_bank = bank[last_idx:-min_extra_len] if min_extra_len > 0 else bank[last_idx:]
            n = _get_biggest_number(new_bank)
            last_idx = bank.index(n, last_idx) + 1
            joltage += n
            min_extra_len -= 1

        biggest_joltages.append(int(joltage))

    return sum(biggest_joltages)


def _get_biggest_number(bank: str) -> str:
    numbers = sorted([n for n in bank])
    return numbers[-1]


# ------------------------------------------------
# Example 
# ------------------------------------------------

banks = []
with open("example.txt", "r") as file:
    for line in file:
        banks.append(line.strip())

assert part1(banks) == 357
assert part2(banks, 2) == 357
assert part2(banks) == 3121910778619

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

banks = []
with open("input.txt", "r") as file:
    for line in file:
        banks.append(line.strip())

assert part1(banks) == 17109
assert part2(banks, 2) == 17109
assert part2(banks) == 169347417057382

print("Puzzle input: Successful")
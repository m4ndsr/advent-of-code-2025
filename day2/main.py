def part1(ranges: list[str]) -> int:
    sum = 0
    
    for id_range in ranges:
        start, end = [int(n) for n in id_range.split("-")]
        
        for id in range(start, end + 1, 1):
            id_str = str(id)
            id_len = len(id_str)
        
            if id_len % 2 != 0:
                continue
        
            mid = id_len // 2 
            if id_str[:mid] == id_str[mid:]:
                sum += id
    
    return sum


def part2(ranges: list[str]) -> int:
    import re

    sum = 0

    for id_range in ranges:
        start, end = [int(n) for n in id_range.split("-")]
        
        for id in range(start, end + 1, 1):
            id_str = str(id)

            # if re.match(r'^(\w+?)\1+$', id_str):
            #     sum += id
            
            # id_len = len(id_str)
            # for amount_of_parts in range(2, id_len + 1):
            #     if id_len % amount_of_parts != 0:
            #         continue

            #     size = id_len // amount_of_parts
            #     pattern = id_str[:size]
            #     if id_str.count(pattern) == amount_of_parts:
            #         sum += id
            #         break

            id_len = len(id_str)
            for size in range(1, (id_len // 2) + 1):
                if id_len % size != 0:
                    continue

                pattern = id_str[:size]
                if (id_len // size) * pattern == id_str:
                    sum += id
                    break

    return sum
        

# ------------------------------------------------
# Example 
# ------------------------------------------------

ranges = []
with open("example.txt", "r") as file:
    ranges = file.readline().split(",")

assert part1(ranges) == 1227775554
assert part2(ranges) == 4174379265

print("Example: Successful")

# ------------------------------------------------
# Puzzle input
# ------------------------------------------------

ranges = []
with open("input.txt", "r") as file:
    ranges = file.readline().split(",")

assert part1(ranges) == 15873079081
assert part2(ranges) == 22617871034

print("Puzzle input: Successful")

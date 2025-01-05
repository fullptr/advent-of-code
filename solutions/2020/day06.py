count_part1 = 0
count_part2 = 0

with open("day06_input.txt") as f:
    for data in f.read().split("\n\n"):
        party = [set(x) for x in data.split("\n")]
        count_part1 += len(set.union(*party))
        count_part2 += len(set.intersection(*party))

print(count_part1)
print(count_part2)
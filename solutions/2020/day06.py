def main(data):
    count_part1 = count_part2 = 0
    for section in data.split("\n\n"):
        party = [set(x) for x in section.split("\n")]
        count_part1 += len(set.union(*party))
        count_part2 += len(set.intersection(*party))
    return count_part1, count_part2
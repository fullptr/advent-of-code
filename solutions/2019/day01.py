def fuel_part2(start):
    fuel = 0
    while start > 6:
        start = start // 3 - 2
        fuel += start
    return fuel

def main(data):
    part1 = sum(int(x)//3-2 for x in data.split("\n"))
    part2 = sum(fuel_part2(int(x)) for x in data.split("\n"))
    return part1, part2
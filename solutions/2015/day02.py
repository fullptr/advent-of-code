from itertools import combinations
from math import prod

def loop_input(data):
    for line in data.split("\n"):
        yield [int(n) for n in line.strip().split("x")]

def main(data):
    part1 = 0
    for dimensions in loop_input(data):
        side_areas = [x * y for x, y in combinations(dimensions, 2)]
        part1 += sum(2 * area for area in side_areas) + min(side_areas)

    part2 = 0
    for dimensions in loop_input(data):
        part2 += 2 * (sum(dimensions) - max(dimensions)) + prod(dimensions)
    
    return part1, part2
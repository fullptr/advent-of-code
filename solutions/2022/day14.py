from itertools import pairwise

def interval(a, b):
    step = 1 if a < b else -1
    while a != b:
        yield a
        a += step
    yield b

def from_string(string):
    return tuple(int(k) for k in string.split(","))

def part1_is_empty(floor, rocks, sand, pos):
    return pos not in rocks and pos not in sand

def part2_is_empty(floor, rocks, sand, pos):
    return part1_is_empty(floor, rocks, sand, pos) and pos[1] < floor

def drop_sand(floor, rocks, sand, pos_is_empty):
    sx = 500
    for sy in range(floor + 1):
        for dx in (0, -1, 1):
            if pos_is_empty(floor, rocks, sand, (sx + dx, sy + 1)):
                sx += dx
                break
        else:
            return (sx ,sy)

def main(data):
    data = data.split("\n")
    rocks = set()
    for line in data:
        coords = [from_string(s) for s in line.split(" -> ")]
        for (x1, y1), (x2, y2) in pairwise(coords):
            if x1 == x2:
                for y in interval(y1, y2):
                    rocks.add((x1, y))
            if y1 == y2:
                for x in interval(x1, x2):
                    rocks.add((x, y1))

    floor = max(y for (x, y) in rocks) + 2

    part1_sand = set()
    while new_sand := drop_sand(floor, rocks, part1_sand, part1_is_empty):
        part1_sand.add(new_sand)

    part2_sand = set()
    while new_sand := drop_sand(floor, rocks, part2_sand, part2_is_empty):
        part2_sand.add(new_sand)
        if new_sand == (500, 0):
            break

    return len(part1_sand), len(part2_sand)
import math

def walk(grid, x, y, dx, dy):
    width = len(grid[0])
    height = len(grid)
    x += dx
    y += dy
    while 0 <= x < width and 0 <= y < height:
        yield grid[y][x]
        x += dx
        y += dy

def seen_from(grid, x, y, dx, dy):
    for tree in walk(grid, x, y, dx, dy):
        if tree >= grid[y][x]:
            return False
    return True

def count_from(grid, x, y, dx, dy):
    count = 0
    for tree in walk(grid, x, y, dx, dy):
        count += 1
        if tree >= grid[y][x]:
            break
    return count

def neighbours(grid, x, y, func):
    return [
        func(grid, x, y, 0, -1),
        func(grid, x, y, -1, 0),
        func(grid, x, y, 1, 0),
        func(grid, x, y, 0, 1)
    ]

def seen(grid, x, y):
    return any(neighbours(grid, x, y, seen_from))

def scenic_score(grid, x, y):
    return math.prod(neighbours(grid, x, y, count_from))

def main(data):
    grid = [l.strip() for l in data.split("\n")]
    width = len(grid[0])
    height = len(grid)

    part1 = part2 = 0
    for y in range(height):
        for x in range(width):
            part1 += seen(grid, x, y)
            part2 = max(part2, scenic_score(grid, x, y))
    return part1, part2
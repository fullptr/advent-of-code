import math

def adjacent_values(data, i, j):
    width = len(data[0])
    height = len(data)
    if i - 1 >= 0:
        yield (i - 1, j), int(data[j][i-1])
    if i + 1 < width:
        yield (i + 1, j), int(data[j][i+1])
    if j - 1 >= 0:
        yield (i, j - 1), int(data[j-1][i])
    if j + 1 < height:
        yield (i, j + 1), int(data[j+1][i])

def low_points(data):
    for j, line in enumerate(data):
        for i, value in enumerate(line):
            if all([x > int(value) for _, x in adjacent_values(data, i, j)]):
                yield (i, j), int(value)

def basin_size(data, i, j):
    remaining_points = {(i, j)}
    seen_points = set()
    while len(remaining_points) > 0:
        p = remaining_points.pop()
        for q, value in adjacent_values(data, *p):
            if value < 9 and q not in seen_points:
                remaining_points.add(q)
        seen_points.add(p)
    return len(seen_points)

def main(data):
    data = [line.strip() for line in data.split("\n")]
    return (
        sum(val + 1 for _, val in low_points(data)),
        math.prod(sorted([basin_size(data, *p) for p, _ in low_points(data)])[-3:])
    )
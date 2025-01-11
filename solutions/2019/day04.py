from util import sliding

def adjacant_digits(value):
    for x, y in sliding(str(value), 2):
        if x == y:
            return 1
    return 0

def strict_adjacant_digits(value):
    found = 0
    for w, x, y, z in sliding([-1, *[int(x) for x in str(value)], -1], 4):
        if w != x and x == y and y != z:
            found = 1
    return found

def increasing_digits(value):
    for x, y in sliding((int(x) for x in str(value)), 2):
        if x > y:
            return False
    return True

def main(data):
    lower, upper = [int(x) for x in data.split("-")]
    part1 = part2 = 0
    for value in range(lower, upper + 1):
        if increasing_digits(value):
            part1 += adjacant_digits(value)
            part2 += strict_adjacant_digits(value)
            
    return part1, part2
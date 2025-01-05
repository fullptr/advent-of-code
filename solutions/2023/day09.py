from itertools import pairwise

def extrapolate(line):
    levels = [line]
    while any(levels[-1]):
        levels.append([b - a for a, b in pairwise(levels[-1])])
    
    while len(levels) > 1:
        *_, diff = levels.pop()
        levels[-1].append(levels[-1][-1] + diff)
        
    return line[-1]

def parse_lines(data):
    for line in data:
        yield [int(x) for x in line.strip().split()]
        
def main(data):
    data = data.split("\n")

    return (
        sum(extrapolate(l) for l in parse_lines(data)),
        sum(extrapolate(list(reversed(l))) for l in parse_lines(data))
    )
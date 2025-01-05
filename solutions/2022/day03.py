def triples(iterable):
    args = [iter(iterable)] * 3
    return zip(*args, strict=True)

def main(data):
    lines = [l.strip() for l in data.split("\n")]
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {letter: idx + 1 for idx, letter in enumerate(letters)}

    part1 = 0
    for line in lines:
        first_half = set(line[:len(line)//2])
        second_half = set(line[len(line)//2:])
        part1 += priorities[(first_half & second_half).pop()]

    part2 = 0
    for a, b, c in triples(lines):
        part2 += priorities[(set(a) & set(b) & set(c)).pop()]
    
    return part1, part2
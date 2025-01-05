def read_lines(data):
    for line in data.split("\n"):
        x, y = line.split()
        yield x, int(y)

def main(data):
    pos = 0
    p1_depth = 0
    p2_depth = 0
    p2_aim = 0

    for directive, value in read_lines(data):
        match directive:
            case "forward":
                pos += value
                p2_depth += value * p2_aim
            case "up":
                p1_depth -= value
                p2_aim -= value
            case "down":
                p1_depth += value
                p2_aim += value

    return pos * p1_depth, pos * p2_depth
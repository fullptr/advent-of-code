def skip_lines(f, count):
    for idx, line in enumerate(f, 1):
        if idx % count == 0:
            yield line

def slope(lines, right, down):
    count = 0
    position = 0
    first_line, *rest = lines
    width = len(first_line)
    for line in skip_lines(rest, down):
        position = (position + right) % width
        if line[position] == "#":
            count += 1
    return count

def main(data):
    lines = data.split("\n")
    return slope(lines, 3, 1), slope(lines, 1, 1) * slope(lines, 3, 1) * slope(lines, 5, 1) * slope(lines, 7, 1) * slope(lines, 1, 2)
def run(code):
    accumulator = 0
    index = 0
    visited = set()

    while index not in visited and index < len(code):
        visited.add(index)

        op, arg = code[index]
        if op == "acc":
            accumulator += arg
            index += 1
        elif op == "jmp":
            index += arg
        else:
            index += 1
        
    return accumulator, index >= len(code)

def part1(code):
    return run(code)[0]

def part2(code):
    for index, (op, arg) in enumerate(code):
        if op == "jmp":
            code[index][0] = "nop"
            acc, success = run(code)
            if success:
                return acc
            code[index][0] = "jmp"
        elif op == "nop":
            code[index][0] = "jmp"
            acc, success = run(code)
            if success:
                return acc
            code[index][0] = "nop"

def format_line(line):
    op, arg = line.strip().split()
    return [op, int(arg)]

with open("day08_input.txt") as f:
    code = [format_line(line) for line in f.readlines()]

print(part1(code))
print(part2(code))
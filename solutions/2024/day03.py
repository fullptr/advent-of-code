import re
   
def main(data): 
    pattern = re.compile(r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))")
    part1 = part2 = 0
    on = True
    for cmd, lhs, rhs in pattern.findall(data):
        if cmd.startswith("mul("):
            part1 += int(lhs) * int(rhs)
            if on:
                part2 += int(lhs) * int(rhs)
        elif cmd.startswith("do("):
            on = True
        elif cmd.startswith("don't("):
            on = False
    return part1, part2
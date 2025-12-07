import math

def make_number(vals):
    num = 0
    for x in vals:
        if x == " ":
            continue
        num = 10 * num + int(x)
    return num

def main(data):
    grid1 = []
    for line in data.split("\n"):
        grid1.append(line.split())
    
    part1 = 0
    for *vals, op in zip(*grid1):
        if op == "+":
            part1 += sum(int(x) for x in vals)
        else:
            part1 += math.prod(int(x) for x in vals)
            
    grid2 = data.split("\n")
    part2 = 0
    curr_op = None
    curr_vals = []
    for *vals, op in zip(*grid2):
        num = make_number(vals)
        if op == "+":
            curr_op = sum
        elif op == "*":
            curr_op = math.prod
            
        if num == 0:
            part2 += curr_op(curr_vals)
            curr_vals = []
        else:
            curr_vals.append(num)
    
    part2 += curr_op(curr_vals)        
    return part1, part2
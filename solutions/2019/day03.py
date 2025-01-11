def traverse_wire(moves):
    curr_x = curr_y = 0
    for move in moves.split(","):
        direction = move[0]
        steps = int(move[1:])
        if direction == "U":
            for _ in range(steps):
                curr_y += 1
                yield (curr_x, curr_y)
        elif direction == "R":
            for _ in range(steps):
                curr_x += 1
                yield (curr_x, curr_y)
        elif direction == "D":
            for _ in range(steps):
                curr_y -= 1
                yield (curr_x, curr_y)
        else:
            for _ in range(steps):
                curr_x -= 1
                yield (curr_x, curr_y)

def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])

def main(data):
    a, b = data.split("\n")
    wire_a = set(traverse_wire(a))
    wire_b = set(traverse_wire(b))
    intersections = wire_a & wire_b
    
    part1 = min(intersections, key=manhattan)
    
    wire_a_intersections = {}
    for step, pos in enumerate(traverse_wire(a), 1):
        if pos in intersections:
            wire_a_intersections[pos] = step
            
    wire_b_intersections = {}
    for step, pos in enumerate(traverse_wire(b), 1):
        if pos in intersections:
            wire_b_intersections[pos] = step
    
    part2 = None
    for pos in intersections:
        if part2 is None:
            part2 = wire_a_intersections[pos] + wire_b_intersections[pos]
        else:
            part2 = min(part2, wire_a_intersections[pos] + wire_b_intersections[pos])
    
    return manhattan(part1), part2
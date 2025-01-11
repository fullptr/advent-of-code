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

def step_distances(moves, intersections):    
    distances = {}
    for step, pos in enumerate(traverse_wire(moves), 1):
        if pos in intersections:
            distances[pos] = step
    return distances

def main(data):
    a, b = data.split("\n")
    
    wire_a = set(traverse_wire(a))
    wire_b = set(traverse_wire(b))
    intersections = wire_a & wire_b
    part1 = min(intersections, key=manhattan)
    
    wire_a_distances = step_distances(a, intersections)
    wire_b_distances = step_distances(b, intersections)
    part2 = min(wire_a_distances[pos] + wire_b_distances[pos] for pos in intersections)
    
    return manhattan(part1), part2
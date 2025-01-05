def instructions():
    with open("day12_input.txt") as f:
        for line in f:
            yield line[0], int(line[1:])

def move(pos, direction, value):
    x, y = pos
    return {
        "N": (x, y + value),
        "S": (x, y - value),
        "E": (x + value, y),
        "W": (x - value, y)
    }[direction]

def get_direction(rotation):
    return {
        0: "N",
        90: "E",
        180: "S",
        270: "W"
    }[rotation]

def part1():
    position = (0, 0)
    rotation = 90 # E
    for action, value in instructions():
        if action in {"N", "E", "S", "W"}:
            position = move(position, action, value)
        elif action == "R":
            rotation = (rotation + value) % 360
        elif action == "L":
            rotation = (rotation - value) % 360
        elif action == "F":
            direction = get_direction(rotation)
            position = move(position, direction, value)
    return abs(position[0]) + abs(position[1])


def rotate_waypoint(waypoint, rotation): # Rotate clockwise
    x, y = waypoint
    return {
        0: (x, y),
        90: (y, -x),
        180: (-x, -y),
        270: (-y, x)
    }[rotation]

def move_to_waypoint(position, waypoint, times):
    x, y = position
    dx, dy = waypoint
    return (x + times * dx, y + times * dy)

def part2():
    position = (0, 0)
    waypoint = (10, 1) # Offset of waypoint in world space coords
    for action, value in instructions():
        if action in {"N", "E", "S", "W"}:
            waypoint = move(waypoint, action, value)
        elif action == "R":
            waypoint = rotate_waypoint(waypoint, value)
        elif action == "L":
            waypoint = rotate_waypoint(waypoint, (-value % 360))
        elif action == "F":
            position = move_to_waypoint(position, waypoint, value)
    return abs(position[0]) + abs(position[1])

print(part1())
print(part2())
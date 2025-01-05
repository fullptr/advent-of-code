def move(p, char):
    match char:
        case "^":
            return (p[0], p[1] + 1)
        case "v":
            return (p[0], p[1] - 1)
        case ">":
            return (p[0] + 1, p[1])
        case "<":
            return (p[0] - 1, p[1])

def visited_houses(steps):
    pos = (0, 0)
    visited = set()
    for step in steps:
        visited.add(pos)
        pos = move(pos, step)
    return visited

def main(data):
    santa = visited_houses(step for i, step in enumerate(data) if i % 2 == 0)
    robo = visited_houses(step for i, step in enumerate(data) if i % 2 != 0)
    return len(visited_houses(data)), len(santa | robo)
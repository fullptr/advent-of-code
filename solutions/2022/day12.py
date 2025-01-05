from queue import SimpleQueue

abc = "abcdefghijklmnopqrstuvwxyz"
levels = {letter: idx for idx, letter in enumerate(abc)}
levels["S"] = 0
levels["E"] = 25

def find(rows, c):
    height = len(rows)
    width = len(rows[0])
    for y in range(height):
        for x in range(width):
            if rows[y][x] == c:
                return (x, y)

def level_of(rows, pos):
    x, y = pos
    idx = rows[y][x]
    return levels[idx]

def valid(rows, pos):
    x, y = pos
    height = len(rows)
    width = len(rows[0])
    return 0 <= x < width and 0 <= y < height

# Neighbour can either climb up 1 to us, or drop down to us
def can_move_from_neighbour(rows, curr, neighbour):
    return level_of(rows, curr) - 1 <= level_of(rows, neighbour)

def neighbours(rows, x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbour = (x + dx), (y + dy)
        if valid(rows, neighbour) and can_move_from_neighbour(rows, (x, y), neighbour):
            yield neighbour

def main(data):
    rows = [l.strip() for l in data.split("\n")]
    S = find(rows, "S")
    E = find(rows, "E")
    
    dist = {}
    queue = SimpleQueue()
    dist[E] = 0

    queue.put(E)
    while not queue.empty():
        x, y = queue.get()
        for neighbour in neighbours(rows, x, y):
            if neighbour not in dist:
                dist[neighbour] = dist[x, y] + 1
                queue.put(neighbour)

    part1 = dist[S]
    min_dist = dist[S]
    for (x, y), distance in dist.items():
        if rows[y][x] == "a" and distance < min_dist:
            min_dist = distance

    return part1, min_dist
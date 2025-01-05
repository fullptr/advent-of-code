from queue import PriorityQueue

def get_value_part1(board, x, y):
    width = len(board[0])
    height = len(board)
    return board[y][x] if 0 <= x < width and 0 <= y < height else None

def get_value_part2(board, x, y):
    width = len(board[0])
    height = len(board)
    if not (0 <= x < 5 * width and 0 <= y < 5 * height):
        return None
    value = (get_value_part1(board, x % width, y % height) + x // width + y // height) % 9
    return value if value != 0 else 9

def unvisited_neighbours(board, i, j, get_value, visited):
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        value = get_value(board, x, y)
        if value is not None and (x, y) not in visited:
            yield (x, y), value

def dijkstra(board, get_value, end_point):
    pq = PriorityQueue()
    pq.put((0, (0, 0))) # score, position
    visited = set()
    while pq:
        current, point = pq.get()
        if point == end_point:
            return current
        for (x, y), score in unvisited_neighbours(board, *point, get_value, visited):
            pq.put((current + score, (x, y)))
            visited.add((x, y))

def main(data):
    board = [[int(n) for n in l.strip()] for l in data.split("\n")]
    width = len(board[0])
    height = len(board)
    return (
        dijkstra(board, get_value_part1, (width - 1, height - 1)),
        dijkstra(board, get_value_part2, (5*width - 1, 5*height - 1))
    )
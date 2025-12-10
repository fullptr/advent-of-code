def generate_points(data):
    for line in data.split("\n"):
        x, y = line.split(",")
        yield int(x), int(y)

def main(data):
    points = list(generate_points(data))
    max_size = 0
    max_x, max_y = 0, 0
    for x1, y1 in points:
        max_x = max(max_x, x1)
        max_y = max(max_y, y1)
        for x2, y2 in points:
            size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_size = max(max_size, size)
            
    print(max_x, max_y)
    grid = [
        [" " for _ in range(max_x)] for _ in range(max_y)
    ]
    for x, y in points:
        grid[y][x] = "#"
    
    return max_size, 0
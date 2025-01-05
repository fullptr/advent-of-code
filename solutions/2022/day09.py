from dataclasses import dataclass

def steps(data):
    for line in data:
        direction, distance = line.strip().split()
        yield direction, int(distance)

@dataclass
class Vec2:
    x: int
    y: int

    def __sub__(self, other):
        return Vec2(self.x-other.x, self.y-other.y)

    def increase(self, other):
        self.x += other.x
        self.y += other.y

def tail_movement(offset: Vec2) -> Vec2:
    if abs(offset.x) > 1:
        offset.x //= 2
    if abs(offset.y) > 1:
        offset.y //= 2
    return offset

def run(data, snek_length):
    snek = [Vec2(0, 0) for _ in range(snek_length)]
    visited = set()

    for direction, distance in steps(data):
        for _ in range(distance):
            # Update head
            match direction:
                case "R": snek[0].increase(Vec2(1, 0))
                case "U": snek[0].increase(Vec2(0, 1))
                case "L": snek[0].increase(Vec2(-1, 0))
                case "D": snek[0].increase(Vec2(0, -1))

            # Update tails
            for i in range(1, len(snek)):
                H = snek[i-1]
                T = snek[i]
                ds = H - T
                if abs(ds.x) > 1 or abs(ds.y) > 1:
                    T.increase(tail_movement(ds))

            visited.add(str(snek[-1]))

    return len(visited)

def main(data):
    data = data.split("\n")
    return run(data, 2), run(data, 10)
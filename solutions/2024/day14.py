import parse
from dataclasses import dataclass
from util import Vec2

@dataclass
class Robot:
    pos: Vec2
    vel: Vec2

def step(robots, width, height):
    for robot in robots:
        robot.pos = robot.pos + robot.vel
        robot.pos = Vec2(robot.pos.x % width, robot.pos.y % height)
        
def safety_factor(robots, width, height):
    tl = tr = bl = br = 0
    for robot in robots:
        if robot.pos.x < width // 2:
            if robot.pos.y < height // 2:
                tl += 1
            elif robot.pos.y > height // 2:
                bl += 1
        elif robot.pos.x > width // 2:
            if robot.pos.y < height // 2:
                tr += 1
            elif robot.pos.y > height // 2:
                br += 1
    return tl * tr * bl * br

def average_position(robots):
    avg_x = sum(r.pos.x for r in robots) // len(robots)
    avg_y = sum(r.pos.y for r in robots) // len(robots)
    return Vec2(avg_x, avg_y)

def parse_robots(data):      
    robots = []
    pattern = "p={:d},{:d} v={:d},{:d}"
    for line in data.split("\n"):
        px, py, vx, vy = parse.parse(pattern, line).fixed
        robots.append(Robot(Vec2(px, py), Vec2(vx, vy)))
    return robots

def part1(data):
    robots = parse_robots(data)
    w = 101
    h = 103
    for _ in range(100):
        step(robots, w, h)
    return safety_factor(robots, w, h)

def longest_contiguous(robots, width, height):
    cells = [" " for _ in range(width * height)]
    for r in robots:
        cells[r.pos.x + r.pos.y * width] = "#"
    longest = 0
    current = 0
    for cell in cells:
        if cell == "#":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest

def part2(data):
    robots = parse_robots(data)
    w = 101
    h = 103
    for i in range(10000):
        step(robots, w, h)
        l = longest_contiguous(robots, w, h)
        if l > 20: # guessing if there's a line of +20 contiguous robots, its the picture
            return i + 1

def main(data):
    return part1(data), part2(data)
import parse

def parse_lines(data):
    line_pattern = "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}"
    for line in data:
        sx, sy, bx, by = parse.search(line_pattern, line)
        yield sx, sy, bx, by
    

def merge_ranges(ranges):
    new_ranges = []
    new_l, new_r = ranges[0]
    for l, r in ranges:
        if new_r < l:
            new_ranges.append((new_l, new_r))
            new_l, new_r = l, r
        else:
            new_r = max(r, new_r)
    new_ranges.append((new_l, new_r))
    return new_ranges

def get_slice(lines, y_coord):
    covered_x_ranges = []
    for sx, sy, bx, by in lines:

        dist = abs(bx - sx) + abs(by - sy) - abs(y_coord - sy)
        if dist > 0:
            covered_x_ranges.append((sx - dist, sx + dist))

    covered_x_ranges.sort()
    covered_x_ranges = merge_ranges(covered_x_ranges)
    return covered_x_ranges

def main(data):
    data = data.split("\n")
    lines = list(parse_lines(data))
    part1 = sum(abs(x - y) for x, y in get_slice(lines, 2_000_000))

    # wont work if the x coord is 0 or 4,000,000 since we're assuming 2 intervals, which is fine
    # for me but not in general, but it's a trivial fix to check that interval[0][0] is not 0
    for y in range(4_000_001):
        intervals = get_slice(lines, y)
        if len(intervals) == 2:
            x = intervals[0][1] + 1 # one past the end of the first interval, one before the start of the next
            part2 = 4_000_000 * x + y
            break
        
    return part1, part2
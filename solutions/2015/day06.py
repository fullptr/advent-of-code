import itertools
from collections import defaultdict

def parse_coord(coord):
    return [int(x) for x in coord.split(",")]

def loop_rect(src, dst):
    x_coords = [x for x in range(src[0], dst[0], 1 if dst[0] > src[0] else -1)] + [dst[0]]
    y_coords = [y for y in range(src[1], dst[1], 1 if dst[1] > src[1] else -1)] + [dst[1]]
    return itertools.product(x_coords, y_coords)


def main(data):
    lines = [l.strip().split() for l in data.split("\n")]
    part1_on = set()
    part2_on = defaultdict(int)

    for line in lines:
        match line:
            case ["toggle", x, "through", y]:
                for i, j in loop_rect(parse_coord(x), parse_coord(y)):
                    if (i, j) in part1_on:
                        part1_on.remove((i, j))
                    else:
                        part1_on.add((i, j))
                    part2_on[i, j] += 2
            case ["turn", "on", x, "through", y]:
                for i, j in loop_rect(parse_coord(x), parse_coord(y)):
                    part1_on.add((i, j))
                    part2_on[i, j] += 1
            case ["turn", "off", x, "through", y]:
                for i, j in loop_rect(parse_coord(x), parse_coord(y)):
                    part1_on.discard((i, j))
                    part2_on[i, j] = max(part2_on[i, j] - 1, 0)
    return len(part1_on), sum(x for x in part2_on.values())
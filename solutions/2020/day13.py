from math import ceil, prod

with open("day13_input.txt") as f:
    estimate = int(next(f))
    buses = [(idx, int(x)) for idx, x in enumerate(next(f).split(",")) if not x.startswith("x")]

def part1(estimate, buses):
    times = ((ceil(estimate / bus) * bus, bus) for _, bus in buses)
    earliest_time, earliest_id = min(times)
    return earliest_id * (earliest_time - estimate)

def part2(buses):
    N = prod(bus for _, bus in buses)
    x = 0
    for index, bus in buses: # index = a_k, bus = n_k
        y = N // bus
        x += index * y * pow(y, -1, bus)
    return -x % N

print(part1(estimate, buses))
print(part2(buses))
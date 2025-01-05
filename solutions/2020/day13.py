from math import ceil, prod

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

def main(data):
    estimate, buses = data.split("\n")
    estimate = int(estimate)
    buses = [(idx, int(x)) for idx, x in enumerate(buses.split(",")) if not x.startswith("x")]
    return part1(estimate, buses), part2(buses)
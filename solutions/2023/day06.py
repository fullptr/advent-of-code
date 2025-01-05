import math

def ways_to_win(t, d):
    x0 = math.ceil((t + math.sqrt(t**2 - 4*d))/2 - 1)
    x1 = math.floor((t - math.sqrt(t**2 - 4*d))/2)
    return x0 - x1

def main(data):
    times_str, distances_str = data.split("\n")

    times = [int(x) for x in times_str.split()[1:]]
    distances = [int(x) for x in distances_str.split()[1:]]
    part1 = math.prod(ways_to_win(t, d) for t, d in zip(times, distances))

    time = int("".join(times_str.split()[1:]))
    distance = int("".join(distances_str.split()[1:]))
    part2 = ways_to_win(time, distance)

    return part1, part2
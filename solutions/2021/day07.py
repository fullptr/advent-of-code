import statistics, math

def triangle(x, y):
    n = abs(x - y)
    return (n * (n + 1)) // 2

def main(data):
    crabs = [int(n) for n in data.split(",")]
    
    median = int(statistics.median(crabs))
    part1 = sum(abs(crab - median) for crab in crabs)

    mean = sum(crabs) / len(crabs)
    part2 = min(
        int(sum(triangle(crab, math.floor(mean)) for crab in crabs)),
        int(sum(triangle(crab, math.ceil(mean)) for crab in crabs))
    )
    
    return part1, part2

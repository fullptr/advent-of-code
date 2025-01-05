from collections import defaultdict
from functools import lru_cache
from math import prod

def funky_fibonacci(n):
    if n < 3:
        return 2 ** (n - 1)

    a = 1
    b = 2
    c = 4
    for _ in range(n - 3):
        a, b, c = b, c, a + b + c
    return c

def part1(delta_counts):
    return delta_counts[1] * delta_counts[3]

def part2(deltas):
    x = "".join(str(s) for s in deltas).split("3")
    x = (len(s) for s in x if s)
    return prod(funky_fibonacci(i) for i in x)

with open("day10_input.txt") as f:
    nums = sorted(map(int, f))

deltas = []
delta_counts = defaultdict(int)
for prev, curr in zip([0, *nums], nums):
    deltas.append(curr - prev)
    delta_counts[curr - prev] += 1

delta_counts[3] += 1

print(part1(delta_counts))
print(part2(deltas))
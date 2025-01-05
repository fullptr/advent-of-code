from day01 import sum_to
from collections import deque

def part1(nums):
    d = deque()
    it = iter(nums)

    for _ in range(25):
        d.append(next(it))

    for x in it:
        if sum_to(d, x, 2) is None:
            return x

        d.popleft()
        d.append(x)

def part2(nums, invalid):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j]
            if sum(subarray) == invalid:
                return min(subarray) + max(subarray)

with open("day09_input.txt") as f:
    nums = list(int(x) for x in f)
    invalid = part1(nums)
    print(invalid)
    print(part2(nums, invalid))
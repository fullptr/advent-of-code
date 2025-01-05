from collections import deque

def sum_to(nums, target, count):
    if count > 1:
        for a in nums:
            if b := sum_to(nums, target - a, count - 1):
                return a * b
    elif target in nums:
        return target
    
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

def main(data):
    nums = list(int(x) for x in data.split("\n"))
    invalid = part1(nums)
    return invalid, part2(nums, invalid)
def sum_to(nums, target, count):
    if count > 1:
        for a in nums:
            if b := sum_to(nums, target - a, count - 1):
                return a * b
    elif target in nums:
        return target

def main(data):
    lines = set(map(int, data.split("\n")))
    return sum_to(lines, 2020, 2), sum_to(lines, 2020, 3)
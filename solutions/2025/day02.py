
def is_invalid_part1(num):
    return num[:len(num)//2] == num[len(num)//2:]

def is_invalid_part2(num):
    for length in range(1, len(num)//2 + 1):
        count = len(num) // length
        start = num[:length]
        if start * count == num:
            return True
    return False

def intervals(data):
    for l in data.split(","):
        left, right = l.strip().split("-")
        for num in range(int(left), int(right) + 1):
            yield str(num)
        
def main(data):
    count1 = count2 = 0
    for num in intervals(data):
        if is_invalid_part1(num):
            count1 += int(num)
        if is_invalid_part2(num):
            count2 += int(num)
    return count1, count2
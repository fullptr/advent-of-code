from collections import Counter

def main(data):
    stone_counts = Counter((int(x) for x in data.split()))

    for iteration in range(75):
        new_stones = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                new_stones[int(str(stone)[:len(str(stone))//2])] += count
                new_stones[int(str(stone)[len(str(stone))//2:])] += count
            else:
                new_stones[stone * 2024] += count
        stone_counts = new_stones
        if iteration == 24:
            part1 = stone_counts.total()
        
    return part1, stone_counts.total()
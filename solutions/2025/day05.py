def parse_ranges(ranges_raw):
    for line in ranges_raw.split("\n"):
        left, right = line.split("-")
        yield int(left), int(right)
        
def check_is_fresh(ingredient, ranges):
    for a, b in ranges:
        if a <= ingredient <= b:
            return True
    return False

def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = []
    curr_min = ranges[0][0]
    curr_max = ranges[0][1]
    for a, b in ranges:
        if a <= curr_max:
            curr_max = max(curr_max, b)
        else:
            merged.append((curr_min, curr_max))
            curr_min = a
            curr_max = b
    merged.append((curr_min, curr_max))
    return merged

def main(data):
    ranges_raw, fresh_raw = data.split("\n\n")
    ranges = list(parse_ranges(ranges_raw))
    fresh = [int(x) for x in fresh_raw.split("\n")]
    
    part1 = 0
    for ingredient in fresh:
        if check_is_fresh(ingredient, ranges):
            part1 += 1
            
    merged_ranges = merge_ranges(ranges)
    part2 = 0
    for a, b in merged_ranges:
        part2 += b - a + 1
    return part1, part2
def get_rolls(data):
    rolls = set()
    for y, row in enumerate(data.split("\n")):
        for x, val in enumerate(row):
            if val == "@":
                rolls.add((x, y))
    return rolls

def count_neighbours(rolls, pos):
    x, y = pos
    count = 0
    if (x + 1, y) in rolls: count += 1
    if (x - 1, y) in rolls: count += 1
    if (x, y + 1) in rolls: count += 1
    if (x, y - 1) in rolls: count += 1
    if (x - 1, y - 1) in rolls: count += 1
    if (x - 1, y + 1) in rolls: count += 1
    if (x + 1, y - 1) in rolls: count += 1
    if (x + 1, y + 1) in rolls: count += 1
    return count

def accessible_rolls(rolls):
    accessible = set()
    for roll in rolls:
        if count_neighbours(rolls, roll) < 4:
            accessible.add(roll)
    return accessible

def main(data):
    rolls = get_rolls(data)
    accessible = accessible_rolls(rolls)
    part1 = part2 = len(accessible)
    while len(accessible) > 0:
        rolls -= accessible
        accessible = accessible_rolls(rolls)
        part2 += len(accessible)
    return part1, part2
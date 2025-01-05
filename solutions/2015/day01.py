from collections import Counter

def main(data):
    counts = Counter(data)
    floor = 0
    for pos, bracket in enumerate(data, 1):
        floor += 1 if bracket == "(" else -1
        if floor < 0:
            break
    return counts["("] - counts[")"], pos
from collections import Counter
def main(data):
    first, *rows = data.split("\n")
    beams = Counter()
    for idx, val in enumerate(first):
        if val == "S":
            beams[idx] += 1
            break
        
    splits = 0
    for row in rows:
        next_beams = Counter()
        for idx, val in enumerate(row):
            if idx in beams:
                if val == "^":
                    splits += 1
                    next_beams[idx - 1] += beams[idx]
                    next_beams[idx + 1] += beams[idx]
                else:
                    next_beams[idx] += beams[idx]
        beams = next_beams
        
    return splits, beams.total()
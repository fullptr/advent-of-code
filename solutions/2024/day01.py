from collections import Counter
from bisect import insort
    
def main(data):
    l = []
    r = []
    for line in data.split("\n"):
        a, b = line.split()
        insort(l, int(a))
        insort(r, int(b))
        
    counts = Counter(r)
    return (
        sum(abs(b - a) for a, b in zip(l, r)),
        sum(a * counts[a] for a in l)
    )
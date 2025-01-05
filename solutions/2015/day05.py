from itertools import pairwise
from collections import Counter

def is_nice_p1(string):
    def conditions():
        yield sum(1 for k in string if k in {"a", "e", "i", "o", "u"}) >= 3
        yield sum(1 for a, b in pairwise(string) if a == b) > 0
        yield all(sub not in string for sub in ["ab", "cd", "pq", "xy"])
    return all(conditions())

def triplewise(iterable):
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c

def quadwise(iterable):
    for (a, _, _), (b, c, d) in pairwise(triplewise(iterable)):
        yield a, b, c, d

def is_nice_p2(string):
    pairs = Counter()
    found_xyx = False
    for a, b in pairwise(string):
        pairs[a, b] += 1
    for a, b, c in triplewise(string):
        if a == b == c:
            pairs[a, b] -= 1
        if a == c:
            found_xyx = True
    for a, b, c, d in quadwise(string):
        if a == b == c == d:
            pairs[a, b] += 1

    return found_xyx and any(x >= 2 for x in pairs.values())

def main(data):
    data = data.split("\n")
    return sum(1 for x in data if is_nice_p1(x)), sum(1 for x in data if is_nice_p2(x))
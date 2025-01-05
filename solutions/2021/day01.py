from itertools import pairwise

def triplet_sums(iterable):
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a + b + c

def main(data):
    data = [int(x) for x in data.split("\n")]
    return sum(1 for a, b in pairwise(data) if b > a), sum(1 for a, b in pairwise(triplet_sums(data)) if int(b) > int(a))
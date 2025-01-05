from itertools import islice

def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def find_marker(data, size):
    for idx, chars in enumerate(window(data, size), size):
        if len(set(chars)) == size:
            return idx

def main(data):
    return find_marker(data, 4), find_marker(data, 14)
import hashlib
import itertools

def find_hash(key, num_zeroes):
    zeroes = "0" * num_zeroes
    for c in itertools.count():
        attempt = f"{key}{c}".encode()
        if hashlib.md5(attempt).hexdigest()[:num_zeroes] == zeroes:
            return c

def main(data):
    return find_hash(data, 5), find_hash(data, 6)
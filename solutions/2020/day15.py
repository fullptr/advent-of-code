def van_eck(start, n):
    if n < len(start):
        return start[n-1]

    curr_val = start[-1]
    seen = {val: idx for idx, val in enumerate(start[:-1])}
    for i in range(len(start) - 1, n - 1):
        next_val = i - seen[curr_val] if curr_val in seen else 0
        seen[curr_val] = i
        curr_val = next_val

    return curr_val

def main(data):
    vals = [int(x) for x in data.split(",")]
    return van_eck(vals, 2020), van_eck(vals, 30000000)
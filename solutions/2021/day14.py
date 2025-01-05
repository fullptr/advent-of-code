from itertools import pairwise
from collections import Counter

def next_step(mappings, state):
    new_state = Counter()
    for (lhs, rhs), middle in mappings.items():
        new_state[lhs, middle] += state[lhs, rhs]
        new_state[middle, rhs] += state[lhs, rhs]
    return new_state

def run(template, mappings, steps):
    state = Counter(pairwise(template))
    for _ in range(steps):
        state = next_step(mappings, state)

    counts = Counter({template[0]: 1})
    for (_, rhs), count in state.items():
        counts[rhs] += count
    return (max(counts.values()) - min(counts.values()))

def main(data):
    template, *mappings = data.split("\n")
    template = template.strip()
    mappings = dict(l.strip().split(" -> ") for l in mappings if l.strip())
    return run(template, mappings, 10), run(template, mappings, 40)
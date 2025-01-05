from itertools import cycle
from math import lcm

def get_cycle(graph, directions, start, is_sentinel):
    curr = start
    count = 0
    for d in cycle(directions):
        if is_sentinel(curr):
            return count
        
        curr = graph[curr][d == "R"]
        count += 1

def main(data):
    directions, edges = data.split("\n\n")
    
    graph = {}
    for line in edges.split("\n"):
        src, dsts = line.split(" = ")
        graph[src] = dsts[1:-1].split(", ")
        
    part1_sentinel = lambda n: n == "ZZZ"  
    part1 = get_cycle(graph, directions, "AAA", part1_sentinel)

    part2_sentinel = lambda n: n.endswith("Z")
    part2 = lcm(*[get_cycle(graph, directions, n, part2_sentinel) for n in graph if n.endswith("A")])

    return part1, part2
from dataclasses import dataclass
from itertools import combinations
import math

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int
    
def length2(pair):
    a, b = pair
    return (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2

def add_edge(graph, edge):
    a, b = edge
    if b not in graph[a]: # connecting both together
        new_circuit = graph[a] | graph[b]
        for p in new_circuit:
            graph[p] = new_circuit

def main(data):
    points = []
    for line in data.split("\n"):
        x, y, z = [int(a) for a in line.split(",")]
        points.append(Point(x, y, z))
        
    edges = sorted(combinations(points, 2), key=length2)

    # point -> set of reachable points
    graph = {p: frozenset([p]) for p in points}
        
    part1 = part2 = None
    for i, (a, b) in enumerate(edges):
        add_edge(graph, (a, b))
        
        if i == 1000 - 1:
            circuits = sorted(set(graph.values()), key=len, reverse=True)
            part1 = math.prod(len(x) for x in circuits[:3])
        if len(graph[a]) == len(points): # we are done
            part2 = a.x * b.x
            break
    
    return part1, part2
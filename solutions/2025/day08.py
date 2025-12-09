from dataclasses import dataclass
from itertools import combinations
from collections import defaultdict

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int
    
def length2(pair):
    a, b = pair
    return (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2

def make_edge_map(edges):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def flood_fill(p, graph):
    """"""
    seen = set()
    to_check = [p]
    while to_check:
        curr = to_check.pop()
        seen.add(curr)
        for n in graph[curr]:
            if n not in seen:
                to_check.append(n)
    return seen

def count_circuits(points, edge_map):
    circuits = []
    
    while points:
        start = points.pop()
        cloud = flood_fill(start, edge_map)
        points -= cloud
        circuits.append(cloud)
    
    return sorted(circuits, key=len, reverse=True)


def make_circuits_with_edges(points, edges):
    edge_map = make_edge_map(edges)
    return count_circuits({p for p in points}, edge_map)

def add_edge(graph, edge):
    a, b = edge
    if b not in graph[a]: # connecting both together
        new_circuit = graph[a] | graph[b]
        for p in new_circuit:
            graph[p] = new_circuit
            
def get_circuits(c):
    circuits = []
    for circuit in c.values():
        if circuit not in circuits:
            circuits.append(circuit)
    return sorted(circuits, key=len, reverse=True)

def main(data):
    points = []
    for line in data.split("\n"):
        x, y, z = [int(a) for a in line.split(",")]
        points.append(Point(x, y, z))
        
    edges = list(combinations(points, 2))
    edges = sorted(edges, key=length2)
    
    # Part 1
    circuits = make_circuits_with_edges(
        {p for p in points},
        edges[:1000]
    )
    a, b, c, *_ = circuits
    part1 = len(a) * len(b) * len(c)
    
    # Part 2
    c = {p: set() for p in points}
    for p in points:
        c[p].add(p)
        
    for a, b in edges:
        add_edge(c, (a, b))            
        if len(c[a]) == len(points): # we are done
            break
    part2 = a.x * b.x
        
    return part1, part2
    
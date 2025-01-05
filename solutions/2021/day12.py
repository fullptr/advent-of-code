from collections import defaultdict

def process_node(graph, visited, current, second_visit_used):
    completed = 0

    for child in graph[current]:
        if child == "start":
            continue
        if child == "end":
            completed += 1
        elif child.islower():
            if child in visited and not second_visit_used:
                completed += process_node(graph, visited | {child}, child, True)
            elif child not in visited:
                completed += process_node(graph, visited | {child}, child, second_visit_used)
        else:
            completed += process_node(graph, visited, child, second_visit_used)

    return completed

def main(data):
    graph = defaultdict(set)
    for line in data.split("\n"):
        lhs, rhs = line.strip().split("-")
        graph[lhs].add(rhs)
        graph[rhs].add(lhs)
    return process_node(graph, set(), "start", True), process_node(graph, set(), "start", False)
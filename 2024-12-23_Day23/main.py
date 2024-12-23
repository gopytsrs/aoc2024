from itertools import combinations
from collections import defaultdict
def parse():
    f = open("input.txt", "r")
    return [f.split("-") for f in f.read().split("\n")]

def get_graph():
    edges = parse()
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph
    

def solve1():
    graph = get_graph()
    connections = set()
    for a, b, c in combinations(graph, 3):
        if (b in graph[a] and c in graph[a] and
            c in graph[b] and a in graph[b] and
            a in graph[c] and b in graph[c]) and "t" in f"{a[0]}{b[0]}{c[0]}":
            connections.add(tuple(sorted([a, b, c])))
    return len(connections)
            
def solve2():
    graph = get_graph()
    groups = []
    for computer in graph:
        connected = False
        for group in groups:
            if all(nei in graph[computer] for nei in group):
                group.add(computer)
                connected = True
        if not connected: # it forms a new group
            group = set()
            group.add(computer)
            groups.append(group)
    return ",".join(sorted(max(groups, key=len)))

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
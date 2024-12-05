from collections import defaultdict, deque

def parse():
    f = open("input.txt").read().split("\n\n")
    rules = [x.split("|") for x in f[0].split("\n")]
    updates = [x.split(",") for x in f[1].split("\n")]
    graph = defaultdict(set)

    for x, y in rules:
        graph[x].add(y)

    return graph, updates

def is_update_valid(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            page1, page2 = update[i], update[j]
            if page1 in rules[page2]:
                return False
    return True

def get_middle_page(update):
    return update[len(update) // 2]

def solve1():
    rules, updates = parse()    
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            total += int(get_middle_page(update))
                    
    return total

def get_sorted_update(update, rules):
    indegree = defaultdict(int)
    
    for page1 in update:
        if page1 not in rules:
            continue
        for page2 in update:
            if page2 in rules[page1]:
                indegree[page2] += 1

           
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_update = []
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in rules[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update

def solve2():
    rules, updates = parse()
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            continue
        sorted_update = get_sorted_update(update, rules)
        total += int(get_middle_page(sorted_update))
    return total
        
print("Part 1:", solve1())
print("Part 2:", solve2())
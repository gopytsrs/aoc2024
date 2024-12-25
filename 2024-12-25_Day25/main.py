def parse():
    f = open("input.txt").read().split("\n\n")
    locks = []
    keys = []
    for line in f:
        line = line.split("\n")
        if line[0].startswith("#"):
            locks.append(line)
        elif line[-1].startswith("#"):
            keys.append(line)
    return locks, keys

def can_fit(key_pattern, lock_pattern):
    return all(k + l <= 5 for k, l in zip(key_pattern, lock_pattern))

def get_patterns(entities):
    patterns = []
    for entity in entities:
        pattern = []
        for col in range(5):
            height = sum(int(entity[row][col] == "#") for row in range(1, 6))
            pattern.append(height)
        patterns.append(pattern)
    return patterns

def get_combinations(lock_patterns, key_patterns):
    combinations = 0
    for lock_pattern in lock_patterns:
        for key_pattern in key_patterns:
            if can_fit(key_pattern, lock_pattern):
                combinations += 1
    return combinations

def solve1():
    locks, keys = parse()
    lock_patterns = get_patterns(locks)
    key_patterns = get_patterns(keys)
    return get_combinations(lock_patterns, key_patterns)
        

print(f"Part 1: {solve1()}")
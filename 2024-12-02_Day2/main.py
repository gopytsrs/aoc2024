def parse():
    res = []
    with open("input.txt") as f:
        for line in f:
            res.append(list(map(int, line.strip().split())))
    return res

def all_increasing(sequence):
    return all(1 <= sequence[i+1] - sequence[i] <= 3 for i in range(len(sequence) - 1))

def all_decreasing(sequence):
    return all(1 <= sequence[i] - sequence[i+1] <= 3 for i in range(len(sequence) - 1))

def solve1():
    lines = parse()
    safe = 0
    for line in lines:
        if all_increasing(line) or all_decreasing(line):
            safe += 1
    return safe

def solve2():
    lines = parse()
    safe = 0
    for line in lines:
        one = line[0]
        removed = False
        for two in range(1, len(line) - 1):
            if not 1 <= line[two] - line[one] <= 3:
                if not removed:
                    removed = True
                else:
                    break
            
    return safe
            
                

print("Part 1:", solve1())
print("Part 2:", solve2())
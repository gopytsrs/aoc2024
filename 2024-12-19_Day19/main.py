def parse():
    d, p = open("input.txt", "r").read().split("\n\n")
    patterns = list(map(str.strip, d.split(",")))
    designs = list(map(str.strip, p.split("\n")))
    return patterns, designs

patterns, designs = parse()
patterns = set(patterns)

def can_form(i, design):
    if i == len(design):
        return True
    for j in range(i, len(design)):
        pattern = design[i:j+1]
        if pattern in patterns:
            if can_form(j+1, design):
                return True
    return False

def solve1():
    return sum(can_form(0, design) for design in designs)

def count_ways(design):
    N = len(design)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(i):
            pattern = design[j:i]
            if pattern in patterns:
                dp[i] += dp[j]
    return dp[N]


def solve2():
    return sum(count_ways(d) for d in designs)
    

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
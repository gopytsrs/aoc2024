from collections import deque
from functools import cache

def parse():
    return open("input.txt").read().splitlines()

KEYPAD = [
    ["7", "8", "9"], 
    ["4", "5", "6"], 
    ["1", "2", "3"], 
    [" ", "0", "A"]
]
KEYPAD_POS = {
    KEYPAD[r][c]: (r, c) 
    for r in range(len(KEYPAD)) 
    for c in range(len(KEYPAD[0]))
}

DPAD = [
    [" ", "^", "A"], 
    ["<", "v", ">"]
]
DPAD_POS = {
    DPAD[r][c]: (r, c) 
    for r in range(len(DPAD)) 
    for c in range(len(DPAD[0]))
}


def is_valid_cell(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def next_cells(r, c, grid):
    for nr, nc, symbol in ((r + 1, c, "v"), (r - 1, c, "^"), (r, c + 1, ">"), (r, c - 1, "<")):
        if is_valid_cell(nr, nc, grid):
            yield nr, nc, symbol

def get_paths(start, end):
    use_keypad = start.isnumeric() or end.isnumeric()
    grid = KEYPAD if use_keypad else DPAD
    pos = KEYPAD_POS if use_keypad else DPAD_POS

    visited = set()
    queue = deque([(*pos[start], [])])
    paths = []

    while queue:
        r, c, path = queue.popleft()
        if (r, c) == pos[end]:
            paths.append("".join(path + ["A"]))
            continue
        for nr, nc, symbol in next_cells(r, c, grid):
            if (nr, nc) not in visited and grid[nr][nc] != " ":
                queue.append((nr, nc, path + [symbol]))
        visited.add((r, c))
        
    return paths

@cache
def get_min_length(sequence, depth):
    min_length = 0
    prev = "A"
    for curr in sequence:
        paths = get_paths(prev, curr)
        if depth == 0:
            min_length += min(len(path) for path in paths)
        else:    
            min_length += min(get_min_length(path, depth - 1) for path in paths)
        prev = curr
    return min_length

def solve1():
    return sum(get_min_length(code, 2) * int(code[:-1]) for code in parse())

def solve2():
    return sum(get_min_length(code, 25) * int(code[:-1]) for code in parse())

print(f"Part 1: {solve1()}")    
print(f"Part 2: {solve2()}")
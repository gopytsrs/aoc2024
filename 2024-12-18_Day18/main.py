def parse():
    with open('input.txt') as f:
        return [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

ROWS = COLS = 71
def next_cells(r, c):
    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            yield nr, nc
            
from collections import deque

def bfs(grid, r, c):
    queue = deque([(r, c)])
    visited = [[False] * COLS for _ in range(ROWS)]
    visited[r][c] = True
    steps = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for nr, nc in next_cells(r, c):
                if (nr, nc) == (ROWS-1, COLS-1):
                    return steps + 1
                if visited[nr][nc] or grid[nr][nc] == -1:
                    continue
                visited[nr][nc] = True
                queue.append((nr, nc))
        steps += 1
    return -1

def solve1():
    corrupted = parse()
    grid = [[0] * COLS for _ in range(ROWS)]
    for i in range(1024):
        r, c = corrupted[i]
        grid[r][c] = -1
    
    return bfs(grid, 0, 0)

def corrupt_grid(grid, r, c, corrupted, corrupt_till_idx):
    new_grid = [row[:] for row in grid]
    for i in range(corrupt_till_idx + 1):
        r, c = corrupted[i]
        new_grid[r][c] = -1
    return new_grid

def solve2():
    corrupted = parse()
    left, right = 0, len(corrupted) - 1
    while left < right:
        mid = (right - left) // 2 + left
        grid = corrupt_grid([[0] * COLS for _ in range(ROWS)], 0, 0, corrupted, mid)
        if bfs(grid, 0, 0) == -1:
            right = mid
        else:
            left = mid + 1
    
    r, c = corrupted[left]
    return f"{r},{c}"

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
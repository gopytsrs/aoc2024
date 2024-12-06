def parse_input():
    f = open("input.txt", "r").read().split("\n")
    return [list(row) for row in f]

def find_start(grid, ROWS, COLS):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "^":
                return r, c
    return -1, -1

def solve1():
    grid = parse_input()
    ROWS, COLS = len(grid), len(grid[0])
    visited = [[False] * COLS for _ in range(ROWS)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    d = 0  # initial direction is "up"
    sr, sc = find_start(grid, ROWS, COLS)

    while 0 <= sr < ROWS and 0 <= sc < COLS:
        visited[sr][sc] = True

        nr, nc = sr + directions[d][0], sc + directions[d][1]

        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "#":
            d = (d + 1) % 4
        else:
            sr, sc = nr, nc

    result = sum(sum(row) for row in visited)
    return result
def simulate_with_obstruction(grid, ROWS, COLS, sr, sc, d, directions):
    visited = set()

    while 0 <= sr < ROWS and 0 <= sc < COLS:
        if (sr, sc, d) in visited:
            return True
        visited.add((sr, sc, d))

        nr, nc = sr + directions[d][0], sc + directions[d][1]

        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "#":
            d = (d + 1) % 4
        else:
            sr, sc = nr, nc

    return False

def solve2():
    grid = parse_input()
    ROWS, COLS = len(grid), len(grid[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    d = 0
    sr, sc = find_start(grid, ROWS, COLS)

    # Brute force try placing an obstruction at each empty cell and see if there is a loop
    valid_positions = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == ".":
                grid[r][c] = "#"
                if simulate_with_obstruction(grid, ROWS, COLS, sr, sc, d, directions):
                    valid_positions += 1
                grid[r][c] = "."

    return valid_positions

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

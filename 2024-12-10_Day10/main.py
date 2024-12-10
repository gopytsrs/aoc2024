# main.py
def parse():
    f = open("input.txt").read().splitlines()
    return [list(map(int, list(x))) for x in f]


grid = parse()
ROWS, COLS = len(grid), len(grid[0])


def next_cells(r, c):
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            yield nr, nc


def get_score(r, c, visited):
    if grid[r][c] == 9:
        return 1
    visited.add((r, c))
    total = 0
    for nr, nc in next_cells(r, c):
        if (nr, nc) in visited or grid[nr][nc] - grid[r][c] != 1:
            continue
        visited.add((nr, nc))
        total += get_score(nr, nc, visited)
    return total


def solve1():
    score = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                visited = set()
                score += get_score(r, c, visited)
    return score

def get_rating(sr, sc):
    unique_paths = set()

    def helper(r, c, path):
        if grid[r][c] == 9:
            unique_paths.add(tuple(path))
            return
        for nr, nc in next_cells(r, c):
            if grid[nr][nc] == grid[r][c] + 1:
                helper(nr, nc, path + [(nr, nc)])

    helper(sr, sc, [(sr, sc)])
    return len(unique_paths)


def solve2():
    rating = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                rating += get_rating(r, c)
    return rating


print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

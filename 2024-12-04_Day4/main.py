def parse():
    grid = []
    with open("input.txt") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def solve1():
    """
    Find xmas in one direction of eight directions.
    """
    grid = parse()
    ROWS, COLS = len(grid), len(grid[0])
    target = "XMAS"

    def dfs(r, c, i, dr, dc):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != target[i]:
            return False
        if i == len(target) - 1:
            return True
        return dfs(r + dr, c + dc, i + 1, dr, dc)

    count = 0
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != target[0]:
                continue
            for dr, dc in directions:
                if dfs(r, c, 0, dr, dc):
                    count += 1

    return count


def solve2():
    """
    Counts the number of X-MAS patterns in the grid, considering all four patterns.
    
    M # S
    # A #
    S # M
    
    M # S
    # A #
    M # S
    
    S # M
    # A #
    S # M
    
    S # M
    # A #
    M # S
    """
    grid = parse()
    ROWS, COLS = len(grid), len(grid[0])
    count = 0
    
    def get_neg_diag(r, c):
        return f"{grid[r-1][c-1]}{grid[r][c]}{grid[r+1][c+1]}"

    def get_pos_diag(r, c):
        return f"{grid[r-1][c+1]}{grid[r][c]}{grid[r+1][c-1]}"

    
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if grid[r][c] == "A":
                if (
                        (get_neg_diag(r, c) == "MAS" and get_pos_diag(r, c) == "MAS") or
                        (get_neg_diag(r, c) == "MAS" and get_pos_diag(r, c) == "SAM") or
                        (get_neg_diag(r, c) == "SAM" and get_pos_diag(r, c) == "MAS") or
                        (get_neg_diag(r, c) == "SAM" and get_pos_diag(r, c) == "SAM")
                    ):
                    count += 1

    return count



print("Part 1:", solve1())
print("Part 2:", solve2())
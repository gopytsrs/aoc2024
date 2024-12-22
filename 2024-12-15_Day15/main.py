from collections import defaultdict, deque

def parse():
    grid, directions = open("input.txt").read().split('\n\n')
    grid = [list(row) for row in grid.split('\n')]
    return grid, [d for d in directions if d in DIRECTIONS_MAPPING]

DIRECTIONS_MAPPING = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
def get_robot_position(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                return r, c

def get_grid_after_directions(grid, directions):
    rr, rc = get_robot_position(grid)
    for d in directions:
        dr, dc = DIRECTIONS_MAPPING[d]
        nr, nc = rr + dr, rc + dc
        while grid[nr][nc] == "O":
            nr, nc = nr + dr, nc + dc
        if grid[nr][nc] == ".":
            grid[rr][rc] = "."
            grid[nr][nc], grid[rr+dr][rc+dc] = grid[rr+dr][rc+dc], "@"
            rr, rc = rr + dr, rc + dc
    return grid

def get_gps_coordinate_sum(grid, target_cell):
    coordinate_sum = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == target_cell:
                coordinate_sum += 100 * r + c
    return coordinate_sum

def get_expanded_grid(grid):
    ROWS, COLS = len(grid), len(grid[0])
    new_grid = []
    for r in range(ROWS):
        new_row = []
        for c in range(COLS):
            if grid[r][c] == "#":
                new_row.append("#")
                new_row.append("#")
            elif grid[r][c] == ".":
                new_row.append(".")
                new_row.append(".")
            elif grid[r][c] == "@":
                new_row.append("@")
                new_row.append(".")
            elif grid[r][c] == "O":
                new_row.append("[")
                new_row.append("]")
        new_grid.append(new_row)
    return new_grid

def get_expanded_grid_after_directions(grid, directions):
    rr, rc = get_robot_position(grid)
    for d in directions:
        dr, dc = DIRECTIONS_MAPPING[d]
        if d in {"<", ">"}:
            nc = rc + dc
            while grid[rr][nc] in {"[", "]"}:
                nc += 2 * dc
            if grid[rr][nc] == ".":
                for c in range(nc, rc, -dc):
                    grid[rr][c] = grid[rr][c-dc]
                rc += dc
                grid[rr][rc] = "@"
                grid[rr][rc-dc] = "."
        elif d in {"^", "v"}:
            queue = deque([(rr + dr, rc)])
            moveable = defaultdict(set)
            while queue:
                r, c = queue.popleft()
                if grid[r][c] == "#":
                    break
                elif grid[r][c] == "]":
                    moveable[r].update([c-1, c])
                    queue.extend([(r+dr, c), (r+dr, c-1)])
                elif grid[r][c] == "[":
                    moveable[r].update([c, c+1])
                    queue.extend([(r+dr, c), (r+dr, c+1)])
                elif grid[r][c] == ".":
                    moveable[r].add(c)
            else:
                for row in sorted(moveable, reverse=(d == "v")):
                    for col in moveable[row]:
                        grid[row][col] = grid[row-dr][col] if col in moveable[row-dr] else "."
                rr += dr
                grid[rr][rc] = "@"
                grid[rr-dr][rc] = "."
    return grid
            
            

def solve1():
    grid, directions = parse()
    grid = get_grid_after_directions(grid, directions)
    return get_gps_coordinate_sum(grid, "O")

def solve2():
    grid, directions = parse()
    grid = get_expanded_grid(grid)
    grid = get_expanded_grid_after_directions(grid, directions)
    return get_gps_coordinate_sum(grid, "[")

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
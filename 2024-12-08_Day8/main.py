from collections import defaultdict
def parse():
    grid = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    
    return grid

from collections import defaultdict

def get_coords(grid):
    coords = defaultdict(set)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != ".":
                coords[grid[r][c]].add((r, c))
    return coords

def is_valid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def solve1():
    grid = parse()
    coords = get_coords(grid)
    unique_antinodes = set()
    for coord_list in coords.values():
        for x1, y1 in coord_list:
            for x2, y2 in coord_list:
                if (x1, y1) == (x2, y2):  # Skip the same antenna
                    continue
                dr = x1 - x2
                dc = y1 - y2
                nr = x1 + dr
                nc = y1 + dc
                if is_valid(nr, nc, grid):
                    unique_antinodes.add((nr, nc))
    
    return len(unique_antinodes)

def solve2():
    grid = parse()
    coords = get_coords(grid)
    unique_antinodes = set()
    for coord_list in coords.values():
        for x1, y1 in coord_list:
            for x2, y2 in coord_list:
                if (x1, y1) == (x2, y2):
                    continue
                dr = x1 - x2
                dc = y1 - y2
                nr = x1
                nc = y1
                while is_valid(nr, nc, grid):
                    unique_antinodes.add((nr, nc))
                    nr += dr
                    nc += dc
    return len(unique_antinodes)
        
print("Part 1:", solve1())
print("Part 2:", solve2())
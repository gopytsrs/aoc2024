def parse():
    f = open("input.txt").read().splitlines()
    return [list(r) for r in f]

grid = parse()
ROWS, COLS = len(grid), len(grid[0])

def next_cells(r, c):
    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            yield nr, nc

def get_cell_perimeter(r, c):
    perimeter = 0
    perimeter += r - 1 < 0 or grid[r-1][c] != grid[r][c]
    perimeter += r + 1 >= ROWS or grid[r+1][c] != grid[r][c]
    perimeter += c - 1 < 0 or grid[r][c-1] != grid[r][c]
    perimeter += c + 1 >= COLS or grid[r][c+1] != grid[r][c]
    return perimeter

from collections import deque

def get_area_and_perimeter(r, c, plant_type, visited):
    queue = deque([(r, c)])
    visited.add((r, c))
    area = 0
    perimeter = 0

    while queue:
        r, c = queue.popleft()
        area += 1
        perimeter += get_cell_perimeter(r, c)  
        for nr, nc in next_cells(r, c):
            if (nr, nc) in visited or grid[nr][nc] != plant_type:
                continue
            queue.append((nr, nc))
            visited.add((nr, nc))
    return area, perimeter

def solve1():
    total_price = 0
    visited = set()
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visited:
                area, perimeter = get_area_and_perimeter(r, c, grid[r][c], visited)
                total_price += area * perimeter

    return total_price

def get_sides(area_cells):
    sides = 0
    for r, c in area_cells:
        sides += ( r - 1, c ) not in area_cells and ( r, c + 1 ) not in area_cells
        sides += ( r - 1, c ) not in area_cells and ( r, c - 1 ) not in area_cells
        sides += ( r + 1, c ) not in area_cells and ( r, c + 1 ) not in area_cells
        sides += ( r + 1, c ) not in area_cells and ( r, c - 1 ) not in area_cells
        sides += ( r - 1, c ) in area_cells and ( r, c - 1 ) in area_cells and ( r - 1, c - 1 ) not in area_cells
        sides += ( r - 1, c ) in area_cells and ( r, c + 1 ) in area_cells and ( r - 1, c + 1 ) not in area_cells
        sides += ( r + 1, c ) in area_cells and ( r, c - 1 ) in area_cells and ( r + 1, c - 1 ) not in area_cells
        sides += ( r + 1, c ) in area_cells and ( r, c + 1 ) in area_cells and ( r + 1, c + 1 ) not in area_cells
    return sides
        
def get_area_and_sides(r, c, plant_type, visited):
    queue = deque([(r, c)])
    visited.add((r, c))
    area = 0
    area_cells = set([(r, c)])
    sides = 0

    while queue:
        r, c = queue.popleft()
        area += 1
        for i, (nr, nc) in enumerate(next_cells(r, c)):
            if (nr, nc) in visited or grid[nr][nc] != plant_type:
                continue
            queue.append((nr, nc))
            visited.add((nr, nc))
            area_cells.add((nr, nc))
            
    return area, get_sides(area_cells)
            

def solve2():
    total_price = 0
    visited = set()

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visited:
                area, sides = get_area_and_sides(r, c, grid[r][c], visited)
                total_price += area * sides

    return total_price


print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
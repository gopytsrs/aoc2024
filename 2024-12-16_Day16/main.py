def parse():
    f = open("input.txt", "r").read().split("\n")
    grid = [list(x) for x in f]
    return grid

grid = parse()
ROWS = len(grid)
COLS = len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # r, c directions

from heapq import heappush, heappop, heapify

def find_start():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "S":
                return r, c

def find_end():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "E":
                return r, c
            
def djikstra(r, c, end_tile, start_cells):
    d = 0
    pq = start_cells
    heapify(pq)
    min_cost = [[[float("inf") for _ in range(4)] for _ in range(COLS)] for _ in range(ROWS)]
    min_cost[r][c][d] = 0
        
    while pq:
        cost, r, c, d = heappop(pq)
        if grid[r][c] == end_tile:
            return min_cost
        

        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != "#":
            if cost + 1 < min_cost[nr][nc][d]:
                min_cost[nr][nc][d] = cost + 1
                heappush(pq, (cost + 1, nr, nc, d))

        nd = (d + 1) % 4
        if cost + 1000 < min_cost[r][c][nd]:
            min_cost[r][c][nd] = cost + 1000
            heappush(pq, (cost + 1000, r, c, nd))
        
        nd = (d - 1) % 4
        if cost + 1000 < min_cost[r][c][nd]:
            min_cost[r][c][nd] = cost + 1000
            heappush(pq, (cost + 1000, r, c, nd))

def solve1():
    sr, sc = find_start()
    er, ec = find_end()
    start_cells = [(0, sr, sc, 0)]
    return min(djikstra(sr, sc, 'E', start_cells)[er][ec])


def solve2():
    sr, sc = find_start()
    er, ec = find_end()
    start_to_end_min_cost = djikstra(sr, sc, 'E', [(0, sr, sc, 0)])
    end_to_start_min_cost = djikstra(er, ec, 'S', [(0, er, ec, d) for d in range(4)])
    result = min(start_to_end_min_cost[er][ec])
    part_of_best_path = set()
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '#':
                continue
            for d1 in range(4):
                for d2 in range(4):
                    if start_to_end_min_cost[r][c][d1] + end_to_start_min_cost[r][c][d2] == result:
                        part_of_best_path.add((r, c))

    return len(part_of_best_path)
    

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

    
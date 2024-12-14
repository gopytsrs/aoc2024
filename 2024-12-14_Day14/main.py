from functools import reduce
from operator import mul
from collections import Counter
import re

def parse():
    robots = []
    pattern = r"-?\d+"
    matches = re.findall(pattern, open("input.txt").read())
    output = [list(map(int, matches[i:i+4])) for i in range(0, len(matches), 4)]
    for c, r, dc, dr in output:
        robots.append((r, c, dr, dc))
    return robots

ROWS = 103
COLS = 101
SECONDS = 100

def get_new_positions(prev_positions, elapsed=SECONDS):
    positions = []
    for r, c, dr, dc in prev_positions:
        nr = (r + dr * elapsed) % ROWS
        nc = (c + dc * elapsed) % COLS
        positions.append((nr, nc, dr, dc))
    return positions

def get_quadrant_counts(positions):
    mid_c = COLS // 2
    mid_r = ROWS // 2
    quadrant_counts = [0, 0, 0, 0]

    for r, c, *_ in positions:
        if r == mid_r or c == mid_c:
            continue
        if r < mid_r and c < mid_c:
            quadrant_counts[0] += 1
        elif r < mid_r and c >= mid_c:
            quadrant_counts[1] += 1
        elif r >= mid_r and c < mid_c:
            quadrant_counts[2] += 1
        elif r >= mid_r and c >= mid_c:
            quadrant_counts[3] += 1

    return quadrant_counts

def part1():
    robots = parse()
    positions = get_new_positions(robots)
    quadrant_counts = get_quadrant_counts(positions)
    return reduce(mul, quadrant_counts)

def part2():
    robots = parse()
    seconds = 0
    while True:
        seconds += 1
        positions = get_new_positions(robots, seconds)
        unique_positions = set((r, c) for r, c, *_ in positions)
        if len(unique_positions) == len(positions):
            break
    return seconds
    
    

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")

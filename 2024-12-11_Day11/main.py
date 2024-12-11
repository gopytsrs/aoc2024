# main.py
def parse():
    f = open("input.txt").read()
    return [int(x) for x in f.split()]

from collections import Counter

def simulate(initial_stones, blinks):
    freq = Counter(initial_stones)

    for _ in range(blinks):
        next_freq = Counter()
        for stone, count in freq.items():
            if stone == 0:
                next_freq[1] += count
            elif len(str(stone)) % 2 == 0:
                string = str(stone)
                mid = len(string) // 2
                left, right = int(string[:mid]), int(string[mid:])
                next_freq[left] += count
                next_freq[right] += count
            else:
                next_freq[stone * 2024] += count
        freq = next_freq

    return sum(freq.values())

def solve1():
    return simulate(parse(), 25)

def solve2():
    return simulate(parse(), 75)

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

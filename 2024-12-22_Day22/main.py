from collections import Counter, deque

def parse():
    return [int(line.strip()) for line in open("input.txt").readlines()]

def get_next_secret(secret):
    next_secret = secret
    next_secret ^= (next_secret * 64) % 16777216
    next_secret ^= (next_secret // 32) % 16777216
    next_secret ^= (next_secret * 2048) % 16777216
    return next_secret

def get_nth_secret(secret, n):
    next_secret = secret
    for _ in range(n):
        next_secret = get_next_secret(next_secret)
    return next_secret

def get_sell_prices(secret, n):
    sell_prices = {}
    prev_secret = secret
    changes = deque(maxlen=4)
    for _ in range(n):
        curr_secret = get_next_secret(prev_secret)
        price_change = curr_secret % 10 - prev_secret % 10
        changes.append(price_change)
        if len(changes) == 4:
            sequence = tuple(changes)
            if sequence not in sell_prices:
                sell_prices[sequence] = curr_secret % 10
        prev_secret = curr_secret
    return sell_prices

def get_max_bananas(secrets):
    sequence_to_total_bananas = Counter()
    for secret in secrets:
        sell_prices = get_sell_prices(secret, 2000)
        for sequence, price in sell_prices.items():
            sequence_to_total_bananas[sequence] += price
    return max(sequence_to_total_bananas.values())

def solve1():
    return sum(get_nth_secret(secret, 2000) for secret in parse())

def solve2():
    return get_max_bananas(parse())

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

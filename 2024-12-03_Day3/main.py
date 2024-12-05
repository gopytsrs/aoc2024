def parse():
    with open ("input.txt") as f:
        return f.read().strip()

import re
def solve1():
    data = parse()
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total

import re

def solve2():
    data = parse()
    token_pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"

    tokens = re.findall(token_pattern, data)

    is_enabled = True
    total = 0
    print(tokens)
    for token in tokens:
        if token == "do()":  # Enable mul
            is_enabled = True
        elif token == "don't()":  # Disable mul
            is_enabled = False
        elif token.startswith("mul("):  # Valid mul instruction
            if is_enabled:
                x, y = map(int, re.findall(r"\d{1,3}", token))
                total += x * y

    return total


print("Part 1:", solve1())
print("Part 2:", solve2())
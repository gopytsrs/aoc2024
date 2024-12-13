import re
def parse():
    pattern = r"\d+"
    content = open("input.txt").read()
    matches = re.findall(pattern, content)
    output = [list(map(int, matches[i:i+6])) for i in range(0, len(matches), 6)]
    return output

def find_min_cost(A_x, A_y, B_x, B_y, P_x, P_y):
    det = A_x * B_y - A_y * B_x
    A_presses = (B_y * P_x - B_x * P_y) // det
    B_presses = (A_x * P_y - A_y * P_x) // det
    result_x = A_presses * A_x + B_presses * B_x
    result_y = A_presses * A_y + B_presses * B_y
    return 3 * A_presses + B_presses if result_x == P_x and result_y == P_y else 0
    

def solve1():
    machines = parse()
    total_cost = 0

    for machine in machines:
        A_x, A_y, B_x, B_y, P_x, P_y = machine
        min_cost = find_min_cost(A_x, A_y, B_x, B_y, P_x, P_y)
        total_cost += min_cost if min_cost else 0

    return total_cost

def solve2():
    machines = parse()
    total_cost = 0

    for machine in machines:
        A_x, A_y, B_x, B_y, P_x, P_y = machine
        P_x += 10**13
        P_y += 10**13
        min_cost = find_min_cost(A_x, A_y, B_x, B_y, P_x, P_y)        
        total_cost += min_cost

    return total_cost


print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

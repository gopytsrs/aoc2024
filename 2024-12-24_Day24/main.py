from itertools import permutations
from collections import deque

def parse():
    values, gates_input = open('input.txt').read().split("\n\n")
    values = values.strip().split("\n")
    gates_input = gates_input.strip().split("\n")
    wires = {}
    gates = []
    for v in values:
        wire, value = v.split(': ')
        wires[wire.strip()] = int(value.strip())
    
    for g in gates_input:
        rest, output = g.split(' -> ')
        output = output.strip()
        x1, op, x2 = rest.strip().split()
        gates.append((op, x1, x2, output))
    
    return wires, gates

def simulate(old_wires, gates):
    wires = old_wires.copy()
    queue = deque(gates)
    while queue:
        for _ in range(len(queue)):
            op, x1, x2, output = queue.popleft()
            if output in wires:
                continue
            if x1 not in wires or x2 not in wires:
                queue.append((op, x1, x2, output))
                continue
            if op == "AND":
                wires[output] = wires[x1] & wires[x2]
            elif op == "OR":
                wires[output] = wires[x1] | wires[x2]
            elif op == "XOR":
                wires[output] = wires[x1] ^ wires[x2]
    return wires

def get_expected_value(wires):
    x_wires = sorted(w for w in wires if w.startswith('x'))
    y_wires = sorted(w for w in wires if w.startswith('y'))
    x_value = 0
    y_value = 0
    for i, (x_wire, y_wire) in enumerate(zip(x_wires, y_wires)):
        x_value += wires[x_wire] * (1 << i)
        y_value += wires[y_wire] * (1 << i)
    return x_value + y_value

def get_actual_value(wires):
    z_wires = sorted(w for w in wires if w.startswith('z'))
    total = 0
    
    for i, wire in enumerate(z_wires):
        total += wires[wire] * (1 << i)
    return total

def solve1():
    wires, gates = parse()
    wires = simulate(wires, gates)
    return get_actual_value(wires)


def solve2():
    original_wires, original_gates = parse()
    expected_value = get_expected_value(original_wires)
    wires = simulate(original_wires, original_gates)
    expected_value = get_expected_value(wires)
    actual_value = get_actual_value(wires)
    wrong_bits = []
    for i in range(46):
        if (expected_value >> i) & 1 != (actual_value >> i) & 1:
            wrong_bits.append(i)
    gate_idxes_to_swap = []
    for i, gate in enumerate(original_gates):
        if gate[3].startswith('z') and int(gate[3][1:]) in wrong_bits:
            gate_idxes_to_swap.append((i, gate))
            
            
    return gate_idxes_to_swap
        
    

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

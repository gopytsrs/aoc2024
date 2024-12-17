def parse():
    r, g = open("input.txt", "r").read().split("\n\n")
    r = r.split("\n")
    A = int(r[0].strip().split(":")[1])
    B = int(r[1].strip().split(":")[1])
    C = int(r[2].strip().split(":")[1])
    program = list(map(int, g.strip().split(":")[1].strip().split(",")))
    return A, B, C, program

def solve1():
    A, B, C, program = parse()
    ip = 0 
    output = []
    def get_combo_operand(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
    
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2 
        if opcode == 0:  # adv
            divisor = 2 ** get_combo_operand(operand)
            A = A // divisor
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = get_combo_operand(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(get_combo_operand(operand) % 8)
        elif opcode == 6:  # bdv
            divisor = 2 ** get_combo_operand(operand)
            B = A // divisor
        elif opcode == 7:  # cdv
            divisor = 2 ** get_combo_operand(operand)
            C = A // divisor
        
    return ",".join(map(str, output))


def solve2():
    _, initial_B, initial_C, program = parse()
    program_output = ",".join(map(str, program))


    for initial_A in range(1, 2**64):
        A = initial_A
        B = initial_B
        C = initial_C
        ip = 0
        output = []
        
        def get_combo_operand(operand):
            if 0 <= operand <= 3:
                return operand
            elif operand == 4:
                return A
            elif operand == 5:
                return B
            elif operand == 6:
                return C

        while ip < len(program):
            opcode = program[ip]
            operand = program[ip + 1]
            ip += 2
            if opcode == 0:  # adv
                divisor = 2 ** get_combo_operand(operand)
                A = A // divisor
            elif opcode == 1:  # bxl
                B = B ^ operand
            elif opcode == 2:  # bst
                B = get_combo_operand(operand) % 8
            elif opcode == 3:  # jnz
                if A != 0:
                    ip = operand
            elif opcode == 4:  # bxc
                B = B ^ C
            elif opcode == 5:  # out
                output.append(get_combo_operand(operand) % 8)
            elif opcode == 6:  # bdv
                divisor = 2 ** get_combo_operand(operand)
                B = A // divisor
            elif opcode == 7:  # cdv
                divisor = 2 ** get_combo_operand(operand)
                C = A // divisor

        curr_output = ",".join(map(str, output))
        
        print("Trying A =", initial_A)
        if curr_output == program_output:
            print("Found A =", initial_A)
            return initial_A
    
print(solve1())
print(solve2())
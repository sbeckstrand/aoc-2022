input = open("input.txt", "r")
register_input = input.read().splitlines()
input.close()

def calc_signal_strength(register_input):
    cycles = 0
    x = 1
    strength = 0
    display = []
    for instruction in register_input:
        inst = instruction.split(" ")
        op = inst[0]
        if op == "noop":
            cycles, strength = increase_cycle(cycles, x, strength, display)
        elif op == "addx":
            for cycle in range (0, 2):
                cycles, strength = increase_cycle(cycles, x, strength, display)
                
            x += int(inst[1])

    for i in range (0, 220, 40):
        print("".join(display[i:i + 40]))
    
    return strength

def increase_cycle(cycle, x, strength, display):
    new_cycle = cycle + 1
    new_strength = strength
    if (new_cycle + 20) % 40 == 0:
        new_strength += new_cycle * x
    
    if (cycle % 40) in [(x - 1), x, (x + 1)]:
        display.append("#")
    else:
        display.append(".")

    return new_cycle, new_strength



print(calc_signal_strength(register_input))
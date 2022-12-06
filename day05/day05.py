input = open("input.txt", "r")
stack_sheet = input.read()
input.close()


def build_stacks(stacks_templates):
    stacks = []
    for line in stacks_templates:
        crates = [line[i:i+4] for i in range(0, len(line), 4)]
        for crate_index in range(0, len(crates)):
            if len(stacks) <= crate_index:
                stacks.append([])
            
            crate = crates[crate_index]

            if crate.startswith("["):
                stacks[crate_index].append(crate.strip())
    
    for stack in stacks:
        stack.reverse()
    
    return stacks

def track_stacks(stack_sheet, model="CrateMover 9000"):
    instructions = stack_sheet.split("\n\n")
    stacks = instructions[0].split("\n")
    stack_queue = build_stacks(stacks)

    changes = instructions[1].split("\n")
    for change in changes:
        cols = change.split(" ")
        to_index, from_index, amount = int(cols[5]) - 1, int(cols[3]) - 1, int(cols[1])
        to_queue = stack_queue[to_index]
        from_queue = stack_queue[from_index]
        if model == "CrateMover 9000":
            to_move = reversed(from_queue[-(amount):])
        elif model == "CrateMover 9001":
            to_move = from_queue[-(amount):]

        stack_queue[to_index].extend(to_move)
        from_queue = from_queue[:len(from_queue) - amount]
        stack_queue[from_index] = from_queue
        
    top = []
    for stack in stack_queue:
        top.append(stack[-1])
    
    return top


print(track_stacks(stack_sheet))
print(track_stacks(stack_sheet, "CrateMover 9001"))
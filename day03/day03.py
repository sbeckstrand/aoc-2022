input = open("input.txt", "r")
rucksacks = input.read().splitlines()
input.close()

def calc_priority(rucksacks, condition=1):
    priority_count = 0
    interval = 1
    if condition == 2:
        interval = 3

    # If condition one, iterate through each rucksack
    # If condition two, iterate through each third rucksack
    for i in range(0, len(rucksacks), interval):
        groups = []
        # If condition one, split each rucksack in half. 
        # If condition two, split rucksacks groups of three.
        if condition == 1:
            rucksack = rucksacks[i]
            groups.append(rucksack[:len(rucksack)//2]) 
            groups.append(rucksack[len(rucksack)//2:])
        elif condition == 2:
            groups = rucksacks[i:i + 3]
        
        # Find common value by converting to sets and finding intersection between each group
        common = list(set(groups[0]).intersection(*groups[0:]))
        
        # Find priority of common character by ascii code
        priority_count += ord(common[0]) - (96 if common[0].islower() else 38)

    return priority_count
    
print(calc_priority(rucksacks))
print(calc_priority(rucksacks, 2))
input = open("input.txt", "r")
rucksacks = input.readlines()
input.close()

def calc_duplicate_priority(rucksacks):
    priority_count = 0
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        comp1 = rucksack[:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]
        common = list(set(comp1).intersection(comp2))
        priority_count += ord(common[0]) - (96 if common[0].islower() else 38)



    return priority_count
        
    
print(calc_duplicate_priority(rucksacks))
f = open("input.txt", "r")
calorie_list = f.readlines()

  
def most_calories(calorie_list, carrier_count):
    cur_cal = 0
    elf_cals = []

    for line in calorie_list:
        if line.strip():
            try:
                cur_cal += int(line)
            except:
                print("Invalid input")
        else:
            elf_cals.append(cur_cal)
            cur_cal = 0
    
    elf_cals.sort(reverse=True)
    return sum(elf_cals[0:carrier_count])


print(most_calories(calorie_list, 1))
print(most_calories(calorie_list, 3))
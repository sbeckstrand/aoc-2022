f = open("input.txt", "r")
guide = f.readlines()

win_con = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

tie_con = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

lose_con = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

point_con = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def follow_guide(guide, input_type):
    score = 0

    for line in guide:
        hands = line.replace("\n", "").split(" ")

        if input_type == "hand":
            
            # For Tie
            if tie_con[hands[0]] == hands[1]:
                score += 3
            
            # For Win
            elif win_con[hands[0]] == hands[1]:
                score += 6
            
            score += point_con[hands[1]]

        elif input_type == "condition":

            # For Tie
            if hands[1] == "Y":
                score += point_con[tie_con[hands[0]]]
                score += 3

            # For Win
            elif hands[1] == "Z":
                score += point_con[win_con[hands[0]]]
                score += 6

            # For Loss
            else:
                score += point_con[lose_con[hands[0]]]
            
            

        
    return score

print(follow_guide(guide, "hand"))
print(follow_guide(guide, "condition"))

        

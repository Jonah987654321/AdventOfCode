file = open("day2_input.txt").read()

score = 0
score_two = 0

win_opts = {"Stein": "Schere", "Schere": "Papier", "Papier": "Stein"}
op = {"A": "Stein", "B": "Papier", "C": "Schere"}
se = {"X": "Stein", "Y": "Papier", "Z": "Schere"}
points = {"Stein": 1, "Schere": 3, "Papier": 2}

for line in file.split("\n"):
    if line != '':
        op_choice = op[line.split(" ")[0]]
        
        #PART 1
        own_choice = se[line.split(" ")[1]]
        score += points[own_choice]
        if own_choice == op_choice:
            score += 3
        else:
            if win_opts[own_choice] == op_choice:
                score += 6

        #PART 2
        if line.split(" ")[1] == "Y":
            own_choice = op_choice
            score_two += 3
            score_two += points[own_choice]
        elif line.split(" ")[1] == "X":
            own_choice = win_opts[op_choice]
            score_two += points[own_choice]
        elif line.split(" ")[1] == "Z":
            for key in win_opts:
                if win_opts[key] == op_choice:
                    own_choice = key
            score_two += 6
            score_two += points[own_choice]

print(score)
print(score_two)

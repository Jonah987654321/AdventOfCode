file = open("day1_input.txt").read()

highest = 0
current = 0

all_cals = []

for line in file.split("\n"):
    if line == '':
        all_cals.append(current)
        if highest < current:
            highest = current
        current = 0
    else:
        current += int(line)

all_cals.sort()

print(sum(all_cals[-3:]))
print(highest)

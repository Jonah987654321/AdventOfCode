import string

file = open("day3_input.txt").read()

priority_sum = 0

alphabet = list(string.ascii_letters)
priorities = {}
i = 1
for l in alphabet:
    priorities[l] = i
    i += 1

group = []
badge_priority_sum = 0

for line in file.split("\n"):
    if line != '':

        #PART 1
        ampp = int(len(line)/2)
        part1 = line[0:ampp]
        part2 = line[ampp:]
        for l in part1:
            if l in part2:
                priority_sum += priorities[l]
                break

        #PART 2
        group.append(line)
        if len(group) == 3:
            for l in group[0]:
                if l in group[1] and l in group[2]:
                    badge_priority_sum += priorities[l]
                    break
            group.clear()

print(priority_sum)
print(badge_priority_sum)

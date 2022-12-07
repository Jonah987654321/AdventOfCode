file = open("day4_input.txt").read()

contained = 0
overlapping = 0

for line in file.split("\n"):
    if line != '':
        elv1 = line.split(",")[0]
        elv2 = line.split(",")[1]
        start1 = int(elv1.split("-")[0])
        end1 = int(elv1.split("-")[1])
        start2 = int(elv2.split("-")[0])
        end2 = int(elv2.split("-")[1])

        #PART 1
        if start1 <= start2 and end2 <= end1 or start2 <= start1 and end1 <= end2:
            contained += 1

        #PART 2
        if start2 <= start1 <= end2 or start1 <= start2 <= end1:
            overlapping += 1

print(contained)
print(overlapping)

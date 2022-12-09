file = open("day9_input.txt").read().splitlines(False)

visited = ["0/9"]

def touching(posH, posT):
    return abs(posH[1]-posT[1])<=1 and abs(posH[0]-posT[0])<=1

posH = [0, 9] #x/y        x→      y↓
posT = [0, 9]

for line in file:
    direction = line.split(" ")[0]
    amount = line.split(" ")[1]
    for x in range(0, int(amount)):
        if direction == "D":
            posH[1] = posH[1]+1
        elif direction == "U":
            posH[1] = posH[1]-1
        elif direction == "L":
            posH[0] = posH[0]-1
        elif direction == "R":
            posH[0] = posH[0]+1
        
        if not touching(posH, posT):
            movX = posH[0]-posT[0]
            if movX > 0:
                posT[0] = posT[0]+1
            elif movX < 0:
                posT[0] = posT[0]-1
            movY = posH[1]-posT[1]
            if movY > 0:
                posT[1] = posT[1]+1
            elif movY < 0:
                posT[1] = posT[1]-1

        if not f"{posT[0]}/{posT[1]}" in visited:
            visited.append(f"{posT[0]}/{posT[1]}") 

print(len(visited))


visited = ["0/9"]
pos = [[0, 9] for _ in range(0, 10)] #x/y        x→      y↓

for line in file:
    direction = line.split(" ")[0]
    amount = line.split(" ")[1]
    for x in range(0, int(amount)):
        if direction == "D":
            pos[0][1] = pos[0][1]+1
        elif direction == "U":
            pos[0][1] = pos[0][1]-1
        elif direction == "L":
            pos[0][0] = pos[0][0]-1
        elif direction == "R":
            pos[0][0] = pos[0][0]+1
        
        for x in range(1, 10):
            if not touching(pos[x-1], pos[x]):
                movX = pos[x-1][0]-pos[x][0]
                if movX > 0:
                    pos[x][0] = pos[x][0]+1
                elif movX < 0:
                    pos[x][0] = pos[x][0]-1
                movY = pos[x-1][1]-pos[x][1]
                if movY > 0:
                    pos[x][1] = pos[x][1]+1
                elif movY < 0:
                    pos[x][1] = pos[x][1]-1

        if not f"{pos[9][0]}/{pos[9][1]}" in visited:
            visited.append(f"{pos[9][0]}/{pos[9][1]}") 

print(len(visited))
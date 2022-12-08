file = open("day8_input.txt").read().splitlines(False)

trees = [list(x) for x in file]

visible = 0

row = 0
column = 0
for k in range(0, len(trees)):
    r = trees[k]
    for t in r:
        if row == 0 or column == 0 or row == len(trees)-1 or column == len(r)-1:
            visible +=1
        else:
            v_dirs = []
            for x in r[:column]:
                if int(x) >= int(t):
                    v_dirs.append(False)
                    break
            for x in r[column+1:]:
                if int(x) >= int(t):
                    v_dirs.append(False)
                    break
            column_trees = [x[column] for x in trees]
            for x in column_trees[:row]:
                if int(x) >= int(t):
                    v_dirs.append(False)
                    break
            for x in column_trees[row+1:]:
                if int(x) >= int(t):
                    v_dirs.append(False)
                    break
            if len(v_dirs) < 4:
                visible += 1
        column += 1
    row += 1
    column = 0

print(visible)

hs = 0

row = 0
column = 0
for k in range(0, len(trees)):
    r = trees[k]
    for t in r:
        num = 0
        for x in reversed(r[:column]):
            if int(x) >= int(t):
                num += 1
                break
            else:
                num += 1
        scenic_score = num
        num = 0
        for x in r[column+1:]:
            if int(x) >= int(t):
                num += 1
                break
            else:
                num += 1
        scenic_score = scenic_score*num
        column_trees = [x[column] for x in trees]
        num = 0
        for x in reversed(column_trees[:row]):
            if int(x) >= int(t):
                num += 1
                break
            else:
                num += 1
        scenic_score = scenic_score*num
        num = 0
        for x in column_trees[row+1:]:
            if int(x) >= int(t):
                num += 1
                break
            else:
                num += 1
        scenic_score = scenic_score*num
        if scenic_score > hs:
            hs = scenic_score
        column += 1
    row += 1
    column = 0

print(hs)

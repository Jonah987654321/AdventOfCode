file = open("day5_input.txt").read()

def sort_dict(dictionary: dict):
    dict_return = {}
    keys = list(dictionary.keys())
    keys.sort()
    for key in keys:
        dict_return[key] = dictionary[key]
    return dict_return

def run_part(part):

    stacks = {}
    first_move = False

    for line in file.split("\n"):
        if line != '':
            if not line.startswith("move"):
                if '[' in line:
                    i = 1
                    while line != '':
                        or_crate = line[0:3]
                        if not or_crate.isspace():
                            crate = or_crate.replace("[", "").replace("]", "")
                            try:
                                stacks[i]
                            except KeyError:
                                stacks[i] = [crate]
                            else:
                                stacks[i].append(crate)
                        line = line[4:]
                        i += 1
            else:
                if not first_move:
                    for d in stacks:
                        stacks[d].reverse()
                    first_move = True
                count = int(line.split(" ")[1])*(-1)
                start_stack = int(line.split(" ")[3])
                end_stack = int(line.split(" ")[5])
                d = stacks[start_stack][count:]
                stacks[start_stack] = stacks[start_stack][:count]
                if part == 1:
                    d.reverse()
                for x in d:
                    stacks[end_stack].append(x)

    stacks = sort_dict(stacks)

    word = ''

    for x in stacks:
        word += stacks[x][-1]

    print(word)

run_part(1)
run_part(2)

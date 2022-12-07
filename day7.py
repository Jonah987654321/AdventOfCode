file = open("day7_input.txt").read().splitlines(False)

def gen_path(working_dir: list):
    path = ""
    for d in working_dir:
        if d == "/":
            path += "/"
        else:
            path += f"{d}/"
    return path

files = {"/": {}}
dir_sizes = {}
working_dir = []
listening = False

for line in file:
    if line.startswith("$"):
        listening = False
        if line.startswith("$ cd "):
            d = line.replace("$ cd ", "")
            if d == "..":
                working_dir = working_dir[:-1]
            else:
                working_dir.append(d)
        elif line.startswith("$ ls"):
            listening = True
    elif listening:
        add_str = "files"
        for x in range(0, len(working_dir)):
            add_str += f"[working_dir[{x}]]"
        if line.split(" ")[0] == "dir":
            add_str += "[line.split(' ')[1]] = {}"
        else:
            add_str += "[line.split(' ')[1]] = line.split(' ')[0]"
            for z in range(1, len(working_dir)+1):
                y = gen_path(working_dir=working_dir[:z])
                try:
                    dir_sizes[y]
                except KeyError:
                    dir_sizes[y] = int(line.split(' ')[0])
                else:
                    dir_sizes[y] = dir_sizes[y]+int(line.split(' ')[0])
        exec(add_str)

total = 0
to_delete = 1000000000000000000000
free_space = 70000000-dir_sizes["/"]
needed_add_space = 30000000-free_space
for x in dir_sizes:
    if dir_sizes[x] <= 100000:
        total += dir_sizes[x]
    if dir_sizes[x] > needed_add_space and dir_sizes[x] < to_delete:
        to_delete = dir_sizes[x]a

print(total)
print(to_delete)

file = open("day10_input.txt").read().splitlines(False)

x = 1
cycle = 0

checks = [20, 60, 100, 140, 180, 220]
checks_sum = 0
line_ends = [40, 80, 120, 160, 200, 240]

ctr_line = ""

for cmd in file:
    needed_cycles = 1
    add = False
    while needed_cycles > 0:
        needed_cycles = needed_cycles-1
        line_pos = cycle%40
        if cycle in line_ends:
            print(ctr_line)
            ctr_line = ""
        if line_pos in [x-1, x, x+1]:
            ctr_line += "⬛"
        else:
            ctr_line += "⬜"
        cycle += 1
        if cycle in checks:
            checks_sum += cycle*x
        if cmd.startswith("noop"):
            pass
        else:
            if cmd.startswith("addx"):
                if not add:
                    needed_cycles += 1
                    add = True
                else:
                    x += int(cmd.lstrip("addx "))

print(ctr_line)

for y in checks:
    if cycle < y:
        checks_sum += y*x

print(checks_sum)

file = open("day6_input.txt").read()

signal = file

def run_part(part: int) -> int:
    result = None
    length = 4 if part==1 else 14
    i = 1
    for l in str(signal):
        if i >= length:
            substr = signal[i-length:i]
            if len(set(substr)) == length:
                result = i
                break
        i += 1

    print(result)

run_part(1)
run_part(2)

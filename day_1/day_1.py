import os


def find_digit(line: str, lr: bool):
    if lr:
        for i in range(0, len(line)):
            if line[i].isdecimal():
                return line[i]
    else:
        for i in range(len(line)-1, -1, -1):
            if line[i].isdecimal():
                return line[i]
    print(line)
    raise Exception("No number in this line")

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
    config_lines = file.readlines()

total = 0

for line in config_lines:
    first = find_digit(line, True)
    last = find_digit(line, False)
    combined = int(first + last)
    total+=combined

print(total)


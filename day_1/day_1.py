import os
from re import search


def find_digit(line: str, lr: bool):
    pattern = r"(one|two|three|four|five|six|seven|eight|nine)"
    mapping = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    if lr:
        for i in range(0, len(line)):
            if line[i].isdecimal():
                return line[i]
            else:
                result = search(pattern, line[:i+1])
                if result:
                    return mapping[result.group(0)]
                
    else:
        for i in range(len(line)-1, -1, -1):
            if line[i].isdecimal():
                return line[i]
            else:
                result = search(pattern, line[i:])
                if result:
                    return mapping[result.group(0)]

    raise Exception("No number in this line")


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
    config_lines = file.readlines()

total = 0

for cfgline in config_lines:
    first = find_digit(cfgline, True)
    last = find_digit(cfgline, False)
    combined = int(first + last)
    total += combined
    #print(first, last, cfgline, combined)


print(total)


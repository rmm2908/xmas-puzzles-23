import os
from re import search


def find_digit(line: str, lr: bool):
    pattern = r"(one|two|three|four|five|six|seven|eight|nine|[1-9])"

    if lr:
        for i in range(0, len(line)):
            result = search(pattern, line[:i+1])
            if result:
                return result.group(0)
                
    else:
        for i in range(len(line)-1, -1, -1):
            result = search(pattern, line[i:])
            if result:
                return result.group(0)

    raise Exception("No number in this line")


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        config_lines = file.readlines()

    total = 0

    mapping = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for cfgline in config_lines:
        first = find_digit(cfgline, True)
        if not first.isdecimal():
            first = mapping[first]
        last = find_digit(cfgline, False)
        if not last.isdecimal():
            last = mapping[last]
        combined = int(first + last)
        total += combined

    print(total)


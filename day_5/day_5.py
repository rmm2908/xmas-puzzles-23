import os


class NumberRange:
    def __init__(self, src_start, dst_start, range_len):
        self.src_start = src_start
        self.dst_start = dst_start
        self.last_num = src_start+range_len-1

    def transform(self, number):
        distance = number - self.src_start
        return distance + self.dst_start

    def __contains__(self, item):
        return self.src_start <= item <= self.last_num


class NumberMapper:
    def __init__(self):
        self.__ranges = []

    def add_range(self, src_start, dst_start, range_len):
        num_range = NumberRange(src_start, dst_start, range_len)
        self.__ranges.append(num_range)

    def transform(self, number):
        for num_range in self.__ranges:
            if number in num_range:
                return num_range.transform(number)
        return number


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        lines = file.readlines()
    numbers = lines[0].split(" ")
    numbers.pop(0)
    numbers = [int(number) for number in numbers]
    lines.pop(0)
    lines = list(filter(lambda line: line != "\n", lines))
    print(lines)


if __name__ == "__main__":
    main()

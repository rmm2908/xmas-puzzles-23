import os


class NumberRange:
    def __init__(self, src_start, dst_start, range_len):
        self.src_start = src_start
        self.dst_start = dst_start
        self.range_len = range_len
        self.last_num = src_start+range_len-1

    def transform(self, number):
        distance = number - self.src_start
        return self.dst_start + distance

    def __contains__(self, item):
        return self.src_start <= item <= self.last_num

    def __str__(self):
        return f"({self.src_start}, {self.dst_start}, {self.range_len})"


class NumberMapper:
    def __init__(self):
        self.__ranges = []

    def add_range(self, ranges):
        num_range = NumberRange(int(ranges[1]), int(ranges[0]), int(ranges[2]))
        self.__ranges.append(num_range)

    def transform(self, number):
        for num_range in self.__ranges:
            if number in num_range:
                return num_range.transform(number)
        return number


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), encoding="UTF-8") as file:
        lines = file.readlines()
    seeds = [int(seed) for seed in filter(lambda item: item.isdigit(), lines[0].strip("\n").split(" "))]
    lines.pop(0)
    transformers = []
    mapper = NumberMapper()
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            transformers.append(mapper)
            i += 2
            mapper = NumberMapper()
        else:
            mapper.add_range(lines[i].strip("\n").split(" "))
            i+=1
    transformers.append(mapper)
    transformers.pop(0)
    for i in range(len(seeds)):
        for transformer in transformers:
            seeds[i] = transformer.transform(seeds[i])
    print(min(*seeds))


if __name__ == "__main__":
    main()

import os


class Gear:
    gears = []

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.nums = []

    def add_num(self, num):
        self.nums.append(num)
        for gear in Gear.gears:
            if gear == self:
                gear.nums += self.nums
                return
        Gear.gears.append(self)

    def __eq__(self, other):
        if not isinstance(other, Gear):
            return False
        return self.x == other.x and self.y == other.y


class Number:

    def __init__(self, matrix, x, y, last):
        if x >= len(matrix) or x < 0:
            raise IndexError("'X' coordinate is out of bounds")
        if y >= (line_ln := len(matrix[x])) or y < 0:
            raise IndexError("'Y' coordinate is out of bounds")
        if last >= line_ln:
            raise IndexError("'Last' coordinate is out of bounds")
        self.matrix = matrix
        self.x, self.y = x, y
        self.last = last
        self.__gear = None
        self.__value = 0

    @property
    def value(self):
        if self.__value == 0:
            self.__value = int(''.join(self.matrix[self.x][self.y:self.last+1]))
        return self.__value

    def __left(self):
        if (char := self.matrix[self.x][self.y-1]) != '.' and not char.isdecimal():
            if char == '*':
                self.__gear = Gear(self.x, self.y - 1)
            return True
        if (char := self.matrix[self.x-1][self.y-1]) != '.' and not char.isdecimal():
            if char == '*':
                self.__gear = Gear(self.x - 1, self.y - 1)
            return True
        if (char := self.matrix[self.x+1][self.y-1]) != '.' and not char.isdecimal():
            if char == '*':
                self.__gear = Gear(self.x + 1, self.y - 1)
            return True
        return False

    def __right(self):
        if (char := self.matrix[self.x][self.last+1]) != '.' and not char.isdecimal():
            if char == '*':
                self.__gear = Gear(self.x, self.last + 1)
            return True
        if (char := self.matrix[self.x-1][self.last+1]) != '.' and not char.isdecimal():
            if char == '*':
                self.__gear = Gear(self.x - 1, self.last + 1)
            return True
        if (char := self.matrix[self.x+1][self.last+1]) != '.' and not char.isdecimal():
            if char == '*':
                self.__gear = Gear(self.x + 1, self.last + 1)
            return True
        return False

    def __up(self):
        for k in range(self.y, self.last+1):
            if (char := self.matrix[self.x-1][k]) != '.' and not char.isdecimal():
                if char == '*':
                    self.__gear = Gear(self.x - 1, k)
                return True
        return False

    def __down(self):
        for k in range(self.y, self.last+1):
            if (char := self.matrix[self.x+1][k]) != '.' and not char.isdecimal():
                if char == '*':
                    self.__gear = Gear(self.x + 1, k)
                return True
        return False

    def is_valid(self):
        if self.__left():
            return True
        if self.__right():
            return True
        if self.__up():
            return True
        if self.__down():
            return True
        return False

    @property
    def gear(self):
        if self.__gear is not None:
            return self.__gear
        self.is_valid()
        return self.__gear

    def __eq__(self, other):
        if not isinstance(other, Number):
            return False
        return self.matrix == other.matrix and self.x == other.x and \
            self.y == other.y and self.__gear == other.gear

    def __str__(self):
        return f"({self.value}, {self.x}, {self.y})"


def find_valid_nums(matrix):
    total = 0
    for i, line in enumerate(matrix):
        line_len = len(line)
        num_start = 0
        for j in range(line_len - 1):
            if line[j].isdecimal() and j != 0 and not line[j - 1].isdecimal():
                num_start = j
            if line[j].isdecimal() and not line[j + 1].isdecimal():
                number = Number(matrix, i, num_start, j)
                if number.is_valid():
                    total += number.value
    return total


def find_gear_ratio(matrix):
    gear_ratio = 0
    for i, line in enumerate(matrix):
        line_len = len(line)
        num_start = 0
        for j in range(line_len - 1):
            if line[j].isdecimal() and j != 0 and not line[j - 1].isdecimal():
                num_start = j
            if line[j].isdecimal() and not line[j + 1].isdecimal():
                number = Number(matrix, i, num_start, j)
                if number.gear:
                    number.gear.add_num(number)
    for gear in Gear.gears:
        if len(gear.nums) > 1:
            gear_ratio += gear.nums[0].value*gear.nums[1].value
    return gear_ratio


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), encoding="UTF-8") as file:
        MATRIX = [['.']+list(line.replace("\n", '.')) for line in file.readlines()]

    head_tail = ['.' for _ in range(len(MATRIX[0]))]
    MATRIX.insert(0, head_tail)
    MATRIX.append(head_tail)

    TOTAL_NUMS = find_valid_nums(MATRIX)
    print('valid: ', TOTAL_NUMS)

    GEAR_RATIO = find_gear_ratio(MATRIX)
    print('gear ratio: ', GEAR_RATIO)

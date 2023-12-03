import os


class Number:

    def __init__(self, matrix, x, y, last):
        if x >= len(matrix) or x < 0:
            raise IndexError("'X' coordinate is out of bounds")
        if y >= (line_ln := len(matrix[x])) or y < 0:
            raise IndexError("'Y' coordinate is out of bounds")
        if last >= line_ln:
            raise IndexError("'Last' coordinate is out of bounds")
        self.matrix = matrix
        self.x = x
        self.y = y
        self.last = last

    @property
    def value(self):
        return int(''.join(self.matrix[self.x][self.y:self.last+1]))

    def __left(self):
        if (char := self.matrix[self.x][self.y-1]) != '.' and not char.isdecimal():
            return True
        if (char := self.matrix[self.x-1][self.y-1]) != '.' and not char.isdecimal():
            return True
        if (char := self.matrix[self.x+1][self.y-1]) != '.' and not char.isdecimal():
            return True
        return False

    def __right(self):
        if (char := self.matrix[self.x][self.last+1]) != '.' and not char.isdecimal():
            return True
        if (char := self.matrix[self.x-1][self.last+1]) != '.' and not char.isdecimal():
            return True
        if (char := self.matrix[self.x+1][self.last+1]) != '.' and not char.isdecimal():
            return True
        return False

    def __up(self):
        for k in range(self.y, self.last+1):
            if (char := self.matrix[self.x-1][k]) != '.' and not char.isdecimal():
                return True
        return False

    def __down(self):
        for k in range(self.y, self.last+1):
            if (char := self.matrix[self.x+1][k]) != '.' and not char.isdecimal():
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


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), encoding="UTF-8") as file:
        MATRIX = [['.']+list(line.replace("\n", '.')) for line in file.readlines()]

    head_tail = ['.' for _ in range(len(MATRIX[0]))]
    MATRIX.insert(0, head_tail)
    MATRIX.append(head_tail)

    TOTAL = 0
    for i, line in enumerate(MATRIX):
        j = 0
        line_len = len(line)
        NUM_START = 0
        for j in range(line_len-1):
            if line[j].isdecimal() and j != 0 and not line[j-1].isdecimal():
                NUM_START = j
            if line[j].isdecimal() and not line[j+1].isdecimal():
                number = Number(MATRIX, i, NUM_START, j)
                if number.is_valid():
                    TOTAL += number.value

    print(TOTAL)

import os


class Card:
    def __init__(self, number, winners, scratchers):
        self.number = number
        self.winners = list(winners)
        self.scratchers = list(scratchers)

    def find_line_score(self):
        points = 1
        result = 0
        for num in self.scratchers:
            if num in self.winners:
                result = points
                points *= 2
        return result


def find_score(scratch_lines):
    total = 0
    for line in scratch_lines:
        scratch_line = line.split(":")
        game_no = int(scratch_line[0].split(" ")[-1])
        nums = scratch_line[1].split("|")
        winning = [int(num) for num in nums[0].split(" ") if len(num) > 0]
        actual = [int(num) for num in nums[1].split(" ") if len(num) > 0]
        card = Card(game_no, winning, actual)
        total += card.find_line_score()
    return total


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt"), encoding="UTF-8") as file:
        cards = file.readlines()
    SCORE = find_score(cards)
    print(SCORE)

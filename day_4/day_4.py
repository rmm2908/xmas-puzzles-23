import os


class Card:
    def __init__(self, winners: [int], scratchers: [int]):
        self.winners = list(winners)
        self.scratchers = list(scratchers)
        self.__matches = None

    def find_line_score(self):
        points = 1
        result = 0
        for num in self.scratchers:
            if num in self.winners:
                result = points
                points *= 2
        return result

    @property
    def matches(self):
        if not self.__matches:
            self.__matches = 0
            for num in self.scratchers:
                if num in self.winners:
                    self.__matches += 1
        return self.__matches

    @classmethod
    def create_card(cls, line):
        scratch_line = line.split(":")
        nums = scratch_line[1].split("|")
        winning = [int(num) for num in nums[0].split(" ") if len(num) > 0]
        actual = [int(num) for num in nums[1].split(" ") if len(num) > 0]
        card = cls(winning, actual)
        return card


def find_score(scratch_lines):
    total = 0
    for card_line in scratch_lines:
        card = Card.create_card(card_line)
        total += card.find_line_score()
    return total


def find_copies(scratch_lines):
    cards = [Card([],[])]
    amounts = [0]
    for line in scratch_lines:
        cards.append(Card.create_card(line))
        amounts.append(1)
    for i in range(1, len(cards)):
        for j in range(i+1, i+cards[i].matches+1):
            amounts[j] += amounts[i]
    return sum(amounts)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), encoding="UTF-8") as file:
        scratch_cards = file.readlines()
    SCORE = find_score(scratch_cards)
    print(SCORE)
    AMOUNT = find_copies(scratch_cards)
    print(AMOUNT)

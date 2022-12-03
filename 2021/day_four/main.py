class Bingo:
    def __init__(self, puzzle_input="puzzle_input.txt"):
        self.bingo_nums = []
        self.bingo_cards = []
        self.load_data(puzzle_input)

    def load_data(self, puzzle_input):
        with open(puzzle_input, "r") as text_file:
            data = text_file.readlines()
            self.bingo_nums = data.pop(0).split(",")
            self.get_bingo_cards(data)

    def get_bingo_cards(self, data):
        temp_bingo_card = self.create_empty_bingo_card()
        index = 0
        for line in data:
            line = line.strip()
            if not line:
                # skip empty lines
                continue
            temp_bingo_card[index % 5] = self.get_row_from_line(line)
            index = index + 1
            if (index % 5) == 0:
                self.bingo_cards.append(temp_bingo_card)
                temp_bingo_card = self.create_empty_bingo_card()

    @staticmethod
    def create_empty_bingo_card():
        return [[0 for i in range(5)] for j in range(5)]

    @staticmethod
    def get_row_from_line(line):
        temp_row = []
        for num in line.split(" "):
            num = num.strip()
            if not num:
                continue
            temp_row.append(num)
        return temp_row

def test():
    squid_bingo = Bingo("test_input.txt")
    assert len(squid_bingo.bingo_nums) == 27
    empty_bingo_card = squid_bingo.create_empty_bingo_card()
    assert len(empty_bingo_card) == 5
    assert len(empty_bingo_card[0]) == 5
    test_bingo_card = []
    test_bingo_card.append(["22", "13", "17", "11", "0"])
    test_bingo_card.append(["8", "2", "23", "4", "24"])
    test_bingo_card.append(["21", "9", "14", "16", "7"])
    test_bingo_card.append(["6", "10", "3", "18", "5"])
    test_bingo_card.append(["1", "12", "20", "15", "19"])
    print(f"test_bingo_card[0] = {test_bingo_card[0]}")
    print(f"squid_bingo[0] = {squid_bingo.bingo_cards[0][0]}")
    assert test_bingo_card[0] == squid_bingo.bingo_cards[0][0]
    assert test_bingo_card[1] == squid_bingo.bingo_cards[0][1]
    assert test_bingo_card[2] == squid_bingo.bingo_cards[0][2]
    assert test_bingo_card[3] == squid_bingo.bingo_cards[0][3]
    assert test_bingo_card[4] == squid_bingo.bingo_cards[0][4]

def main():
    test()

if __name__ == "__main__":
    main()

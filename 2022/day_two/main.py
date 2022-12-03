from dataclasses import dataclass

@dataclass
class Round:
    opp_choice: str
    my_choice: str
    loss = [10,20,33]
    win = [12,17,34]
    draw = [9, 18, 36]

    def get_outcome(self):
        opp_nums = {
            "A":1,
            "B":2,
            "C":4,
        }
        my_nums = {
            "X":8,
            "Y":16,
            "Z":32,
        }
        outcome = my_nums[self.my_choice] | opp_nums[self.opp_choice]
        if outcome in self.win:
            return 6
        if outcome in self.draw:
            return 3
        return 0

    def get_score(self):
        choice = {
            "X":1,
            "Y":2,
            "Z":3,
        }
        outcome = self.get_outcome()
        return int(outcome + choice[self.my_choice])

def main(file_name: str="puzzle_input.txt") -> None:
    puzzle_input = get_puzzle_input(file_name)
    rounds = create_rounds(puzzle_input)
    total_score = 0
    for tmp_round in rounds:
        score = tmp_round.get_score()
        total_score += score
    print(f"total = {total_score}")

def get_puzzle_input(file_name: str) -> list:
    with open(file_name, "r") as puzzle_input:
        return puzzle_input.readlines()

def create_rounds(puzzle_input: list) -> list:
    rounds = []
    for line in puzzle_input:
        opp_choice, your_choice = line.strip().split(" ")
        rounds.append(Round(opp_choice, your_choice))
    return rounds

if __name__ == "__main__":
    main("test_input.txt")
    main("puzzle_input.txt")

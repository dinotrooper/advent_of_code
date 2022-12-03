from dataclasses import dataclass

@dataclass
class Round:
    opp_choice: str
    desired_outcome: str
    #           R    P    S
    choices = ["A", "B", "C"]

    def get_winning_choice(self):
        opp_i = self.choices.index(self.opp_choice)
        return (opp_i + 1) % 3

    def get_losing_choice(self):
        opp_i = self.choices.index(self.opp_choice)
        losing_choice = opp_i - 1
        if losing_choice < 0:
            return losing_choice + 3
        return losing_choice

    def get_score(self):
        if self.desired_outcome == "Y":
            return self.choices.index(self.opp_choice) + 1 + 3
        if self.desired_outcome == "X":
            return self.get_losing_choice() + 1
        return self.get_winning_choice() + 1 + 6

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

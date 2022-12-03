from dataclasses import dataclass

@dataclass
class Elf:
    total: int

def main(file_name: str="puzzle_input.txt") -> None:
    puzzle_input = get_puzzle_input(file_name)
    elves = create_elves(puzzle_input)
    elves.sort(key=lambda elf : elf.total, reverse=True)
    print(elves[0])
    top_three = sum([x.total for x in elves[0:3]])
    print(top_three)

def get_puzzle_input(file_name: str) -> list:
    with open(file_name, "r") as puzzle_input:
        return puzzle_input.readlines()

def create_elves(puzzle_input: list) -> list:
    elves = []
    delimiter = "\n"
    temp_total = 0
    for i, line in enumerate(puzzle_input):
        if line == delimiter:
            new_elf = create_new_elf(temp_total)
            elves.append(new_elf)
            temp_total = 0
            continue
        temp_total = temp_total + int(line.strip())
        if i == (len(puzzle_input) - 1):
            new_elf = create_new_elf(temp_total)
            elves.append(new_elf)
    return elves

def create_new_elf(temp_total) -> Elf:
    return Elf(temp_total)

def get_elf_with_most_calories(elves) -> int:
    highest = 0
    for i, elf in enumerate(elves):
        if elf.total > highest:
            highest = elf.total
            elves.pop(i)
    return highest

if __name__ == "__main__":
    main("test_input.txt")
    main("puzzle_input.txt")

def get_puzzle_input(puzzle_input):
    with open(puzzle_input, "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(line.strip())
        return lines

def get_sets(line):
    first, second = line.split(",")
    first_one, first_two = [int(x) for x in first.split("-")]
    second_one, second_two = [int(x) for x in second.split("-")]
    first_range = list(range(first_one, first_two+1))
    second_range = list(range(second_one, second_two+1))
    return first_range, second_range

def fully_overlap(first, second):
    if len(first) > len(second):
        for two in second:
            if two not in first:
                return False
    else:
        for one in first:
            if one not in second:
                return False
    return True

def one_overlap(first, second):
    for one in first:
        if one in second:
            return True
    return False


def main(puzzle_input):
    lines = get_puzzle_input(puzzle_input)
    total = 0
    for x in lines:
        first_range, second_range = get_sets(x)
        if one_overlap(first_range, second_range):
            total = total + 1
    print(total)

if __name__ == "__main__":
    main("test_input.txt")
    main("puzzle_input.txt")

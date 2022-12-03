def sum_prio(file_name: str="puzzle_input.txt") -> int:
    puzzle_input = get_puzzle_input(file_name)
    sacks = get_sacks(puzzle_input)
    groups = group_up_sacks(sacks)
    total = 0
    for group in groups:
        item = get_common_item_in_three_sacks(group)
        total = total + get_prio_of_item(item)
    return total

def get_puzzle_input(file_name: str) -> list:
    with open(file_name, "r") as puzzle_input:
        return puzzle_input.readlines()

def get_sacks(puzzle_input) -> list:
    sacks = []
    for line in puzzle_input:
        line = line.strip()
        sacks.append(line)
    return sacks

def get_compartments_of_sack(sack):
    divider = int(len(sack) / 2)
    sack_one = sack[0:divider]
    sack_two = sack[divider:]
    return (sack_one, sack_two)

def group_up_sacks(sacks, group_size=3):
    all_groups = []
    divider = int(len(sacks) / group_size)
    for i in range(divider):
        j = i * group_size
        group = []
        for x in range(group_size):
            sub = sacks[j+x]
            group.append(sub)
        all_groups.append(group)
    return all_groups

def get_common_item_in_compartments(sack) -> str:
    first, second = sack
    for f_letter in first:
        for s_letter in second:
            if f_letter == s_letter:
                return f_letter
    return "0"

def get_common_item_in_three_sacks(sacks) -> str:
    first, second, third = sacks
    for f_letter in first:
        for s_letter in second:
            if f_letter != s_letter:
                continue
            for t_letter in third:
                if f_letter == t_letter:
                    return f_letter
    return "0"

def get_prio_of_item(item) -> int:
    ascii_item = ord(item)
    if ascii_item >= 97:
        return ascii_item - 96
    return ascii_item - 38

if __name__ == "__main__":
    print(sum_prio("puzzle_input.txt"))

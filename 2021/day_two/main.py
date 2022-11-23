def get_int_from_line(line):
    line = line.strip()
    return int(line.split(" ")[-1])

def main():
    values = []
    with open("puzzle_input.txt", "r") as puzzle_input:
        for line in puzzle_input.readlines():
            values.append(line)

    depth = 0
    aim = 0
    horizontal = 0
    for value in values:
        if "forward" in value:
            num = get_int_from_line(value)
            depth = depth + (aim * num)
            horizontal = horizontal + num
        if "up" in value:
            aim =  aim - get_int_from_line(value)
        if "down" in value:
            aim = aim + get_int_from_line(value)

    print(depth * horizontal)

if __name__ == "__main__":
    main()

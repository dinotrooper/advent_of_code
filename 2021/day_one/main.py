def main():
    values = []
    with open("puzzle_input.txt", "r") as puzzle_input:
        for line in puzzle_input.readlines():
            values.append(int(line))

    count = 0
    for i, value in enumerate(values):
        if i < 3:
            continue
        prev_total = values[i - 1] + values[i - 2] + values[i - 3]
        current_total = value + values[i - 2] + values[i - 1]
        if current_total > prev_total:
            count = count + 1
    print(count)

if __name__ == "__main__":
    main()

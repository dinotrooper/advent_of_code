def main():
    old_text = open("puzzle_input.txt", "r")
    input = []
    for line in old_text.readlines():
        line = line.strip()
        if line:
            input.append(line)
    new_text = open("puzzle_input.txt", "w")
    for line in input:
        new_text.write(line + "\n")

if __name__ == "__main__":
    main()

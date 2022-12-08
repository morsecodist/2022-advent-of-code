with open("2022-12-06/part_one_input.txt") as f:
    for line in f:
        chars = list(line)
        for i, c in enumerate(chars):
            if i < 4:
                continue
            if len(set(chars[i-4:i])) == 4:
                print(i + 1)
                break
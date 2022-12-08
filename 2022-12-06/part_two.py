with open("2022-12-06/part_one_input.txt") as f:
    for line in f:
        chars = list(line)
        for i, c in enumerate(chars):
            if i < 14:
                continue
            if len(set(chars[i-14:i])) == 14:
                print(chars[i-14:i])
                print(i)
                break
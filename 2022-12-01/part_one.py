def sums():
    with open('2022-12-01/input_part_one.txt') as f:
        total = 0
        for line in f:
            stripped = line.strip()
            if not stripped:
                yield total
                total = 0
                continue
            total += int(stripped)
        yield total

print(max(sums()))
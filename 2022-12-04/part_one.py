total = 0
with open("2022-12-04/input_part_one.txt") as f:
    for raw_line in f:
        line = raw_line.strip()
        ranges = line.split(",")
        ranges = [[int(n) for n in r.split("-")] for r in ranges]
        ranges = sorted(ranges, key=lambda x: tuple([x[0], -x[1]]))
        print(ranges, ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1])
        if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
            total += 1

print(total)
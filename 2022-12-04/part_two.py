total = 0
with open("2022-12-04/input_part_two.txt") as f:
    for raw_line in f:
        line = raw_line.strip()
        ranges = line.split(",")
        ranges = [int(n) for r in ranges for n in r.split("-")]
        for i in range(min(ranges), max(ranges) + 1):
            if ranges[0] <= i <= ranges[1] and ranges[2] <= i <= ranges[3]:
                total += 1
                break

print(total)
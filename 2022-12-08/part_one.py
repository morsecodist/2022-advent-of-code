with open("2022-12-08/part_one_input.txt") as f:
    heights = [[int(n) for n in line.strip()] for line in f ]

visible = set()

for reverse in [True, False]:
    for i, row in enumerate(heights):
        max_height = -1
        j_iter = range(len(row))
        for j in reversed(j_iter) if reverse else j_iter:
            height = heights[i][j]
            if height > max_height:
                visible.add((i, j))
                max_height = height

    for j in range(len(heights[0])):
        max_height = -1
        i_iter = range(len(heights))
        for i in reversed(i_iter) if reverse else i_iter:
            height = heights[i][j]
            if height > max_height:
                visible.add((i, j))
                max_height = height

print(len(visible))

for i, row in enumerate(heights):
    print([f" {n} " if (i, j) in visible else f"[{n}]" for j, n in enumerate(row)])
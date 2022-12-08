with open("2022-12-08/part_two_input.txt") as f:
    heights = [[int(n) for n in line.strip()] for line in f ]

def arr_score(height, arr):
    idx = next((i for i, e in enumerate(arr) if e >= height), -1)
    return idx + 1 if idx >= 0 else len(arr)

def scenic_score(start, heights):
    i_start, j_start = start
    height = heights[i_start][j_start]

    row = heights[i_start]
    right_score = arr_score(height, row[j_start+1:])
    left_score = arr_score(height, list(reversed(row[:j_start])))

    column = [heights[i][j_start] for i in range(len(heights))]
    up_score = arr_score(height, column[i_start+1:])
    down_score = arr_score(height, list(reversed(column[:i_start])))

    return right_score * left_score * up_score * down_score

print(max(scenic_score((i, j), heights) for i, row in enumerate(heights) for j, _ in enumerate(row)))

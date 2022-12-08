scores = {
    'A X\n': 3 + 1,
    'A Y\n': 6 + 2,
    'A Z\n': 0 + 3,
    'B X\n': 0 + 1,
    'B Y\n': 3 + 2,
    'B Z\n': 6 + 3,
    'C X\n': 6 + 1,
    'C Y\n': 0 + 2,
    'C Z\n': 3 + 3,
}


def score_iter():
    with open('2022-12-02/input_part_one.txt') as f:
        for line in f:
            yield scores[line]

print(sum(score_iter()))
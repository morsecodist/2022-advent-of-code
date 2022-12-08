scores = {
    'A X\n': 0 + 3,
    'A Y\n': 3 + 1,
    'A Z\n': 6 + 2,
    'B X\n': 0 + 1,
    'B Y\n': 3 + 2,
    'B Z\n': 6 + 3,
    'C X\n': 0 + 2,
    'C Y\n': 3 + 3,
    'C Z\n': 6 + 1,
}


def score_iter():
    with open('2022-12-02/input_part_two.txt') as f:
        for line in f:
            yield scores[line]

print(sum(score_iter()))
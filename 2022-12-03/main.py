def _priority(char: str):
    n = ord(char)
    if n >= 97:
        return n - 96
    return n - 38


def priorities_part_one():
    with open('2022-12-03/input.txt') as f:
        for line in f:
            char_list = list(set(line[:len(line)//2]) & set(line[len(line)//2:]))
            assert len(char_list) == 1, char_list
            yield _priority(char_list[0])


def priorities_part_two():
    with open('2022-12-03/input_part_two.txt') as f:
        s = set()
        for i, line in enumerate(f):
            if not s:
                s = set(line.strip()) 
            else:
                s &= set(line.strip())

            if i % 3 == 2:
                char_list = list(s)
                assert len(char_list) == 1, char_list
                yield _priority(char_list[0])
                s = set()

print(sum(priorities_part_two()))

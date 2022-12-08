import re

n = 0
stacks = []
mode = 'build'

with open("2022-12-05/input_one.txt") as f:
    for line in f:
        if re.match(f"\s*\[", line):
            if n == 0:
                n = len(line) // 4
                stacks = [[] for _ in range(n)]
            for i, stack in enumerate(stacks):
                start = 4 * i + 1
                crate = line[start:start + 1]
                if crate != ' ':
                    stack.append(crate)
            continue

        if line.startswith("move"):
            m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            nn = int(m.group(1))
            src = int(m.group(2)) - 1
            dst = int(m.group(3)) - 1
            assert len(stacks[src]) >= nn
            for _ in range(nn):
                stacks[dst] = stacks[src][:1] + stacks[dst]
                stacks[src] = stacks[src][1:]

print("".join(stack[0] for stack in stacks))
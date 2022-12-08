from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class File:
    name: str
    size: int

    def compute_size(self):
        return self.size

@dataclass
class Directory:
    name: str
    size: int
    parent: any
    children: Dict[str, any]

    def compute_size(self):
        size = sum(node.compute_size() for node in self.children.values())
        self.size = size
        return size

root = Directory("/", 0, None, {})
directories = [root]
current = root

with open("2022-12-07/part_one_input.txt") as f:
    for line in f:
        if line == "$ cd ..\n":
            current = current.parent
        elif line == "$ cd /\n":
            current = root
        elif line.startswith("$ cd"):
            name = line.strip().split()[-1]
            current = current.children[name]
        elif line.startswith("dir"):
            name = line.strip().split()[-1]
            current.children[name] = Directory(name, 0, current, {})
            directories.append(current.children[name])
        elif line[0].isdigit():
            size, name = line.strip().split()
            current.children[name] = File(name, int(size))

root.compute_size()
print(sum(d.size for d in directories if d.size <= 100000))

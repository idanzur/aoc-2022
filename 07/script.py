#!/usr/bin/python3
import sys
from dataclasses import dataclass, field
from enum import Enum, auto

file = './sample.txt' if 0 else './input.txt'


class TYPES(Enum):
    DIR = auto()
    FILE = auto()


class MODES(Enum):
    CMD = auto()
    OUTPUT = auto()


@dataclass
class FS:
    name: str
    type: TYPES
    children: list['FS'] = field(default_factory=list)
    parent: 'FS' = None
    size: int = None

    def append(self, name: str, _type: TYPES, size: int = None):
        self.children.append(FS(name=name, type=_type, size=size, parent=self))

    def calc_sizes(self):
        if self.size is not None:
            return self.size
        size = 0
        for child in self.children:
            if child.type == TYPES.FILE:
                size += child.size
            else:
                size += child.calc_sizes()
        self.size = size
        return self.size

    def __str__(self):
        if self.type == TYPES.FILE:
            return f'{self.name} (file, size={self.size})'
        return f'{self.name} (dir, size={self.size})'


def print_fs(fs: FS, depth=0):
    print(f'{"  " * depth}{fs}')
    for child in fs.children:
        print_fs(child, depth + 1)


def find_dirs(fs: FS) -> int:
    res = 0
    for d in fs.children:
        if d.type == TYPES.FILE:
            continue
        if d.size < 100000:
            res += d.size
        res += find_dirs(d)
    return res


def find_dirs2(fs: FS, size) -> list[int]:
    res = []
    for d in fs.children:
        if d.type == TYPES.FILE:
            continue
        if d.size >= size:
            res.append(d.size)
        res.extend(find_dirs2(d, size))
    return res


def handle_output(output: list[str], fs: FS) -> None:
    for row in output:
        match row.split():
            case ['dir', name]:
                fs.append(name, TYPES.DIR)
            case [size, name]:
                fs.append(name, TYPES.FILE, int(size))


def generate_fs():
    with open(file) as f:
        data = f.read().splitlines()
    fs = FS(name='/', type=TYPES.DIR)
    root_fs = fs
    mode = None
    output = []
    for row in data[1:]:
        if row.startswith('$'):
            if output:
                handle_output(output, fs)
                output = []
            mode = MODES.CMD
            row = row[2:]
            match row.split():
                case ['cd', '/']:
                    fs = root_fs
                case ['cd', '..']:
                    fs = fs.parent
                case ['cd', _dir]:
                    for i, child in enumerate(fs.children):
                        if child.type == TYPES.DIR and child.name == _dir:
                            fs = fs.children[i]
                            break
                case ['ls']:
                    mode = MODES.OUTPUT
        if mode == mode.OUTPUT:
            output.append(row)
    handle_output(output, fs)

    root_fs.calc_sizes()
    return root_fs


def part1():
    root_fs = generate_fs()
    ans = find_dirs(root_fs)
    print(f'part 1: {ans}')


def part2():
    root_fs = generate_fs()
    free_space = 70_000_000 - root_fs.size
    target = 30_000_000 - free_space
    ans = min(find_dirs2(root_fs, target))
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

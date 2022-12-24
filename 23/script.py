#!/usr/bin/python3
from collections import defaultdict

file = './sample.txt' if 0 else './input.txt'

Elf = tuple[int, int]


def get_boundaries(elfs: set[Elf]) -> tuple[int, int, int, int]:
    return min([elf[0] for elf in elfs]), \
           min([elf[1] for elf in elfs]), \
           max([elf[0] for elf in elfs]), \
           max([elf[1] for elf in elfs]),


def print_elfs(elfs: set[Elf]) -> None:
    min_x, min_y, max_x, max_y = get_boundaries(elfs)
    res = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            row.append('#' if (x, y) in elfs else '.')
        res.append(''.join(row))
    print('\n'.join(res))


def propose_move(elfs: set[Elf], elf, start: int) -> Elf | None:
    x, y = elf
    N = (x, y - 1) not in elfs
    S = (x, y + 1) not in elfs
    E = (x + 1, y) not in elfs
    W = (x - 1, y) not in elfs
    NE = (x + 1, y - 1) not in elfs
    SE = (x + 1, y + 1) not in elfs
    NW = (x - 1, y - 1) not in elfs
    SW = (x - 1, y + 1) not in elfs
    options = [
        (N and NE and NW, (x, y - 1)),
        (S and SE and SW, (x, y + 1)),
        (W and NW and SW, (x - 1, y)),
        (E and NE and SE, (x + 1, y))
    ]
    if all(opt[0] for opt in options):
        return None
    for i in range(start, start + 4):
        opt, move = options[i % 4]
        if opt:
            return move
    return None


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    elfs: set[Elf] = set()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == '#':
                elfs.add((x, y))
    for i in range(10):
        moves: dict[Elf, list[Elf]] = defaultdict(list)
        for elf in elfs:
            if move := propose_move(elfs, elf, i):
                moves[move].append(elf)
        for move, _elfs in moves.items():
            if len(_elfs) == 1:
                elfs.remove(_elfs[0])
                elfs.add(move)

    min_x, min_y, max_x, max_y = get_boundaries(elfs)
    size = ((max_x + 1) - min_x) * ((max_y + 1) - min_y)
    ans = size - len(elfs)
    print(f'part 1: {ans}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()

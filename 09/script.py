#!/usr/bin/python3
import numpy as np

file = './sample.txt' if 0 else './input.txt'

dirs = {
    'R': np.array([1, 0]),
    'U': np.array([0, 1]),
    'L': np.array([-1, 0]),
    'D': np.array([0, -1])
}


def move_tail(head, tail, prev_head):
    if all(np.abs(head - tail) <= 1):
        return tail
    return prev_head


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    tail = np.array([0, 0])
    head = np.array([0, 0])
    positions = []
    for row in data:
        _dir, count = row.split()
        for _ in range(int(count)):
            prev_head = head.copy()
            head += dirs[_dir]
            tail = move_tail(head, tail, prev_head)
            positions.append(tail.copy())
    ans = len(set(map(tuple, positions)))
    print(f'part 1: {ans}')


def print_chain(chain):
    grid = np.chararray((5, 6))
    grid[:] = '.'
    for i, row in enumerate(chain):
        if grid[row[1], row[0]] != b'.':
            continue
        grid[row[1], row[0]] = str(i) if i else 'H'
    res = '\n'.join([''.join(row.decode()) for row in grid[::-1]])
    print(res)


diagonals = np.array([[1, 1], [1, -1], [-1, 1], [-1, - 1]])


def move_tail2(head, tail):
    if all(np.abs(head - tail) <= 1):
        return tail
    if head[0] == tail[0]:
        tail[1] += 1 if (head[1] - tail[1]) > 0 else -1
        return tail
    if head[1] == tail[1]:
        tail[0] += 1 if (head[0] - tail[0]) > 0 else -1
        return tail
    positions = tail + diagonals
    for p in positions:
        if all(np.abs(head - p) <= 1):
            return p
    print(head, tail, '\n', positions)


def part2():
    with open(file) as f:
        data = f.read().splitlines()
    chain = np.zeros((10, 2), dtype=int)
    positions = []
    for row in data:
        _dir, count = row.split()
        for _ in range(int(count)):
            chain[0] += dirs[_dir]
            for i in range(1, len(chain)):
                head = chain[i - 1]
                tail = chain[i].copy()
                chain[i] = move_tail2(head, tail)
            positions.append(chain[-1].copy())
    ans = len(set(map(tuple, positions)))
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

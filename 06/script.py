#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'


def solve(size):
    with open(file) as f:
        data = f.read()

    for i in range(0, len(data) - size):
        if len(set(data[i:i + size])) == size:
            return i + size


def part1():
    print(f'part 1: {solve(4)}')


def part2():
    print(f'part 2: {solve(14)}')


if __name__ == '__main__':
    part1()
    part2()

#!/usr/bin/python3
from functools import reduce

file = './sample.txt' if 0 else './input.txt'


def part1():
    with open(file, 'rb') as f:
        data = f.read().splitlines()
    ans = 0
    for row in data:
        size = len(row) // 2
        left = set(row[:size])
        right = set(row[size:])
        common = (left & right).pop()
        common -= 96 if common >= 97 else 38
        ans += common
    print(f'part 1: {ans}')


def part2():
    with open(file, 'rb') as f:
        data = f.read().splitlines()
    ans = 0
    for i in range(0, len(data), 3):
        group = map(set, data[i: i + 3])
        common = reduce(lambda x, y: x & y, group).pop()
        common -= 96 if common >= 97 else 38
        ans += common
    print(f'part 1: {ans}')


if __name__ == '__main__':
    part1()
    part2()

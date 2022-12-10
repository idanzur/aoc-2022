#!/usr/bin/python3
import re

file = './sample.txt' if 0 else './input.txt'


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    ans = 0
    for line in data:
        s1, e1, s2, e2 = [int(i) for i in re.findall('\d+', line)]
        ans += (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1)
    print(f'part 1: {ans}')


def part2():
    with open(file) as f:
        data = f.read().splitlines()
    ans = 0
    for line in data:
        s1, e1, s2, e2 = [int(i) for i in re.findall('\d+', line)]
        elf1 = set(range(s1, e1 + 1))
        elf2 = set(range(s2, e2 + 1))
        ans += bool(elf1 & elf2)
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

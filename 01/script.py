#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'


def part1():
    with open(file) as f:
        data = f.read()
    elfs = data.split('\n\n')
    ans = max(sum(map(int, elf.split('\n'))) for elf in elfs)
    print(f'part 1: {ans}')


def part2():
    with open(file) as f:
        data = f.read()
    elfs = data.split('\n\n')
    sums = sorted((sum(map(int, elf.split('\n'))) for elf in elfs))
    ans = sum(sums[-3:])
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

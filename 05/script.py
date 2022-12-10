#!/usr/bin/python3
import re
from collections import defaultdict

file = './sample.txt' if 0 else './input.txt'


def parse_data():
    with open(file) as f:
        data = f.read()
    draw, rules = data.split('\n\n')
    stacks = defaultdict(list)
    for row in draw.splitlines()[:-1]:
        items = re.findall('(.{3})(?:\s|$)', row)
        for i, item in enumerate(items):
            if item.strip():
                stacks[i + 1].insert(0, item[1])
    return stacks, rules


def part1():
    stacks, rules = parse_data()
    for rule in rules.splitlines():
        count, start, end = [int(i) for i in re.findall('\d+', rule)]
        for _ in range(count):
            stacks[end].append(stacks[start].pop())
    ans = [stacks[i + 1].pop() for i in range(len(stacks))]
    ans = ''.join(ans)
    print(f'part 1: {ans}')


def part2():
    stacks, rules = parse_data()
    for rule in rules.splitlines():
        count, start, end = [int(i) for i in re.findall('\d+', rule)]
        stacks[end].extend(stacks[start][-count:])
        for _ in range(count):
            stacks[start].pop()
    ans = [stacks[i + 1].pop() for i in range(len(stacks))]
    ans = ''.join(ans)
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

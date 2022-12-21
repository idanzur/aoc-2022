#!/usr/bin/python3
from dataclasses import dataclass
from operator import add, sub, mul, floordiv
from typing import Callable

file = './sample.txt' if 0 else './input.txt'

Operator = Callable[[int, int], int]

operators: dict[str, Operator] = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


@dataclass
class Monkey:
    name: str
    left: str | int
    right: str | int
    operator: Operator

    @property
    def value(self) -> int:
        return self.operator(self.left, self.right)


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    known: dict[str, int] = {}
    monkeys: list[Monkey] = []
    for row in data:
        match row.split():
            case [name, n]:
                known[name[:-1]] = int(n)
            case [name, left, op, right]:
                monkeys.append(Monkey(name[:-1], left, right, operators[op]))
    while not known.get('root'):
        for monkey in monkeys[::-1]:
            if type(monkey.left) is str:
                monkey.left = known.get(monkey.left, monkey.left)
            if type(monkey.right) is str:
                monkey.right = known.get(monkey.right, monkey.right)
            if type(monkey.left) is int and type(monkey.right) is int:
                known[monkey.name] = monkey.value
                monkeys.remove(monkey)
    ans = known['root']
    print(f'part 1: {ans}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()

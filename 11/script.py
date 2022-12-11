#!/usr/bin/python3
import re
import operator
from dataclasses import dataclass
from typing import Callable
from functools import reduce

file = './sample.txt' if 0 else './input.txt'

op_to_func = {
    '+': operator.add,
    '*': operator.mul
}


def get_op_func(line) -> Callable[[int], int]:
    match line.split():
        case ['old', op, 'old']:
            return lambda x: op_to_func[op](x, x)
        case ['old', op, n]:
            return lambda x: op_to_func[op](x, int(n))


@dataclass
class Monkey:
    items: list[int]
    op: Callable[[int], int]
    div_test: int
    test_true: int
    test_false: int
    count: int = 0


def print_monkeys(monkeys: list[Monkey]):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: {", ".join(str(_i) for _i in m.items)}')


def parse_monkeys() -> list[Monkey]:
    with open(file) as f:
        data = f.read().split('\n\n')
    monkeys = []
    for chunk in data:
        start, op, test, _true, _false = chunk.splitlines()[1:]
        start = [int(i) for i in re.findall('\d+', start)]
        test = int(re.findall('\d+', test)[0])
        _true = int(re.findall('\d+', _true)[0])
        _false = int(re.findall('\d+', _false)[0])
        op = get_op_func(op.split(' = ')[1])
        monkeys.append(Monkey(items=start, op=op, div_test=test, test_true=_true, test_false=_false))
    return monkeys


def part1():
    monkeys = parse_monkeys()
    for _ in range(20):
        for m in monkeys:
            for item in m.items:
                m.count += 1
                item = m.op(item) // 3
                target = m.test_true if item % m.div_test == 0 else m.test_false
                monkeys[target].items.append(item)
            m.items = []

    most_active = sorted(m.count for m in monkeys)
    ans = most_active[-1] * most_active[-2]
    print(f'part 1: {ans}')


def part2():
    monkeys = parse_monkeys()
    mod = reduce(operator.mul, [m.div_test for m in monkeys])
    for _ in range(10_000):
        for m in monkeys:
            for item in m.items:
                m.count += 1
                item = m.op(item) % mod
                target = m.test_true if item % m.div_test == 0 else m.test_false
                monkeys[target].items.append(item)
            m.items = []

    most_active = sorted(m.count for m in monkeys)
    ans = most_active[-1] * most_active[-2]
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

#!/usr/bin/python3
import json
from functools import cmp_to_key

file = './sample.txt' if 0 else './input.txt'


def compare(left: list, right: list) -> int:
    for l, r in zip(left, right):
        t_l = type(l)
        t_r = type(r)
        if t_l is int and t_r is int:
            if l < r:
                return 1
            if l > r:
                return -1
            continue
        if t_l is int:
            l = [l]
        if t_r is int:
            r = [r]
        if res := compare(l, r):
            return res

    if len(left) < len(right):
        return 1
    if len(left) > len(right):
        return -1
    return 0


def part1():
    with open(file) as f:
        data = f.read().split('\n\n')
    ans = 0
    for i, pairs in enumerate(data, start=1):
        left, right = pairs.splitlines()
        left = json.loads(left)
        right = json.loads(right)
        if compare(left, right) == 1:
            ans += i

    print(f'part 1: {ans}')


def part2():
    with open(file) as f:
        data = f.read().split('\n\n')
    packets = [[[2]], [[6]]]
    for i, pairs in enumerate(data, start=1):
        left, right = pairs.splitlines()
        left = json.loads(left)
        right = json.loads(right)
        packets.extend([left, right])

    packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    ans = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

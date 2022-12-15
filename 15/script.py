#!/usr/bin/python3
import re
from dataclasses import dataclass

file = './sample.txt' if 0 else './input.txt'


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Pair:
    beacon: Point
    sensor: Point
    distance: int = None

    def __post_init__(self):
        self.distance = distance(self.sensor, self.beacon)


Range = tuple[int, int]


def distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def is_overlap(r1: Range, r2: Range) -> bool:
    return r1[0] <= r2[0] <= r1[1] or \
           r1[0] <= r2[1] <= r1[1] or \
           r2[0] <= r1[0] <= r2[1] or \
           r2[0] <= r1[1] <= r2[1] or \
           (r1[1] + 1) == r2[0] or \
           (r2[1] + 1) == r1[1]


def combine(r1: Range, r2: Range) -> Range:
    return min(r1[0], r2[0]), max(r1[1], r2[1])


def try_reduce(ranges: list[Range]) -> bool:
    for i, r1 in enumerate(ranges):
        for j, r2 in enumerate(ranges[i + 1:]):
            if is_overlap(r1, r2):
                new_r = combine(r1, r2)
                ranges.remove(r2)
                ranges.remove(r1)
                ranges.append(new_r)
                return True
    return False


def parse_input() -> list[Pair]:
    with open(file) as f:
        data = f.read().splitlines()
    pairs: list[Pair] = []

    for row in data:
        s_x, s_y, b_x, b_y = [int(i) for i in re.findall('=(-?\d+)', row)]
        pairs.append(Pair(beacon=Point(b_x, b_y), sensor=Point(s_x, s_y)))
    return pairs


def part1():
    pairs = parse_input()
    target = 2000000
    beacons_on_target: set[Point] = set()
    ranges: list[Range] = []
    for p in pairs:
        if p.beacon.y == target:
            beacons_on_target.add(p.beacon)
        d = p.distance - abs(p.sensor.y - target)
        if d <= 0:
            continue
        ranges.append((p.sensor.x - d, p.sensor.x + d))

    while try_reduce(ranges):
        pass
    ans = sum((r[1] - r[0]) + 1 for r in ranges) - len(beacons_on_target)
    print(f'part 1: {ans}')


def part2():
    pairs = parse_input()
    max_target = 4_000_000
    for target in range(max_target):
        beacons_on_target: set[Point] = set()
        ranges: list[Range] = []
        for p in pairs:
            if p.beacon.y == target:
                beacons_on_target.add(p.beacon)
            d = p.distance - abs(p.sensor.y - target)
            if d <= 0:
                continue
            ranges.append((max(0, p.sensor.x - d), min(max_target, p.sensor.x + d)))

        while try_reduce(ranges):
            pass
        if len(ranges) == 2:
            x = max(ranges[0][0], ranges[0][1]) - 1
            ans = 4000000 * x + target
            print(f'part 2: {ans}')
            return


if __name__ == '__main__':
    part1()
    part2()

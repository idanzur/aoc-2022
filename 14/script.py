#!/usr/bin/python3
import re
from dataclasses import dataclass

file = './sample.txt' if 0 else './input.txt'


@dataclass(frozen=True)
class Point:
    x: int
    y: int


Points = set[Point]


def drop_sand(points: Points) -> bool:
    x = 500
    y = 0
    for _ in range(1000):
        if Point(x, y + 1) not in points:
            y += 1
            continue
        if Point(x - 1, y + 1) not in points:
            x -= 1
            y += 1
            continue
        if Point(x + 1, y + 1) not in points:
            x += 1
            y += 1
            continue
        points.add(Point(x, y))
        return True
    return False


def create_points() -> Points:
    with open(file) as f:
        data = f.read().splitlines()
    points: Points = set()
    for row in data:
        path_points: list[Point] = []
        nums = list(map(int, re.findall('\d+', row)))
        for i in range(0, len(nums), 2):
            path_points.insert(0, Point(nums[i], nums[i + 1]))

        for p1, p2 in zip(path_points, path_points[1:]):
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                    points.add(Point(x, y))
    return points


def part1():
    points = create_points()
    ans = 0
    while drop_sand(points):
        ans += 1
    print(f'part 1: {ans}')


def drop_sand2(points: Points, floor: int) -> bool:
    x = 500
    y = 0
    if Point(x, y) in points:
        return False
    for _ in range(1000):
        if y + 1 == floor:
            points.add(Point(x, y))
            return True
        if Point(x, y + 1) not in points:
            y += 1
            continue
        if Point(x - 1, y + 1) not in points:
            x -= 1
            y += 1
            continue
        if Point(x + 1, y + 1) not in points:
            x += 1
            y += 1
            continue
        points.add(Point(x, y))
        return True
    return False


def part2():
    points = create_points()
    floor = max([p.y for p in points]) + 2
    ans = 0
    while drop_sand2(points, floor):
        ans += 1
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

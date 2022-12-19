#!/usr/bin/python3
import sys
from dataclasses import dataclass

file = './sample.txt' if 0 else './input.txt'


@dataclass
class Point:
    x: int
    y: int
    z: int

    def is_touching(self, other: 'Point') -> bool:
        return (self.x + 1 == other.x and self.y == other.y and self.z == other.z) \
               or (self.x - 1 == other.x and self.y == other.y and self.z == other.z) \
               or (self.x == other.x and self.y + 1 == other.y and self.z == other.z) \
               or (self.x == other.x and self.y - 1 == other.y and self.z == other.z) \
               or (self.x == other.x and self.y == other.y and self.z + 1 == other.z) \
               or (self.x == other.x and self.y == other.y and self.z - 1 == other.z)


def get_surface_area(points: list[Point]) -> int:
    count = 0
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            count += p1.is_touching(p2)
    return len(points) * 6 - count


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    points: list[Point] = []
    for row in data:
        x, y, z = [int(i) for i in row.split(',')]
        points.append(Point(x, y, z))

    ans = get_surface_area(points)
    print(f'part 1: {ans}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()

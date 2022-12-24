#!/usr/bin/python3
import re
from dataclasses import dataclass
from enum import Enum

file = './sample.txt' if 0 else './input.txt'


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)


class Cell(Enum):
    EMPTY = '.'
    WALL = '#'


@dataclass
class Path:
    length: int
    direction: int


directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1)
]

def is_point_valid(board: dict[Point, Cell], point: Point) -> bool:
    return board[point] == Cell.EMPTY


def part1():
    with open(file) as f:
        data = f.read()
    data, path = data.split('\n\n')
    path = 'R' + path

    board: dict[Point, Cell] = {}
    horizontal_cycle: dict[int, tuple[int, int]] = {}
    vertical_cycle: dict[int, tuple[int, int]] = {}
    for y, row in enumerate(data.splitlines()):
        flag = True
        for x, cell in enumerate(row):
            if cell == ' ':
                continue
            p = Point(x, y)
            if flag:
                horizontal_cycle[y] = (x, len(row) - 1)
                flag = False
            board[p] = Cell.EMPTY if cell == '.' else Cell.WALL
            if Point(x, y - 1) not in board:
                vertical_cycle[x] = (y, 0)
            vertical_cycle[x] = (vertical_cycle[x][0], max(vertical_cycle[x][1], y))

    paths: list[Path] = [Path(int(length), 1 if d == 'R' else -1) for d, length in re.findall('([RL])(\d+)+', path)]

    start: Point = Point(min([p.x for p in board if p.y == 0]), 0)
    dir_index = None
    for path in paths:
        dir_index = 0 if dir_index is None else (dir_index + path.direction) % 4
        for _ in range(path.length):
            next_point = start + directions[dir_index]
            if next_point in board:
                if board[next_point] == Cell.EMPTY:
                    start = next_point
                    continue
                else:
                    break
            next_x = start.x
            next_y = start.y
            if dir_index == 0:
                next_x = horizontal_cycle[next_y][0]
            elif dir_index == 1:
                next_y = vertical_cycle[next_x][0]
            elif dir_index == 2:
                next_x = horizontal_cycle[next_y][1]
            else:
                next_y = vertical_cycle[next_x][1]
            next_point = Point(next_x, next_y)
            if board[next_point] == Cell.EMPTY:
                start = next_point
            else:
                break
    ans = (start.y + 1) * 1000 + (start.x + 1) * 4 + dir_index
    print(f'part 1: {ans}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()

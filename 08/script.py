#!/usr/bin/python3
import numpy as np

file = './sample.txt' if 0 else './input.txt'


def visible_mat(grid: np.array, rot):
    res = np.zeros(grid.shape, dtype=bool)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if y == 0 or y == len(grid) - 1 or x == 0:
                res[y, x] = True
            elif all(grid[y, :x] < cell):
                res[y, x] = True
    return np.rot90(res, rot)


def visible_mat2(grid: np.array, rot):
    res = np.zeros(grid.shape)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if y == 0 or y == len(grid) - 1 or x == 0 or x == len(grid):
                res[y, x] = 0
            else:
                s = 0
                for i in np.flip(grid[y, :x] < cell):
                    s += 1
                    if not i:
                        break
                res[y, x] = s
    return np.rot90(res, rot)


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    grid = np.array([list(map(int, row)) for row in data])
    res = np.zeros(grid.shape, dtype=bool)
    for i in range(4):
        res |= visible_mat(np.rot90(grid, i), -i)
    ans = res.sum()
    print(f'part 1: {ans}')


def part2():
    with open(file) as f:
        data = f.read().splitlines()
    grid = np.array([list(map(int, row)) for row in data])
    res = np.ones(grid.shape)
    for i in range(4):
        res *= visible_mat2(np.rot90(grid, i), -i)
    ans = int(res.max())
    print(f'part 2: {ans}')


if __name__ == '__main__':
    part1()
    part2()

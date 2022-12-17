#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'

Shape = set[tuple[int, int]]
Grid = set[tuple[int, int]]
SHAPES: list[Shape] = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},  # -
    {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},  # +
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},  # L
    {(0, 0), (0, 1), (0, 2), (0, 3)},  # I
    {(0, 0), (1, 0), (0, 1), (1, 1)}  # square
]
JET: dict[str, int] = {'>': 1, '<': -1}


def position_shape(shape: Shape, height: int) -> Shape:
    return {(x + 2, y + height + 3) for x, y in shape}


def push_shape(shape: Shape, grid: Grid, jet: int) -> Shape:
    for x, y in shape:
        if not (0 <= (x + jet) < 7 and (x + jet, y) not in grid):
            return shape
    return {(x + jet, y) for x, y in shape}


def drop_shape(shape: Shape) -> Shape:
    return {(x, y - 1) for x, y in shape}


def part1():
    with open(file) as f:
        data = f.read()
    data_len = len(data)
    grid = {(x, -1) for x in range(7)}
    height = 0
    jet_index = 0
    for i in range(2022):
        shape = position_shape(SHAPES[i % 5], height)
        while True:
            jet = JET[data[jet_index % data_len]]
            jet_index += 1
            shape = push_shape(shape, grid, jet)
            new_shape = drop_shape(shape)
            if new_shape & grid:
                grid |= shape
                break
            shape = new_shape
        height = max(y for _, y in grid) + 1
    print(f'part 1: {height}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()

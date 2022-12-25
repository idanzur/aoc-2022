#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'

SNAFU_TO_DIGITS: dict[str, int] = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

DIGITS_TO_SNAFU: dict[int, str] = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}


def snafu2decimal(snafu: str) -> int:
    return sum([SNAFU_TO_DIGITS[d] * (5 ** i) for i, d in enumerate(snafu[::-1])])


def decimal2snafu(num: int, power: int = None, res: str = "") -> str | None:
    if power is None:
        power = find_power(num)
    if power == -1:
        return res.lstrip('0') if num == 0 else None
    options = [(num - (5 ** power) * i, i) for i in range(-2, 3)]
    (num1, i1), (num2, i2) = sorted(options, key=lambda x: abs(x[0]))[:2]
    return \
        decimal2snafu(num1, power - 1, res + DIGITS_TO_SNAFU[i1]) or \
        decimal2snafu(num2, power - 1, res + DIGITS_TO_SNAFU[i2])


def find_power(num: int) -> int:
    i = 1
    res = 1
    while (i * 5) <= num:
        i *= 5
        res += 1
    return res


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    total = sum(snafu2decimal(snafu) for snafu in data)
    ans = decimal2snafu(total)
    print(f'part 1: {ans}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()

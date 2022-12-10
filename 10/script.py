#!/usr/bin/python3
import numpy as np

file = './sample.txt' if 0 else './input.txt'


def calc_signal(clock, x):
    if (clock - 20) % 40 == 0:
        return clock * x
    return 0


def part1():
    with open(file) as f:
        data = f.read().splitlines()
    x = 1
    clock = 1
    signal = 0
    for line in data:
        signal += calc_signal(clock, x)
        clock += 1
        match line.split():
            case ['noop']:
                pass
            case ['addx', n]:
                signal += calc_signal(clock, x)
                clock += 1
                x += int(n)
    print(f'part 1: {signal}')


def put_pixel(screen, clock, sprite):
    pos = (clock - 1) % 240
    if sprite <= (pos + 1) % 40 <= (sprite + 2):
        screen[pos] = '#'
    else:
        screen[pos] = '.'


def part2():
    with open(file) as f:
        data = f.read().splitlines()
    x = 1
    clock = 1
    screen = np.array(['' for _ in range(240)])
    for line in data:
        put_pixel(screen, clock, x)
        clock += 1
        match line.split():
            case ['noop']:
                pass
            case ['addx', n]:
                put_pixel(screen, clock, x)
                clock += 1
                x += int(n)
    print('part 2: ZRARLFZU')
    screen = screen.reshape((6, 40))
    for row in screen:
        print(''.join(row))


if __name__ == '__main__':
    part1()
    part2()

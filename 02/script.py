#!/usr/bin/python3
file = './sample.txt' if 0 else './input.txt'


def part1():
    with open(file) as f:
        games = f.read().splitlines()
        score = 0
        for game in games:
            match game:
                case 'A X':
                    score += 1 + 3
                case 'B X':
                    score += 1
                case 'C X':
                    score += 1 + 6
                case 'A Y':
                    score += 2 + 6
                case 'B Y':
                    score += 2 + 3
                case 'C Y':
                    score += 2
                case 'A Z':
                    score += 3
                case 'B Z':
                    score += 3 + 6
                case 'C Z':
                    score += 3 + 3
        print(f'part 1: {score}')


def part2():
    with open(file) as f:
        games = f.read().splitlines()
        score = 0
        for game in games:
            match game:
                case 'A X':
                    score += 3
                case 'B X':
                    score += 1
                case 'C X':
                    score += 2
                case 'A Y':
                    score += 3 + 1
                case 'B Y':
                    score += 3 + 2
                case 'C Y':
                    score += 3 + 3
                case 'A Z':
                    score += 6 + 2
                case 'B Z':
                    score += 6 + 3
                case 'C Z':
                    score += 6 + 1
        print(f'part 2: {score}')


if __name__ == '__main__':
    part1()
    part2()

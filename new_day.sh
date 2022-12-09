#!/bin/sh
set -xe

mkdir $1
cd $1
cat > script.py <<EOF
#!/usr/bin/python3
file = './sample.txt' if 1 else './input.txt'


def part1():
    with open(file) as f:
        data = f.read()


def part2():
    pass


if __name__  == '__main__':
    part1()
    # part2()
EOF
DAY=$(echo -n $1 | sed  's/^0//g')
curl https://adventofcode.com/2022/day/$DAY/input -s --header "Cookie: session=$(cat ../session.txt)" -o input.txt
truncate -s-1 input.txt 
touch sample.txt

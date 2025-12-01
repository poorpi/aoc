# https://adventofcode.com/2025/day/1
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    s = 50
    zero_count = 0
    for line in data.splitlines():
        if line[0] == 'L':
            s -= int(line[1:])
            s %= 100
        else:
            s += int(line[1:])
            s %= 100
        if s == 0:
            zero_count += 1
    return zero_count


def part2(data):
    s = 50
    zero_count = 0
    for line in data.splitlines():
        dir = line[0]
        num = int(line[1:])
        for _ in range(num):
            if dir == 'L':
                s -= 1
            else:
                s += 1
            if s == 0 or s == 100:
                zero_count += 1
            s %= 100

    return zero_count


run_sample = False
sample = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''
data = aoc.get_data(1, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

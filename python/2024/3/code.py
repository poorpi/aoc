# https://adventofcode.com/2024/day/3
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    import re

    sum = 0
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)', data)
    for match in matches:
        match = match.replace('mul(', '').replace(')', '')
        a, b = map(int, match.split(','))
        sum += a * b
    return sum


def part2(data):
    import re

    sum = 0
    matches = re.findall('(mul\(\d{1,3},\d{1,3}\))|(don\'t)|(do)', data)
    disabled = False
    for match in matches:
        if match[1] == 'don\'t':
            disabled = True
            continue
        if match[2] == 'do':
            disabled = False
            continue
        if disabled:
            continue
        match = match[0].replace('mul(', '').replace(')', '')
        a, b = map(int, match.split(','))
        sum += a * b
    return sum


run_sample = False
sample = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
data = aoc.get_data(3, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

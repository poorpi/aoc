# https://adventofcode.com/2024/day/1
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    left = []
    right = []
    for line in data.splitlines():
        left.append(int(line.split(' ')[0]))
        right.append(int(line.split(' ')[-1]))
    return sum([abs(l - r) for l, r in zip(sorted(left), sorted(right))])


def part2(data):
    left = []
    right = []
    for line in data.splitlines():
        left.append(int(line.split(' ')[0]))
        right.append(int(line.split(' ')[-1]))

    return sum([x * right.count(x) for x in left])


run_sample = False
sample = '''3   4
4   3
2   5
1   3
3   9
3   3'''
data = aoc.get_data(1, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

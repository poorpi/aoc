# https://adventofcode.com/2024/day/2
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc

def part1(data):
    safe = 0
    for line in data.splitlines():
        levels = [int(x) for x in line.split()]
        order = None
        is_safe = True
        for i in range(len(levels) - 1):
            if order is None:
                if levels[i] > levels[i + 1]:
                    order = 'inc'
                elif levels[i] < levels[i + 1]:
                    order = 'dec'
            else:
                if order == 'inc':
                    if levels[i] < levels[i + 1]:
                        is_safe = False
                        break
                elif order == 'dec':
                    if levels[i] > levels[i + 1]:
                        is_safe = False
                        break
            diff = abs(levels[i] - levels[i + 1])
            if diff < 1 or diff > 3:
                is_safe = False
                break

        if is_safe:
            safe += 1

    return safe

def part2(data):

    def solve(levels):
        order = None
        for i in range(len(levels) - 1):
            if order is None:
                if levels[i] > levels[i + 1]:
                    order = 'inc'
                elif levels[i] < levels[i + 1]:
                    order = 'dec'
            else:
                if order == 'inc':
                    if levels[i] < levels[i + 1]:
                        return False
                elif order == 'dec':
                    if levels[i] > levels[i + 1]:
                        return False
            diff = abs(levels[i] - levels[i + 1])
            if diff < 1 or diff > 3:
                return False
        return True

    safe = 0
    for line in data.splitlines():
        levels = [int(x) for x in line.split()]
        for i in range(len(levels)):
            d = levels[:]
            d.pop(i)
            res = solve(d)
            if res:
                safe += 1
                break
    return safe

run_sample = False
sample = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
data = aoc.get_data(2, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

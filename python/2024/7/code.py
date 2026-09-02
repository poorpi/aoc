# https://adventofcode.com/2024/day/7
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def check(result, values, total):
    v = values.copy()
    if len(v) == 0:
        return total == result

    if total > result:
        return False

    i = v.pop(0)
    if check(result, v, total + i):
        return True
    if total != 0 and check(result, v, total * i):
        return True

    return False


def part1(data):
    sum = 0
    for line in data.splitlines():
        d = list(map(int, line.replace(':', '').split(' ')))
        res = d.pop(0)
        if check(res, d, 0):
            sum += res

    return sum


def check2(result, values, total):
    v = values.copy()
    if len(v) == 0:
        return total == result

    if total > result:
        return False

    i = v.pop(0)
    if check2(result, v, total + i):
        return True
    if total != 0 and check2(result, v, total * i):
        return True
    if check2(result, v, int(str(total) + str(i))):
        return True

    return False


def part2(data):
    sum = 0
    for line in data.splitlines():
        d = list(map(int, line.replace(':', '').split(' ')))
        res = d.pop(0)
        if check2(res, d, 0):
            sum += res

    return sum


run_sample = False
sample = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
data = aoc.get_data(7, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

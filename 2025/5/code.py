# https://adventofcode.com/2025/day/5
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc
import utils


def part1(data):
    sum = 0
    fresh_ids = []
    ingredient_ids = []
    read_ingredients = False
    data.strip()
    for line in data.splitlines():
        if line == '':
            read_ingredients = True
            continue
        if not read_ingredients:
            split = line.split('-')
            fresh_ids.append((int(split[0]), int(split[1])))
        else:
            ingredient_ids.append(int(line))

    for ingredient in ingredient_ids:
        for fresh in fresh_ids:
            if fresh[0] <= ingredient <= fresh[1]:
                sum += 1
                break
    return sum


def part2(data):
    fresh_ids = []
    data.strip()
    for line in data.splitlines():
        if line == '':
            break
        split = line.split('-')
        fresh_ids.append((int(split[0]), int(split[1])))

    fresh_ids = utils.merge_intervals(fresh_ids)

    l = sum(end - start + 1 for start, end in fresh_ids)
    return l


run_sample = False
sample = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
data = aoc.get_data(5, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

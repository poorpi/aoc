# https://adventofcode.com/2025/day/6
import sys
import os
from collections import defaultdict

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    stuff = defaultdict(list)
    data.strip()
    for line in data.splitlines():
        for i, n in enumerate(line.split()):
            stuff[i].append(n)
    sum = 0

    for row in stuff:
        op = stuff[row].pop()
        if op == '*':
            prod = 1
            for n in stuff[row]:
                prod *= int(n)
            sum += prod
        elif op == '+':
            partial = 0
            for n in stuff[row]:
                partial += int(n)
            sum += partial
    return sum


def part2(data):
    grid = []
    for line in data.splitlines():
        grid.append(list(line))
    grid = [list(row) for row in zip(*grid)]
    
    operations = []
    components = []
    numbers = []
    for row in grid:
        op = row.pop()
        if op in ['*', '+']:
            operations.append(op)
        n = ''
        for c in row:
            if c != ' ':
                n += c
        if n != '':
            numbers.append(int(n))
        else:
            components.append(numbers)
            numbers = []
    components.append(numbers)
    
    sum = 0
    for op, numbers in zip(operations, components):
        if op == '*':
            prod = 1
            for n in numbers:
                prod *= n
            sum += prod
        elif op == '+':
            partial = 0
            for n in numbers:
                partial += n
            sum += partial
    return sum


run_sample = False
sample = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''
data = aoc.get_data(6, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

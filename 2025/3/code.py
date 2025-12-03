# https://adventofcode.com/2025/day/3
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def solve(data, dim):
    sum = 0
    for bank in data.splitlines():
        on = [0] * dim
        bank_length = len(bank)
        for idx, battery in enumerate(bank):
            joltage = int(battery)
            for d in range(dim):
                if joltage > on[d] and bank_length - idx > dim - 1 - d:
                    on[d] = joltage
                    for reset_d in range(d + 1, dim):
                        on[reset_d] = 0
                    break
        partial = int(''.join(str(x) for x in on))
        sum += partial
    return sum


def part1(data):
    return solve(data, 2)


def part2(data):
    return solve(data, 12)


run_sample = False
sample = '''987654321111111
811111111111119
234234234234278
818181911112111'''
data = aoc.get_data(3, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

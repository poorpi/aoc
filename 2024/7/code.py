# https://adventofcode.com/2024/day/7
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    return None


def part2(data):
    return None

    
data = aoc.get_data(7, 2024)
print('Part 1:', part1(data))
print('Part 2:', part2(data))

# https://adventofcode.com/2025/day/4
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


MOORE = [
    (-1,-1), (0,-1), (1,-1),
    (-1, 0),         (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def neighborhood(grid, x, y, offsets=None, wrap=False):
    offsets = offsets or MOORE
    h, w = len(grid), len(grid[0])
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if wrap:
            nx %= w
            ny %= h
        elif not (0 <= nx < w and 0 <= ny < h):
            continue
        yield grid[ny][nx]


def part1(data):
    grid = []
    for line in data.splitlines():
        grid.append(list(line))
    width = len(grid[0])
    height = len(grid)
    
    sum = 0
    for y in range(height):
        for x in range(width):
            cell = grid[y][x]
            if cell != '@':
                continue
            neighbors = list(neighborhood(grid, x, y))
            count = 0
            for n in neighbors:
                if n == '@':
                    count += 1
            if count < 4:
                sum += 1
    return sum


def part2(data):
    grid = []
    for line in data.splitlines():
        grid.append(list(line))
    width = len(grid[0])
    height = len(grid)
    
    sum = 0
    part_sum = 1
    while part_sum > 0:
        part_sum = 0
        for y in range(height):
            for x in range(width):
                cell = grid[y][x]
                if cell != '@':
                    continue
                neighbors = list(neighborhood(grid, x, y))
                count = 0
                for n in neighbors:
                    if n == '@':
                        count += 1
                if count < 4:
                    grid[y][x] = '.'
                    part_sum += 1
        sum += part_sum
    return sum


run_sample = False
sample = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''
data = aoc.get_data(4, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

# LOL, 06:08:30

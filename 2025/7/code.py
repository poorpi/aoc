# https://adventofcode.com/2025/day/7
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc
import utils


def part1(data):
    grid = []
    for line in data.splitlines():
        grid.append(list(line))

    row = 0
    col = 0
    for c in grid[0]:
        if c == 'S':
            break
        col += 1

    splits = set()
    beams = set()
    beams.add((row, col))
    while True:
        new_beams = set()
        for beam in beams:
            row, col = beam
            if grid[row][col] == '^':
                splits.add((row, col))
                if col - 1 >= 0:
                    grid[row][col - 1] = '|'
                    new_beams.add((row, col - 1))
                if col + 1 < len(grid[0]):
                    grid[row][col + 1] = '|'
                    new_beams.add((row, col + 1))
            else:
                if row + 1 < len(grid):
                    grid[row][col] = '|'
                    new_beams.add((row + 1, col))
        beams = new_beams
        if len(beams) == 0:
            break

    return len(splits)


def part2(data):
    grid = []
    for line in data.splitlines():
        l = list(line)
        for i, c in enumerate(l):
            if c == 'S':
                l[i] = 1
            elif c == '.':
                l[i] = 0
        grid.append(l)
         
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '^':
                if col - 1 >= 0:
                    grid[row][col - 1] += grid[row - 1][col]
                if col + 1 < len(grid[0]):
                    grid[row][col + 1] += grid[row - 1][col]
            else:
                if row - 1 >= 0 and grid[row - 1][col] != '^':
                    grid[row][col] += grid[row - 1][col]

    return sum(grid[-1])


run_sample = False
sample = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''
data = aoc.get_data(7, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

# https://adventofcode.com/2024/day/4
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    sum = 0
    for i, line in enumerate(data.splitlines()):
        for j in range(len(line)):
            if 'X' != line[j]:
                continue
            # horizontal
            s = ''
            for k in range(4):
                if j + k >= len(line):
                    break
                s += line[j + k]
            if s == 'XMAS':
                sum += 1
            s = ''
            # horizontal backwards
            for k in range(4):
                if j - k < 0:
                    break
                s += line[j - k]
            if s == 'XMAS':
                sum += 1
            s = ''
            # vertical
            for k in range(4):
                if i + k >= len(data.splitlines()):
                    break
                s += data.splitlines()[i + k][j]
            if s == 'XMAS':
                sum += 1
            s = ''
            # vertical backwards
            for k in range(4):
                if i - k < 0:
                    break
                s += data.splitlines()[i - k][j]
            if s == 'XMAS':
                sum += 1
            s = ''
            # diagonal down right
            for k in range(4):
                if i + k >= len(data.splitlines()) or j + k >= len(line):
                    break
                s += data.splitlines()[i + k][j + k]
            if s == 'XMAS':
                sum += 1
            s = ''
            # diagonal up right
            for k in range(4):
                if i - k < 0 or j + k >= len(line):
                    break
                s += data.splitlines()[i - k][j + k]
            if s == 'XMAS':
                sum += 1
            s = ''
            # diagonal down left
            for k in range(4):
                if i + k >= len(data.splitlines()) or j - k < 0:
                    break
                s += data.splitlines()[i + k][j - k]
            if s == 'XMAS':
                sum += 1
            s = ''
            # diagonal up left
            for k in range(4):
                if i - k < 0 or j - k < 0:
                    break
                s += data.splitlines()[i - k][j - k]
            if s == 'XMAS':
                sum += 1
    return sum


def part2(data):
    sum = 0
    for i, line in enumerate(data.splitlines()):
        for j in range(len(line)):
            if 'A' != line[j]:
                continue
            # diagonal left
            s1 = ''
            s2 = ''
            for k in range(-1, 2, 1):
                if i + k < 0 or i + k >= len(data.splitlines()) or j + k < 0 or j + k >= len(line):
                    continue
                s1 += data.splitlines()[i + k][j + k]
            # diagonal right
            for k in range(-1, 2, 1):
                if i + k < 0 or i + k >= len(data.splitlines()) or j - k < 0 or j - k >= len(line):
                    continue
                s2 += data.splitlines()[i + k][j - k]
            if (s1 == 'MAS' or s1 == 'SAM') and (s2 == 'MAS' or s2 == 'SAM'):
                sum += 1
    return sum


run_sample = False
sample = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
data = aoc.get_data(4, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

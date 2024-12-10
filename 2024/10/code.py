# https://adventofcode.com/2024/day/10
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):

    def solve(s, peaks, d):
        x, y = s
        if d[y][x] == 9:
            peaks.add(s)
            return
        if x - 1 >= 0 and d[y][x - 1] - d[y][x] == 1:
            solve((x - 1, y), peaks, d)
        if x + 1 < len(d[0]) and d[y][x + 1] - d[y][x] == 1:
            solve((x + 1, y), peaks, d)
        if y - 1 >= 0 and d[y - 1][x] - d[y][x] == 1:
            solve((x, y - 1), peaks, d)
        if y + 1 < len(d) and d[y + 1][x] - d[y][x] == 1:
            solve((x, y + 1), peaks, d)

    d = []
    starts = []
    for y, line in enumerate(data.splitlines()):
        l = []
        for c in line:
            if c == '.':
                l.append(-1)
            else:
                l.append(int(c))
        d.append(l)
        last = 0
        while 0 in l[last:]:
            ix = l.index(0, last)
            starts.append((ix, y))
            last = ix + 1

    total_scores = 0
    for s in starts:
        peaks = set()
        solve(s, peaks, d)
        total_scores += len(peaks)

    return total_scores


def part2(data):

    def solve(s, peaks, d):
        x, y = s
        if d[y][x] == 9:
            if s in peaks:
                peaks[s] += 1
            else:
                peaks[s] = 1
            return
        if x - 1 >= 0 and d[y][x - 1] - d[y][x] == 1:
            solve((x - 1, y), peaks, d)
        if x + 1 < len(d[0]) and d[y][x + 1] - d[y][x] == 1:
            solve((x + 1, y), peaks, d)
        if y - 1 >= 0 and d[y - 1][x] - d[y][x] == 1:
            solve((x, y - 1), peaks, d)
        if y + 1 < len(d) and d[y + 1][x] - d[y][x] == 1:
            solve((x, y + 1), peaks, d)

    d = []
    starts = []
    for y, line in enumerate(data.splitlines()):
        l = []
        for c in line:
            if c == '.':
                l.append(-1)
            else:
                l.append(int(c))
        d.append(l)
        last = 0
        while 0 in l[last:]:
            ix = l.index(0, last)
            starts.append((ix, y))
            last = ix + 1

    total_rating = 0
    for s in starts:
        peaks = dict()
        solve(s, peaks, d)
        rating = sum(peaks.values())
        total_rating += rating

    return total_rating


run_sample = False
# sample = '''0123
# 1234
# 8765
# 9876'''
# sample = '''89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732'''
# sample = '''...0...
# ...1...
# ...2...
# 6543456
# 7.....7
# 8.....8
# 9.....9'''
# sample = '''..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....'''
# sample = '''.....0.
# ..4321.
# ..5..2.
# ..6543.
# ..7..4.
# ..8765.
# ..9....'''
# sample = '''..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....'''
# sample = '''012345
# 123456
# 234567
# 345678
# 4.6789
# 56789.'''
sample = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
data = aoc.get_data(10, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

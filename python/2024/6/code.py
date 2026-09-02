# https://adventofcode.com/2024/day/6
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    dirs = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]
    s = ()
    d = []
    for y, line in enumerate(data.splitlines()):
        d.append(list(line))
        try:
            x = line.index('^')
            s = (x, y)
        except ValueError:
            continue
    visited = []
    run = True
    dir = [0, -1]
    visited.append(s)
    while run:
        x, y = s
        x += dir[0]
        y += dir[1]
        if x < 0 or y < 0 or x >= len(d[0]) or y >= len(d):
            break
        if d[y][x] == '#':
            dir = dirs[(dirs.index(dir) + 1) % 4]
            continue
        d[s[1]][s[0]] = 'X'
        visited.append((x, y))
        s = (x, y)
    return len(set(visited))


def part2(data):
    dirs = [
        ([0, -1], '^'),
        ([1, 0], '>'),
        ([0, 1], 'v'),
        ([-1, 0], '<'),
    ]
    s = ()
    d = []
    v = []
    for y, line in enumerate(data.splitlines()):
        v.append([set()] * len(line))
        d.append(list(line))
        try:
            x = line.index('^')
            s = (x, y)
        except ValueError:
            continue
    obstacles = []
    for i in range(len(d)):
        for j in range(len(d[0])):
            dd = [row[:] for row in d]
            vv = [[cell.copy() for cell in row] for row in v]
            ss = (s[0], s[1])
            idir = 0
            dir, arrow = dirs[idir]
            if dd[i][j] == '^':
                continue
            dd[ss[1]][ss[0]] = 'X'
            dd[i][j] = '#'
            while True:
                x, y = ss
                x += dir[0]
                y += dir[1]
                next_idir = (idir + 1) % 4
                next_dir, next_arrow = dirs[idir]
                if x < 0 or y < 0 or x >= len(dd[0]) or y >= len(dd):
                    vv[ss[1]][ss[0]].add(arrow)
                    dd[ss[1]][ss[0]] = 'X'
                    break
                if dd[y][x] == '#':
                    idir = next_idir
                    dir, arrow = next_dir, next_arrow
                    continue
                if arrow in vv[ss[1]][ss[0]]:
                    obstacles.append((i, j))
                    break
                dd[ss[1]][ss[0]] = 'X'
                vv[ss[1]][ss[0]].add(arrow)
                ss = (x, y)
    return len(set(obstacles))


run_sample = False
sample = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
data = aoc.get_data(6, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

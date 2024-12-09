# https://adventofcode.com/2024/day/8
import sys
import os
import itertools

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):

    def get_x(v, l):
        return v % l

    def get_y(v, l):
        return v // l

    def offset(a, b):
        return (abs(a[0] - b[0]), abs(a[1] - b[1]))

    anthena_types = set(data)
    anthena_types.remove('\n')
    anthena_types.remove('.')
    d = []
    rows = len(data.splitlines()[0])
    cols = len(data.splitlines())
    for line in data.splitlines():
        d += list(line)

    antinodes = set()
    for type in anthena_types:
        positions = []
        try:
            last_ix = 0
            while True:
                ix = d.index(type, last_ix)
                positions.append((get_x(ix, rows), get_y(ix, rows)))
                last_ix = ix + 1
        except ValueError:
            pass

        for a, b in itertools.combinations(positions, 2):
            a, b = sorted([a, b], key=lambda x: (x[1], x[0]))
            o = offset(a, b)
            if a[0] <= b[0]:
                if a[0] - o[0] >= 0 and a[1] - o[1] >= 0:
                    antinodes.add((a[0] - o[0], a[1] - o[1]))
                if b[0] + o[0] < rows and b[1] + o[1] < cols:
                    antinodes.add((b[0] + o[0], b[1] + o[1]))
            else:
                if a[0] + o[0] < rows and a[1] - o[1] >= 0:
                    antinodes.add((a[0] + o[0], a[1] - o[1]))
                if b[0] - o[0] >= 0 and b[1] + o[1] < cols:
                    antinodes.add((b[0] - o[0], b[1] + o[1]))

    # for a in antinodes:
    #     d[a[1] * rows + a[0]] = '#'
    # for x in range(rows):
    #     print(''.join(d[x * rows : (x + 1) * rows]))
    return len(antinodes)


def part2(data):

    def get_x(v, l):
        return v % l

    def get_y(v, l):
        return v // l

    def offset(a, b):
        return (abs(a[0] - b[0]), abs(a[1] - b[1]))

    anthena_types = set(data)
    anthena_types.remove('\n')
    anthena_types.remove('.')
    d = []
    rows = len(data.splitlines()[0])
    cols = len(data.splitlines())
    for line in data.splitlines():
        d += list(line)

    antinodes = set()
    for type in anthena_types:
        positions = []
        try:
            last_ix = 0
            while True:
                ix = d.index(type, last_ix)
                positions.append((get_x(ix, rows), get_y(ix, rows)))
                last_ix = ix + 1
        except ValueError:
            pass
        for pos in positions:
            antinodes.add(pos)
        for a, b in itertools.combinations(positions, 2):
            a, b = sorted([a, b], key=lambda x: (x[1], x[0]))
            so = offset(a, b)
            o = so
            if a[0] <= b[0]:
                while True:
                    added = False
                    if a[0] - o[0] >= 0 and a[1] - o[1] >= 0:
                        antinodes.add((a[0] - o[0], a[1] - o[1]))
                        added = True
                    if b[0] + o[0] < rows and b[1] + o[1] < cols:
                        antinodes.add((b[0] + o[0], b[1] + o[1]))
                        added = True
                    o = (o[0] + so[0], o[1] + so[1])
                    if not added:
                        break
            else:
                while True:
                    added = False
                    if a[0] + o[0] < rows and a[1] - o[1] >= 0:
                        antinodes.add((a[0] + o[0], a[1] - o[1]))
                        added = True
                    if b[0] - o[0] >= 0 and b[1] + o[1] < cols:
                        antinodes.add((b[0] - o[0], b[1] + o[1]))
                        added = True
                    o = (o[0] + so[0], o[1] + so[1])
                    if not added:
                        break

    # for a in antinodes:
    #     d[a[1] * rows + a[0]] = '#'
    # for x in range(rows):
    #     print(''.join(d[x * rows : (x + 1) * rows]))
    return len(antinodes)


run_sample = False
sample = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
sample = '''T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........'''
data = aoc.get_data(8, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

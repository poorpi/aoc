# https://adventofcode.com/2025/day/9
import sys
import os
import shapely

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def area(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1])+ 1) 


def part1(data):
    red_tiles = []
    for line in data.splitlines():
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))

    max_area = 0
    for ix, c1 in enumerate(red_tiles):
        for c2 in red_tiles[ix + 1:]:
            max_area = max(max_area, area(c1, c2))
    return max_area


def part2(data):
    red_tiles = []
    for line in data.splitlines():
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))
    
    areas = []
    for ix, c1 in enumerate(red_tiles):
        for c2 in red_tiles[ix + 1:]:
            areas.append((area(c1, c2), c1, c2))
    areas.sort(key=lambda x: x[0], reverse=True)

    polygon = shapely.Polygon(red_tiles)
    for a, c1, c2 in areas:
        rect = shapely.Polygon([c1, (c1[0], c2[1]), c2, (c2[0], c1[1])])
        if polygon.contains(rect):
            break
    return a


run_sample = False
sample = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''
data = aoc.get_data(9, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

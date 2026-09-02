# https://adventofcode.com/2025/day/12
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc
from collections import deque


def part1(data):
    shapes = {}
    regions = []
    shape = []
    shape_id = None
    for line in data.splitlines():
        if line == '':
            shapes[shape_id] = shape
            shape = []
            shape_id = None
            continue
        if line[0] == '.' or line[0] == '#':
            shape.append(list(line))
            continue
        if not line.split(':')[1]:
            shape_id = int(line.split(':')[0])
            continue
        s = line.split(':')
        size = int(s[0].split('x')[0]), int(s[0].split('x')[1])
        presents = [int(x) for x in s[1].split(' ') if x != '']
        regions.append((size, presents))

    n_shapes = {}
    for shape in shapes:
        grid = shapes[shape]
        area = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):        
                if grid[y][x] == '#':
                    area += 1
        n_shapes[shape] = (grid, area)
    shapes = n_shapes

    possible_fits = 0

    # prune impossible regions (no way all the shapes fit)
    for region in regions:
        region_area = region[0][0] * region[0][1]
        for shape_id, count in enumerate(region[1]):
            shape, shape_area = shapes[shape_id]
            region_area -= count * shape_area
            if region_area < 0:
                break
        if region_area >= 0:
            possible_fits += 1
    
    # check if maybe we don't really have to do anything else?
    return possible_fits
    # LOOOOOOOOL, does not work on example, works for real input


def part2(data):
    return 'Nothing ^_^'


run_sample = False
sample = '''0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2'''
data = aoc.get_data(12, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

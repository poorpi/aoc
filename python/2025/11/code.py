# https://adventofcode.com/2025/day/11
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc
import utils
from collections import deque
from functools import lru_cache


@utils.time_it
def part1(data):
    paths_num = 0
    devices = {}
    for line in data.splitlines():
        line = line.split(':')
        devices[line[0]] = line[1].split()
    q = deque()
    q.append('you')
    while q:
        device = q.popleft()
        for output in devices[device]:
            if output == 'out':
                paths_num += 1
            else:
                q.append(output)
    return paths_num


@utils.time_it
def part2(data):
    devices = {}
    for line in data.splitlines():
        line = line.split(':')
        devices[line[0]] = line[1].split()
    
    @lru_cache(maxsize=None)
    def connect(device, seen_dac, seen_fft):
        if device == 'out':
            return int(seen_dac and seen_fft)
        else:
            seen_dac = seen_dac or device == 'dac'
            seen_fft = seen_fft or device == 'fft'
            return sum(connect(output, seen_dac, seen_fft) for output in devices[device])

    return connect('svr', False, False)


run_sample = False
sample = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''
sample_2 = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''
data = aoc.get_data(11, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample_2))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

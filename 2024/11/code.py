# https://adventofcode.com/2024/day/11
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    d = list(map(int, data.split(' ')))
    blinks = 25
    for b in range(blinks):
        new_d = []
        for i in range(len(d)):
            if d[i] == 0:
                new_d.append(1)
            elif len(str(d[i])) % 2 == 0:
                l = str(d[i])[0 : len(str(d[i])) // 2]
                r = str(d[i])[len(str(d[i])) // 2 :]
                new_d += [int(l), int(r)]
            else:
                new_d.append(d[i] * 2024)
        d = new_d
    return len(d)


def part2(data):

    def blink(n, current_count, new_stones):
        if n == 0:
            if 1 in new_stones:
                new_stones[1] += current_count
            else:
                new_stones[1] = current_count
        elif len(str(n)) % 2 == 0:
            l = int(str(n)[0 : len(str(n)) // 2])
            if l in new_stones:
                new_stones[l] += current_count
            else:
                new_stones[l] = current_count
            r = int(str(n)[len(str(n)) // 2 :])
            if r in new_stones:
                new_stones[r] += current_count
            else:
                new_stones[r] = current_count
        else:
            if n * 2024 in new_stones:
                new_stones[n * 2024] += current_count
            else:
                new_stones[n * 2024] = current_count

    d = list(map(int, data.split(' ')))
    stones = {}
    for dd in d:
        stones[dd] = 1

    for _ in range(75):
        new_stones = {}
        for n in stones:
            current_count = stones[n]
            blink(n, current_count, new_stones)
        stones = new_stones
    return sum(stones.values())


run_sample = False
sample = '''0 1 10 99 999'''
sample = '''125 17'''
data = aoc.get_data(11, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

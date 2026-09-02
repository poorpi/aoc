# https://adventofcode.com/2024/day/9
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    d = []
    id = 0
    for i in range(len(data)):
        if data[i] == '\n':
            break
        if i % 2 == 0:
            # file
            d += [str(id)] * int(data[i])
            id += 1
        else:
            # free space
            d += ['.'] * int(data[i])

    i = 0
    j = len(d) - 1
    while i < j:
        if d[i] == '.' and d[j] != '.':
            d[i] = d[j]
            d[j] = '.'
        if d[i] != '.':
            i += 1
        if d[j] == '.':
            j -= 1

    s = 0
    for i in range(len(d)):
        if d[i] != '.':
            s += int(d[i]) * i
    return s


def part2(data):
    id = 0
    ix = 0
    files = []  # (id, index, size)
    free_space = []  # (index, size)
    for i in range(len(data)):
        if data[i] == '\n':
            break
        if i % 2 == 0:
            # file
            files.append((id, ix, int(data[i])))
            id += 1
            ix += int(data[i])
        else:
            # free space
            free_space.append((ix, int(data[i])))
            ix += int(data[i])

    files.sort(key=lambda x: x[0], reverse=True)
    moved_files = []  # (id, index, size)
    i = 0
    while True:
        if i > len(free_space) - 1:
            break
        fs_ix, fs_size = free_space.pop(i)
        found = False
        for j in range(len(files)):
            f_id, f_ix, f_size = files.pop(j)
            if f_size <= fs_size:
                found = True
                break
            else:
                files.insert(j, (f_id, f_ix, f_size))
        if not found:
            free_space.insert(i, (fs_ix, fs_size))
            i += 1
            continue
        if fs_ix >= f_ix:
            files.insert(j, (f_id, f_ix, f_size))
            free_space.insert(i, (fs_ix, fs_size))
            i += 1
            continue
        f_ix = fs_ix
        fs_ix += f_size
        fs_size -= f_size
        moved_files.append((f_id, f_ix, f_size))
        if fs_size > 0:
            free_space.insert(i, (fs_ix, fs_size))

    d = ['.'] * ix
    for m_f in moved_files:
        for i in range(m_f[2]):
            d[m_f[1] + i] = str(m_f[0])
    for f in files:
        for i in range(f[2]):
            d[f[1] + i] = str(f[0])

    s = 0
    for i in range(len(d)):
        if d[i] != '.':
            s += int(d[i]) * i
    return s


run_sample = False
sample = '''2333133121414131402'''
data = aoc.get_data(9, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

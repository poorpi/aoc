# https://adventofcode.com/2024/day/5
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    rules = []
    updates = []
    for line in data.splitlines():
        if '|' in line:
            a, b = map(int, line.split('|'))
            rules.append((a, b))
        if ',' in line:
            update = list(map(int, line.split(',')))
            updates.append(update)
        else:
            continue
    sum = 0
    for update in updates:
        good = True
        for a, b in rules:
            if a in update and b in update:
                index_of_a = update.index(a)
                index_of_b = update.index(b)
                if index_of_a > index_of_b:
                    good = False
                    break
        if good:
            sum += update[len(update) // 2]
    return sum


def part2(data):
    rules = []
    updates = []
    for line in data.splitlines():
        if '|' in line:
            a, b = map(int, line.split('|'))
            rules.append((a, b))
        if ',' in line:
            update = list(map(int, line.split(',')))
            updates.append(update)
        else:
            continue
    broken = []
    for update in updates:
        for a, b in rules:
            if a in update and b in update:
                index_of_a = update.index(a)
                index_of_b = update.index(b)
                if index_of_a > index_of_b:
                    broken.append(update)
                    break
    sum = 0
    for x in broken:
        cur = x
        while True:
            whole = True
            for a, b in rules:
                if a in cur and b in cur:
                    index_of_a = cur.index(a)
                    index_of_b = cur.index(b)
                    if index_of_a > index_of_b:
                        cur[index_of_a], cur[index_of_b] = cur[index_of_b], cur[index_of_a]
                        whole = False
                        break
            if whole:
                break
        sum += cur[len(cur) // 2]
    return sum


run_sample = False
sample = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
data = aoc.get_data(5, 2024)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

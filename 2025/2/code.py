# https://adventofcode.com/2025/day/2
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1_old(data):
    # original "clever" approach
    sum = 0
    bf_sum = 0
    data = data.strip()
    for id_range in data.split(','):
        # we can check only "half" the range to find the invalid IDs
        invalid_ranges = []
        start_str, end_str = id_range.split('-')
        start = int(start_str)
        end = int(end_str)
        start_begin = start_str[:len(start_str)//2]
        if not start_begin:
            start_begin = start_str # must be single digit
        end_begin = end_str[:(len(end_str)//2) + 1]
        if not end_begin:
            end_begin = end_str # must be single digit
        if start_begin[0] > end_begin[0]: # fixes case like 5-12 that should catch 11 :shrug:
            start_begin = end_begin[0]
        if start_begin == 0:
            start_begin = 1
        half_start = int(start_begin)
        half_end = int(end_begin)
        for i in range(half_start, half_end + 1):
            invalid_range = int(str(i)*2)
            if invalid_range >= start and invalid_range <= end:
                invalid_ranges.append(invalid_range)
                sum += invalid_range

        # Brute force check to verify if we missed anything
        for id in range(start, end + 1):
            if not len(str(id)) % 2 == 0:
                continue
            str_id = str(id)
            first_half = str_id[:len(str_id)//2]
            second_half = str_id[len(str_id)//2:]
            if first_half == second_half:
                if id not in invalid_ranges:
                    print(f'BF found invalid ID:{id} in range {id_range}')
                bf_sum += id

    print(f'Part 1 BF Sum: {bf_sum}')
    return sum


def part1(data):
    # after doing part 2 with regex - do part 1 with regex too :shrug:
    import re
    sum = 0
    data = data.strip()
    for id_range in data.split(','):
        start, end = map(int, id_range.split('-'))
        for id in range(start, end + 1):
            str_id = str(id)
            if re.match(r'^([0-9]+)\1$', str_id): # match one or more digits into a capture group, then match that capture group once more till the end
                sum += id

    return sum


def part2(data):
    import re
    sum = 0
    data = data.strip()
    for id_range in data.split(','):
        start, end = map(int, id_range.split('-'))
        for id in range(start, end + 1):
            str_id = str(id)
            if re.match(r'^([0-9]+)\1+$', str_id): # match one or more digits into a capture group, then match that same capture group one or more times till the end
                sum += id

    return sum


run_sample = False
sample = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
data = aoc.get_data(2, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

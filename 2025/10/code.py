# https://adventofcode.com/2025/day/10
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc
from collections import deque
import numpy as np
import scipy as sp

def part1(data):
    sum = 0
    for line in data.splitlines():
        lights = []
        buttons = []
        joltages = []
        i = -1
        button = []
        for c in line:
            if c == '[':
                i += 1
                continue
            if c == ']':
                i += 1
                continue
            if c == '(':
                i += 1
                continue
            if c == ')':
                buttons.append(button)
                button = []
                i -= 1
                continue
            if c == '{':
                i += 2
                continue
            if c == '}':
                break
            if i == 0:
                lights.append(c)
            if i == 2:
                button.append(c)
            if i == 3:
                joltages.append(c)
        n_buttons = []
        for button in buttons:
            b = []
            for x in ''.join(button).split(','):
                b.append(int(x))
            n_buttons.append(b)
        buttons = n_buttons
        n_joltages = []
        for joltage in ''.join(joltages).split(','):
            n_joltages.append(int(joltage))
        joltages = n_joltages
        n_lights = []
        for light in lights:
            if light == '#':
                n_lights.append(True)
            else:
                n_lights.append(False)
        lights = n_lights

        q = deque()
        q.append((([False] * len(lights), 0)))
        visited_states = set()
        while len(q) > 0:
            state, depth = q.popleft()
            solved = False
            for b in buttons:
                new_state = [x for x in state]
                for bb in b:
                    new_state[bb] = not new_state[bb]
                if new_state == lights:
                    solved = True
                    break
                if tuple(new_state) not in visited_states:
                    visited_states.add(tuple(new_state))
                    q.append((new_state, depth + 1))
            if solved:
                sum += depth + 1
                break

    return sum


def part2(data):
    sum = 0
    for line in data.splitlines():
        lights = []
        buttons = []
        joltages = []
        i = -1
        button = []
        for c in line:
            if c == '[':
                i += 1
                continue
            if c == ']':
                i += 1
                continue
            if c == '(':
                i += 1
                continue
            if c == ')':
                buttons.append(button)
                button = []
                i -= 1
                continue
            if c == '{':
                i += 2
                continue
            if c == '}':
                break
            if i == 0:
                lights.append(c)
            if i == 2:
                button.append(c)
            if i == 3:
                joltages.append(c)
        n_buttons = []
        for button in buttons:
            b = []
            for x in ''.join(button).split(','):
                b.append(int(x))
            n_buttons.append(b)
        buttons = n_buttons
        n_joltages = []
        for joltage in ''.join(joltages).split(','):
            n_joltages.append(int(joltage))
        joltages = n_joltages

        coefficients = []
        for b in buttons:
            coefficient = [0] * len(joltages)
            for bb in b:
                coefficient[bb] += 1
            coefficients.append(coefficient)
        result = sp.optimize.linprog([1] * len(buttons), A_eq=np.transpose(coefficients), b_eq=joltages, integrality=1)
        sum += int(result.fun)
        

    return sum


run_sample = False
sample = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''
data = aoc.get_data(10, 2025)
if run_sample:
    print('Part 1:', part1(sample))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))

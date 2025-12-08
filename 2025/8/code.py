# https://adventofcode.com/2025/day/8
import sys
import os
import math

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def distance(a, b):
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]))


def part1(data, count=1000):
    coords = []
    for line in data.splitlines():
        x, y, z = map(int, line.split(','))
        coords.append((x, y, z))
    
    distances = []
    num = 0
    for i in range(len(coords)):
        coordinates = coords[i]
        for c in coords[i + 1:]:
            num += 1
            distances.append((distance(coordinates, c), coordinates, c))

    distances = sorted(distances, key=lambda x: x[0])

    circuits = []
    c = set()
    c.add(distances[0][1])
    c.add(distances[0][2])
    circuits.append(c)
    for i in range(1, count):
        s = distances[i][1]
        e = distances[i][2]
        added = False
        for j in range(len(circuits)):
            circuit = circuits[j]
            if s in circuit or e in circuit:
                circuit.add(s)
                circuit.add(e)
                added = True
                for k in range(j + 1, len(circuits)):
                    if s in circuits[k] or e in circuits[k]:
                        circuit.update(circuits[k])
                        circuits.pop(k)
                        break
                circuits[j] = circuit
                break
        if not added:
            c = set()
            c.add(s)
            c.add(e)
            circuits.append(c)
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part2(data):
    coords = []
    for line in data.splitlines():
        x, y, z = map(int, line.split(','))
        coords.append((x, y, z))
    
    distances = []
    num = 0
    for i in range(len(coords)):
        coordinates = coords[i]
        for c in coords[i + 1:]:
            num += 1
            distances.append((distance(coordinates, c), coordinates, c))

    distances = sorted(distances, key=lambda x: x[0])

    circuits = []
    c = set()
    c.add(distances[0][1])
    c.add(distances[0][2])
    circuits.append(c)
    l = 1
    i = 0
    while l < len(coords):
        i += 1
        s = distances[i][1]
        e = distances[i][2]
        added = False
        for j in range(len(circuits)):
            circuit = circuits[j]
            if s in circuit or e in circuit:
                circuit.add(s)
                circuit.add(e)
                added = True
                for k in range(j + 1, len(circuits)):
                    if s in circuits[k] or e in circuits[k]:
                        circuit.update(circuits[k])
                        circuits.pop(k)
                        break
                circuits[j] = circuit
                l = len(circuit)
                break
        if not added:
            c = set()
            c.add(s)
            c.add(e)
            circuits.append(c)
            l = 1
    return s[0] * e[0]


run_sample = False
sample = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''
data = aoc.get_data(8, 2025)
if run_sample:
    print('Part 1:', part1(sample, 10))
    print('Part 2:', part2(sample))
else:
    print('Part 1:', part1(data, 1000))
    print('Part 2:', part2(data))

import requests
from datetime import date
from os import makedirs
from os.path import exists
from dotenv import load_dotenv, dotenv_values

if not exists('.env'):
    with open('.env', 'w') as f:
        f.write('SESSION="{session}"'.format(session=input('Enter your session cookie: ')))

load_dotenv()
CURRENT_YEAR = date.today().year
DATA_FILE_TEMPLATE = '{year}/data/{day}.data'
URL_TEMPLATE = 'https://adventofcode.com/{year}/day/{day}/input'


def init(year=CURRENT_YEAR):
    makedirs(str(year) + '/data')
    for day in range(1, 26):
        day_dir = str(year) + '/' + str(day)
        makedirs(day_dir)
        with open(day_dir + '/code.py', 'w') as f:
            f.write(
                '''# https://adventofcode.com/{year}/day/{day}
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import aoc_utils as aoc


def part1(data):
    return None


def part2(data):
    return None

    
data = aoc.get_data({day}, {year})
print('Part 1:', part1(data))
print('Part 2:', part2(data))
'''.format(
                    year=year, day=day
                )
            )


def get_data(day, year=CURRENT_YEAR):
    file = DATA_FILE_TEMPLATE.format(year=year, day=day)
    if exists(file):
        with open(file, 'r') as f:
            return f.read()
    else:
        url = URL_TEMPLATE.format(year=year, day=day)
        r = requests.get(url, cookies={'session': dotenv_values('.env')['SESSION']})
        if not r.ok:
            r.raise_for_status()
        with open(file, 'w') as f:
            f.write(r.text)
        return r.text

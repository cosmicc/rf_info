#!/usr/bin/env python3

import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('csv_file', action='store', help='CSV file to parse')
parser.add_argument('unit', nargs='?', default='hz', help='hz, khz, Mhz, Ghz')
args = parser.parse_args()

data_file = Path(args.csv_file)
if not data_file.exists() or not data_file.is_file():
    print('CSV file invalid or cannot be found')
    exit(1)

file_split = data_file.stem.split('_')
if len(file_split) != 2:
    print('Cannot determine country from file')
    exit(1)
country = file_split[0]
new_data_file = Path(f'/opt/rf_info/rf_info/data/{country.lower()}_data.py')


def parse_line(pa):
    newpa = []
    fixed = False
    mobile = False
    amateur = False
    broadcast = False
    for a in pa:
        asp = a.strip().split(' ')
        for each in asp:
            if len(each) > 1:
                for c in each:
                    if c.isnumeric():
                        if each in asp:
                            asp.remove(each)
            elif len(each) == 1:
                asp.remove(each)
        if 'AMATEUR' in asp or 'AMATEUR-SATELITE' in asp:
            amateur = True
        if 'BROADCASTING' in asp:
            broadcast = True
        if 'FIXED' in asp:
            fixed = True
        if 'MOBILE' in asp:
            mobile = True
        a = ' '.join(asp)
        if a.strip().lower() == 'fixed':
            fixed = True
        elif a.strip().lower() == 'mobile':
           mobile = True
        else:
            newpa.append(a.strip().title())
    return newpa, amateur, fixed, mobile, broadcast


def write_header():
    with new_data_file.open(mode='w') as f:
        print('from .rangekeydict import RangeKeyDict', file=f)
        print(' ', file=f)
        print('ALLOCATIONS = RangeKeyDict({', file=f)


def write_footer():
    with new_data_file.open(mode='a') as f:
        print('})', file=f)


write_header()
with open(str(data_file)) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row["Min (MHz)"].isnumeric():
            minfreq = int(row["Min (MHz)"])
        else:
            minfreq = float(row["Min (MHz)"])
        if row["Max (MHz)"].isnumeric():
            maxfreq = int(row["Max (MHz)"])
        else:
            maxfreq = float(row["Max (MHz)"])
        minfreq = minfreq * 1000000
        maxfreq = maxfreq * 1000000

        sa, amateur, fixed, mobile, broadcast = parse_line(row["Secondary Allocations"].split(','))
        pa, amateur, fixed, mobile, broadcast = parse_line(row["Primary Allocations"].split(','))
        with new_data_file.open(mode='a') as f:
            print(f'    ({int(minfreq)}, {int(maxfreq)}): ({amateur}, {fixed}, {mobile}, {broadcast}, {pa}, {sa}),', file=f)
        # print(int(minfreq), int(maxfreq), pa, sa, amateur, fixed, mobile, broadcast)
write_footer()

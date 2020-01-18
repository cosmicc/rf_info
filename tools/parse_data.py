#!/usr/bin/env python3

'''
Dev tool for building country allocation files
data parsed from: http://www.grss-ieee.org/frequency_allocations.html

'''

import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('csv_file', action='store', help='CSV file to parse')
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
new_data_file = Path(f'/opt/rf_info/rf_info/data/a_allocations.py')


def parse_line(pa):
    newpa = []
    fixed = False
    mobile = False
    amateur = False
    broadcast = False
    for a in pa:
        asp = a.strip().split(' ')
        for each in asp:
            if len(each) > 3:
                if each[0] == '(' and each[1].isnumeric() and each[2] == '.':
                    if each in asp:
                        e = each.split(',')
                        o = 0
                        if len(e) > 1:
                            n = ''
                            for f in e:
                                if o != len(e) - 1:
                                    n = n + f + ']['
                                else:
                                    n = n + f
                                o += 1
                            neach = n
                        else:
                            neach = each
                        asp[asp.index(each)] = neach.replace('(', '[').replace(')', ']')

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
    if len(newpa) > 0:
        if newpa[0] == '':
            newpa = []
    return newpa, amateur, fixed, mobile, broadcast


def parse_footnotes(footnote):
    footsplit = (footnote.replace('<b>', '').replace('</b>', '')).strip().split('<br>')
    newfoot = []
    for each in footsplit:
        if len(each) > 0:
            if each[0].isnumeric():
                if each[1] == '.':
                    for i, c in enumerate(each):
                        if c == ':':
                            break
                    each = '[' + each
                    newfoot.append(each[:i+1] + ']' + each[i+1:])
                else:
                    newfoot.append(str(each.strip()))
            else:
                newfoot.append(str(each.strip()))
    print(type(newfoot))
    return newfoot


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

        sa, amateur, fixed, mobile, broadcast = parse_line(row["Secondary Allocations"].split(', '))
        pa, amateur2, fixed2, mobile2, broadcast2 = parse_line(row["Primary Allocations"].split(', '))
        if not fixed and fixed2:
            fixed = True
        if not mobile and mobile2:
            mobile = True
        if not broadcast and broadcast2:
            broadcast = True
        if not amateur and amateur2:
            amateur = True

        fn = parse_footnotes(row['Footnotes'])
        print(type(fn))
        #print(fn)
        with new_data_file.open(mode='a') as f:
            print(f'    ({int(minfreq)}, {int(maxfreq)}): ({amateur}, {fixed}, {mobile}, {broadcast}, {pa}, {sa}, {fn}),', file=f)
        # print(int(minfreq), int(maxfreq), pa, sa, amateur, fixed, mobile, broadcast)
write_footer()

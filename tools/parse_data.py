#!/usr/bin/env python3

'''
Dev tool for building country allocation files
data parsed from: http://www.grss-ieee.org/frequency_allocations.html

'''

import csv
import argparse
from pathlib import Path
from iso3166 import countries

import sys
sys.path.insert(1, '/opt/rf_info/rf_info/data')

from countrymap import COUNTRY_MAP

country_map_file = Path('/opt/rf_info/rf_info/data/countrymap.py')

parser = argparse.ArgumentParser()
parser.add_argument('--force', '-f', action='store_true', help='Force overwrite')
parser.add_argument('--list', '-l', action='store_true', help='List currently supported countries')
parser.add_argument('--shortlist', '-sl', action='store_true', help='short country list for readme')
args = parser.parse_args()

if args.shortlist:
    clist = []
    for key, value in COUNTRY_MAP.items():
        clist.append(f'{countries.get(key).name} ({countries.get(key).alpha2})')
    print(', '.join(clist))
    exit(0)
elif args.list:
    for key, value in COUNTRY_MAP.items():
        print(f'{countries.get(key).name} ({countries.get(key).alpha2})')
    exit(0)

def check_countrymap(country, letter):
    if country.alpha2.upper() in COUNTRY_MAP:
        if COUNTRY_MAP[country.alpha2.upper()] == letter:
            print(f'[ {country.alpha2.upper()} ] already exists as [ {letter.upper()} ] in countrymap')
            data_file.unlink()
        else:
            print(f'[ {country.alpha2.upper()} ] exists but different [ COUNTRY_MAP[country.alpha2.upper()].upper() ] -> [ {letter.upper()} ]')
            COUNTRY_MAP.update({country.alpha2.upper(): letter.lower()})
            with country_map_file.open(mode='w') as f:
                print(f'COUNTRY_MAP = {COUNTRY_MAP}', file=f)
            data_file.unlink()
    else:
        print(f'[ {country.alpha2.upper()} ] does not exist in countrymap. adding it.')
        COUNTRY_MAP.update({country.alpha2.upper(): letter.lower()})
        with country_map_file.open(mode='w') as f:
            print(f'COUNTRY_MAP = {COUNTRY_MAP}', file=f)
        data_file.unlink()


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
    return newfoot


def write_header():
    with new_data_file.open(mode='w') as f:
        print('from .rangekeydict import RangeKeyDict', file=f)
        print(' ', file=f)
        print('ALLOCATIONS = RangeKeyDict({', file=f)


def write_footer():
    with new_data_file.open(mode='a') as f:
        print('})', file=f)


pth = Path('/home/ip')
for dtfl in pth.iterdir():
    if dtfl.suffix == '.csv':
        data_file = dtfl

        if not data_file.exists() or not data_file.is_file():
            print('CSV file invalid or cannot be found')
            exit(1)

        fs = data_file.stem
        try:
            country = countries.get(fs.title())
        except:
            print(f'Cannot determine country from filename {fs}')
            break

        csv_size = data_file.stat().st_size
        if csv_size == 635414:
            letter = 'a'
            print(f'{country.name} [ {country.alpha2} ] is [ {letter.upper()} ] Type')
            check_countrymap(country, letter)
        elif csv_size == 682975:
            letter = 'b'
            print(f'{country.name} [ {country.alpha2} ] is [ {letter.upper()} ] Type')
            check_countrymap(country, letter)
        elif csv_size == 660096:
            letter = 'c'
            print(f'{country.name} [ {country.alpha2} ] is [ {letter.upper()} ] Type')
            check_countrymap(country, letter)
        else:
            letter = 'd'
            print(f'{country.name} [ {country.alpha2} ] is UNKNOWN TYPE! making [ {letter.upper()} ] file')
            check_countrymap(country, letter)
            args,force = True

        new_data_file = Path(f'/opt/rf_info/rf_info/data/{letter.lower()}_allocations.py')

        if args.force:
            print(f'Forcing overwrite of the {letter} allocation file')
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
                    #print(fn)
                    with new_data_file.open(mode='a') as f:
                        print(f'    ({int(minfreq)}, {int(maxfreq)}): ({amateur}, {fixed}, {mobile}, {broadcast}, {pa}, {sa}, {fn}),', file=f)
                    # print(int(minfreq), int(maxfreq), pa, sa, amateur, fixed, mobile, broadcast)
            write_footer()

#!/usr/bin/env python3

'''
Dev tool for building regional allocation data parsed from CSV exports of:
    http://www.grss-ieee.org/frequency_allocations.html
'''

import argparse
import csv
from pathlib import Path

from iso3166 import countries
from rf_info.countrymap import COUNTRY_MAP


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
COUNTRY_MAP_FILE = PROJECT_ROOT / 'rf_info' / 'countrymap.py'
DATA_DIR = PROJECT_ROOT / 'rf_info' / 'data'
SIZE_TO_TYPE = {
    635414: 'a',
    682975: 'b',
    660096: 'c',
}


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', '-f', action='store_true', help='Force overwrite')
    parser.add_argument('--list', '-l', action='store_true', help='List currently supported countries')
    parser.add_argument('--shortlist', '-sl', action='store_true', help='short country list for readme')
    parser.add_argument('--type', choices=('a', 'b', 'c'), help='allocation file type for unknown CSV sizes')
    parser.add_argument('--remove-input', action='store_true', help='delete source CSVs after successful processing')
    return parser.parse_args(argv)


def print_country_shortlist():
    clist = []
    for key in COUNTRY_MAP:
        clist.append('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))
    print(', '.join(clist))


def print_country_list():
    for key in COUNTRY_MAP:
        print('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))


def save_countrymap():
    with COUNTRY_MAP_FILE.open(mode='w') as f:
        print('COUNTRY_MAP = {}'.format(COUNTRY_MAP), file=f)


def check_countrymap(country, letter):
    country_code = country.alpha2.upper()
    if country_code in COUNTRY_MAP:
        if COUNTRY_MAP[country_code] == letter:
            print('[ {} ] already exists as [ {} ] in countrymap'.format(country_code, letter.upper()))
        else:
            print('[ {} ] exists but different [ {} ] -> [ {} ]'.format(country_code, COUNTRY_MAP[country_code].upper(), letter.upper()))
            COUNTRY_MAP.update({country_code: letter.lower()})
            save_countrymap()
    else:
        print('[ {} ] does not exist in countrymap. adding it.'.format(country_code))
        COUNTRY_MAP.update({country_code: letter.lower()})
        save_countrymap()


def parse_line(pa):
    newpa = []
    fixed = False
    mobile = False
    amateur = False
    broadcast = False
    satellite = False
    for a in pa:
        asp = a.strip().split(' ')
        for each in asp:
            if len(each) > 3:
                if each[0] == '(' and each[1].isnumeric() and each[2] == '.':
                    if each in asp:
                        e = each.split(',')
                        if len(e) > 1:
                            neach = ']['.join(e)
                        else:
                            neach = each
                        asp[asp.index(each)] = neach.replace('(', '[').replace(')', ']')

        if 'AMATEUR' in asp or 'Amateur' in asp or 'AMATEUR-SATELLITE' in asp or 'Amateur-Satellite' in asp:
            amateur = True
        if 'BROADCASTING' in asp or 'Broadcasting' in asp:
            broadcast = True
        if 'FIXED' in asp or 'Fixed' in asp:
            fixed = True
        if 'MOBILE' in asp or 'Mobile' in asp:
            mobile = True
        if 'SATELLITE' in asp or 'Satellite' in asp:
            satellite = True
        a = ' '.join(asp)
        if a.strip().lower() == 'fixed':
            fixed = True
        elif a.strip().lower() == 'mobile':
            mobile = True
        else:
            newpa.append(a.strip().title())
    if newpa and newpa[0] == '':
        newpa = []
    return newpa, amateur, fixed, mobile, broadcast, satellite


def parse_footnotes(footnote):
    footsplit = (footnote.replace('<b>', '').replace('</b>', '')).strip().split('<br>')
    newfoot = []
    for each in footsplit:
        if len(each) == 0:
            continue
        if each[0].isnumeric() and len(each) > 1 and each[1] == '.':
            for index, char in enumerate(each):
                if char == ':':
                    each = '[' + each
                    newfoot.append(each[:index + 1] + ']' + each[index + 1:])
                    break
            else:
                newfoot.append(str(each.strip()))
        else:
            newfoot.append(str(each.strip()))
    return newfoot


def write_header(new_data_file):
    with new_data_file.open(mode='w') as f:
        print('from rf_info.data.rangekeydict import RangeKeyDict', file=f)
        print('', file=f)
        print('ALLOCATIONS = RangeKeyDict([', file=f)


def write_footer(new_data_file):
    with new_data_file.open(mode='a') as f:
        print('])', file=f)


def determine_type(data_file, override):
    if override:
        return override
    csv_size = data_file.stat().st_size
    if csv_size not in SIZE_TO_TYPE:
        raise ValueError('Unknown allocation CSV size {}; pass --type a, b, or c'.format(csv_size))
    return SIZE_TO_TYPE[csv_size]


def parse_frequency_mhz(value):
    if value.isnumeric():
        return int(value)
    return float(value)


def process_file(data_file, args):
    try:
        country = countries.get(data_file.stem.title())
    except KeyError:
        print('Cannot determine country from filename {}'.format(data_file.stem))
        return

    letter = determine_type(data_file, args.type)
    print('{} [ {} ] is [ {} ] Type'.format(country.name, country.alpha2, letter.upper()))
    check_countrymap(country, letter)

    new_data_file = DATA_DIR / '{}_allocations.py'.format(letter.lower())
    if new_data_file.exists() and not args.force:
        print('Skipping {}; use --force to overwrite {}'.format(data_file, new_data_file))
        return

    write_header(new_data_file)
    with data_file.open() as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            minfreq = parse_frequency_mhz(row['Min (MHz)']) * 1000000
            maxfreq = parse_frequency_mhz(row['Max (MHz)']) * 1000000

            sa, amateura, fixeda, mobilea, broadcasta, sata = parse_line(row['Secondary Allocations'].split(', '))
            pa, amateurb, fixedb, mobileb, broadcastb, satb = parse_line(row['Primary Allocations'].split(', '))
            fixed = fixeda or fixedb
            mobile = mobilea or mobileb
            broadcast = broadcasta or broadcastb
            amateur = amateura or amateurb
            sat = sata or satb
            fn = parse_footnotes(row['Footnotes'])

            with new_data_file.open(mode='a') as f:
                print(
                    '    (({}, {}), ({}, {}, {}, {}, {}, {}, {}, {})),'.format(
                        int(minfreq),
                        int(maxfreq),
                        amateur,
                        fixed,
                        mobile,
                        broadcast,
                        sat,
                        repr(pa),
                        repr(sa),
                        repr(fn),
                    ),
                    file=f,
                )
    write_footer(new_data_file)

    if args.remove_input:
        data_file.unlink()


def main(argv=None):
    args = parse_args(argv)
    if args.shortlist:
        print_country_shortlist()
        return 0
    if args.list:
        print_country_list()
        return 0

    for data_file in BASE_DIR.iterdir():
        if data_file.suffix == '.csv':
            process_file(data_file, args)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

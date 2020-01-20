#!/usr/bin/env python3

import argparse
import json
import sys

import rf_info
from colorama import Fore, Style, deinit, init
from iso3166 import countries


def fkey(key):
    key = key.title().replace('_', ' ')
    if 'Itu' in key:
        skey = key.split(' ')
        key = 'ITU {}'.format(skey[1])
    if 'Nato' in key:
        key = 'NATO Band'
    return key


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    sys.tracebacklimit = 0  # Disable showing tracebacks
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(rf_info.__version__))
    parser.add_argument('frequency', nargs='?', help='radio frequency')
    parser.add_argument('unit', nargs='?', default='hz', help='hz, khz, mhz, ghz')
    parser.add_argument('country', nargs='?', default='us', help='us, ca, uk, jp, etc...')
    parser.add_argument('--nocolor', action='store_true', help='no color terminal output')
    parser.add_argument('--raw', action='store_true', help='raw output')
    parser.add_argument('--json', action='store_true', help='json output')
    parser.add_argument('--list', '-l', action='store_true', help='list all supported countries')
    parser.add_argument('--shortlist', '-sl', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    if not args.nocolor:
        KEYCOLOR = Style.BRIGHT + Fore.WHITE
        VALUECOLOR = Style.BRIGHT + Fore.YELLOW
        RESET = Style.RESET_ALL
        TRUECOLOR = Fore.GREEN
        FALSECOLOR = Style.BRIGHT + Fore.RED
        NOTESCOLOR = Fore.CYAN
        ALLOCATIONCOLOR = Style.BRIGHT + Fore.YELLOW
        init()
    else:
        KEYCOLOR = ''
        VALUECOLOR = ''
        RESET = ''
        TRUECOLOR = ''
        FALSECOLOR = ''
        NOTESCOLOR = ''
        ALLOCATIONCOLOR = ''

    if args.shortlist:
        from .data.countrymap import COUNTRY_MAP
        clist = []
        for key, value in COUNTRY_MAP.items():
            clist.append('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))
        print(', '.join(clist))
        exit(0)
    elif args.list:
        from .data.countrymap import COUNTRY_MAP
        for key, value in COUNTRY_MAP.items():
            print('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))
        exit(0)

    if args.frequency is None:
        raise ValueError('You must specify a frequency')

    frequency_object = rf_info.Frequency(str(args.frequency), unit=str(args.unit).lower(), country=str(args.country))
    frequency_dict = frequency_object.__dict__
    if not args.raw and not args.json:
        print(' ')
        for key, value in frequency_dict.items():
            if value is not None:

                if key == 'primary_allocation':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for each in value:
                            print('    {}{}{}'.format(ALLOCATIONCOLOR, each, RESET))

                elif key == 'secondary_allocation':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for each in value:
                            print('    {}{}{}'.format(ALLOCATIONCOLOR, each, RESET))

                elif key == 'allocation_notes':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for each in value:
                            print('    {}{}{}'.format(NOTESCOLOR, each, RESET))

                elif key == 'amateur_details':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for key, each in value.items():
                            print('    {}{}: {}{}{}'.format(KEYCOLOR, key.title(), VALUECOLOR, each, RESET))

                elif key == 'broadcasting_details':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for each in value:
                            print('    {}{}{}'.format(VALUECOLOR, each, RESET))

                elif key == 'services_details':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for each in value:
                            print('    {}{}{}'.format(VALUECOLOR, each, RESET))

                elif key == 'satellite_details':
                    if len(value) > 0:
                        print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                        for key, each in value.items():
                            print('    {}{}: {}{}{}'.format(KEYCOLOR, key.title(), VALUECOLOR, each, RESET))

                else:
                    if not value:
                        print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, FALSECOLOR, value, RESET))
                    elif isinstance(value, bool):
                        print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, TRUECOLOR, value, RESET))
                    else:
                        print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, VALUECOLOR, value, RESET))
        print(' ')

    elif not args.json:
        for key, value in frequency_dict.items():
            print('{}={}'.format(key, value))
    else:
        print(json.dumps(frequency_dict, indent=4, sort_keys=False))

    if not args.nocolor:
        deinit()

    return 0

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
    if 'Ieee' in key:
        skey = key.split(' ')
        key = 'IEEE {}'.format(skey[1])
    if 'Ism' in key:
        skey = key.split(' ')
        key = 'ISM {}'.format(skey[1])
    if 'Nato' in key:
        key = 'NATO Band'
    return key


def get_frequency_obj(frequency, unit, country):
    if frequency is None:
        raise ValueError('You must specify a frequency')
    return rf_info.Frequency(str(frequency), unit=str(unit).lower(), country=str(country))


def run_json(frequency_obj):
    for key, value in frequency_obj.__dict__.items():
        print('{}={}'.format(key, value))


def run_raw(frequency_obj):
    print(json.dumps(frequency_obj.__dict__, indent=4, sort_keys=False))


def run_shortlist():
    from .countrymap import COUNTRY_MAP
    clist = []
    for key, value in COUNTRY_MAP.items():
        clist.append('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))
    print(', '.join(clist))


def run_country_list():
    from .countrymap import COUNTRY_MAP
    for key, value in COUNTRY_MAP.items():
        print('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))


def verify_country(country):
    from .countrymap import COUNTRY_MAP
    if country.upper() not in COUNTRY_MAP:
        raise ValueError('Specified Country is Not Supported')


def run_output(frequency, unit, country):
    frequency_obj = get_frequency_obj(frequency, unit, country)
    frequency_dict = frequency_obj.__dict__
    print(' ')
    countryabbr = 'us'
    for key, value in frequency_dict.items():
        if value is not None:
            if key == 'country_abbr':
                countryabbr = value

            elif key == 'country_name':
                print('{}{}: {}{} ({}){}'.format(KEYCOLOR, 'Country', VALUECOLOR, value, countryabbr, RESET))

            elif key == 'primary_allocation':
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
                    # print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                    for key, each in value.items():
                        print('    {}{}: {}{}{}'.format(KEYCOLOR, key.title(), VALUECOLOR, each, RESET))

            elif key == 'broadcasting_details':
                if len(value) > 0:
                    # print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                    for each in value:
                        print('    {}{}{}'.format(VALUECOLOR, each, RESET))

            elif key == 'services_details':
                if len(value) > 0:
                    print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, VALUECOLOR, value, RESET))

            elif key == 'satellite_details':
                if len(value) > 0:
                    # print('{}{}{}:'.format(KEYCOLOR, fkey(key), RESET))
                    for key, each in value.items():
                        print('    {}{}: {}{}{}'.format(KEYCOLOR, key.title(), VALUECOLOR, each, RESET))

            elif key == 'ism_band':
                if len(value) > 0:
                    print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, TRUECOLOR, 'True', RESET))
                    for key, each in value.items():
                        print('    {}{}: {}{}{}'.format(KEYCOLOR, key.title(), VALUECOLOR, each, RESET))
                else:
                    print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, FALSECOLOR, 'False', RESET))

            else:
                if not value:
                    print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, FALSECOLOR, value, RESET))
                elif isinstance(value, bool):
                    print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, TRUECOLOR, value, RESET))
                else:
                    print('{}{}{}: {}{}{}'.format(KEYCOLOR, fkey(key), RESET, VALUECOLOR, value, RESET))
    print(' ')


def main(argv=None):
    global VALUECOLOR, KEYCOLOR, RESET, TRUECOLOR, FALSECOLOR, NOTESCOLOR, ALLOCATIONCOLOR
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(rf_info.__version__))
    mgroup = parser.add_mutually_exclusive_group()
    parser.add_argument('frequency', nargs='?', help='radio frequency')
    parser.add_argument('unit', nargs='?', default='hz', help='hz, khz, mhz, ghz')
    parser.add_argument('country', nargs='?', default='us', help='us, ca, uk, jp, etc...')
    mgroup.add_argument('-i', action='store', dest='interactive', metavar='country', help='interactive terminal input for <country>')
    parser.add_argument('--nocolor', action='store_true', help='no color terminal output')
    mgroup.add_argument('--raw', action='store_true', help='raw output')
    mgroup.add_argument('--json', action='store_true', help='json output')
    mgroup.add_argument('--list', action='store_true', help='list all supported countries')
    mgroup.add_argument('--shortlist', '-sl', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--debug', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    if not args.debug:
        sys.tracebacklimit = 0  # Disable showing tracebacks

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
        run_shortlist()
        return 0
    elif args.list:
        run_country_list()
        return 0
    elif args.json:
        run_json(get_frequency_obj(args.frequency, args.unit, args.country))
        return 0
    elif args.raw:
        run_raw(get_frequency_obj(args.frequency, args.unit, args.country))
        return 0
    elif args.interactive:
        verify_country(args.interactive)
        answer = ''
        unit = 'hz'
        while answer.lower() != 'quit' and answer.lower() != 'exit' and answer.lower() != 'q':
            answer = input("Frequency({})> ".format(args.interactive.upper()))
            if answer != '':
                if len(answer.split(' ')) > 1:
                    answer = answer.split(' ')[0]
                    unit = answer.split(' ')[1]
                try:
                    run_output(answer, unit, args.country)
                except Exception as e:
                    print('{}{}{}'.format(VALUECOLOR, e, RESET))

        print('Exiting.')
        return 0
    else:
        run_output(args.frequency, args.unit, args.country)
        return 0

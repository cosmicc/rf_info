#!/usr/bin/env python3

import argparse
import sys
import json

from colorama import Fore, Style, init, deinit
import rf_info


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    sys.tracebacklimit = 0  # Disable showing tracebacks
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(rf_info.__version__))
    parser.add_argument('frequency', action='store', help='radio frequency')
    parser.add_argument('unit', nargs='?', default='hz', help='hz, khz, mhz, ghz')
    parser.add_argument('country', nargs='?', default='us', help='us, ca, uk, jp, etc...')
    parser.add_argument('--nocolor', action='store_true', help='no color terminal output')
    parser.add_argument('--raw', action='store_true', help='raw output for parsing')
    parser.add_argument('--json', action='store_true', help='json output for parsing')
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

    frequency_object = rf_info.Frequency(str(args.frequency), unit=str(args.unit).lower(), country=str(args.country))
    frequency_dict = frequency_object.__dict__
    if not args.raw and not args.json:
        print(' ')
        for key, value in frequency_dict.items():
            if value is not None:

                if key == 'primary_allocation':
                    if len(value) > 0:
                        print(f'\n{KEYCOLOR}{key.title()}{RESET}:')
                        for each in value:
                            print(f'    {ALLOCATIONCOLOR}{each}{RESET}')

                elif key == 'secondary_allocation':
                    if len(value) > 0:
                        print(f'\n{KEYCOLOR}{key.title()}{RESET}:')
                        for each in value:
                            print(f'    {ALLOCATIONCOLOR}{each}{RESET}')

                elif key == 'allocation_notes':
                    if len(value) > 0:
                        print(f'\n{KEYCOLOR}{key.title()}{RESET}:')
                        for each in value:
                            print(f'    {NOTESCOLOR}{each}{RESET}\n')

                elif key == 'amateur_details':
                    if len(value) > 0:
                        print(f'{KEYCOLOR}{key.title()}{RESET}:')
                        for each in value:
                            print(f'    {VALUECOLOR}{each}{RESET}')
                else:
                    if not value:
                        print(f'{KEYCOLOR}{key.title()}{RESET}: {FALSECOLOR}{value}{RESET}')
                    elif isinstance(value, bool):
                        print(f'{KEYCOLOR}{key.title()}{RESET}: {TRUECOLOR}{value}{RESET}')
                    else:
                        print(f'{KEYCOLOR}{key.title()}{RESET}: {VALUECOLOR}{value}{RESET}')
        print(' ')

    elif not args.json:
        for key, value in frequency_dict.items():
            print(f'{key}={value}')
    else:
        print(json.dumps(frequency_dict, indent=4, sort_keys=False))

    if not args.nocolor:
        deinit()

    return 0

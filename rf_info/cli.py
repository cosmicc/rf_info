#!/usr/bin/env python3

import argparse
import json
import sys

import rf_info
from colorama import Fore, Style, init, deinit
from iso3166 import countries


def get_frequency_obj(frequency, unit, country):
    if frequency is None:
        raise ValueError('You must specify a frequency')
    return rf_info.Frequency(str(frequency), unit=str(unit).lower(), country=str(country))


def display_raw(frequency_obj):
    print(frequency_obj.__dict__)


def display_json(frequency_obj):
    print(json.dumps(frequency_obj.__dict__, indent=4, sort_keys=False))


def country_shortlist():
    from .countrymap import COUNTRY_MAP
    clist = []
    for key, value in COUNTRY_MAP.items():
        clist.append('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))
    print(', '.join(clist))


def country_list():
    from .countrymap import COUNTRY_MAP
    for key, value in COUNTRY_MAP.items():
        print('{} ({})'.format(countries.get(key).name, countries.get(key).alpha2))


def verify_country(country):
    from .countrymap import COUNTRY_MAP
    if country.upper() not in COUNTRY_MAP:
        raise ValueError('Specified Country is Not Supported')


def display_results(frequency, unit, country):
    frequency_obj = get_frequency_obj(frequency, unit, country)
    fd = frequency_obj
    print(' ')
    # DISPLAY
    print(' {}Display: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.display, RESET))
    # UNITS
    print(' {}Hz: {}{:,}{}'.format(KEYCOLOR, VALUECOLOR, fd.units['hz'], RESET))
    if fd.units['khz'].is_integer():
        print(' {}Khz: {}{:,}{}'.format(KEYCOLOR, VALUECOLOR, int(fd.units['khz']), RESET))
    else:
        print(' {}Khz: {}{:,g}{}'.format(KEYCOLOR, VALUECOLOR, fd.units['khz'], RESET))
    if fd.units['mhz'].is_integer():
        print(' {}Mhz: {}{:,}{}'.format(KEYCOLOR, VALUECOLOR, int(fd.units['mhz']), RESET))
    else:
        print(' {}Mhz: {}{:,g}{}'.format(KEYCOLOR, VALUECOLOR, fd.units['mhz'], RESET))
    if fd.units['ghz'].is_integer():
        print(' {}Ghz: {}{:,}{}'.format(KEYCOLOR, VALUECOLOR, int(fd.units['ghz']), RESET))
    else:
        print(' {}Ghz: {}{:,g}{}'.format(KEYCOLOR, VALUECOLOR, fd.units['ghz'], RESET))
    print(' {}Wavelength: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.wavelength, RESET))
    # ITU
    if fd.itu['number'] is not None:
        print(' {}ITU Band: {}{} - {} ({}){}'.format(KEYCOLOR, VALUECOLOR, fd.itu['number'], fd.itu['abbr'], fd.itu['band'], RESET))
    # IEEE    
    if fd.ieee['band'] is not None:
        print(' {}IEEE Band: {}{} ({}){}'.format(KEYCOLOR, VALUECOLOR, fd.ieee['band'], fd.ieee['description'], RESET))
    else:
        print(' {}IEEE Band: {}None{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # NATO    
    if fd.nato['band'] is not None:
        print(' {}NATO Band: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.nato['band'], RESET))
    else:
        print(' {}NATO Band: {}None{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # WAVEGUIDE    
    if fd.waveguide['band'] is not None:
        print(' {}Waveguide Band: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.waveguide['band'], RESET))
    else:
        print(' {}Waveguide Band: {}None{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # MICROWAVE    
    if fd.microwave['band'] is not None:
        print(' {}Microwave Band: {}{} ({}){}'.format(KEYCOLOR, VALUECOLOR, fd.microwave['band'], fd.microwave['allocation'], RESET))
    else:
        print(' {}Microwave Band: {}None{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    print(' {}Country: {}{} ({}){}'.format(KEYCOLOR, VALUECOLOR, fd.country['name'], fd.country['abbr'], RESET))
    # SERVICES
    if fd.services is not None:
        print(' {}Services: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.services, RESET))
    # BROADCASTING
    if fd.broadcasting['allocated']:
        if len(fd.broadcasting['details']) > 0:
            print(' {}Broadcasting: {}True {}({}){}'.format(KEYCOLOR, TRUECOLOR, VALUECOLOR, fd.broadcasting['details'], RESET))
        else:
            print(' {}Broadcasting: {}True{}'.format(KEYCOLOR, TRUECOLOR, RESET))
    else:
        print(' {}Broadcasting: {}False{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # WIFI
    if fd.wifi['allocated']:
        print(' {}Wifi: {}True{}'.format(KEYCOLOR, TRUECOLOR, RESET))
        print('   - {}{}{}'.format(VALUECOLOR, fd.wifi['details'], RESET))
    else:
        print(' {}Wifi: {}False{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # AMATEUR    
    if fd.amateur['allocated']:
        print(' {}Amateur: {}True{}'.format(KEYCOLOR, TRUECOLOR, RESET))
        if fd.amateur['modes'] is not None:
            print('   {}Modes: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.amateur['modes'], RESET))
            print('   {}License: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.amateur['license'], RESET))
            print('   {}Power: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.amateur['power'], RESET))
    else:
        print(' {}Amateur: {}False{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # SATELLITE    
    if fd.satellite['allocated']:
        print(' {}Satellite: {}True{}'.format(KEYCOLOR, TRUECOLOR, RESET))
        if fd.satellite['name'] is not None:
            print('   {}Name: {}{} [{}]{}'.format(KEYCOLOR, VALUECOLOR, fd.satellite['name'], fd.satellite['sat-id'], RESET))
            print('   {}Link: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.satellite['link'], RESET))
            print('   {}Modes: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.satellite['modes'], RESET))
            print('   {}Status: {}{}{}'.format(KEYCOLOR, VALUECOLOR, fd.satellite['status'], RESET))
    else:
        print(' {}Satellite: {}False{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # FIXED STATION    
    if fd.station['fixed']:
        print(' {}Fixed Station: {}True{}'.format(KEYCOLOR, TRUECOLOR, RESET))
    else:
        print(' {}Fixed Station: {}False{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # MOBILE STATION    
    if fd.station['mobile']:
        print(' {}Mobile Station: {}True{}'.format(KEYCOLOR, TRUECOLOR, RESET))
    else:
        print(' {}Mobile Station: {}False{}'.format(KEYCOLOR, FALSECOLOR, RESET))
    # PRIMARY ALLOCATION    
    if fd.ieee_allocation['primary']:
        if len(fd.ieee_allocation['primary']) > 0:
            print(' {}Primary Allocation:{}'.format(KEYCOLOR, RESET))
            for each in fd.ieee_allocation['primary']:
                print('   - {}{}{}'.format(ALLOCATIONCOLOR, each, RESET))
    # SECONDARY ALLOCATION            
    if fd.ieee_allocation['secondary']:
        if len(fd.ieee_allocation['secondary']) > 0:
            print(' {}Secondary Allocation:{}'.format(KEYCOLOR, RESET))
            for each in fd.ieee_allocation['secondary']:
                print('   - {}{}{}'.format(ALLOCATIONCOLOR, each, RESET))
    # ALLOCATION_NOTES
    if fd.ieee_allocation['notes']:
        if len(fd.ieee_allocation['notes']) > 0:
            print(' {}Allocation Notes: {}'.format(KEYCOLOR, RESET))
            for each in fd.ieee_allocation['notes']:
                print('   - {}{}{}'.format(NOTESCOLOR, each, RESET))


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
        country_shortlist()
        return 0
    elif args.list:
        country_list()
        return 0
    elif args.json:
        display_json(get_frequency_obj(args.frequency, args.unit, args.country))
        return 0
    elif args.raw:
        display_raw(get_frequency_obj(args.frequency, args.unit, args.country))
        return 0
    elif args.interactive:
        verify_country(args.interactive)
        answer = ''
        unit = 'hz'
        print('Enter q to quit')
        while answer.lower() != 'quit' and answer.lower() != 'exit' and answer.lower() != 'q':
            answer = input("Frequency ({})> ".format(args.interactive.lower()))
            if answer != '' and answer.lower() != 'quit' and answer.lower() != 'exit' and answer.lower() != 'q':
                if len(answer.split(' ')) > 1:
                    answer = answer.split(' ')[0]
                    unit = answer.split(' ')[1]
                try:
                    display_results(answer, unit, args.country)
                except Exception as e:
                    print('{}{}{}'.format(VALUECOLOR, e, RESET))

        print('Exiting.')
        return 0
    else:
        if args.country:
            verify_country(args.country)
        display_results(args.frequency, args.unit, args.country)
        return 0


if __name__ == '__main__':
    main()

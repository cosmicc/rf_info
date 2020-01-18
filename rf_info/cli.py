#!/usr/bin/env python3

import argparse
import sys

import rf_info


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    sys.tracebacklimit = 0  # Disable showing tracebacks
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version', version='%(prog)s {}'.format(rf_info.__version__))
    parser.add_argument('frequency', action='store', help='radio frequency')
    parser.add_argument('unit', nargs='?', default='hz', help='hz, khz, mhz, ghz')
    parser.add_argument('country', nargs='?', default='us', help='us, ca, uk, jp, etc...')
    parser.add_argument('--raw', '-r', action='store_true', help='includes raw output (for debugging)')
    args = parser.parse_args(argv)

    result = rf_info.Frequency(str(args.frequency), str(args.unit).lower()).__dict__
    print(' ')
    for key, value in result.items():
        if key.lower() == 'band_use':
            if len(value) == 0:
                print('%s: %s' % (key.title(), 'Unknown'))
            else:
                newval = ''
                loop = 0
                for each in value:
                    if loop == 0:
                        loop += 1
                        newval = each
                    else:
                        newval = f'{newval}, {each}'
                print('%s: %s' % (key.title(), newval))
        else:
            if value is not None:
                print('%s: %s' % (key.title(), value))
    print(' ')
    if args.raw:
        print('Raw:')
        for key, value in result.items():
            print(f'{key}: {value}')
        print(' ')
        print(result)
        print(' ')
    return 0

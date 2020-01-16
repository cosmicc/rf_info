#!/usr/bin/env python3

import argparse
import sys

import rf_info


def remove_all_butfirst(s, substr):
    try:
        first_occurrence = s.index(substr) + len(substr)
    except ValueError:
        return s
    else:
        return s[:first_occurrence] + s[first_occurrence:].replace(substr, "")


def main():
    sys.tracebacklimit = 0  # Disable showing tracebacks
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version', version='%(prog)s {}'.format(rf_info.__version__))
    parser.add_argument('frequency', action='store', help='Radio Frequency to get information about')
    parser.add_argument('--raw', '-r', action='store_true', help='Includes raw output (for debugging)')
    parser.add_argument('suffix', nargs='?', default='hz', help='Hz, Khz, Mhz, Ghz')
    args = parser.parse_args()

    result = rf_info.Frequency(str(args.frequency), args.suffix).__dict__
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

        elif key.lower() == 'hz' or key.lower() == 'khz' or key.lower() == 'mhz' or key.lower() == 'ghz':
            print('%s: %s' % (key.title(), value[0]))
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


if __name__ == "__main__":
    sys.exit(main())

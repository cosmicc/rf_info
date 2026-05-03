#!/usr/bin/env python3

'''
Dev tool for building satellite data parsed from:
    https://www.ne.jp/asahi/hamradio/je9pel/satslist.csv
'''

import argparse
import csv
import difflib
import re
import shutil
from pathlib import Path

import requests
from rf_info.rf_info import parse_freq


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
DATA_FILE = PROJECT_ROOT / 'rf_info' / 'data' / 'satellites.py'
TEMP_FILE = BASE_DIR / 'satslist.tmp'
DOWNLOAD_FILE = BASE_DIR / 'satslist.csv'
SOURCE_URLS = (
    'https://www.ne.jp/asahi/hamradio/je9pel/satslist.csv',
    'http://www.ne.jp/asahi/hamradio/je9pel/satslist.csv',
)
INACTIVE_STATES = {
    'inactive',
    're-entered',
    'failure',
    'non-operational',
    'launch failed',
}
STATE_VALUES = INACTIVE_STATES | {
    'active',
    'deep space',
    'to be launched',
    'unknown',
    'weather sat',
}


def file_diff(file1, file2):
    old_lines = file2.read_text().splitlines()
    new_lines = file1.read_text().splitlines()
    diff = list(difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=str(file2),
        tofile=str(file1),
        lineterm='',
    ))
    if diff:
        print('\n'.join(diff))
        return True
    return False


def download_file(target):
    last_error = None
    for url in SOURCE_URLS:
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as error:
            last_error = error
            continue
        target.write_bytes(response.content)
        return url
    raise RuntimeError('Error downloading satellite data: {}'.format(last_error))


def write_header(file):
    with file.open(mode='w') as f:
        print('from rf_info.data.rangekeydict import RangeKeyDict', file=f)
        print('', file=f)
        print('SATELLITES = RangeKeyDict([', file=f)


def write_footer(file):
    with file.open(mode='a') as f:
        print('])', file=f)


def write_line(minfreq, maxfreq, name, satid, mode, callsign, state, link):
    values = (
        name.strip(),
        satid.strip(),
        link.capitalize(),
        mode.strip(),
        callsign.strip(),
        state,
    )
    with TEMP_FILE.open(mode='a') as f:
        print('    (({}, {}), {}),'.format(int(minfreq), int(maxfreq), repr(values)), file=f)


def validate_freq(freq):
    freq = freq.strip()
    if not freq:
        return None

    unit = 'mhz'
    lowered = freq.lower()
    if 'x' in lowered or '~' in freq or not freq[0].isnumeric():
        return None

    freq = freq.replace('*', '')
    if '(' in freq:
        freq = freq.split('(')[0]
    if re.fullmatch(r'\d+\s+\d+', freq):
        freq = re.sub(r'\s+', '.', freq, count=1)
    if 'ghz' in lowered:
        freq = re.sub('ghz', '', freq, flags=re.IGNORECASE)
        unit = 'ghz'
    else:
        freq = re.sub('mhz', '', freq, flags=re.IGNORECASE)

    try:
        return parse_freq(freq.strip(), unit)
    except ValueError:
        return None


def iter_frequencies(raw_value):
    if not raw_value:
        return

    for part in raw_value.split('/'):
        part = part.strip()
        if '-' in part:
            low, high = part.split('-', 1)
            minfreq = validate_freq(low)
            maxfreq = validate_freq(high)
            if minfreq and maxfreq:
                if minfreq > maxfreq:
                    minfreq, maxfreq = maxfreq, minfreq
                yield minfreq, maxfreq + 1
        else:
            minfreq = validate_freq(part)
            if minfreq:
                yield minfreq, minfreq + 1


def add_header_to_download(file):
    csv_header = 'name;sat-id;uplink;downlink;beacon;mode;callsign;state\n'
    lines = file.read_text().splitlines(True)
    if lines and lines[0].startswith('name;'):
        return
    file.write_text(csv_header + ''.join(lines))


def normalize_row(row):
    normalized = {
        key: (value or '').strip()
        for key, value in row.items()
        if key is not None
    }
    state = normalized.get('state', '').lower()

    # A small number of upstream rows have the mode and callsign columns
    # shifted right after a duplicated beacon frequency.
    shifted_mode = validate_freq(normalized.get('mode', '')) is not None
    if shifted_mode and normalized.get('callsign') and state in STATE_VALUES:
        normalized['mode'] = normalized['callsign']
        normalized['callsign'] = ''

    return normalized


def build_data_file(download, temp_file):
    write_header(temp_file)
    add_header_to_download(download)

    with download.open() as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            row = normalize_row(row)
            state_value = (row.get('state') or '').strip()
            if not state_value or state_value.lower() in INACTIVE_STATES:
                continue

            line_count += 1
            state = state_value.title()
            for minfreq, maxfreq in iter_frequencies(row.get('uplink')):
                write_line(minfreq, maxfreq, row.get('name', ''), row.get('sat-id', ''), row.get('mode', ''), row.get('callsign', ''), state, 'uplink')
            for minfreq, maxfreq in iter_frequencies(row.get('downlink')):
                write_line(minfreq, maxfreq, row.get('name', ''), row.get('sat-id', ''), row.get('mode', ''), row.get('callsign', ''), state, 'downlink')
            for minfreq, maxfreq in iter_frequencies(row.get('beacon')):
                write_line(minfreq, maxfreq, row.get('name', ''), row.get('sat-id', ''), row.get('mode', ''), row.get('callsign', ''), state, 'beacon')

    write_footer(temp_file)
    return line_count


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--yes', '-y', action='store_true', help='replace data file without prompting')
    args = parser.parse_args(argv)

    print('')
    source_url = download_file(DOWNLOAD_FILE)
    print('Satellite data downloaded from {}'.format(source_url))

    try:
        line_count = build_data_file(DOWNLOAD_FILE, TEMP_FILE)
        print('{} Entries'.format(line_count))

        if not DATA_FILE.exists():
            if not TEMP_FILE.is_file():
                raise RuntimeError('Temporary satellite data file was not created')
            shutil.copy(str(TEMP_FILE), str(DATA_FILE))
            print('Replaced: {}'.format(DATA_FILE))
        else:
            different = file_diff(TEMP_FILE, DATA_FILE)
            if different:
                if args.yes:
                    answer = 'y'
                else:
                    answer = input('Replace Data File? {y/N]} ')
                if answer.lower() == 'y':
                    shutil.copy(str(TEMP_FILE), str(DATA_FILE))
                    print('Replaced: {}'.format(DATA_FILE))
                else:
                    print('Not saving changes.')
            else:
                print('No changes to save')
    finally:
        if TEMP_FILE.exists():
            TEMP_FILE.unlink()
        if DOWNLOAD_FILE.exists():
            DOWNLOAD_FILE.unlink()

    print('Complete')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

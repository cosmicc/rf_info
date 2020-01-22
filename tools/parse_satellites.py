#!/usr/bin/env python3

'''
Dev tool for building country allocation files data parsed from:
    http://www.ne.jp/asahi/hamradio/je9pel/satslist.csv

'''

import argparse
import csv
import shutil
from pathlib import Path

import requests
from rf_info.rf_info import parse_freq

parser = argparse.ArgumentParser()
args = parser.parse_args()

data_file = Path('../rf_info/data/satellites.py')
temp_file = Path('./satslist.tmp')
dl_file = Path('./satslist.csv')


def diff(file1, file2):
    diffr = False
    f1 = open(str(file1), "r")
    f2 = open(str(file2), "r")
    for line1 in f1:
        for line2 in f2:
            if line1 == line2:
                pass
            else:
                print(f'{line1}{line2}')
                diffr = True
            break
    f1.close()
    f2.close()
    return diffr


def download_file():
    fname = 'satslist.csv'
    url = 'http://www.ne.jp/asahi/hamradio/je9pel/' + fname
    try:
        r = requests.get(url)
    except:
        print('Error downloading data {}'.format(url))
        exit(1)
    else:
        open(fname, 'wb').write(r.content)
        print('Satellite data downloaded')


def parse_line(pa):
    newpa = []
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


def write_header(file):
    with file.open(mode='w') as f:
        print('from rf_info.data.rangekeydict import RangeKeyDict', file=f)
        print(' ', file=f)
        print('SATELLITES = RangeKeyDict({', file=f)


def write_footer(file):
    with file.open(mode='a') as f:
        print('})', file=f)


def write_line(minfreq, maxfreq, name, satid, mode, callsign, state, link):
    with temp_file.open(mode='a') as f:
        print(f'    ({int(minfreq)}, {int(maxfreq)}): ("{name}", "{satid}", "{link.capitalize()}", "{mode}", "{callsign}", "{state}"),', file=f)


def validate_freq(freq):
    valid = True
    freq = freq.strip()
    unit = 'mhz'
    if 'x' in freq:
        valid = False
    if '~' in freq:
        valid = False
    if not freq[0].isnumeric():
        valid = False
    if '*' in freq:
        freq = freq.replace('*', '')
    if '(' in freq:
        freq = freq.split('(')[0]
    if 'GHz' in freq:
        freq = freq.split('GHz')[0]
        unit = 'ghz'
    if valid:
        return parse_freq(freq, unit)
    else:
        return False


print(' ')
download_file()

if not dl_file.exists():
    print('Cannot find satslist.csv file to process')
    exit(1)

write_header(temp_file)

csv_header = 'name;sat-id;uplink;downlink;beacon;mode;callsign;state\n'


with open(str(dl_file), "r+") as file:
    lines = file.readlines()
    lines.insert(0, csv_header)
    file.seek(0)
    file.writelines(lines)


with open(str(dl_file)) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if row['state'] != 'inactive' and row['state'] != 're-entered' and row['state'] != 'failure' and row['state'] != 'Non-Operational' and row['state'] != 'Launch failed':
            line_count += 1
            if row['uplink'] is not None:

                if '/' in row['uplink']:
                    usplit = row['uplink'].split('/')
                    for each in usplit:
                        if '-' in each:
                            nusplit = each.split('-')
                            minfreq = validate_freq(nusplit[0])
                            maxfreq = validate_freq(nusplit[1])
                            if minfreq and maxfreq:
                                write_line(minfreq, maxfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'uplink')
                        else:
                            minfreq = validate_freq(each)
                            if minfreq:
                                write_line(minfreq, minfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'uplink')

                elif '-' in row['uplink']:
                    usplit = row['uplink'].split('-')
                    minfreq = validate_freq(usplit[0])
                    maxfreq = validate_freq(usplit[1])
                    if minfreq and maxfreq:
                        write_line(minfreq, maxfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'uplink')

                elif '.' in row['uplink'] or row['uplink'].isnumeric():
                    minfreq = validate_freq(row['uplink'])
                    if minfreq:
                        write_line(minfreq, minfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'uplink')
            if row['downlink'] is not None:

                if '/' in row['downlink']:
                    usplit = row['downlink'].split('/')
                    for each in usplit:
                        if '-' in each:
                            nusplit = each.split('-')
                            minfreq = validate_freq(nusplit[0])
                            maxfreq = validate_freq(nusplit[1])
                            if minfreq and maxfreq:
                                write_line(minfreq, maxfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'downlink')
                        else:
                            minfreq = validate_freq(each)
                            if minfreq:
                                write_line(minfreq, minfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'downlink')

                elif '-' in row['downlink']:
                    usplit = row['downlink'].split('-')
                    minfreq = validate_freq(usplit[0])
                    maxfreq = validate_freq(usplit[1])
                    if minfreq and maxfreq:
                        write_line(minfreq, maxfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'downlink')

                elif '.' in row['downlink'] or row['downlink'].isnumeric():
                    if 'x' not in row['downlink']:
                        minfreq = validate_freq(row['downlink'])
                        if minfreq:
                            write_line(minfreq, minfreq + 1, row['name'], row['sat-id'], row['mode'], row['callsign'], row['state'], 'downlink')

write_footer(temp_file)
print(f'{line_count} Entries')

if not data_file.exists():
    assert temp_file.is_file()
    shutil.copy(str(temp_file), str(data_file))
    print(f'Replaced: {str(data_file)}')
else:
    diffr = diff(temp_file, data_file)
    if diffr:
        answer = input("Replace Data File? {y/N]} ")
        if answer.lower() == 'y':
            shutil.copy(str(temp_file), str(data_file))
            print(f'Replaced: {str(data_file)}')
        else:
            print('Not saving changes.')
    else:
        print('No changes to save')

temp_file.unlink()
if dl_file.exists():
    download_file.unlink()
    pass

print('Complete')

#!/usr/bin/env python3

import pytest
from rf_info import cli
from hypothesis import given, settings
from hypothesis.strategies import integers

MIN = 1
MAX = 999999999999
TEST_UNITS = (
             ('137100000', 'Hz', 'us', '137.100.000'),
             ('1,000,000', 'hz', '', '1.000.000'),
             ('1000', 'HZ', 'GB', '1.000'),
             ('142.233', 'khz', 'JP', '142.233'),
             ('3542.23', 'mhz', 'CA', '3.542.230.000'),
             ('988,232.000', 'HZ', 'US', '988.232.000'),
             ('12,000.000', '', '', '12.000.000'),
             ('1', 'ghz', 'Us', '1.000.000.000'),
             ('.012', 'GHZ', 'uS', '12.000.000'),
             ('.001', 'Mhz', 'es', '1.000'),
             ('10', 'gHZ', 'ES', '10.000.000.000'),
             ('300', 'mhZ', 'MX', '300.000.000'),
             ('2.455.234.113', 'hz', 'us', '2.455.234.113'),
)


def test_out_of_range():
    with pytest.raises(Exception) as e:
        freq = MAX + 1
        assert cli.main([str(freq)])
    assert str(e.value) == "Frequency Out of Range"

    with pytest.raises(Exception) as e:
        freq = -234
        assert cli.main([str(freq)])
    assert str(e.value) == "Invalid Frequency Specified"


def test_invalids():
    template = '{0:20s} | {1:2s}'
    print(' ')
    print(template.format('FREQUENCY', '=='))
    with pytest.raises(Exception) as e:
        freq = '1i89'
        print(template.format(str(freq), '--'))
        assert cli.main([str(freq)])
    assert str(e.value) == "Invalid Frequency Specified"

    with pytest.raises(Exception) as e:
        freq = ['189', 'jk']
        print(template.format(str(freq), '--'))
        assert cli.main([freq[0], freq[1]])
    assert str(e.value) == "Invalid Unit Specified"


def test_cli():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'units', '=='))

    for (freq, unit, country, expected) in TEST_UNITS:

        exit_status = cli.main(['123', '--raw'])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), '--raw', ok))
        assert exit_status == 0

        exit_status = cli.main(['144.100.000', '--json'])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), '--json', ok))
        assert exit_status == 0

        exit_status = cli.main(['123', '--nocolor'])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), '--nocolor', ok))
        assert exit_status == 0

        exit_status = cli.main(['--shortlist'])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), '--json', ok))
        assert exit_status == 0

        exit_status = cli.main(['--list'])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), '--json', ok))
        assert exit_status == 0

        exit_status = cli.main([str(freq), unit, country])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), unit, ok))
        assert exit_status == 0


def test_interactive():
    input_values = ['1', 'quit']
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    cli.input = mock_input
    cli.print = lambda s :output.append(s)
    cli.main(['-i', 'us'])
    assert output == [
                       'Enter q to quit',
                       'Frequency (us)> ',
                       ' ',
                       ' \x1b[1m\x1b[37mDisplay: \x1b[1m\x1b[33m000.000.001\x1b[0m',
                       ' \x1b[1m\x1b[37mHz: \x1b[1m\x1b[33m1\x1b[0m',
                       ' \x1b[1m\x1b[37mKhz: \x1b[1m\x1b[33m0.001\x1b[0m',
                       ' \x1b[1m\x1b[37mMhz: \x1b[1m\x1b[33m1e-06\x1b[0m',
                       ' \x1b[1m\x1b[37mGhz: \x1b[1m\x1b[33m1e-09\x1b[0m',
                       ' \x1b[1m\x1b[37mWavelength: \x1b[1m\x1b[33m300,000,000m\x1b[0m',
                       ' \x1b[1m\x1b[37mITU Band: \x1b[1m\x1b[33m1 - ELF (Extremely Low '
                       'Frequency)\x1b[0m',
                       ' \x1b[1m\x1b[37mIEEE Band: \x1b[1m\x1b[31mNone\x1b[0m',
                       ' \x1b[1m\x1b[37mNATO Band: \x1b[1m\x1b[33mA\x1b[0m',
                       ' \x1b[1m\x1b[37mWaveguide Band: \x1b[1m\x1b[31mNone\x1b[0m',
                       ' \x1b[1m\x1b[37mMicrowave Band: \x1b[1m\x1b[31mNone\x1b[0m',
                       ' \x1b[1m\x1b[37mCountry: \x1b[1m\x1b[33mUnited States of America (US)\x1b[0m',
                       ' \x1b[1m\x1b[37mBroadcasting: \x1b[1m\x1b[31mFalse\x1b[0m',
                       ' \x1b[1m\x1b[37mWifi: \x1b[1m\x1b[31mFalse\x1b[0m',
                       ' \x1b[1m\x1b[37mAmateur: \x1b[1m\x1b[31mFalse\x1b[0m',
                       ' \x1b[1m\x1b[37mSatellite: \x1b[1m\x1b[31mFalse\x1b[0m',
                       ' \x1b[1m\x1b[37mFixed Station: \x1b[1m\x1b[31mFalse\x1b[0m',
                       ' \x1b[1m\x1b[37mMobile Station: \x1b[1m\x1b[31mFalse\x1b[0m',
                       ' \x1b[1m\x1b[37mPrimary Allocation:\x1b[0m',
                       '   - \x1b[1m\x1b[33m(Not Allocated)\x1b[0m',
                       ' \x1b[1m\x1b[37mAllocation Notes: \x1b[0m',
                       '   - \x1b[36m[5.53]: Administrations authorizing the use of frequencies '
                       'below 8.3 kHz shall ensure that no harmful interference is caused to '
                       'services to which the bands above 8.3 kHz are allocated. (WRC-12)\x1b[0m',
                       '   - \x1b[36m[5.54]: Administrations conducting scientific research using '
                       'frequencies below 8.3 kHz are urged to advise other administrations that may '
                       'be concerned in order that such research may be afforded all practicable '
                       'protection from harmful interference. (WRC-12)\x1b[0m',
                       'Frequency (us)> ',
                       'Exiting.',
                     ]


@settings(deadline=300, max_examples=50)
@given(integers(min_value=MIN, max_value=MAX))
def test_hypothesis(a):
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'units', '=='))
    exit_status = cli.main([str(a)])
    ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
    print(template.format(str(a), 'hz', ok))
    assert exit_status == 0

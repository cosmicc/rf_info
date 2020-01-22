#!/usr/bin/env python3

import pytest
from rf_info import cli

MAX = 999999999999
RAND_TESTS = 500
TEST_UNITS = (
             ('144.100.000', 'Hz', 'us', '144.100.000'),
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

        exit_status = cli.main([str(freq), unit, country])
        ok = 'OK' if exit_status == 0 else 'XX ({})'.format(exit_status)
        print(template.format(str(freq), unit, ok))
        assert exit_status == 0

#!/usr/bin/env python3

import pytest
from rf_info import cli

MAX = 999999999999


TEST_SERVICES = (
                ('462562500', 'General Mobile Radio Service (GMRS)'),
)

TEST_BROADCAST = (
                 ('89.900.000', 'FM Radio'),
                 ('155.500', 'Longwave AM Radio International'),
                 ('55.500.000', 'VHF Television'),
                 ('510.000.000', 'UHF Television'),
)

TEST_IEEE = (
            ('1.525.500.000', 'L'),
            ('17.155.000.000', 'Ku'),
            ('34.567.121.000', 'Ka'),
            ('105.157.100.000', 'W'),
)

TEST_BANDTYPE = (
                ('132.000.000', 'Air Band'),
                ('166.580.000', 'Marine VHF'),
                ('27.405.000', 'CB'),
                ('462.562.500', 'GMRS'),
)

TEST_DISPLAY = (
               ('132.158.000', '132.158.000'),
               ('1,000,000', '1.000.000'),
               (1000, '1.000'),
               (142.233, '142.233'),
               (3542.23, '354.223'),
               ('988,232.000', '988.232.000'),
               ('12,000.000', '12.000.000'),
               ('1', '1'),
               ('.012', '12'),
               (.001, '1'),
)

TEST_UNITS = (
             ('132.158.000', 'Hz', '132.158.000'),
             ('1,000,000', '', '1.000.000'),
             ('1000', 'HZ', '1.000'),
             ('142.233', 'khz', '142.233'),
             ('3542.23', 'mhz', '3.542.230.000'),
             ('988,232.000', 'HZ', '988.232.000'),
             ('12,000.000', '', '12.000.000'),
             ('1', 'ghz', '1.000.000.000'),
             ('.012', 'GHZ', '12.000.000'),
             ('.001', 'Mhz', '1.000'),
             ('10', 'gHZ', '10.000.000.000'),
             ('300', 'mhZ', '300.000.000'),
)


RAND_TESTS = 500


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
    print(template.format('FREQUENCY', 'suffix', '=='))
    for (freq, unit, expected) in TEST_UNITS:
        exit_status = cli.main([str(freq), unit])
        ok = 'OK' if exit_status == 0 else f'XX ({exit_status})'
        print(template.format(str(freq), unit, ok))
        assert exit_status == 0
    exit_status = cli.main(['123', '-r'])
    ok = 'OK' if exit_status == 0 else f'XX ({exit_status})'
    print(template.format(str(freq), '-r', ok))
    assert exit_status == 0

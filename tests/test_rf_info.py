#!/usr/bin/env python3

import os
import pytest
from rf_info import rf_info
from random import randint
from rf_info import cli
from hypothesis import given, assume
from hypothesis.strategies import integers

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
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Frequency Out of Range"

    with pytest.raises(Exception) as e:
        freq = -234
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Invalid Frequency Specified"


def test_tiny_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1, 9999)
        result = rf_info.Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu_abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_small_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(10000, 999999)
        result = rf_info.Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu_abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_medium_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1000000, MAX)
        result = rf_info.Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu_abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_large_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1000000000, MAX)
        result = rf_info.Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu_abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_types():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'TYPE', '=='))

    result = rf_info.Frequency('1')
    assert isinstance(result.info(), dict)

    for (freq, expected) in TEST_DISPLAY:
        result = rf_info.Frequency(freq).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(freq), f'{type(freq)}', ok))
        assert isinstance(result, dict)

    with pytest.raises(Exception) as e:
        freq = [1, 2, 3]
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = (1, 2, 3)
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = True
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = {'freq': 123}
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"


def test_invalids():
    template = '{0:20s} | {1:2s}'
    print(' ')
    print(template.format('FREQUENCY', '=='))
    with pytest.raises(Exception) as e:
        freq = '1i89'
        print(template.format(str(freq), '--'))
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Invalid Frequency Specified"

    with pytest.raises(Exception) as e:
        freq = ['189', 'jk']
        print(template.format(str(freq), '--'))
        assert rf_info.Frequency(freq[0], freq[1])
    assert str(e.value) == "Invalid Unit Specified"


def test_dial():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'DISPLAY', '=='))
    for (freq, expected) in TEST_DISPLAY:
        result = rf_info.Frequency(freq)
        ok = 'OK' if result.display == expected else 'XX'
        print(template.format(str(freq), str(result.display), ok))
        assert result.display == expected


def test_ieee():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'IEEE', '=='))
    for (f, expected) in TEST_IEEE:
        result = rf_info.Frequency(f)
        ok = 'OK' if result.ieee_band == expected else 'XX'
        print(template.format(str(f), str(result.ieee_band), ok))
        assert result.ieee_band == expected


def test_band_use():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'USE', '=='))
    for (f, expected) in TEST_BROADCAST:
        result = rf_info.Frequency(f)
        ok = 'OK' if expected in result.band_use else 'XX'
        print(template.format(str(f), str(result.band_use), ok))
        assert expected in result.band_use


def test_services():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'SERVICE', '=='))
    for (f, expected) in TEST_SERVICES:
        result = rf_info.Frequency(f)
        ok = 'OK' if expected in result.band_use else 'XX'
        print(template.format(str(f), str(result.band_use), ok))
        assert expected in result.band_use


def test_units():
    template = '{0:20s} | {1:20s} | {3:20s} | {3:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'UNIT', 'RESULT', '=='))
    for (freq, unit, expected) in TEST_UNITS:
        result = rf_info.Frequency(freq, unit)
        ok = 'OK' if result.display == expected else 'XX'
        print(template.format(str(freq), unit, result.display, ok))
        assert result.display == expected


@given(integers(min_value=1, max_value=MAX))
def test_integers(a):
    result = rf_info.Frequency(a)
    assert isinstance(result.__dict__, dict)
    assert result.hz[1] == a
    assert result.khz[1] == a / 1000
    assert result.mhz[1] == a / 1000000
    assert result.ghz[1] == a / 1000000000


def test_cli():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'suffix', '=='))
    for (freq, unit, expected) in TEST_UNITS:
        exit_status = os.system(f'rf-info {freq} {unit} > /dev/null')
        ok = 'OK' if exit_status == 0 else f'XX ({exit_status})'
        print(template.format(str(freq), unit, ok))
        assert exit_status == 0

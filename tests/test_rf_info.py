#!/usr/bin/env python3

from random import randint

import pytest
from hypothesis import given
from hypothesis.strategies import integers
from rf_info import Frequency

MIN = 1
MAX = 999999999999
RAND_TESTS = 500

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
               ('1,000,000', '001.000.000'),
               (1000, '000.001.000'),
               (142.233, '000.142.233'),
               (3542.23, '000.354.223'),
               ('988,232.000', '988.232.000'),
               ('12,000.000', '012.000.000'),
               ('1', '000.000.001'),
               ('.012', '000.000.012'),
               (.001, '000.000.001'),
)

TEST_UNITS = (
             ('144.100.000', 'Hz', '144.100.000'),
             ('132.158.000', 'Hz', '132.158.000'),
             ('1,000,000', '', '001.000.000'),
             ('1000', 'HZ', '000.001.000'),
             ('142.233', 'khz', '000.142.233'),
             ('3542.23', 'mhz', '3.542.230.000'),
             ('988,232.000', 'HZ', '988.232.000'),
             ('12,000.000', '', '012.000.000'),
             ('1', 'ghz', '1.000.000.000'),
             ('.012', 'GHZ', '012.000.000'),
             ('.001', 'Mhz', '000.001.000'),
             ('10', 'gHZ', '10.000.000.000'),
             ('300', 'mhZ', '300.000.000'),
)


def test_out_of_range():
    with pytest.raises(Exception) as e:
        freq = MAX + 1
        assert Frequency(freq)
    assert str(e.value) == "Frequency Out of Range"

    with pytest.raises(Exception) as e:
        freq = -234
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Specified"


def test_tiny_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1, 9999)
        result = Frequency(random).__dict__
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
        random = randint(10_000, 999_999)
        result = Frequency(random).__dict__
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
        random = randint(1_000_000, MAX)
        result = Frequency(random).__dict__
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
        random = randint(1_000_000_000, MAX)
        result = Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu_abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_types():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'TYPE', '=='))

    for (freq, expected) in TEST_DISPLAY:
        result = Frequency(freq).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(freq), f'{type(freq)}', ok))
        assert isinstance(result, dict)

    with pytest.raises(Exception) as e:
        freq = [1, 2, 3]
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = (1, 2, 3)
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = True
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = {'freq': 123}
        print(template.format(str(freq), f'{type(freq)}', '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"


def test_invalids():
    template = '{0:20s} | {1:2s}'
    print(' ')
    print(template.format('FREQUENCY', '=='))
    with pytest.raises(Exception) as e:
        freq = '1i89'
        print(template.format(str(freq), '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Specified"

    with pytest.raises(Exception) as e:
        freq = ['189', 'jk']
        print(template.format(str(freq), '--'))
        assert Frequency(freq[0], freq[1])
    assert str(e.value) == "Invalid Unit Specified"


def test_dial():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'DISPLAY', '=='))
    for (freq, expected) in TEST_DISPLAY:
        result = Frequency(freq)
        ok = 'OK' if result.display == expected else 'XX'
        print(template.format(str(freq), str(result.display), ok))
        assert result.display == expected


def test_ieee():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'IEEE', '=='))
    for (f, expected) in TEST_IEEE:
        result = Frequency(f)
        ok = 'OK' if result.ieee_band == expected else 'XX'
        print(template.format(str(f), str(result.ieee_band), ok))
        assert result.ieee_band == expected


def test_band_use():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'USE', '=='))
    for (f, expected) in TEST_BROADCAST:
        result = Frequency(f)
        ok = 'OK' if expected in result.band_use else 'XX'
        print(template.format(str(f), str(result.band_use), ok))
        assert expected in result.band_use


def test_services():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'SERVICE', '=='))
    for (f, expected) in TEST_SERVICES:
        result = Frequency(f)
        ok = 'OK' if expected in result.band_use else 'XX'
        print(template.format(str(f), str(result.band_use), ok))
        assert expected in result.band_use


def test_units():
    template = '{0:20s} | {1:20s} | {3:20s} | {3:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'UNIT', 'RESULT', '=='))
    for (freq, unit, expected) in TEST_UNITS:
        result = Frequency(freq, unit)
        ok = 'OK' if result.display == expected else 'XX'
        print(template.format(str(freq), unit, result.display, ok))
        assert result.display == expected


@given(integers(min_value=MIN, max_value=MAX))
def test_elements(a):
    NoneType = type(None)
    result = Frequency(a)
    assert isinstance(result.__dict__, dict)
    assert result.hz == a
    assert result.khz == a / 1_000
    assert result.mhz == a / 1_000_000
    assert result.ghz == a / 1_000_000_000
    assert isinstance(result.info(), dict)
    assert isinstance(result.details(), dict)
    assert isinstance(str(result), str)
    assert str(result) == f'{result.display} - {result.hz} hz'
    assert isinstance(int(result), int)
    assert int(result) == result.hz
    assert isinstance(result.display, str)
    assert isinstance(result.hz, int)
    assert isinstance(result.khz, (int, float))
    assert isinstance(result.mhz, (int, float))
    assert isinstance(result.ghz, (int, float))
    assert isinstance(result.wavelength, str)
    assert isinstance(result.band_use, tuple)
    assert isinstance(result.itu_band, str)
    assert isinstance(result.itu_abbr, str)
    assert isinstance(result.itu_num, int)
    assert isinstance(result.ieee_band, (str, NoneType))
    assert isinstance(result.ieee_description, (str, NoneType))
    assert isinstance(result.nato_band, (str, NoneType))
    assert isinstance(result.waveguide_band, (str, NoneType))
    assert isinstance(result.amateur_band, tuple)
    assert isinstance(result.amateur_band[0], bool)


@given(integers(min_value=MIN, max_value=int(MAX / 2)), integers(min_value=MIN, max_value=int(MAX / 2)))
def test_addition(a, b):
    resulta = Frequency(a)
    resultb = Frequency(b)
    result = resulta + resultb
    assert isinstance(result.__dict__, dict)
    assert result.hz == resulta.hz + resultb.hz
    result = resulta + b
    assert result.hz == resulta.hz + resultb.hz
    result = resulta + str(b)
    assert result.hz == resulta.hz + resultb.hz


@given(integers(min_value=10000, max_value=MAX), integers(min_value=MIN, max_value=9999))
def test_subtraction(a, b):
    resulta = Frequency(a)
    resultb = Frequency(b)
    result = resulta - resultb
    assert isinstance(result.__dict__, dict)
    assert result.hz == resulta.hz - resultb.hz
    result = resulta - b
    assert result.hz == resulta.hz - resultb.hz
    result = resulta - str(b)
    assert result.hz == resulta.hz - resultb.hz


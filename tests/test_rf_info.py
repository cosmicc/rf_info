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


TEST_COUNTRY = (
               ('144.100.000', 'US', '144.100.000'),
               ('132.158.000', 'us', '132.158.000'),
               ('1,000,000', 'GB', '001.000.000'),
               ('1000', 'ca', '000.001.000'),
               ('142.233', 'jP', '000.142.233'),
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

    with pytest.raises(Exception) as e:
        assert Frequency('1', 'hz', 'CX')
    assert str(e.value) == "Specified Country is Not Supported"

    with pytest.raises(Exception) as e:
        assert Frequency('1', country='XX')
    assert str(e.value) == "Invalid Country Specified"


def test_tiny_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1, 9999)
        result = Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu']['abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_small_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(10000, 999999)
        result = Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu']['abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_medium_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1000000, 999999999)
        result = Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu']['abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_large_random():
    template = '{0:20s} | {1:10s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'ITU', '=='))
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        random = randint(1000000000, MAX)
        result = Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu']['abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_types():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'TYPE', '=='))

    for (freq, expected) in TEST_DISPLAY:
        result = Frequency(freq).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(freq), '{}'.format(type(freq)), ok))
        assert isinstance(result, dict)

    with pytest.raises(Exception) as e:
        freq = [1, 2, 3]
        print(template.format(str(freq), '{}'.format(type(freq)), '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = (1, 2, 3)
        print(template.format(str(freq), '{}'.format(type(freq)), '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = True
        print(template.format(str(freq), '{}'.format(type(freq)), '--'))
        assert Frequency(freq)
    assert str(e.value) == "Invalid Frequency Type"

    with pytest.raises(Exception) as e:
        freq = {'freq': 123}
        print(template.format(str(freq), '{}'.format(type(freq)), '--'))
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


def test_display():
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
        ok = 'OK' if result.ieee['band'] == expected else 'XX'
        print(template.format(str(f), str(result.ieee['band']), ok))
        assert result.ieee['band'] == expected


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
    assert isinstance(result.units, dict)
    assert isinstance(result.units['hz'], int)
    assert isinstance(result.units['khz'], (int, float))
    assert isinstance(result.units['mhz'], (int, float))
    assert isinstance(result.units['ghz'], (int, float))
    assert result.units['hz'] == a
    assert result.units['khz'] == a / 1000
    assert result.units['mhz'] == a / 1000000
    assert result.units['ghz'] == a / 1000000000
    assert isinstance(result.info(), dict)
    assert isinstance(result.details(), dict)
    assert isinstance(str(result), str)
    assert str(result) == '{} - {} hz'.format(result.display, result.units['hz'])
    assert isinstance(int(result), int)
    assert int(result) == result.units['hz']
    assert isinstance(repr(result), str)
    assert repr(result) == "rf_info.Frequency('{}', 'hz', 'us')".format(result.display)
    assert isinstance(result.display, str)
    assert isinstance(result.wavelength, str)
    assert isinstance(result.itu, dict)
    assert isinstance(result.ieee, (dict))
    assert isinstance(result.nato, (dict))
    assert isinstance(result.waveguide, (dict))
    assert isinstance(result.microwave, (dict))
    assert isinstance(result.amateur, dict)
    assert isinstance(result.station, dict)
    assert isinstance(result.broadcasting, dict)
    assert isinstance(result.wifi, dict)
    assert isinstance(result.satellite, dict)
    assert isinstance(result.ism, (dict))
    assert isinstance(result.ieee_allocation['primary'], tuple)
    assert isinstance(result.ieee_allocation['secondary'], tuple)
    assert isinstance(result.ieee_allocation['notes'], tuple)


@given(integers(min_value=MIN, max_value=int(MAX / 2)), integers(min_value=MIN, max_value=int(MAX / 2)))
def test_addition(a, b):
    resulta = Frequency(a)
    resultb = Frequency(b)
    result = resulta + resultb
    assert isinstance(result.__dict__, dict)
    assert result.units['hz'] == resulta.units['hz'] + resultb.units['hz']
    result = resulta + b
    assert result.units['hz'] == resulta.units['hz'] + resultb.units['hz']
    result = resulta + str(b)
    assert result.units['hz'] == resulta.units['hz'] + resultb.units['hz']


@given(integers(min_value=10000, max_value=MAX), integers(min_value=MIN, max_value=9999))
def test_subtraction(a, b):
    resulta = Frequency(a)
    resultb = Frequency(b)
    result = resulta - resultb
    assert isinstance(result.__dict__, dict)
    assert result.units['hz'] == resulta.units['hz'] - resultb.units['hz']
    result = resulta - b
    assert result.units['hz'] == resulta.units['hz'] - resultb.units['hz']
    result = resulta - str(b)
    assert result.units['hz'] == resulta.units['hz'] - resultb.units['hz']


def test_countries():
    template = '{0:20s} | {1:20s} | {3:20s} | {3:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'COUNTRY', 'RESULT', '=='))
    for (freq, country, expected) in TEST_COUNTRY:
        result = Frequency(freq, 'hz', country)
        ok = 'OK' if result.display == expected else 'XX'
        print(template.format(str(freq), country, result.display, ok))
        assert result.display == expected
        assert result.country['abbr'] == country.upper()

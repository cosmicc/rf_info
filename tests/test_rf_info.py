#!/usr/bin/env python3

import pytest
from rf_info import rf_info
from random import randint

TEST_BROADCAST = (
                 ('89.900.000', 'FM Radio'),
                 ('155.500', 'Longwave AM'),
                 ('55.500.000', 'VHF TV'),
                 ('510.000.000', 'UHF TV'),
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

TEST_DIAL = (
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

RAND_TESTS = 500


def test_out_of_range():
    with pytest.raises(Exception) as e:
        freq = 1359239234234
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Frequency Out of Range"

    with pytest.raises(Exception) as e:
        freq = -234
        assert rf_info.Frequency(freq)
    assert str(e.value) == "Frequency Out of Range"


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
        random = randint(1000000, 999999999)
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
        random = randint(1000000000, 999999999999)
        result = rf_info.Frequency(random).__dict__
        ok = 'OK' if isinstance(result, dict) else 'XX'
        print(template.format(str(random), result['itu_abbr'], ok))
        assert isinstance(result, dict)
        rand_tests -= 1


def test_types():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'TYPE', '=='))

    for (freq, expected) in TEST_DIAL:
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


def test_dial():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'DIAL', '=='))
    for (freq, expected) in TEST_DIAL:
        result = rf_info.Frequency(freq).__dict__
        ok = 'OK' if result['dial'] == expected else 'XX'
        print(template.format(str(freq), str(result['dial']), ok))
        assert result['dial'] == expected


def test_ieee():
    template = '{0:20s} | {1:20s} | {2:2s}'
    print(' ')
    print(template.format('FREQUENCY', 'IEEE', '=='))
    for (f, expected) in TEST_IEEE:
        result = rf_info.Frequency(f)
        ok = 'OK' if result.ieee_band == expected else 'XX'
        print(template.format(str(f), str(result.ieee_band), ok))
        assert result.ieee_band == expected

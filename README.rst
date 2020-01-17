=======
rf-info
=======


.. image:: https://img.shields.io/github/v/release/cosmicc/rf_info.svg?include_prereleases
        :target: https://github.com/cosmicc/rf_info

.. image:: https://img.shields.io/pypi/v/rf_info.svg
        :target: https://pypi.python.org/pypi/rf_info

.. image:: https://pyup.io/repos/github/cosmicc/rf_info/python-3-shield.svg
        :target: https://pyup.io/repos/github/cosmicc/rf_info/
        :alt: Python 3

.. image:: https://img.shields.io/github/license/cosmicc/rf_info.svg
        :target: https://github.com/cosmicc/rf_info

.. image:: https://coveralls.io/repos/github/cosmicc/rf_info/badge.svg?branch=master
        :target: https://coveralls.io/github/cosmicc/rf_info?branch=master

.. image:: https://img.shields.io/travis/cosmicc/rf_info.svg
        :target: https://travis-ci.org/cosmicc/rf_info

.. image:: https://readthedocs.org/projects/rf-info/badge/?version=latest
        :target: https://radio-frequency.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/cosmicc/rf_info/shield.svg
     :target: https://pyup.io/repos/github/cosmicc/rf_info/
     :alt: Updates



Command line & Python library for obtaining details about a radio frequency


* Free software: MIT license
* Documentation: https://rf-info.readthedocs.io.
* Python 3.6, 3.7, 3.8 & pypy3 tested


Features
--------

Returns information about a radio frequency (US only for now)

- Band Use
- Wavelength
- ITU Band Description
- ITU Band Abbreviation
- ITU Band Number
- IEEE Band Name
- NATO Band Name
- Waveguide Band Name
- Amateur Radio Details (Type, Class, Max Power), - Not yet Implimented

Let me know if there is additional details you would like to see added,
or if someone would like to donate some EU/Other band info to add ;-)

Usage
-------
Frequency format examples:
89910000, 23,450,000, 12,634.534

Also supports "Radio Display" frequency representation (Dotted notation):
124.125.000, 198.000.050, 1.500.125.000

Suffix examples:
hz, khz, Mhz, Ghz (Case Insensitive)


Command Line:

rf-info <frequency> [<suffix>]


Python:

from rf-info import Frequency

freq = Frequency('112.434.000')

Then:

freq.details()

returns a dictionary:

{'display': '144.051.000', 'hz': 144051000, 'khz': 144051.0, 'mhz': 144.051, 'ghz': 0.144051, 'wavelength': '2m', 'itu_band': 'Very High Frequency', 'itu_abbr': 'VHF', 'itu_num': 8, 'ieee_band': 'VHF', 'ieee_description': 'Very High Frequency', 'nato_band': 'A', 'waveguide_band': None, 'band_use': (), 'amateur_band': (True, 'Class', 'Use', 'General CW and weak signals')}

or you can get individual items directly:

freq.itu_band

freq.wavelength

Also supports adding and subtracting frequencies.  Either a frequency object, int, or string representation of a frequency:

new_freq_object = Frequency('000.123.000') + Frequency('7', 'khz')  # Adds 7khz to 123khz

new_freq_object = Frequency('1', 'mhz') + 7000  # Adds 7khz to 1mhz

new_freq_object = Frequency('123.000') - '000.007.000'  # Subtracts 7khz from 123khz


Todo
-------

- Amateur Radio Details
- WIFI band details
- Cellular band details
- Sattelite band details
- GMRS, CB, & WIFI Specific Channels
- Add more reserved frequency details

Credits
-------

Ian Perry (ianperry99@gmail.com)

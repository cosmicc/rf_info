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

Also supports "Radio Dial" frequency representation (Dotted notation):
124.125.000, 198.000.050, 1.500.125.000

Suffix examples:
hz, Khz, Mhz, Ghz


Command Line:

rf-info <frequency> [<suffix>]


Python:

from rf-info import Frequency

freq = Frequency('112.434.000')

Then: 

freq.info()

returns a dictionary:

{'dial': '144.125', 'hz': ('144,125 hz', 144125), 'khz': ('144.125 Khz', 144.125), 'mhz': ('0.144125 Mhz', 0.144125), 'ghz': ('0.000144125 Ghz', 0.000144125), 'wavelength': '2,081m', 'band_use': (), 'itu_band': 'Low Frequency', 'itu_abbr': 'LF', 'itu_num': 5, 'ieee_band': None, 'ieee_description': None, 'nato_band': 'A', 'waveguide_band': None, 'amateur_band': (False,)}

or you can get individual items directly:

freq.itu_band

freq.wavelength



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

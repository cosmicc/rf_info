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
* Linux & Windows with color terminal support  


Features
--------

Returns information about a radio frequency (Country Specific)

- "Radio Display" format (Dotted notaton) 
- hz, khz, Mhz  and Ghz representations of the frequency  
- Frequency Wavelength
- ITU Band Description
- ITU Band Abbreviation
- ITU Band Number
- IEEE Band Name
- NATO Band Name
- Waveguide Band Name
- Fixed Station & Mobile Station Designations
- Broadcast Information 
- Primary Band Allocations
- Secondary Band Allocations
- Detailed footnotes for each band allocation  
- Amateur Radio Details (Usage, License Class, Max Power) * Not yet complete

Currently supported band allocations for countries: 
United States (US), Canada (CA), Brazil (BR), Spain (ES), United Kingdom (GB), Russian Federation (RU), Ukraine (UA), Japan (JP), India (IN), Korea, Republic of (KR), Thailand (TH), Switzerland (CH), Chile (CL), Denmark (DK), Finland (FI), France (FR), Hungary (HU), Indonesia (ID), Iceland (IS), Italy (IT), Mexico (MX), Netherlands (NL), New Zealand (NZ), Norway (NO), Poland (PL), South Africa (ZA), Sweden (SE), Venezuela (VE), Australia (AU), Slovenia (SI), Ireland (IE), Belgium (BE), Austria (AT), Argentina (AR), Israel (IL), Romania (RO), China (CN), Uruguay (UY), Greece (GR), Panama (PA), Peru (PE)

I can easily add support for more countries upon request

Command line supports color, raw parsable, and json output


Install
-------

Python library Requires:
::

$ pip3 install iso3166

Command Line Requires:
::

$ pip3 install iso3166 colorama

Install:
::

$ pip3 install rf-info


Usage
-------

  Command Line:
::

$ rf-info <frequency> [<units>] [<country>]


Frequency format examples:
::

$ rf-info 89910000
$ rf-info 23,450,000
$ rf-info 12,634.534
$ rf-info 12_000_000
$ rf-info 344_500.100

Also supports "Radio Display" frequency representation (Dotted notation):
::

$ rf-info 124.125.000
$ rf-info 1.500.125.000
$ rf-info 000.012.500

Suffix examples:
hz, khz, Mhz, Ghz  (Case Insensitive)
::

$ rf-info 123.100 mhz
$ rf-info 4.5 ghz

Country examples (2 digit abbriviation, 3 digit abbriviation, 3 digit number, or full name):
US, USA, 040, JPN, es, Spain  (Case Insensitive)
::

$ rf-info 144.400.000 hz US
$ rf-info 88 mhz JPN 

 Python:
::

>>> from rf_info import Frequency
>>> freq = Frequency('112.434.000')
>>> freq.details()

returns a dictionary:
::

>>> {'display': '144.100.000', 'hz': 144100000, 'khz': 144100.0, 'mhz': 144.1, 'ghz': 0.1441, 'wavelength': '2m', 'itu_band': 'Very High Frequency', 'itu_abbr': 'VHF', 'itu_num': 8, 'ieee_band': 'VHF', 'ieee_description': 'Very High Frequency', 'nato_band': 'A', 'waveguide_band': None, 'country_abbr': 'US', 'country_name': 'United States of America', 'amateur': True, 'fixed_station': False, 'mobile_station': False, 'broadcast': False, 'primary_allocation': ['Amateur', 'Amateur-Satellite'], 'secondary_allocation': [], 'allocation_notes': ['[5.216]: Additional allocation: in China, the band 144-146 MHz is also allocated to the aeronautical mobile (OR) service on a secondary basis.']}

or you can get individual items directly:
::

>>> freq.itu_band
>>> freq.wavelength
>>> freq.primary_allocation

Also supports adding and subtracting frequencies.  Either a frequency object, int, or string representation of a frequency, returns a new frequency object:
::

>>> new_freq_object = Frequency('001.123.000') + Frequency('7', 'khz')  # Adds 7 khz to 1.123 mhz
>>> new_freq_object = Frequency('1', 'mhz') + 15000  # Adds 15 khz to 1 mhz
>>> new_freq_object = Frequency('123,000') - '000.007.000'  # Subtracts 7 khz from 123 khz

Example command line output:
::

$ rf-info 144.100.000 hz US
::

 Display: 144.100.000
 Hz: 144100000
 Khz: 144100.0
 Mhz: 144.1
 Ghz: 0.1441
 Wavelength: 2m
 Itu_Band: Very High Frequency
 Itu_Abbr: VHF
 Itu_Num: 8
 Ieee_Band: VHF
 Ieee_Description: Very High Frequency
 Nato_Band: A
 Country_Abbr: US
 Country_Name: United States of America
 Fixed_Station: False
 Mobile_Station: False
 Broadcasting: False
 Amateur: True
 Amateur_Details:
  General CW and weak signals
  License Class
  Max Power      
 Primary_Allocation:
  Amateur
  Amateur-Satellite
 Allocation_Notes:
  [5.216]: Additional allocation: in China, the band 144-146 MHz is also allocated to the aeronautical mobile (OR) service on a secondary basis.
::


Todo
-------

- More WIFI band details (channels)
- More Cellular band details (channels)
- More Sattelite band details


Credits
-------

M. Ian Perry (ianperry99@gmail.com)
AD8DL

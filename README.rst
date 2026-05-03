=======
rf-info
=======


.. image:: https://img.shields.io/github/v/release/cosmicc/rf_info.svg?include_prereleases
        :target: https://github.com/cosmicc/rf_info

.. image:: https://img.shields.io/pypi/v/rf_info.svg
        :target: https://pypi.org/project/rf-info/

.. image:: https://img.shields.io/github/license/cosmicc/rf_info.svg
        :target: https://github.com/cosmicc/rf_info

.. image:: https://coveralls.io/repos/github/cosmicc/rf_info/badge.svg?branch=master
        :target: https://coveralls.io/github/cosmicc/rf_info?branch=master

.. image:: https://github.com/cosmicc/rf_info/actions/workflows/ci.yml/badge.svg
        :target: https://github.com/cosmicc/rf_info/actions/workflows/ci.yml

.. image:: https://readthedocs.org/projects/rf-info/badge/?version=latest
        :target: https://rf-info.readthedocs.io/?badge=latest
        :alt: Documentation Status


Command line & Python library for obtaining details about a radio frequency


* Free software: MIT license
* Documentation: https://rf-info.readthedocs.io.
* Python 3.10 through 3.14 tested. Not compatible with Python 2.x
* Linux & Windows with color, json output, and interactive terminal support


Features
--------

Returns information about a radio frequency.

- "Radio Display" format (Dotted notaton)
- hz, khz, Mhz  and Ghz representations of the frequency
- Frequency Wavelength
- ITU Band Description
- ITU Band Abbreviation
- ITU Band Number
- ISM Band Type & Description
- IEEE Band Name
- NATO Band Name
- Waveguide Band Name
- Microwave Band Name & Description
- Fixed Station & Mobile Station Designations
- IEEE Primary Band Allocations
- IEEE Secondary Band Allocations
- Detailed IEEE footnotes for each band allocation
- Active, unknown, deep-space, weather, and upcoming satellite frequency records from the JE9PEL list (1,309 indexed records as of 2026-04-26)
- Amateur Radio Modes, License Class, Max Power (US Only)
- Broadcasting Band Number & Details (US Only)
- Wi-Fi Frequency Details, including 6 GHz Wi-Fi 6E/7 ranges (US Only)
- Other Services CB, GMRS, Aircraft Band, Etc (US Only)

Currently supported band allocations for countries:
United States (US), Canada (CA), Brazil (BR), Spain (ES), United Kingdom (GB), Russian Federation (RU), Ukraine (UA), Japan (JP), India (IN), Korea, Republic of (KR), Thailand (TH), Switzerland (CH), Chile (CL), Denmark (DK), Finland (FI), France (FR), Hungary (HU), Indonesia (ID), Iceland (IS), Italy (IT), Mexico (MX), Netherlands (NL), New Zealand (NZ), Norway (NO), Poland (PL), South Africa (ZA), Sweden (SE), Venezuela (VE), Australia (AU), Slovenia (SI), Ireland (IE), Belgium (BE), Austria (AT), Argentina (AR), Israel (IL), Romania (RO), China (CN), Uruguay (UY), Greece (GR), Panama (PA), Peru (PE)

I can easily add support for more countries upon request

Includes man pages and texinfo documentation


Data Sources
------------

Satellite data is generated from the JE9PEL satellite list. US Wi-Fi, 5.9 GHz ITS/C-V2X, mobile broadband, and broadcast TV ranges are aligned with current FCC/eCFR band definitions. International allocation tables are stored by ITU region and can be regenerated from CSV exports with ``tools/parse_allocations.py``.


Install
-------
::

    $ pip install rf-info


Command Line Usage
------------------
::

    $ rf-info <frequency> [<units>] [<country>]

Frequency format examples::

    $ rf-info 89910000
    $ rf-info 23,450,000
    $ rf-info 12,634.534
    $ rf-info 12_000_000
    $ rf-info 344_500.100

Also supports "Radio Display" frequency representation (Dotted notation)::

    $ rf-info 124.125.000
    $ rf-info 1.500.125.000
    $ rf-info 000.012.500

Unit examples:
hz, khz, Mhz, Ghz  (Case Insensitive)::

    $ rf-info 123.100 mhz
    $ rf-info 4.5 ghz

Country examples (2 digit abbriviation, 3 digit abbriviation, 3 digit number, or full name)
US, USA, 040, JPN, Spain  (Case Insensitive)::

    $ rf-info 144.400.000 hz US
    $ rf-info 88 mhz JPN


Python Library Usage
---------------------
::

    >>> from rf_info import Frequency
    >>> freq = Frequency('144.890.000')
    >>> freq.details()

Returns a dictionary with normalized fields::

    >>> details = freq.details()
    >>> details['display']
    '144.890.000'
    >>> details['amateur']['details']
    ({'modes': 'CW, Phone, Image, RTTY/Data', 'license': 'Tech, General, Extra', 'power': 'MAX'}, {'modes': 'FM repeater inputs', 'license': 'Tech, General, Extra', 'power': 'MAX'})
    >>> details['ieee_allocation']['primary']
    ('Amateur', 'Amateur-Satellite')


Or you can get individual items directly::

    >>> freq.itu
    >>> freq.itu['band']
    >>> freq.wavelength
    >>> freq.ieee_allocation['primary']

Also supports adding and subtracting frequencies.  Either a frequency object, int, or string representation of a frequency, returns a new frequency object::

    >>> new_freq_object = Frequency('001.123.000') + Frequency('7', 'khz')  # Adds 7 khz to 1.123 mhz
    >>> new_freq_object = Frequency('1', 'mhz') + 15000  # Adds 15 khz to 1 mhz
    >>> new_freq_object = Frequency('123,000') - '000.007.000'  # Subtracts 7 khz from 123 khz


Output Example
--------------
::

    $ rf-info 435.890.000 hz US

     Display: 435.890.000
     Hz: 435,890,000
     Khz: 435,890
     Mhz: 435.89
     Ghz: 0.43589
     Wavelength: 68cm
     ITU Band: 9 - UHF (Ultra High Frequency)
     IEEE Band: UHF (Ultra High Frequency)
     NATO Band: B
     Waveguide Band: None
     Microwave Band: None
     Country: United States of America (US)
     Broadcasting: False
     Wifi: False
     Amateur: True
       Modes: Satellite only uplink/downlink
       License: Tech, General, Extra
       Power: MAX
     Satellite: True
       Name: JAS-2 (FO-29) [24278]
       Link: Downlink
       Modes: SSB CW (DigiTalker)
       Status: Active
     Fixed Station: False
     Mobile Station: False
     Primary Allocation:
       - Radiolocation
     Secondary Allocation:
       - Amateur
       - Earth Exploration-Satellite (Active) [5.279A]
     Allocation Notes:
       - [5.279A]: The use of the frequency band 432-438 MHz by sensors in the Earth exploration-satellite service (active) shall be in accordance with Recommendation ITU-R RS.1260-1. Additionally, the Earth exploration-satellite service (active) in the frequency band 432-438 MHz shall not cause harmful interference to the aeronautical radionavigation service in China. The provisions of this footnote in no way diminish the obligation of the Earth exploration-satellite service (active) to operate as a secondary service in accordance with Nos. 5.29 and 5.30. (WRC-15)


Todo
-------

- Keep ITU/FCC allocation data synced with current regulatory publications


Credits
-------

M. Ian Perry (ianperry99@gmail.com)
AD8DL

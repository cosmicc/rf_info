=======
rf-info
=======

.. image:: https://img.shields.io/github/v/release/cosmicc/rf-info.svg?include_prereleases 
        :target: https://github.com/cosmicc/rf-info
        
.. image:: https://img.shields.io/pypi/v/rf-info.svg
        :target: https://pypi.python.org/pypi/rf-info

.. image:: https://pyup.io/repos/github/cosmicc/rf-info/python-3-shield.svg
        :target: https://pyup.io/repos/github/cosmicc/rf-info/
        :alt: Python 3
        
.. image:: https://img.shields.io/github/license/cosmicc/rf-info.svg
        :target: https://github.com/cosmicc/rf-info

.. image:: https://img.shields.io/travis/cosmicc/rf-info.svg
        :target: https://travis-ci.org/cosmicc/rf-info

.. image:: https://readthedocs.org/projects/rf-info/badge/?version=latest
        :target: https://radio-frequency.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/cosmicc/rf-info/shield.svg
     :target: https://pyup.io/repos/github/cosmicc/rf-info/
     :alt: Updates



Radio Frequency Information


* Free software: MIT license
* Documentation: https://rfi-info.readthedocs.io.


Features
--------

Returns information about a radio frequency (US only for now)

- Band Use 
- ITU Band Description 
- ITU Band Abbreviation
- ITU Band Number
- IEEE Band Name
- NATO Band Name
- Amateur Radio Details (Type, Class, Max Power), - Not yet Implimented
- Wavelength  
- Waveguide Band Name
- Meters

Usage
-------
Frequency format examples:
62.761.000, 89910000, 23,450,000, 12,634.534

Command Line:
rfi-info <frequency> [<suffix>]

Python:
from rf-info import Frequency

freq = Frequency('112.434.000')

Then: 

freq.__dict__

returns a dictionary:
{ frequency: '89.900 Mhz', band_desc: 'Very High Frequency', band_type: None, meters: None, itu_abbr: 'VHF', itu_num: 8, ieee: 'VHF', nato: 'A', broadcast: 'FM Radio' }

or

freq.itu_band

returns only itu_band 


Todo
-------

- Convert to dictionary lookups instead of if/thens
- Amateur Radio Details
- Wavelength Range
- WIFI bandtypes
- Cellular bandtpes
- Sattelite bandtypes
- GMRS & CB Specific Channels

Credits
-------

Ian Perry (ianperry99@gmail.com)

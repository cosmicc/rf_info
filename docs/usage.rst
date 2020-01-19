=====
Usage
=====

Python
------------

To use rf-info in a python project::

    >>> from rf_info import Frequency
    >>> freq = Frequency('112.434.000')

then::    
    >>> freq.details()  

Returns a dictionary of all details::
    >>> {'display': '144.100.000', 'hz': 144100000, 'khz': 144100.0, 'mhz': 144.1, 'ghz': 0.1441, 'wavelength': '2m', 'itu_band': 'Very High Frequency', 'itu_abbr': 'VHF', 'itu_num': 8, 'ieee_band': 'VHF', 'ieee_description': 'Very High Frequency', 'nato_band': 'A', 'waveguide_band': None, 'country_abbr': 'US', 'country_name': 'United States of America', 'amateur': True, 'fixed_station': False, 'mobile_station': False, 'broadcast': False, 'primary_allocation': ['Amateur', 'Amateur-Satellite'], 'secondary_allocation': [], 'allocation_notes': ['[5.216]: Additional allocation: in China, the band 144-146 MHz is also allocated to the aeronautical mobile (OR) service on a secondary basis.']}

You can also get each detail individually::

    >>> freq.itu_band
    >>> freq.wavelength
    >>> freq.Primary_Allocation

Also supports adding and subtracting frequencies. Start with a frequency object then annd or subtract another frequency object, int, or string representation of a frequency, returns a new frequency object::

    >>> new_freq_object = Frequency('001.123.000') + Frequency('7', 'khz')  # Adds 7 khz to 1.123 mhz
    >>> new_freq_object = Frequency('1', 'mhz') + 15000  # Adds 15 khz to 1 mhz
    >>> new_freq_object = Frequency('123,000') - '000.007.000'  # Subtracts 7 khz from 123 khz


Command Line
-------------

To use the rf-info command line tool::    

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

Suffix examples: hz, khz, Mhz, Ghz (Case Insensitive)::

    $ rf-info 123.100 mhz
    $ rf-info 4.5 ghz

Country examples (2 digit abbriviation, 3 digit abbriviation, 3 digit number, or full name): US, USA, 040, JPN, es, Spain (Case Insensitive)::

    $ rf-info 144.400.000 hz US
    $ rf-info 88 mhz JPN

Example command line output::

    $ rf-info 144.100.000 hz US
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
        [5.216]: Additional allocation: in China, the band 144-146 MHz is also allocated to the aeronautical mobile (OR) service on a

You also can print the info in raw or json formatted output::

    $ rf-info 144.000 hz --raw
    $ rf-info 144.000 hz --json


#!/usr/bin/env python3

from iso3166 import countries
from .data.countrymap import COUNTRY_MAP


def remove_all_butfirst(s, substr):
    first_occurrence = s.index(substr) + len(substr)
    return s[:first_occurrence] + s[first_occurrence:].replace(substr, "")


def parse_freq(freq, unit):
    argfreq = freq.replace('.', '').replace(',', '').replace('_', '').replace(' ', '')
    if unit.lower() == 'khz':
        mindigits = 3
    elif unit.lower() == 'mhz':
        mindigits = 6
    elif unit.lower() == 'ghz':
        mindigits = 9
    elif unit.lower() == 'hz':
        if argfreq.isnumeric():
            return int(argfreq)
        else:
            raise ValueError('Invalid Frequency Specified')
    else:
        raise ValueError('Invalid Unit Specified')
    if '.' in freq:
        nfreq = remove_all_butfirst(freq, '.').split('.')
        while len(nfreq[1]) < mindigits:
            nfreq[1] = nfreq[1] + '0'
        return int(''.join(nfreq))
    else:
        for each in range(mindigits):
            argfreq = argfreq + '0'
        argfreq = str(int(argfreq))
        return int(argfreq)


class Frequency():

    def __init__(self, freq, unit='hz', country='us'):
        # Hack for pytest to test cli inputs
        if unit == '':
            unit = 'hz'

        # Determine Country and import country data
        try:
            scountry = countries.get(country)
        except KeyError:
            raise ValueError('Invalid Country Specified')
        cc = scountry.alpha2.upper()
        if cc not in COUNTRY_MAP:
            raise ValueError('Specified Country is Not Supported')

        from .data.international import IEEE, ITU, NATO, WAVEGUIDE

        if COUNTRY_MAP[cc] == 'a':
            from .data.a_allocations import ALLOCATIONS
        elif COUNTRY_MAP[cc] == 'b':
            from .data.b_allocations import ALLOCATIONS
        elif COUNTRY_MAP[cc] == 'c':
            from .data.c_allocations import ALLOCATIONS

        if scountry.alpha2.upper() == 'US':
            from .data.us_extras import SERVICES, BROADCAST, AMATEUR

        # Parse Frequency and unit inputs
        if (isinstance(freq, float) or isinstance(freq, str) or isinstance(freq, int)) and type(freq) != bool:
            intfreq = parse_freq(str(freq), unit)
        else:
            raise TypeError('Invalid Frequency Type')
        if intfreq < 1 or intfreq > 999_999_999_999:
            raise ValueError(f'Frequency Out of Range')

        # Create Display Frequency
        dispfreq = str(intfreq)[::-1]
        while len(dispfreq) < 9:
            dispfreq = dispfreq + '0'
        dispfreq = '.'.join(dispfreq[i:i + 3] for i in range(0, len(dispfreq), 3))
        self.display = dispfreq[::-1]

        # Create Unit frequencies
        self.hz = int(intfreq)
        self.khz = float(intfreq / 1_000)
        self.mhz = float(intfreq / 1_000_000)
        self.ghz = float(intfreq / 1_000_000_000)

        # Create ITU, IEEE, and Wavelength
        itu = ITU[intfreq]
        ieee = IEEE[intfreq]
        meter = 300_000_000 / intfreq
        if meter >= 1:
            self.wavelength = '{:,}'.format(int(meter))
            self.wavelength = f'{self.wavelength}m'
        elif meter >= 0.01:
            sub = int(str(meter).split('.')[1])
            self.wavelength = f'{str(sub)[:2]}cm'
        elif meter < 0.01:
            sub = int(str(meter).split('.')[1]) * 1000
            self.wavelength = f'{str(sub)[:2]}mm'
        self.itu_band = itu[2]
        self.itu_abbr = itu[1]
        self.itu_num = itu[0]
        if ieee is not None:
            self.ieee_band = ieee[0]
            self.ieee_description = ieee[1]
        else:
            self.ieee_band = None
            self.ieee_description = None

        # Create NATO and Waveguide
        self.nato_band = NATO[intfreq]
        self.waveguide_band = WAVEGUIDE[intfreq]

        # Set Country
        self.country_abbr = scountry.alpha2.upper()
        self.country_name = scountry.name

        # Set Allocations
        self.fixed_station = ALLOCATIONS[intfreq][1]
        self.mobile_station = ALLOCATIONS[intfreq][2]
        self.broadcasting = ALLOCATIONS[intfreq][3]

        if 'BROADCAST' in locals():
            br = BROADCAST[intfreq]
            if br is None:
                self.broadcasting_details = []
            else:
                self.broadcasting_details = br
        else:
            self.broadcasting_details = []

        self.amateur = ALLOCATIONS[intfreq][0]
        if 'AMATEUR' in locals():
            am = AMATEUR[intfreq]
            if am is None:
                self.amateur_details = []
            else:
                self.amateur_details = am
        else:
            self.amateur_details = []

        if 'SERVICES' in locals():
            sv = SERVICES[intfreq]
            if sv is None:
                self.services_details = []
            else:
                self.services_details = sv
        else:
            self.services_details = []


        self.primary_allocation = ALLOCATIONS[intfreq][4]
        self.secondary_allocation = ALLOCATIONS[intfreq][5]
        self.allocation_notes = ALLOCATIONS[intfreq][6]


    def info(self):
        return self.__dict__

    def details(self):
        return self.__dict__

    def __repr__(self):
        return "Frequency('{}')".format(self.display)

    def __str__(self):
        return f'{self.display} - {self.hz} hz'

    def __int__(self):
        return int(self.hz)

    def __add__(self, other):
        if isinstance(other, Frequency):
            return Frequency(self.hz + other.hz)
        elif isinstance(other, int):
            return Frequency(self.hz + other)
        elif isinstance(other, str):
            otherf = Frequency(other)
            return Frequency(self.hz + otherf.hz)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Frequency):
            return Frequency(self.hz - other.hz)
        elif isinstance(other, int):
            return Frequency(self.hz - other)
        elif isinstance(other, str):
            otherf = Frequency(other)
            return Frequency(self.hz - otherf.hz)
        else:
            raise TypeError

    def __len__(self):
        return len(str(self.hz))


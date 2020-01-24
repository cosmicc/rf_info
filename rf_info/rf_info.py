#!/usr/bin/env python3

from iso3166 import countries
from .countrymap import COUNTRY_MAP


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
        first_occurrence = freq.index('.') + 1
        nfreq = (freq[:first_occurrence] + freq[first_occurrence:].replace(".", "")).split('.')
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
        if country == '':
            country = 'us'

        # Determine Country and import country data
        try:
            scountry = countries.get(country)
        except KeyError:
            raise ValueError('Invalid Country Specified')
        cc = scountry.alpha2.upper()
        if cc not in COUNTRY_MAP:
            raise ValueError('Specified Country is Not Supported')

        from rf_info.data.international import ISM, IEEE, ITU, NATO, WAVEGUIDE, MICROWAVE
        from rf_info.data.satellites import SATELLITES

        if COUNTRY_MAP[cc] == 'a':
            from rf_info.data.a_allocations import ALLOCATIONS
        elif COUNTRY_MAP[cc] == 'b':
            from rf_info.data.b_allocations import ALLOCATIONS
        elif COUNTRY_MAP[cc] == 'c':
            from rf_info.data.c_allocations import ALLOCATIONS

        if scountry.alpha2.upper() == 'US':
            from rf_info.data.us import BROADCAST, AMATEUR, WIFI, SERVICES

        # Parse Frequency and unit inputs
        if (isinstance(freq, float) or isinstance(freq, str) or isinstance(freq, int)) and type(freq) != bool:
            intfreq = parse_freq(str(freq), unit)
        else:
            raise TypeError('Invalid Frequency Type')
        if intfreq < 1 or intfreq > 999999999999:
            raise ValueError('Frequency Out of Range')

        # Display Frequency
        dispfreq = str(intfreq)[::-1]
        while len(dispfreq) < 9:
            dispfreq = dispfreq + '0'
        dispfreq = '.'.join(dispfreq[i:i + 3] for i in range(0, len(dispfreq), 3))
        self.display = dispfreq[::-1]

        # Unit frequencies
        self.hz = int(intfreq)
        self.khz = float(intfreq / 1000)
        self.mhz = float(intfreq / 1000000)
        self.ghz = float(intfreq / 1000000000)

        # ITU, IEEE, and Wavelength
        itu = ITU[intfreq]
        ieee = IEEE[intfreq]
        meter = 300000000 / intfreq
        if meter >= 1:
            self.wavelength = '{:,}'.format(int(meter))
            self.wavelength = '{}m'.format(self.wavelength)
        elif meter >= 0.01:
            sub = int(str(meter).split('.')[1])
            self.wavelength = '{}cm'.format(str(sub)[:2])
        elif meter < 0.01:
            sub = int(str(meter).split('.')[1]) * 1000
            self.wavelength = '{}mm'.format(str(sub)[:2])
        self.itu_band = itu[2]
        self.itu_abbr = itu[1]
        self.itu_num = itu[0]
        if ieee is not None:
            self.ieee_band = ieee[0]
            self.ieee_description = ieee[1]
        else:
            self.ieee_band = None
            self.ieee_description = None

        # NATO data
        self.nato_band = NATO[intfreq]

        # Waveguide data
        self.waveguide_band = WAVEGUIDE[intfreq]

        # Microwave data
        if MICROWAVE[intfreq] is None:
            self.microwave_band = None
            self.microwave_details = None
        else:
            self.microwave_band = MICROWAVE[intfreq][0]
            self.microwave_details = (MICROWAVE[intfreq][1])

        # Set Country
        self.country_abbr = scountry.alpha2.upper()
        self.country_name = scountry.name

        # ISM Band data
        if ISM[intfreq] is not None:
            keys = ['type', 'description']
            self.ism_band = dict(zip(keys, ISM[intfreq]))
        else:
            self.ism_band = None

        # Broadcasting data
        self.broadcasting = ALLOCATIONS[intfreq][3]
        if 'BROADCAST' in locals():
            broadcast = BROADCAST[intfreq]
            if broadcast is not None:
                self.broadcasting = True
                self.broadcasting_details = broadcast
            else:
                self.broadcasting_details = None
        else:
            self.broadcasting_details = None

        # Wifi data
        if 'WIFI' in locals():
            wifi = WIFI[intfreq]
            if wifi is not None:
                self.wifi = True
                self.wifi_details = wifi
            else:
                self.wifi = False
                self.wifi_details = None
        else:
            self.wifi = False
            self.wifi_details = None

        # Satellite data
        self.satellite = ALLOCATIONS[intfreq][4]
        if 'SATELLITES' in locals():
            satellite = SATELLITES[intfreq]
            if satellite is not None:
                self.satellite = True
                keys = ['name', 'sat-id', 'link', 'modes', 'callsign', 'status']
                self.satellite_details = dict(zip(keys, satellite))
            else:
                self.satellite_details = None
        else:
            self.satellite_details = None

        # Amateur radio data
        self.amateur = ALLOCATIONS[intfreq][0]
        if 'AMATEUR' in locals():
            amateur = AMATEUR[intfreq]
            if amateur is not None:
                self.amateur = True
                keys = ['license', 'power', 'modes']
                self.amateur_details = dict(zip(keys, amateur))
            else:
                self.amateur_details = None
        else:
            self.amateur_details = None

        # Other Services data
        if 'SERVICES' in locals():
            services = SERVICES[intfreq]
            if services is not None:
                self.services_details = services
            else:
                self.services_details = None
        else:
            self.services_details = None

        # Fixed & Mobile station data
        self.fixed_station = ALLOCATIONS[intfreq][1]
        self.mobile_station = ALLOCATIONS[intfreq][2]

        # IEEE Allocations
        self.primary_allocation = tuple(ALLOCATIONS[intfreq][5])
        self.secondary_allocation = tuple(ALLOCATIONS[intfreq][6])
        self.allocation_notes = tuple(ALLOCATIONS[intfreq][7])

    def info(self):
        return self.__dict__

    def details(self):
        return self.__dict__

    def __repr__(self):
        return "Frequency('{}')".format(self.display)

    def __str__(self):
        return '{} - {} hz'.format(self.display, self.hz)

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

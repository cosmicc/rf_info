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

        from .data.international import ISM, IEEE, ITU, NATO, WAVEGUIDE, MICROWAVE
        from .data.satellites import SATELLITES

        if COUNTRY_MAP[cc] == 'a':
            from .data.a_allocations import ALLOCATIONS
        elif COUNTRY_MAP[cc] == 'b':
            from .data.b_allocations import ALLOCATIONS
        elif COUNTRY_MAP[cc] == 'c':
            from .data.c_allocations import ALLOCATIONS

        if scountry.alpha2.upper() == 'US':
            from .data.us import BROADCAST, AMATEUR, WIFI, SERVICES

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
        self.units = {'hz': int(intfreq), 'khz': float(intfreq / 1000), 'mhz': float(intfreq / 1000000), 'ghz': float(intfreq / 1000000000)}

        # Wavelength data
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

        # ITU data
        itu = ITU[intfreq]
        if itu:
            self.itu = {'number': itu[0], 'band': itu[2], 'abbr': itu[1]}
        else:
            self.itu = {'number': None, 'band': None, 'abbr': None}

        # IEEE data
        ieee = IEEE[intfreq]
        if ieee:
            self.ieee = {'band': ieee[0], 'description': ieee[1]}
        else:
            self.ieee = {'band': None, 'description': None}

        # NATO data
        nato = NATO[intfreq]
        if nato:
            self.nato = {'band': nato[0]}
        else:
            self.nato = {'band': None}

        # ISM Band data
        if ISM[intfreq] is not None:
            keys = ['type', 'description']
            self.ism = dict(zip(keys, ISM[intfreq]))
        else:
            self.ism = {'band': None, 'description': None}

        # Waveguide data
        waveguide = WAVEGUIDE[intfreq]
        if waveguide:
            self.waveguide = {'band': waveguide[0]}
        else:
            self.waveguide = {'band': None}

        # Microwave data
        if MICROWAVE[intfreq] is None:
            self.microwave = {'band': None, 'allocation': None}
        else:
            self.microwave = {'band': MICROWAVE[intfreq][0], 'allocation': MICROWAVE[intfreq][1]}

        # Set Country
        self.country = {'name': scountry.name, 'abbr': scountry.alpha2.upper()}

        # Broadcasting data
        broadcasting = ALLOCATIONS[intfreq][3]
        if 'BROADCAST' in locals():
            broadcast = BROADCAST[intfreq]
            if broadcasting:
                if broadcast is not None:
                    if len(broadcast) > 0:
                        self.broadcasting = {'allocated': True, 'details': broadcast}
                else:
                    self.broadcasting = {'allocated': True, 'details': tuple()}
            else:
                self.broadcasting = {'allocated': False, 'details': tuple()}
        else:
            self.broadcasting = {'allocated': False, 'details': tuple()}

        # Wifi data
        if 'WIFI' in locals():
            wifi = WIFI[intfreq]
            if wifi is not None:
                self.wifi = {'allocated': True, 'details': wifi}
            else:
                self.wifi = {'allocated': False, 'details': None}
        else:
            self.wifi = {'allocated': False, 'details': None}

        # Amateur radio data
        amateur = ALLOCATIONS[intfreq][0]
        if 'AMATEUR' in locals():
            amateurdetail = AMATEUR[intfreq]
            if amateur:
                if amateurdetail is not None:
                    self.amateur = {'allocated': True, 'modes': amateurdetail[0], 'license': amateurdetail[1], 'power': amateurdetail[2]}
                else:
                    self.amateur = {'allocated': True, 'modes': None, 'license': None, 'power': None}
            else:
                self.amateur = {'allocated': False, 'modes': None, 'license': None, 'power': None}
        else:
            self.amateur = {'allocated': False, 'modes': None, 'license': None, 'power': None}

        # Satellite data
        satellite = ALLOCATIONS[intfreq][4]
        if 'SATELLITES' in locals():
            satdetail = SATELLITES[intfreq]
            if satdetail is not None:
                self.satellite = {'allocated': True, 'name': satdetail[0], 'sat-id': satdetail[1], 'link': satdetail[2], 'modes': satdetail[3], 'callsign': satdetail[4], 'status': satdetail[5]}
            elif satellite:
                self.satellite = {'allocated': True, 'name': None, 'sat-id': None, 'link': None, 'modes': None, 'callsign': None, 'status': None}
            else:
                self.satellite = {'allocated': False, 'name': None, 'sat-id': None, 'link': None, 'modes': None, 'callsign': None, 'status': None}
        else:
            self.satellite = {'allocated': False, 'name': None, 'sat-id': None, 'link': None, 'modes': None, 'callsign': None, 'status': None}

        # Other Services data
        if 'SERVICES' in locals():
            services = SERVICES[intfreq]
            if services is not None:
                self.services = services
            else:
                self.services = None
        else:
            self.services = None

        # Fixed & Mobile station data
        self.station = {'fixed': ALLOCATIONS[intfreq][1], 'mobile': ALLOCATIONS[intfreq][2]}

        # IEEE Allocation
        self.ieee_allocation = {'primary': tuple(ALLOCATIONS[intfreq][5]), 'secondary': tuple(ALLOCATIONS[intfreq][6]), 'notes': tuple(ALLOCATIONS[intfreq][7])}

    def info(self):
        return self.__dict__

    def details(self):
        return self.__dict__

    def __repr__(self):
        return "rf_info.Frequency('{}', 'hz', '{}')".format(self.display, self.country['abbr'].lower())

    def __str__(self):
        return '{} - {} hz'.format(self.display, self.units['hz'])

    def __int__(self):
        return int(self.units['hz'])

    def __add__(self, other):
        if isinstance(other, Frequency):
            return Frequency(self.units['hz'] + other.units['hz'])
        elif isinstance(other, int):
            return Frequency(self.units['hz'] + other)
        elif isinstance(other, str):
            otherf = Frequency(other)
            return Frequency(self.units['hz'] + otherf.units['hz'])
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Frequency):
            return Frequency(self.units['hz'] - other.units['hz'])
        elif isinstance(other, int):
            return Frequency(self.units['hz'] - other)
        elif isinstance(other, str):
            otherf = Frequency(other)
            return Frequency(self.units['hz'] - otherf.units['hz'])
        else:
            raise TypeError

    def __len__(self):
        return len(str(self.units['hz']))

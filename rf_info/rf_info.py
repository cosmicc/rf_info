#!/usr/bin/env python3

from iso3166 import countries
from .countrymap import COUNTRY_MAP


SATELLITE_KEYS = ('name', 'sat-id', 'link', 'modes', 'callsign', 'status')
AMATEUR_KEYS = ('modes', 'license', 'power')


def parse_freq(freq, unit):
    freq = str(freq).strip()
    unit = unit.lower()
    argfreq = freq.replace('.', '').replace(',', '').replace('_', '').replace(' ', '')
    if unit == 'khz':
        mindigits = 3
    elif unit == 'mhz':
        mindigits = 6
    elif unit == 'ghz':
        mindigits = 9
    elif unit == 'hz':
        if argfreq.isnumeric():
            return int(argfreq)
        else:
            raise ValueError('Invalid Frequency Specified')
    else:
        raise ValueError('Invalid Unit Specified')
    if '.' in freq:
        cleanfreq = freq.replace(',', '').replace('_', '').replace(' ', '')
        first_occurrence = cleanfreq.index('.') + 1
        nfreq = (cleanfreq[:first_occurrence] + cleanfreq[first_occurrence:].replace(".", "")).split('.')
        while len(nfreq[1]) < mindigits:
            nfreq[1] = nfreq[1] + '0'
        return int(''.join(nfreq))
    else:
        for each in range(mindigits):
            argfreq = argfreq + '0'
        argfreq = str(int(argfreq))
        return int(argfreq)


def _lookup_all(table, frequency):
    if hasattr(table, 'get_all'):
        return table.get_all(frequency)
    value = table[frequency]
    if value is None:
        return tuple()
    return (value,)


def _first_or_none(values):
    if values:
        return values[0]
    return None


def _dict_records(keys, records):
    return tuple(dict(zip(keys, record)) for record in records)


class Frequency:
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
        else:
            raise ValueError('Specified Country is Not Supported')

        if scountry.alpha2.upper() == 'US':
            from .data.us import BROADCAST, AMATEUR, WIFI, SERVICES

        # Parse Frequency and unit inputs
        if (isinstance(freq, float) or isinstance(freq, str) or isinstance(freq, int)) and not isinstance(freq, bool):
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
            self.wavelength = '{}cm'.format(int(meter * 100))
        elif meter < 0.01:
            self.wavelength = '{}mm'.format(int(meter * 1000))

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
        ism = ISM[intfreq]
        if ism is not None:
            keys = ['type', 'description']
            self.ism = dict(zip(keys, ism))
        else:
            self.ism = {'type': None, 'description': None}

        # Waveguide data
        waveguide = WAVEGUIDE[intfreq]
        if waveguide:
            self.waveguide = {'band': waveguide}
        else:
            self.waveguide = {'band': None}

        # Microwave data
        microwave = MICROWAVE[intfreq]
        if microwave is None:
            self.microwave = {'band': None, 'allocation': None}
        else:
            self.microwave = {'band': microwave[0], 'allocation': microwave[1]}

        # Set Country
        self.country = {'name': scountry.name, 'abbr': scountry.alpha2.upper()}
        allocation = ALLOCATIONS[intfreq]
        if allocation is None:
            allocation = (False, False, False, False, False, [], [], [])

        # Broadcasting data
        broadcasting = allocation[3]
        if 'BROADCAST' in locals():
            broadcast = _lookup_all(BROADCAST, intfreq)
            if broadcasting:
                self.broadcasting = {'allocated': True, 'details': broadcast}
            else:
                self.broadcasting = {'allocated': False, 'details': tuple()}
        else:
            self.broadcasting = {'allocated': False, 'details': tuple()}

        # Wifi data
        if 'WIFI' in locals():
            wifi = _lookup_all(WIFI, intfreq)
            if wifi:
                self.wifi = {'allocated': True, 'details': wifi}
            else:
                self.wifi = {'allocated': False, 'details': tuple()}
        else:
            self.wifi = {'allocated': False, 'details': tuple()}

        # Amateur radio data
        amateur = allocation[0]
        if 'AMATEUR' in locals():
            amateurdetails = _dict_records(AMATEUR_KEYS, _lookup_all(AMATEUR, intfreq))
            first_amateur = _first_or_none(amateurdetails)
            if amateur:
                if first_amateur is not None:
                    self.amateur = {'allocated': True, 'modes': first_amateur['modes'], 'license': first_amateur['license'], 'power': first_amateur['power'], 'details': amateurdetails}
                else:
                    self.amateur = {'allocated': True, 'modes': None, 'license': None, 'power': None, 'details': tuple()}
            else:
                self.amateur = {'allocated': False, 'modes': None, 'license': None, 'power': None, 'details': tuple()}
        else:
            self.amateur = {'allocated': False, 'modes': None, 'license': None, 'power': None, 'details': tuple()}

        # Satellite data
        satellite = allocation[4]
        if 'SATELLITES' in locals():
            satdetails = _dict_records(SATELLITE_KEYS, _lookup_all(SATELLITES, intfreq))
            first_satellite = _first_or_none(satdetails)
            if first_satellite is not None:
                self.satellite = {'allocated': True, 'name': first_satellite['name'], 'sat-id': first_satellite['sat-id'], 'link': first_satellite['link'], 'modes': first_satellite['modes'], 'callsign': first_satellite['callsign'], 'status': first_satellite['status'], 'details': satdetails}
            elif satellite:
                self.satellite = {'allocated': True, 'name': None, 'sat-id': None, 'link': None, 'modes': None, 'callsign': None, 'status': None, 'details': tuple()}
            else:
                self.satellite = {'allocated': False, 'name': None, 'sat-id': None, 'link': None, 'modes': None, 'callsign': None, 'status': None, 'details': tuple()}
        else:
            self.satellite = {'allocated': False, 'name': None, 'sat-id': None, 'link': None, 'modes': None, 'callsign': None, 'status': None, 'details': tuple()}

        # Other Services data
        if 'SERVICES' in locals():
            services = _lookup_all(SERVICES, intfreq)
            if services:
                self.services = services
            else:
                self.services = tuple()
        else:
            self.services = tuple()

        # Fixed & Mobile station data
        self.station = {'fixed': allocation[1], 'mobile': allocation[2]}

        # IEEE Allocation
        self.ieee_allocation = {'primary': tuple(allocation[5]), 'secondary': tuple(allocation[6]), 'notes': tuple(allocation[7])}

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
            return Frequency(self.units['hz'] + other.units['hz'], country=self.country['abbr'])
        elif isinstance(other, int):
            return Frequency(self.units['hz'] + other, country=self.country['abbr'])
        elif isinstance(other, str):
            otherf = Frequency(other)
            return Frequency(self.units['hz'] + otherf.units['hz'], country=self.country['abbr'])
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Frequency):
            return Frequency(self.units['hz'] - other.units['hz'], country=self.country['abbr'])
        elif isinstance(other, int):
            return Frequency(self.units['hz'] - other, country=self.country['abbr'])
        elif isinstance(other, str):
            otherf = Frequency(other)
            return Frequency(self.units['hz'] - otherf.units['hz'], country=self.country['abbr'])
        else:
            raise TypeError

    def __len__(self):
        return len(str(self.units['hz']))

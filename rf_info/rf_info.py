from .rf_us_data import BROADCAST, HAM, IEEE, ITU, NATO, SERVICES, WAVEGUIDE


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

    def __init__(self, freq, unit='hz'):
        # Hack for pytest to test cli inputs
        if unit == '':
            unit = 'hz'

        # Parse Frequency and unit inputs
        if (isinstance(freq, float) or isinstance(freq, str) or isinstance(freq, int)) and type(freq) != bool:
            self.__intfreq = parse_freq(str(freq), unit)
        else:
            raise TypeError('Invalid Frequency Type')
        if self.__intfreq < 1 or self.__intfreq > 999999999999:
            raise ValueError(f'Frequency Out of Range')

        # Create Display Frequency
        dispfreq = str(self.__intfreq)[::-1]
        while len(dispfreq) < 9:
            dispfreq = dispfreq + '0'
        dispfreq = '.'.join(dispfreq[i:i + 3] for i in range(0, len(dispfreq), 3))
        self.display = dispfreq[::-1]

        # Create Unit frequencies
        self.hz = int(self.__intfreq)
        self.khz = float(self.__intfreq / 1_000)
        self.mhz = float(self.__intfreq / 1_000_000)
        self.ghz = float(self.__intfreq / 1_000_000_000)

        # Create ITU, IEEE, and Wavelength
        itu = ITU[self.__intfreq]
        ieee = IEEE[self.__intfreq]
        meter = 300_000_000 / self.__intfreq
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
        self.nato_band = NATO[self.__intfreq]
        self.waveguide_band = WAVEGUIDE[self.__intfreq]

        # Create Band Usage
        self.band_use = []
        if BROADCAST[self.__intfreq] is not None and BROADCAST[self.__intfreq]:
            self.band_use.append(BROADCAST[self.__intfreq])
        if SERVICES[self.__intfreq] is not None and SERVICES[self.__intfreq]:
            self.band_use.append(SERVICES[self.__intfreq])
        if len(self.band_use) == 0:
            self.band_use = tuple()
        else:
            self.band_use = tuple(self.band_use)

        # Create Amateur Band Use
        ham = HAM[self.__intfreq]
        if ham is None:
            self.amateur_band = ((False, ))
        else:
            self.amateur_band = ((True, )) + ham

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

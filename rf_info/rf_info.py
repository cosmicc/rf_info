from .rf_us_data import ITU, IEEE, NATO, WAVEGUIDE, BROADCAST, SERVICES, HAM

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
        if unit == '':
            unit = 'hz'
        if (isinstance(freq, float) or isinstance(freq, str) or isinstance(freq, int)) and type(freq) != bool:
            self.__intfreq = parse_freq(str(freq), unit)
        else:
            raise TypeError('Invalid Frequency Type')
        if self.__intfreq < 1 or self.__intfreq > 999999999999:
            raise ValueError(f'Frequency Out of Range')

        strfreq = str(self.__intfreq)[::-1]
        strfreq = '.'.join(strfreq[i:i + 3] for i in range(0, len(strfreq), 3))
        self.display = strfreq[::-1]

        self.hz = ('{:,} hz'.format(int(self.__intfreq)), (int(self.__intfreq)))
        self.khz = ('{:,} Khz'.format(float(self.__intfreq / 1000)), (float(self.__intfreq / 1000)))
        self.mhz = ('{:,} Mhz'.format(float(self.__intfreq / 1000000)), (float(self.__intfreq / 1000000)))
        self.ghz = ('{:,} Ghz'.format(float(self.__intfreq / 1000000000)), (float(self.__intfreq / 1000000000)))

        itu = ITU[self.__intfreq]
        ieee = IEEE[self.__intfreq]
        meter = 300000000 / self.__intfreq
        if meter >= 1:
            self.wavelength = '{:,}'.format(int(meter))
            self.wavelength = f'{self.wavelength}m'
        elif meter >= 0.01:
            sub = int(str(meter).split('.')[1])
            self.wavelength = f'{str(sub)[:2]}cm'
        elif meter < 0.01:
            sub = int(str(meter).split('.')[1]) * 1000
            self.wavelength = f'{str(sub)[:2]}mm'
        self.band_use = []

        if BROADCAST[self.__intfreq] is not None and BROADCAST[self.__intfreq]:
            self.band_use.append(BROADCAST[self.__intfreq])

        if SERVICES[self.__intfreq] is not None and SERVICES[self.__intfreq]:
            self.band_use.append(SERVICES[self.__intfreq])

        self.itu_band = itu[2]
        self.itu_abbr = itu[1]
        self.itu_num = itu[0]

        if ieee is not None:
            self.ieee_band = ieee[0]
            self.ieee_description = ieee[1]
        else:
            self.ieee_band = None
            self.ieee_description = None

        self.nato_band = NATO[self.__intfreq]
        self.waveguide_band = WAVEGUIDE[self.__intfreq]
        ham = HAM[self.__intfreq]
        if ham is None:
            self.amateur_band = ((False, ))
        else:
            self.amateur_band = ((True, )) + ham

        if len(self.band_use) == 0:
            self.band_use = tuple()
        else:
            self.band_use = tuple(self.band_use)

    def info(self):
        return self.__dict__

    def __str__(self):
        return self.display

    def __int__(self):
        return int(self.hz[1])

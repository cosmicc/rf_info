from .rf_data import ITU, IEEE, NATO, WAVEGUIDE, BROADCAST, SERVICES, HAM


def remove_all_butfirst(s, substr):
    try:
        first_occurrence = s.index(substr) + len(substr)
    except ValueError:
        return s
    else:
        return s[:first_occurrence] + s[first_occurrence:].replace(substr, "")


def parse_freq(freq, suffix):
    nfreq = freq
    argfreq = nfreq.replace('.', '').replace(',', '').replace('_', '').replace(' ', '')
    if suffix.lower() == 'khz':
        multp = (100, 1000)
    elif suffix.lower() == 'mhz':
        multp = (100000, 1000000)
    elif suffix.lower() == 'ghz':
        multp = (100000000, 1000000000)
    else:
        if argfreq.isnumeric():
            return int(argfreq)
        else:
            raise ValueError('Invalid Frequency Specified')
            exit(1)
    if '.' in freq:
        argfreq = float(remove_all_butfirst(nfreq.replace(',', '').replace('_', '').replace(' ', ''), '.'))
        argfreq = str(argfreq * multp[0]).replace('.', '')
    else:
        argfreq = int(argfreq) * multp[1]
    if argfreq.isnumeric():
        return int(argfreq)
    else:
        raise ValueError('Invalid Frequency Specified')


class Frequency():

    def __init__(self, freq, suffix='hz'):
        if isinstance(freq, float):
            intfreq = parse_freq(str(freq), suffix)
        elif isinstance(freq, str):
            intfreq = parse_freq(freq, suffix)
        elif isinstance(freq, int) and type(freq) != bool:
            intfreq = parse_freq(str(freq), suffix)
        else:
            raise TypeError('Invalid Frequency Type')
        if intfreq < 1 or intfreq > 999999999999:
            raise ValueError(f'Frequency Out of Range')

        strfreq = str(intfreq)[::-1]
        strfreq = '.'.join(strfreq[i:i + 3] for i in range(0, len(strfreq), 3))
        self.dial = strfreq[::-1]

        self.hz = ('{:,} hz'.format(int(intfreq)), (int(intfreq)))
        self.khz = ('{:,} Khz'.format(float(intfreq / 1000)), (float(intfreq / 1000)))
        self.mhz = ('{:,} Mhz'.format(float(intfreq / 1000000)), (float(intfreq / 1000000)))
        self.ghz = ('{:,} Ghz'.format(float(intfreq / 1000000000)), (float(intfreq / 1000000000)))

        itu = ITU[intfreq]
        ieee = IEEE[intfreq]
        meter = 300000000 / intfreq
        if meter >= 1:
            self.wavelength = '{:,}'.format(int(meter))
            self.wavelength = f'{self.wavelength}m'
        elif meter >= 0.01:
            sub = int(str(meter).split('.')[1])
            self.wavelength = f'{str(sub)[:2]}cm'
        elif meter < 0.01:
            sub = int(str(meter).split('.')[1]) * 1000
            self.wavelength = f'{str(sub)[:2]}mm'
        else:
            self.wavelength = 'N/A'
        self.band_use = []

        if BROADCAST[intfreq] is not None and BROADCAST[intfreq]:
            self.band_use.append(BROADCAST[intfreq])

        if SERVICES[intfreq] is not None and SERVICES[intfreq]:
            self.band_use.append(SERVICES[intfreq])

        if itu is not None:
            self.itu_band = itu[2]
            self.itu_abbr = itu[1]
            self.itu_num = itu[0]
        else:
            self.itu_band = itu
            self.itu_abbr = itu
            self.itu_num = itu

        if ieee is not None:
            if ieee:
                self.ieee_band = ieee[0]
                self.ieee_description = ieee[1]
            else:
                self.ieee_band = None
                self.ieee_description = None
        else:
            self.ieee_band = None
            self.ieee_description = None

        self.nato_band = NATO[intfreq]
        self.waveguide_band = WAVEGUIDE[intfreq]
        ham = HAM[intfreq]
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

from .rangekeydict import RangeKeyDict

WAVEGUIDE = RangeKeyDict({
    (0, 1700000001): None,
    (1700000001, 2200000001): 'R',
    (2200000001, 2600000001): 'R & D',
    (2600000001, 3300000001): 'D & S',
    (3300000001, 3950000001): 'S & E',
    (3950000001, 4900000001): 'E & G',
    (4900000001, 5850000001): 'G & F',
    (5850000001, 7050000001): 'F & C',
    (7050000001, 8200000001): 'C & H',
    (8200000001, 10100000001): 'H & X',
    (10100000001, 12400000001): 'X',
    (12400000001, 18000000001): 'Ku',
    (18000000001, 26500000001): 'K',
    (26500000001, 33000000001): 'Ka',
    (33000000001, 40000000001): 'Ka & Q',
    (40000000001, 50000000001): 'Q & U',
    (50000000001, 60000000001): 'U & V',
    (60000000001, 75000000001): 'V & E',
    (75000000001, 90000000001): 'E & W',
    (90000000001, 110000000001): 'W & F',
    (110000000001, 140000000001): 'F & D',
    (140000000001, 170000000001): 'D',
    (170000000001, 325000000001): 'N/A',
    (325000000001, 500000000001): 'Y',
})

ITU = RangeKeyDict({
    (0, 31): (1, 'ELF', 'Extremely Low Frequency'),
    (31, 301): (2, 'SLF', 'Super Low Frequency'),
    (301, 3001): (3, 'ULF', 'Ultra Low Frequency'),
    (3001, 30001): (4, 'VLF', 'Very Low Frequency'),
    (30001, 300001): (5, 'LF', 'Low Frequency'),
    (300001, 3000001): (6, 'MF', 'Medium Frequency'),
    (3000001, 30000001): (7, 'HF', 'High Frequency'),
    (30000001, 300000001): (8, 'VHF', 'Very High Frequency'),
    (300000001, 3000000001): (9, 'UHF', 'Ultra High Frequency'),
    (3000000001, 30000000001): (10, 'SHF', 'Super High Frequency'),
    (30000000001, 300000000001): (11, 'EHF', 'Extremely High Frequency'),
    (300000000001, 3000000000001): (12, 'THF', 'Terehertz Frequency'),
})

IEEE = RangeKeyDict({
    (0, 3000001): None,
    (3000001, 30000001): ('HF', 'High Frequency'),
    (30000001, 300000001): ('VHF', 'Very High Frequency'),
    (300000001, 1000000001): ('UHF', 'Ultra High Frequency'),
    (1000000001, 2000000001): ('L', 'Long Wave'),
    (2000000001, 4000000001): ('S', 'Short Wave'),
    (4000000001, 8000000001): ('C', 'S and X Compromise'),
    (8000000001, 12000000001): ('X', 'WWII Fire Control, Exotic'),
    (12000000001, 18000000001): ('Ku', 'Kurz-under'),
    (18000000001, 27000000001): ('K', 'Kurz (Short)'),
    (27000000001, 40000000001): ('Ka', 'Kurz-above'),
    (40000000001, 75000000001): ('V', 'N/A'),
    (75000000001, 110000000001): ('W', 'N/A'),
    (110000000001, 300000000001): ('G', 'Millimeter'),
})

NATO = RangeKeyDict({
    (0, 250000001): 'A',
    (250000001, 500000001): 'B',
    (500000001, 1000000001): 'C',
    (1000000001, 2000000001): 'D',
    (2000000001, 3000000001): 'E',
    (3000000001, 4000000001): 'F',
    (4000000001, 6000000001): 'G',
    (6000000001, 8000000001): 'H',
    (8000000001, 10000000001): 'I',
    (10000000001, 20000000001): 'J',
    (20000000001, 40000000001): 'K',
    (40000000001, 60000000001): 'L',
    (60000000001, 100000000001): 'M',
})

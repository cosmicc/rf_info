from .rangekeydict import RangeKeyDict


SATELLITES = RangeKeyDict({
    (435030000, 435180000): (['OSCAR 10', 'AO-10', 'LSB/CW', 'Uplink', 'Mode B Analog']),
    (145975000, 145825000): (['OSCAR 10', 'AO-10', 'LSB/CW', 'Downlink', 'Mode B Analog']),
    (145865000, 145905000): (['RS-10', 'RS-10', 'USB/CW', 'Uplink', 'Mode A Analog']),
    (29360000, 29400000): (['RS-10', 'RS-10', '', 'Downlink', 'Mode A Analog']),
    (21210000, 21250000): (['RS-12', 'RS-12', 'USB/CW', 'Uplink', 'Mode K Analog']),
    (29410000, 29450000): (['RS-12', 'RS-12', '', 'Downlink', 'Mode K Analog']),
    (145910000, 145950000): (['RS-12', 'RS-12', '', 'Downlink', 'Mode K Analog']),
    (145858000, 145898000): (['RS-15', 'RS-15', '', 'Uplink', 'Mode A Analog']),
    (29354000, 29394000): (['RS-15', 'RS-15', '', 'Downlink', 'Mode A Analog']),
    (145900000, 146000000): (['JASIB', 'FO-20', 'LSB/CW', 'Uplink', 'Mode J Analog']),
    (435900000, 435800000): (['JASIB', 'FO-20', '', 'Downlink', 'Mode J Analog']),
    (145850000, 145850001): (['8J1JBS', '', 'AFSK FM', 'Uplink', '1200 Baud PSK']),
    (145890000, 145890001): (['8J1JBS', '', 'AFSK FM', 'Uplink', '1200 Baud PSK']),
    (145910000, 145910001): (['8J1JBS', '', 'AFSK FM', 'Uplink', '1200 Baud PSK']),
    (435910000, 435910001): (['8J1JBS', '', '', 'Downlink', '1200 Baud PSK']),
    (145900000, 146000000): (['JAS2', 'FO-29', 'AFSK FM', 'Uplink', 'Mode J Analog']),
    (435900000, 435800000): (['JAS2', 'FO-29', '', 'Downlink', 'Mode J Analog']),
    (145850000, 145850001): (['JAS2', '', 'AFSK FM', 'Uplink', '1200-9600 Baud PSK or DV']),
    (145870000, 145870001): (['JAS2', '', 'AFSK FM', 'Uplink', '1200-9600 Baud PSK or DV']),
    (145890000, 145890001): (['JAS2', '', 'AFSK FM', 'Uplink', '1200-9600 Baud PSK or DV']),
    (145910000, 145910001): (['JAS2', '', 'AFSK FM', 'Uplink', '1200-9600 Baud PSK or DV']),
    (435910000, 435910001): (['JAS2', '', '', 'Downlink', '1200 Baud PSK']),
    (145850000, 145850001): (['EYESAT/AMRAD', 'AO-27', 'FM', 'Uplink', 'Part Time Repeater']),
    (436800000, 436800001): (['EYESAT/AMRAD', 'AO-27', 'FM', 'Downlink', 'Part Time Repeater']),
    (145985000, 436800001): (['MIR', 'MIR', '', 'Uplink/Downlink', 'FM Voice and Packet']),
    (435750000, 435750001): (['SAFEX', '', '', 'Uplink', 'FM Voice; Repeater']),
    (435950000, 435950001): (['SAFEX', '', '', 'Downlink', 'FM Voice; Repeater']),
    (435725000, 435725001): (['SAFEX', '', '', 'Uplink', 'Dgr. Voice']),
    (435925000, 435925001): (['SAFEX', '', '', 'Downlink', 'Dgr. Voice']),
    (435975000, 435975001): (['SAFEX', '', '', 'Uplink', 'Packet']),
    (437975000, 437975001): (['SAFEX', '', '', 'Downlink', 'Packet']),
    (144490000, 144490001): (['SAREX', 'SHUTTLE', '', 'Uplink', '1200 Baud AFSK']),
    (144450000, 144450001): (['SAREX', 'SHUTTLE', '', 'Uplink', '1200 Baud AFSK/FM Voice']),
    (144470000, 144470001): (['SAREX', 'SHUTTLE', '', 'Uplink', 'FM Voice']),
    (145550000, 145550001): (['SAREX', 'SHUTTLE', '', 'Downlink', '1200 Baud AFSK/FM Voice']),
    (145815000, 145815001): (['SAREX', 'SHUTTLE', '', 'Downlink', '1200 Baud AFSK/FM Voice']),
    (145840000, 145840001): (['SAREX', 'SHUTTLE', '', 'Downlink', '1200 Baud AFSK/FM Voice']),
    (145900000, 145900001): (['PACAST', 'AO-16', 'FM', 'Uplink', '1200 Baud PSK']),
    (145920000, 145920001): (['PACAST', 'AO-16', 'FM', 'Uplink', '1200 Baud PSK']),
    (145940000, 145940001): (['PACAST', 'AO-16', 'FM', 'Uplink', '1200 Baud PSK']),
    (437051300, 437015301): (['PACAST', 'AO-16', 'FM', 'Downlink', '1200 Baud PSK']),
    (145825000, 145825001): (['DOVE', 'DO-17', '', 'Downlink', '1200 Baud PSK']),
    (2401220000, 2401220000): (['DOVE', 'DO-17', '', 'Downlink', '1200 Baud PSK']),
    (437075000, 437100001): (['WEBERSAT', 'WO-18', 'FM', 'Downlink', '1200 Baud PSK (img)']),
    (145840000, 145840001): (['LUSAT', 'LO-19', '', 'Uplink', '1200 Baud PSK']),
    (145860000, 145860001): (['LUSAT', 'LO-19', '', 'Uplink', '1200 Baud PSK']),
    (145880000, 145880001): (['LUSAT', 'LO-19', '', 'Uplink', '1200 Baud PSK']),
    (437125000, 437150001): (['LUSAT', 'LO-19', 'FM', 'Downlink', '1200 Baud PSK']),
    (145900000, 145900001): (['OSCAR-22', 'UO-22', '', 'Uplink', '9600 Baud AFSK']),
    (435120000, 435120001): (['OSCAR-22', 'UO-22', '', 'Downlink', '9600 Baud AFSK']),
    (145875000, 145875001): (['ITAMSAT', 'IO-26', '', 'Uplink', '1200 Baud PSK']),
    (145900000, 145900001): (['ITAMSAT', 'IO-26', '', 'Uplink', '1200 Baud PSK']),
    (145925000, 145925001): (['ITAMSAT', 'IO-26', '', 'Uplink', '1200 Baud PSK']),
    (145950000, 145950001): (['ITAMSAT', 'IO-26', 'FM', 'Uplink', '1200 Baud PSK']),
    (435822000, 435822001): (['ITAMSAT', 'IO-26', '', 'Downlink', '1200 Baud PSK']),
    (145850000, 145850001): (['KITSAT A (HL01)', 'KO-23', '', 'Uplink', '9600 Baud AFSK']),
    (145900000, 145900001): (['KITSAT A (HL01)', 'KO-23', '', 'Uplink', '9600 Baud AFSK']),
    (435173000, 435173001): (['KITSAT A (HL01)', 'KO-23', '', 'Downlink', '9600 Baud AFSK']),
    (145980000, 145980001): (['KITSAT B (HL02)', 'KO-25', '', 'Uplink', '9600 Baud AFSK']),
    (436500000, 436500001): (['KITSAT B (HL02)', 'KO-25', '', 'Downlink', '9600 Baud AFSK']),
})

MICROWAVE = RangeKeyDict({
    (1000000000, 2000000000): ('L', 'Military telemetry, GPS, mobile phones (GSM), amateur radio'),
    (2000000000, 4000000000): ('S', 'Weather radar, surface ship radar, and some communications satellites (microwave ovens, microwave devices/communications, radio astronomy, mobile phones, wireless LAN, Bluetooth, ZigBee, GPS, amateur radio)'),
    (4000000000, 8000000000): ('C', 'Long-distance radio telecommunications'),
    (8000000000, 12000000000): ('X', 'Satellite communications, radar, terrestrial broadband, space communications, amateur radio, molecular rotational spectroscopy'),
    (12000000000, 18000000000): ('Ku', 'Satellite communications, molecular rotational spectroscopy'),
    (18000000000, 26500000000): ('K', 'Radar, satellite communications, astronomical observations, automotive radar, molecular rotational spectroscopy'),
    (26500000000, 40000000000): ('Ka', 'Satellite communications, molecular rotational spectroscopy'),
    (33000000000, 50000000000): ('Q', 'Satellite communications, terrestrial microwave communications, radio astronomy, automotive radar, molecular rotational spectroscopy'),
    (40000000000, 60000000000): ('U', 'Overlaps with Q band'),
    (50000000000, 75000000000): ('V', 'Millimeter wave radar research, molecular rotational spectroscopy and other kinds of scientific research'),
    (75000000000, 110000000000): ('W', 'Satellite communications, millimeter-wave radar research, military radar targeting and tracking applications, and some non-military applications, automotive radar'),
    (90000000000, 140000000000): ('F', 'SHF transmissions: Radio astronomy, microwave devices/communications, wireless LAN, most modern radars, communications satellites, satellite television broadcasting, DBS, amateur radio'),
    (110000000000, 170000000000): ('D', 'EHF transmissions: Radio astronomy, high-frequency microwave radio relay, microwave remote sensing, amateur radio, directed-energy weapon, millimeter wave scanner'),
})

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
    (110000000001, 300000000001): ('G', '(mm)'),
})

NATO = RangeKeyDict({
    (0, 250000001): 'A',
    (250000000, 500000001): 'B',
    (500000000, 1000000001): 'C',
    (1000000000, 2000000001): 'D',
    (2000000000, 3000000001): 'E',
    (3000000000, 4000000001): 'F',
    (4000000000, 6000000001): 'G',
    (6000000000, 8000000001): 'H',
    (8000000000, 10000000001): 'I',
    (10000000000, 20000000001): 'J',
    (20000000000, 40000000001): 'K',
    (40000000000, 60000000001): 'L',
    (60000000000, 100000000001): 'M',
    (100000000000, 200000000001): 'N',
})

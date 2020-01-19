from .rangekeydict import RangeKeyDict

AMATEUR = RangeKeyDict({
    (135700, 135800): (['General, Extra', '1W EIRP', 'CW, Phone, Image, RTTY/Data']),  # 2200 Meters

    (472000, 479000): (['General, Extra', '5W EIRP', 'CW, Phone, Image, RTTY/Data']),  # 630 Meters

    (1800000, 1831000): (['General, Extra', 'Power', 'CW, RTTY, and other narrowband modes']),  # 160 Meters
    (1830000, 1841000): (['General, Extra', 'Power', 'CW, RTTY, and other narrowband modes, Intercontinental QSOs only']),
    (1840000, 1851000): (['General, Extra', 'Power', 'CW, SSB, SSTV, and other wideband modes, Intercontinental QSOs only']),
    (1850000, 2000000): (['General, Extra', 'Power', 'CW, Phone, SSTV and other wideband modes']),

    (3590000, 3591000): (['Class', 'Use', 'RTTY DX']),  # 80 Meters
    (3580000, 3621000): (['Class', 'Use', 'RTTY']),
    (3620000, 3636000): (['Class', 'Use', 'Packet']),
    (3790000, 3801000): (['Class', 'Use', 'DX Window']),
    (3845000, 3846000): (['Class', 'Use', 'SSTV']),
    (3885000, 3886000): (['Class', 'Use', 'AM calling frequency']),

    (5332000, 5333000): (['Class', 'Use', '5330.5 kHz Amateur Tuning Frequency']),  # 60 Meters
    (5348000, 5349000): (['Class', 'Use', '5346.5 kHz Amateur Tuning Frequency']),
    (5368000, 5369000): (['Class', 'Use', '5366.5 kHz Amateur Tuning Frequency']),
    (5373000, 5374000): (['Class', 'Use', '5371.5 kHz Amateur Tuning Frequency']),
    (5405000, 5406000): (['Class', 'Use', '5403.5 kHz Amateur Tuning Frequency']),

    (7040000, 7041000): (['Class', 'Use', 'RTTY DX']),  # 40 Meters
    (7080000, 7101000): (['Class', 'Use', 'RTTY']),
    (7171000, 7172000): (['Class', 'Use', 'SSTV']),
    (7290000, 7291000): (['Class', 'Use', 'AM calling frequency']),

    (10130000, 10141000): (['Class', 'Use', 'RTTY']),  # 30 Meters
    (10140000, 10151000): (['Class', 'Use', 'Packet']),

    (14070000, 14095000): (['Class', 'Use', 'RTTY']),  # 20 Meters
    (14095000, 14100000): (['Class', 'Use', 'Packet']),
    (14100000, 14101000): (['Class', 'Use', 'NCDXF Beacons']),
    (14100000, 14113000): (['Class', 'Use', 'Packet']),
    (14230000, 14231000): (['Class', 'Use', 'SSTV']),
    (14286000, 14287000): (['Class', 'Use', 'AM calling frequency']),

    (18100000, 18105000): (['Class', 'Use', 'RTTY']),  # 17 Meters
    (18105000, 18110000): (['Class', 'Use', 'Packet']),

    (21070000, 21101000): (['Class', 'Use', 'RTTY']),  # 15 Meters
    (21100000, 21111000): (['Class', 'Use', 'Packet']),
    (21340000, 21341000): (['Class', 'Use', 'SSTV']),

    (24920000, 24926000): (['Class', 'Use', 'RTTY']),  # 12 Meters
    (24925000, 24931000): (['Class', 'Use', 'Packet']),

    (28000000, 28071000): (['Class', 'Use', 'CW']),  # 10 Meters
    (28070000, 28151000): (['Class', 'Use', 'RTTY']),
    (28150000, 28191000): (['Class', 'Use', 'CW']),
    (28200000, 28301000): (['Class', 'Use', 'Beacons']),
    (28300000, 29300000): (['Class', 'Use', 'Phone']),
    (28680000, 28681000): (['Class', 'Use', 'SSTV']),
    (29000000, 29201000): (['Class', 'Use', 'AM']),
    (29300000, 29511000): (['Class', 'Use', 'Satellite Downlinks']),
    (29520000, 29591000): (['Class', 'Use', 'Repeater Inputs']),
    (29600000, 29601000): (['Class', 'Use', 'FM Simplex']),
    (29610000, 29701000): (['Class', 'Use', 'Repeater Outputs']),

    (50000000, 50100000): (['Tech, General, Extra', 'MAX', 'CW Only']),  # 6 Meters
    (50100000, 54000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),

    (144000000, 144051000): (['Tech, General, Extra', 'MAX', 'EME (CW)']),  # 2 Meters
    (144050000, 144101000): (['Tech, General, Extra', 'MAX', 'General CW and weak signals']),
    (144100000, 144201000): (['Tech, General, Extra', 'MAX', 'EME and weak signal SSB']),
    (144200000, 144201000): (['Tech, General, Extra', 'MAX', 'National Calling Frequency']),
    (144200000, 144275000): (['Tech, General, Extra', 'MAX', 'General SSB Operation']),
    (144275000, 144301000): (['Tech, General, Extra', 'MAX', 'Propagation']),
    (144301000, 148000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, RTTY/Data']),

    (222000000, 225000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),  # 1.25 Meters

    (420000000, 450000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),  # 70 cm

    (902000000, 928000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),  # 33 cm

    (1240000000, 1300000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),  # 70 cm

    (2300000000, 2310000000): (['Tech, General, Extra', 'MAX', 'No Designations']),  # Higher
    (2390000000, 2450000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (3300000000, 3500000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (5650000000, 5925000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (10000000000, 10500000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (24000000000, 24250000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (47000000000, 47200000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (77000000000, 81000000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (122250000000, 123000000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (134000000000, 141000000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (241000000000, 250000000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
    (300000000000, 999999999999): (['Tech, General, Extra', 'MAX', 'No Designations']),
})


SERVICES = RangeKeyDict({
    (26965000, 27405001): (['Citizen Band (CB)']),
    (462562500, 467725000): (['General Mobile Radio Service (GMRS)']),
})


BROADCAST = RangeKeyDict({
    (148500, 283501): (['Longwave AM Radio International']),
    (535000, 1710001): (['Mediumwave AM Radio US']),
    (2300000, 2495000): (["Medium Frequency Radio International"]),
    (3800000, 4000000): (["High Frequency Radio International"]),
    (4750000, 5060000): (["High Frequency Radio International"]),
    (5950000, 6200000): (["High Frequency Radio US"]),
    (7100000, 7300000): (["High Frequency Radio US"]),
    (9500000, 9900000): (["High Frequency Radio US"]),
    (11650000, 12050000): (["High Frequency Radio US"]),
    (13600000, 13800000): (["High Frequency Radio US"]),
    (15100000, 15600000): (["High Frequency Radio US"]),
    (17550000, 17900000): (["High Frequency Radio US"]),
    (21450000, 21850000): (["High Frequency Radio US"]),
    (25600000, 26100000): (["High Frequency Radio US"]),
    # (3000000, 30000001): 'Shortwave AM Radio',
    (155500000, 174000001): (['Marine VHF']),
    (47000000, 68000001): (['VHF Television']),
    (470000000, 582000001): (['UHF Television']),
    (582000000, 862000000): (['UHF Television']),
    (87500000, 108000001): (['FM Radio']),
    (2182000, 2182001): (['Marine Emergency']),
    (285000, 315501): (['Aviation']),
    (340000, 350001): (['Aviation SSB']),
    (285000, 315501): (['Aviation']),
})


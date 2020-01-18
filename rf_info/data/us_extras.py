from .rangekeydict import RangeKeyDict

AMATEUR = RangeKeyDict({
    (1800000, 1831000): (['Class', 'Use', 'CW, RTTY, and other narrowband modes']),
    (1830000, 1841000): (['Class', 'Use', 'CW, RTTY, and other narrowband modes, Intercontinental QSOs only']),
    (1840000, 1851000): (['Class', 'Use', 'CW, SSB, SSTV, and other wideband modes, Intercontinental QSOs only']),
    (1850000, 2000000): (['Class', 'Use', 'CW, Phone, SSTV and other wideband modes']),
    (3590000, 3591000): (['Class', 'Use', 'RTTY DX']),
    (3580000, 3621000): (['Class', 'Use', 'RTTY']),
    (3620000, 3636000): (['Class', 'Use', 'Packet']),
    (3790000, 3801000): (['Class', 'Use', 'DX Window']),
    (3845000, 3846000): (['Class', 'Use', 'SSTV']),
    (3885000, 3886000): (['Class', 'Use', 'AM calling frequency']),
    (5332000, 5333000): (['Class', 'Use', '5330.5 kHz Amateur Tuning Frequency']),
    (5348000, 5349000): (['Class', 'Use', '5346.5 kHz Amateur Tuning Frequency']),
    (5368000, 5369000): (['Class', 'Use', '5366.5 kHz Amateur Tuning Frequency']),
    (5373000, 5374000): (['Class', 'Use', '5371.5 kHz Amateur Tuning Frequency']),
    (5405000, 5406000): (['Class', 'Use', '5403.5 kHz Amateur Tuning Frequency']),
    (7040000, 7041000): (['Class', 'Use', 'RTTY DX']),
    (7080000, 7101000): (['Class', 'Use', 'RTTY']),
    (7171000, 7172000): (['Class', 'Use', 'SSTV']),
    (7290000, 7291000): (['Class', 'Use', 'AM calling frequency']),
    (10130000, 10141000): (['Class', 'Use', 'RTTY']),
    (10140000, 10151000): (['Class', 'Use', 'Packet']),
    (14070000, 14095000): (['Class', 'Use', 'RTTY']),
    (14095000, 14100000): (['Class', 'Use', 'Packet']),
    (14100000, 14101000): (['Class', 'Use', 'NCDXF Beacons']),
    (14100000, 14113000): (['Class', 'Use', 'Packet']),
    (14230000, 14231000): (['Class', 'Use', 'SSTV']),
    (14286000, 14287000): (['Class', 'Use', 'AM calling frequency']),
    (18100000, 18105000): (['Class', 'Use', 'RTTY']),
    (18105000, 18110000): (['Class', 'Use', 'Packet']),
    (21070000, 21101000): (['Class', 'Use', 'RTTY']),
    (21100000, 21111000): (['Class', 'Use', 'Packet']),
    (21340000, 21341000): (['Class', 'Use', 'SSTV']),
    (24920000, 24926000): (['Class', 'Use', 'RTTY']),
    (24925000, 24931000): (['Class', 'Use', 'Packet']),
    (28000000, 28071000): (['Class', 'Use', 'CW']),
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
    (144000000, 144051000): (['Class', 'Use', 'EME (CW)']),
    (144050000, 144101000): (['Class', 'Use', 'General CW and weak signals']),
    (144100000, 144201000): (['Class', 'Use', 'EME and weak signal SSB']),
    (144200000, 144201000): (['Class', 'Use', 'National Calling Frequency']),
    (144200000, 144275000): (['Class', 'Use', 'General SSB Operation']),
    (144275000, 144301000): (['Class', 'Use', 'Propagation']),
    # (144050, 144101): ('Class', 'Use', 'New OSCAR sub-band'),
    # (144050, 144101): ('Class', 'Use', 'Linear Translator Inputs'),
    # (144050, 144101): ('Class', 'Use', 'FM Repeater Inputs'),
    # (144050, 144101): ('Class', 'Use', 'Weak signal and FM simplex (145010, 30, 50, 70, 90 are widely used for packet)'),
    # (144050, 144101): ('Class', 'Use', 'Linear Translator Outputs'),
    # (144050, 144101): ('Class', 'Use', 'FM Repeater Outputs'),
    # (144050, 144101): ('Class', 'Use', 'Miscellaneous and Experimental Modes'),
    # (144050, 144101): ('Class', 'Use', 'OSCAR Sub-Band'),
    # (144050, 144101): ('Class', 'Use', 'Repeater Inputs'),
    # (144050, 144101): ('Class', 'Use', 'Simplex'),
    # (144050, 144101): ('Class', 'Use', 'Repeater Outputs'),
    # (144050, 144101): ('Class', 'Use', 'Repeater Outputs'),
    # (144050, 144101): ('Class', 'Use', 'Simplex'),
    # (144050, 144101): ('Class', 'Use', 'Repeater Inputs'),
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

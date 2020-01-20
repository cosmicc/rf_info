from rf_info.data.rangekeydict import RangeKeyDict

AMATEUR = RangeKeyDict({
    # 2200 Meters
    (135700, 135800): ('General, Extra', '1W EIRP', 'CW, Phone, Image, RTTY/Data'),

    # 630 Meters
    (472000, 479000): ('General, Extra', '5W EIRP', 'CW, Phone, Image, RTTY/Data'),

    # 160 Meters
    (1800000, 1831000): (['General, Extra', 'Power', 'CW, RTTY, and other narrowband modes']),
    (1830000, 1841000): (['General, Extra', 'Power', 'CW, RTTY, and other narrowband modes, Intercontinental QSOs only']),
    (1840000, 1851000): (['General, Extra', 'Power', 'CW, SSB, SSTV, and other wideband modes, Intercontinental QSOs only']),
    (1850000, 2000000): (['General, Extra', 'Power', 'CW, Phone, SSTV and other wideband modes']),

    # 80 Meters
    (3590000, 3591000): (['License Class', 'MAX', 'RTTY DX']),
    (3580000, 3621000): (['License Class', 'MAX', 'RTTY']),
    (3620000, 3636000): (['License Class', 'MAX', 'Packet']),
    (3790000, 3801000): (['License Class', 'MAX', 'DX Window']),
    (3845000, 3846000): (['License Class', 'MAX', 'SSTV']),
    (3885000, 3886000): (['License Class', 'MAX', 'AM calling frequency']),

    # 60 Meters
    (5332000, 5333000): (['License Class', '200 W EIRP', '5330.5 kHz Amateur Tuning Frequency']),
    (5348000, 5349000): (['License Class', '200 W EIRP', '5346.5 kHz Amateur Tuning Frequency']),
    (5368000, 5369000): (['License Class', '200 W EIRP', '5366.5 kHz Amateur Tuning Frequency']),
    (5373000, 5374000): (['License Class', '200 W EIRP', '5371.5 kHz Amateur Tuning Frequency']),
    (5405000, 5406000): (['License Class', '200 W EIRP', '5403.5 kHz Amateur Tuning Frequency']),

    # 40 Meters
    (7040000, 7041000): (['License Class', 'MAX', 'RTTY DX']),
    (7080000, 7101000): (['License Class', 'MAX', 'RTTY']),
    (7171000, 7172000): (['License Class', 'MAX', 'SSTV']),
    (7290000, 7291000): (['License Class', 'MAX', 'AM calling frequency']),

    # 30 Meters
    (10130000, 10141000): (['License Class', 'MAX', 'RTTY']),
    (10140000, 10151000): (['License Class', 'MAX', 'Packet']),

    # 20 Meters
    (14070000, 14095000): (['License Class', 'MAX', 'RTTY']),
    (14095000, 14100000): (['License Class', 'MAX', 'Packet']),
    (14100000, 14101000): (['License Class', 'MAX', 'NCDXF Beacons']),
    (14100000, 14113000): (['License Class', 'MAX', 'Packet']),
    (14230000, 14231000): (['License Class', 'MAX', 'SSTV']),
    (14286000, 14287000): (['License Class', 'MAX', 'AM calling frequency']),

    # 17 Meters
    (18100000, 18105000): (['License Class', 'MAX', 'RTTY']),
    (18105000, 18110000): (['License Class', 'MAX', 'Packet']),

    # 15 Meters
    (21070000, 21101000): (['License Class', 'MAX', 'RTTY']),
    (21100000, 21111000): (['License Class', 'MAX', 'Packet']),
    (21340000, 21341000): (['License Class', 'MAX', 'SSTV']),

    # 12 Meters
    (24920000, 24926000): (['License Class', 'MAX', 'RTTY']),
    (24925000, 24931000): (['License Class', 'MAX', 'Packet']),

    # 10 Meters
    (28000000, 28071000): (['License Class', 'MAX', 'CW']),
    (28070000, 28151000): (['License Class', 'MAX', 'RTTY']),
    (28150000, 28191000): (['License Class', 'MAX', 'CW']),
    (28200000, 28301000): (['License Class', 'MAX', 'Beacons']),
    (28300000, 29300000): (['License Class', 'MAX', 'Phone']),
    (28680000, 28681000): (['License Class', 'MAX', 'SSTV']),
    (29000000, 29201000): (['License Class', 'MAX', 'AM']),
    (29300000, 29511000): (['License Class', 'MAX', 'Satellite Downlinks']),
    (29520000, 29591000): (['License Class', 'MAX', 'Repeater Inputs']),
    (29600000, 29601000): (['License Class', 'MAX', 'FM Simplex']),
    (29610000, 29701000): (['License Class', 'MAX', 'Repeater Outputs']),

    # 6 Meters
    (50000000, 50060001): (['Tech, General, Extra', 'MAX', 'CW Only']),
    (50060000, 50080001): (['Tech, General, Extra', 'MAX', 'CW Only']),
    (50080000, 50100001): (['Tech, General, Extra', 'MAX', 'CW Only']),
    (50100000, 50600001): (['Tech, General, Extra', 'MAX', 'SSB']),
    (50125000, 50125001): (['Tech, General, Extra', 'MAX', 'SSB DX calling frequency']),
    (50200000, 50200001): (['Tech, General, Extra', 'MAX', 'SSB domestic calling frequency (Note: Suggest QSY up for local & down for long-distance QSOs)']),
    (50400000, 50400001): (['Tech, General, Extra', 'MAX', 'AM calling frequency']),
    (50600000, 51000001): (['Tech, General, Extra', 'MAX', 'Experimental & Special modes']),
    (50700000, 50700001): (['Tech, General, Extra', 'MAX', 'RTTY calling frequency']),
    (50800000, 50980001): (['Tech, General, Extra', 'MAX', 'Radio Control (R/C) channels, 10 channels spaced 20 kHz apart']),
    (51000000, 51100001): (['Tech, General, Extra', 'MAX', 'Pacific DX window']),
    (51000000, 52000001): (['Tech, General, Extra', 'MAX', 'FM Repeaters']),
    (51100000, 52000001): (['Tech, General, Extra', 'MAX', 'FM Repeaters & Simplex']),
    (52000000, 52050001): (['Tech, General, Extra', 'MAX', 'Pacific DX window']),
    (52000000, 53000001): (['Tech, General, Extra', 'MAX', 'FM Repeaters & Simplex']),
    (53000000, 54000001): (['Tech, General, Extra', 'MAX', 'Present radio control (R/C) channels, 10 channels spaced 100 kHz apart']),

    # 2 Meters
    (144000000, 144050001): (['Tech, General, Extra', 'MAX', 'EME (CW)']),
    (144275000, 144300001): (['Tech, General, Extra', 'MAX', 'Propagation beacons']),
    (144050000, 144100001): (['Tech, General, Extra', 'MAX', 'General CW and weak signals']),
    (144100000, 144200001): (['Tech, General, Extra', 'MAX', 'EME and weak signal SSB']),
    (144200000, 144200001): (['Tech, General, Extra', 'MAX', 'National SSB Calling Frequency']),
    (144200000, 144275001): (['Tech, General, Extra', 'MAX', 'General SSB Operation, USB']),
    (144275000, 144300001): (['Tech, General, Extra', 'MAX', 'Propagation beacons']),
    (144300001, 148000001): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, RTTY/Data']),
    (144300000, 144500001): (['Tech, General, Extra', 'MAX', 'OSCAR subband & simplex']),
    (144500000, 144600001): (['Tech, General, Extra', 'MAX', 'Linear translator outputs']),
    (144600000, 144900001): (['Tech, General, Extra', 'MAX', 'FM repeater inputs']),
    (144900000, 145100001): (['Tech, General, Extra', 'MAX', 'Weak signal & FM simplex']),
    (145100000, 145200001): (['Tech, General, Extra', 'MAX', 'Linear translator outputs % packet']),
    (145200000, 145500001): (['Tech, General, Extra', 'MAX', 'FM repeater outputs']),
    (145500000, 145800001): (['Tech, General, Extra', 'MAX', 'Miscellaneous and experimental modes']),
    (145500000, 145800001): (['Tech, General, Extra', 'MAX', 'OSCAR subband - Satellite use ONLY!']),
    (146010000, 146370001): (['Tech, General, Extra', 'MAX', 'Repeater inputs']),
    (146400000, 146580001): (['Tech, General, Extra', 'MAX', 'Simplex']),
    (146610000, 146970001): (['Tech, General, Extra', 'MAX', 'Repeater outputs']),
    (147000000, 147390001): (['Tech, General, Extra', 'MAX', 'Repeater outputs']),
    (147420000, 147570001): (['Tech, General, Extra', 'MAX', 'Simplex']),
    (147600000, 147990001): (['Tech, General, Extra', 'MAX', 'Repeater inputs']),

    # 1.25 Meters
    (222000000, 225000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),

    # 70 cm
    (420000000, 450000001): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),
    (420000000, 426000001): (['Tech, General, Extra', 'MAX', 'ATV repeater or simplex with 421.25 MHz video carrier control links and experimental']),
    (426000000, 432080001): (['Tech, General, Extra', 'MAX', 'EME']),
    (432080000, 432100001): (['Tech, General, Extra', 'MAX', 'Weak signal CW']),
    (432100000, 432100001): (['Tech, General, Extra', 'MAX', '70 cm CW/SSB calling frequency']),
    (432100000, 433000001): (['Tech, General, Extra', 'MAX', 'Mixed-mode and weak-signal work']),
    (432300000, 432400001): (['Tech, General, Extra', 'MAX', 'Beacons']),
    (433000000, 435000001): (['Tech, General, Extra', 'MAX', 'Auxiliary/repeater links']),
    (435000000, 438000001): (['Tech, General, Extra', 'MAX', 'Satellite only uplink/downlink']),
    (438000000, 444000001): (['Tech, General, Extra', 'MAX', 'ATV repeater input with 439.250 MHz video carrier frequency and repeater links']),
    (442000000, 445000001): (['Tech, General, Extra', 'MAX', 'Repeater inputs & outputs (local option)']),
    (445000000, 447000001): (['Tech, General, Extra', 'MAX', 'Shared by auxiliary and control links, repeaters and simplex (local option); 446.00 MHz national simplex frequency']),
    (447000000, 450000001): (['Tech, General, Extra', 'MAX', 'Repeater inputs & outputs']),

    # 33 cm
    (902000000, 928000001): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),
    (902000000, 904000001): (['Tech, General, Extra', 'MAX', 'Narrow-bandwidth, weak-signal communications']),
    (902000000, 902800001): (['Tech, General, Extra', 'MAX', 'SSTV, FAX, ACSB, experimental']),
    (902800000, 903000001): (['Tech, General, Extra', 'MAX', 'CW & EME Only']),
    (903000000, 903050001): (['Tech, General, Extra', 'MAX', 'EME Only']),
    (903070000, 903080001): (['Tech, General, Extra', 'MAX', 'CW beacons']),
    (903100000, 903100001): (['Tech, General, Extra', 'MAX', 'CW, SSB calling frequency']),
    (903400000, 903600001): (['Tech, General, Extra', 'MAX', 'Crossband linear translator inputs']),
    (903600000, 903800001): (['Tech, General, Extra', 'MAX', 'Crossband linear translator outputs']),
    (903800000, 904000001): (['Tech, General, Extra', 'MAX', 'Experimental beacons exclusive']),
    (904000000, 906000001): (['Tech, General, Extra', 'MAX', 'Digital communications']),
    (906000000, 907000001): (['Tech, General, Extra', 'MAX', 'Narrow bandwidth FM-simplex services, 25 kHz channels']),
    (906500000, 906500001): (['Tech, General, Extra', 'MAX', 'National simplex frequency']),
    (907000000, 910000001): (['Tech, General, Extra', 'MAX', ' FM repeater inputs paired with 919-922 MHz; 119 pairs every 25 kHz; e.g., 907.025, 907.050, 907.075, etc., 908-920 MHz uncoordinated pair']),
    (910000000, 916000001): (['Tech, General, Extra', 'MAX', 'ATV']),
    (916000000, 918000001): (['Tech, General, Extra', 'MAX', 'Digital communications']),
    (918000000, 919000001): (['Tech, General, Extra', 'MAX', 'Narrow-bandwidth, FM control links and remote bases']),
    (919000000, 922000001): (['Tech, General, Extra', 'MAX', 'FM repeater outputs, paired with 907-910 MHz']),
    (922000000, 928000001): (['Tech, General, Extra', 'MAX', 'Wide-bandwidth experimental, simplex ATV, Spread Spectrum']),

    # 23 cm
    (1240000000, 1300000000): (['Tech, General, Extra', 'MAX', 'CW, Phone, Image, MCW, RTTY/Data']),
    ####

    # Higher
    (2300000000, 2310000000): (['Tech, General, Extra', 'MAX', 'No Designations']),
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

WIFI = RangeKeyDict({
    # 2.4ghz
    (1, 2): ('802.11b 2.4ghz Channel 1'),
    (2, 3): ('802.11b 2.4ghz Channel 2'),

    # 5ghz
    (2, 3): ('802.11a 5ghz Channel 36'),
})

SERVICES = RangeKeyDict({
    # CB
    (26965000, 27405001): ('Citizen Band (CB)'),

    # GMRS
    (462562500, 467725000): ('General Mobile Radio Service (GMRS)'),
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
})

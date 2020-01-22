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
    # 900mhz

    (902000000, 904000000): ('802.11ah 900Mhz (1-2 Mhz Bandwidth)'),
    (904000000, 920000001): ('802.11ah 900Mhz (1-16 Mhz Bandwidth)'),
    (920000000, 928000001): ('802.11ah 900Mhz (1-8 Mhz Bandwidth)'),

    # 2.4ghz
    (2401000000, 2423000001): ('802.11b 2.4ghz Channel 1 (2.412 Ghz Center)'),
    (2406000000, 2428000001): ('802.11b 2.4ghz Channel 2 (2.417 Ghz Center)'),
    (2411000000, 2433000001): ('802.11b 2.4ghz Channel 3 (2.422 Ghz Center)'),
    (2416000000, 2438000001): ('802.11b 2.4ghz Channel 4 (2.427 Ghz Center)'),
    (2421000000, 2443000001): ('802.11b 2.4ghz Channel 5 (2.432 Ghz Center)'),
    (2426000000, 2448000001): ('802.11b 2.4ghz Channel 6 (2.437 Ghz Center)'),
    (2431000000, 2453000001): ('802.11b 2.4ghz Channel 7 (2.442 Ghz Center)'),
    (2436000000, 2458000001): ('802.11b 2.4ghz Channel 8 (2.447 Ghz Center)'),
    (2441000000, 2463000001): ('802.11b 2.4ghz Channel 9 (2.452 Ghz Center)'),
    (2446000000, 2468000001): ('802.11b 2.4ghz Channel 10 (2.457 Ghz Center)'),
    (2451000000, 2473000001): ('802.11b 2.4ghz Channel 11 (2.462 Ghz Center)'),

    # 3.65ghz
    (3657500000, 3660000001): ('802.11y 3.65ghz Channel 131 (5Mhz Bandwidth)'),
    (3660000000, 3664500001): ('802.11y 3.65ghz Channel 132 (5-10mhz Bandwidth)'),
    (3665000000, 3667500001): ('802.11y 3.65ghz Channel 133 (5-20Mhz Bandwidth)'),
    (3670000000, 3672500001): ('802.11y 3.65ghz Channel 134 (5-10mhz Bandwidth)'),
    (3675000000, 3677500001): ('802.11y 3.65ghz Channel 135 (5mhz Bandwidth)'),
    (3680000000, 3682500001): ('802.11y 3.65ghz Channel 136 (5mhz Bandwidth)'),
    (3685000000, 3687500001): ('802.11y 3.65ghz Channel 137 (5-20mhz Bandwidth)'),
    (3690000000, 3692500001): ('802.11y 3.65ghz Channel 138 (5-10mhz Bandwidth)'),

    # 5ghz
    (5150000000, 5190000001): ('802.11a 5ghz Channel 32-34'),
    (5170000000, 5250000001): ('802.11a 5ghz Channel 36-48'),
    (5170000000, 5250000001): ('802.11a 5ghz Channel 42-46 DFS'),
    (5250000000, 5330000001): ('802.11a 5ghz Channel 52-64 DFS'),
    (5330000000, 5350000001): ('802.11a 5ghz Channel 68'),
    (5470000000, 5490000001): ('802.11a 5ghz Channel 96'),
    (5490000000, 5570000001): ('802.11a 5ghz Channel 100-112 DFS'),
    (5570000000, 5650000001): ('802.11a 5ghz Channel 116-128 DFS'),
    (5650000000, 5730000001): ('802.11a 5ghz Channel 132-144 DFS'),
    (5735000000, 5815000001): ('802.11a 5ghz Channel 149-161 DFS'),
    (5815000000, 5835000001): ('802.11a 5ghz Channel 165 DFS'),

    # 5.9ghz
    (5850000000, 5925000001): ('802.11p 5.9ghz (Reserved)'),

    # 60ghz
    (57240000000, 59400000001): ('802.11ad 60ghz WiGig Channel 1'),
    (59400000000, 61560000001): ('802.11ad 60ghz WiGig Channel 2'),
    (61560000000, 63720000001): ('802.11ad 60ghz WiGig Channel 3'),
    (63720000000, 65880000001): ('802.11ad 60ghz WiGig Channel 4'),
    (65880000000, 68040000001): ('802.11ad 60ghz WiGig Channel 5'),
    (68040000000, 70200000001): ('802.11ad 60ghz WiGig Channel 6'),
})

SERVICES = RangeKeyDict({
    # CB
    (26965000, 26975000): ('Citizen Band (CB) Channel 1'),
    (26975000, 26985000): ('Citizen Band (CB) Channel 2'),
    (26985000, 27005000): ('Citizen Band (CB) Channel 3'),
    (27005000, 27015000): ('Citizen Band (CB) Channel 4'),
    (27015000, 27025000): ('Citizen Band (CB) Channel 5'),
    (27025000, 27035000): ('Citizen Band (CB) Channel 6'),
    (27035000, 27055000): ('Citizen Band (CB) Channel 7'),
    (27055000, 27065000): ('Citizen Band (CB) Channel 8'),

    (27065000, 27075000): ('Citizen Band (CB) Channel 9 Emergency'),
    (27075000, 27085000): ('Citizen Band (CB) Channel 10'),
    (27085000, 27105000): ('Citizen Band (CB) Channel 11'),
    (27105000, 27115000): ('Citizen Band (CB) Channel 12'),
    (27115000, 27125000): ('Citizen Band (CB) Channel 13'),
    (27125000, 27135000): ('Citizen Band (CB) Channel 14'),
    (27135000, 27155000): ('Citizen Band (CB) Channel 15'),
    (27155000, 27165000): ('Citizen Band (CB) Channel 16'),
    (27165000, 27175000): ('Citizen Band (CB) Channel 17'),
    (27175000, 27185000): ('Citizen Band (CB) Channel 18'),

    (27185000, 27205000): ('Citizen Band (CB) Channel 19 Highway'),
    (27205000, 27215000): ('Citizen Band (CB) Channel 20'),
    (27215000, 27225000): ('Citizen Band (CB) Channel 21'),
    (27225000, 27235000): ('Citizen Band (CB) Channel 22'),
    (27235000, 27245000): ('Citizen Band (CB) Channel 24'),
    (27245000, 27255000): ('Citizen Band (CB) Channel 25'),
    (27255000, 27265000): ('Citizen Band (CB) Channel 23'),
    (27265000, 27275000): ('Citizen Band (CB) Channel 26'),
    (27275000, 27285000): ('Citizen Band (CB) Channel 27'),

    (27285000, 27295000): ('Citizen Band (CB) Channel 28'),
    (27295000, 27305000): ('Citizen Band (CB) Channel 29'),
    (27305000, 27315000): ('Citizen Band (CB) Channel 30'),
    (27315000, 27325000): ('Citizen Band (CB) Channel 31'),
    (27325000, 27335000): ('Citizen Band (CB) Channel 32'),
    (27335000, 27345000): ('Citizen Band (CB) Channel 33'),
    (27345000, 27355000): ('Citizen Band (CB) Channel 34'),
    (27355000, 27365000): ('Citizen Band (CB) Channel 35'),
    (27365000, 27375000): ('Citizen Band (CB) Channel 36'),
    (27375000, 27385000): ('Citizen Band (CB) Channel 37'),
    (27385000, 27395000): ('Citizen Band (CB) Channel 38'),
    (27395000, 27405000): ('Citizen Band (CB) Channel 39'),
    (27405000, 27415000): ('Citizen Band (CB) Channel 40'),

    # GMRS
    (462562500, 462587500): ('General Mobile Radio Service (GMRS) Channel 1 [5W]'),
    (462587500, 462612500): ('General Mobile Radio Service (GMRS) Channel 2 [5W]'),
    (462612500, 462637500): ('General Mobile Radio Service (GMRS) Channel 3 [5W]'),
    (462637500, 462662500): ('General Mobile Radio Service (GMRS) Channel 4 [5W]'),
    (462662500, 462687500): ('General Mobile Radio Service (GMRS) Channel 5 [5W]'),
    (462687500, 462712500): ('General Mobile Radio Service (GMRS) Channel 6 [5W]'),
    (462712500, 462742500): ('General Mobile Radio Service (GMRS) Channel 7 [5W]'),
    (467562500, 467587500): ('General Mobile Radio Service (GMRS) Channel 8 [0.5W]'),
    (467587500, 467612500): ('General Mobile Radio Service (GMRS) Channel 9 [0.5W]'),
    (467612500, 467637500): ('General Mobile Radio Service (GMRS) Channel 10 [0.5W]'),
    (467637500, 467662500): ('General Mobile Radio Service (GMRS) Channel 11 [0.5W]'),
    (467662500, 467687500): ('General Mobile Radio Service (GMRS) Channel 12 [0.5W]'),
    (467687500, 467712500): ('General Mobile Radio Service (GMRS) Channel 13 [0.5W]'),
    (467712500, 467737500): ('General Mobile Radio Service (GMRS) Channel 14 [0.5W]'),
    (462550000, 462575000): ('General Mobile Radio Service (GMRS) Channel 15 [50W]'),
    (462575000, 462600000): ('General Mobile Radio Service (GMRS) Channel 16 [50W]'),
    (462600000, 462625000): ('General Mobile Radio Service (GMRS) Channel 17 [50W]'),
    (462625000, 462650000): ('General Mobile Radio Service (GMRS) Channel 18 [50W]'),
    (462650000, 462675000): ('General Mobile Radio Service (GMRS) Channel 19 [50W]'),
    (462675000, 462700000): ('General Mobile Radio Service (GMRS) Channel 20 [50W]'),
    (462700000, 462725000): ('General Mobile Radio Service (GMRS) Channel 21 [50W]'),
    (462725000, 462750000): ('General Mobile Radio Service (GMRS) Channel 22 [50W]'),
    (467550000, 467575000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467575000, 467600000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467600000, 467625000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467625000, 467650000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467650000, 467675000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467675000, 467700000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467700000, 467725000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),
    (467725000, 467750000): ('General Mobile Radio Service (GMRS) Repeater Input [50W]'),

    # Aircraft Band
    (108000000, 137000001): ("VHF Aircraft band"),
    (225000000, 399950001): ("UHF Military aircraft band"),
    (243000000, 243000001): ("Military emergency & guard channel"),
    (190000, 415001): ("Low frequency non-directional beacons"),
    (510000, 535001): ("Medium frequency non-directional beacons"),
    (329300000, 335000001): ("UHF Aircraft ILS glide path"),
    (75000000, 75000001): ("Aircraft ILS marker beacons"),
    (962000000, 1150000001): ("Distance Measuring Equipment"),
    (1575420000, 1585650001): ("GPS L1 Receive Satellite Frequency"),
    (1227600000, 1237830001): ("GPS L2 Receive Satellite Frequency"),

    # Cellular
    (710000000, 716000001): ("Cellular AT&T LTE (Lower band)"),
    (740000000, 746000001): ("Cellular AT&T LTE (Lower band)"),
    (710000000, 716000001): ("Cellular AT&T LTE (Lower band)"),
    (746000000, 757000001): ("Cellular AT&T LTE (Higher band)"),
    (776000000, 787000001): ("Cellular AT&T LTE (Higher band)"),
    (806000000, 869000001): ("Cellular Old Nextel-Soon to be LTE 4G"),
    (824000000, 896000001): ("Cellular Traditional"),
    (896000000, 940000001): ("Cellular New Nextel SMR/iDEN"),
    (1710000000, 1755000001): ("Cellular AWS T-Mobile 3G/4G (UTMS Band 4)"),
    (2110000000, 2155000001): ("Cellular AWS T-Mobile 3G/4G (UTMS Band 4)"),
    (1850000000, 1990000001): ("Cellular Traditional PCS Sprint 4G/LTE WiMax"),
    (2500000000, 2700000001): ("Cellular Sprint/Clear 4G/LTE WiMax"),
})

BROADCAST = RangeKeyDict({
    (148500, 283501): ('Longwave AM Radio International'),
    (535000, 1710001): ('Mediumwave AM Radio US'),
    (2300000, 2495000): ('Medium Frequency Radio International'),
    (3800000, 4000000): ('High Frequency Radio International'),
    (4750000, 5060000): ('High Frequency Radio International'),
    (5950000, 6200000): ('High Frequency Radio US'),
    (7100000, 7300000): ('High Frequency Radio US'),
    (9500000, 9900000): ('High Frequency Radio US'),
    (11650000, 12050000): ('High Frequency Radio US'),
    (13600000, 13800000): ('High Frequency Radio US'),
    (15100000, 15600000): ('High Frequency Radio US'),
    (17550000, 17900000): ('High Frequency Radio US'),
    (21450000, 21850000): ('High Frequency Radio US'),
    (25600000, 26100000): ('High Frequency Radio US'),
    # (3000000, 30000001): 'Shortwave AM Radio',
    (155500000, 174000001): ('Marine VHF'),
    (47000000, 68000001): ('VHF Television'),
    (470000000, 582000001): ('UHF Television'),
    (582000000, 862000000): ('UHF Television'),
    (87500000, 108000001): ('FM Radio'),
    (2182000, 2182001): ('Marine Emergency'),
    (285000, 315501): ('Aviation'),
    (340000, 350001): ('Aviation SSB'),
})

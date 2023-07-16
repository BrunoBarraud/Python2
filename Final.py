import random 

grupos = {
    'Grupo A': [
        {'fecha': '21-nov', 'hora': '10:00', 'lugar': 'Al Bayt', 'pais_1': 'Qatar', 'pais_2': 'Ecuador'},
        {'fecha': '21-nov', 'hora': '04:00', 'lugar': 'Al Thumama', 'pais_1': 'Senegal', 'pais_2': 'Países Bajos'},
        {'fecha': '25-nov', 'hora': '07:00', 'lugar': 'Al Thumama', 'pais_1': 'Qatar', 'pais_2': 'Senegal'},
        {'fecha': '25-nov', 'hora': '10:00', 'lugar': 'Khalifa International', 'pais_1': 'Países Bajos', 'pais_2': 'Ecuador'},
        {'fecha': '29-nov', 'hora': '09:00', 'lugar': 'Al Bayt', 'pais_1': 'Países Bajos', 'pais_2': 'Qatar'},
        {'fecha': '29-nov', 'hora': '09:00', 'lugar': 'Khalifa International', 'pais_1': 'Ecuador', 'pais_2': 'Senegal'}
    ],
    'Grupo B': [
        {'fecha': '21-nov', 'hora': '07:00', 'lugar': 'Khalifa International', 'pais_1': 'Inglaterra', 'pais_2': 'Irán'},
        {'fecha': '21-nov', 'hora': '13:00', 'lugar': 'Ahmad Bin Ali', 'pais_1': 'Estados Unidos', 'pais_2': 'Gales'},
        {'fecha': '25-nov', 'hora': '13:00', 'lugar': 'Al Bayt', 'pais_1': 'Inglaterra', 'pais_2': 'Estados Unidos'},
        {'fecha': '25-nov', 'hora': '04:00', 'lugar': 'Ahmad Bin Ali', 'pais_1': 'Gales', 'pais_2': 'Irán'},
        {'fecha': '29-nov', 'hora': '13:00', 'lugar': 'Ahmad Bin Ali', 'pais_1': 'Gales', 'pais_2': 'Inglaterra'},
        {'fecha': '29-nov', 'hora': '13:00', 'lugar': 'Al Thumama', 'pais_1': 'Irán', 'pais_2': 'Estados Unidos'}
    ],
    'Grupo C': [
        {'fecha': '22-nov', 'hora': '04:00', 'lugar': 'Lusail Iconic', 'pais_1': 'Argentina', 'pais_2': 'Arabia Saudí'},
        {'fecha': '22-nov', 'hora': '10:00', 'lugar': 'Stadium 974', 'pais_1': 'México', 'pais_2': 'Polonia'},
        {'fecha': '26-nov', 'hora': '13:00', 'lugar': 'Lusail Iconic', 'pais_1': 'Argentina', 'pais_2': 'México'},
        {'fecha': '26-nov', 'hora': '07:00', 'lugar': 'Education City', 'pais_1': 'Polonia', 'pais_2': 'Arabia Saudí'},
        {'fecha': '30-nov', 'hora': '13:00', 'lugar': 'Stadium 974', 'pais_1': 'Polonia', 'pais_2': 'Argentina'},
        {'fecha': '30-nov', 'hora': '13:00', 'lugar': 'Lusail Iconic', 'pais_1': 'Arabia Saudí', 'pais_2': 'México'}
    ],
    'Grupo D': [
        {'fecha': '22-nov', 'hora': '13:00', 'lugar': 'Al Janoub', 'pais_1': 'Francia', 'pais_2': 'Australia'},
        {'fecha': '22-nov', 'hora': '07:00', 'lugar': 'Education City', 'pais_1': 'Dinamarca', 'pais_2': 'Túnez'},
        {'fecha': '02-nov', 'hora': '10:00', 'lugar': 'Stadium 974', 'pais_1': 'Francia', 'pais_2': 'Dinamarca'},
        {'fecha': '26-nov', 'hora': '96:00', 'lugar': 'Al Janoub', 'pais_1': 'Túnez', 'pais_2': 'Australia'},
        {'fecha': '30-nov', 'hora': '09:00', 'lugar': 'Education City', 'pais_1': 'Túnez', 'pais_2': 'Francia'},
        {'fecha': '30-nov', 'hora': '09:00', 'lugar': 'Al Janoub', 'pais_1': 'Australia', 'pais_2': 'Dinamarca'}
    ],
    'Grupo E': [
        {'fecha': '23-nov', 'hora': '10:00', 'lugar': 'Al Thumama', 'pais_1': 'España', 'pais_2': 'Costa Rica'},
        {'fecha': '23-nov', 'hora': '07:00', 'lugar': 'Khalifa International', 'pais_1': 'Alemania', 'pais_2': 'Japón'},
        {'fecha': '27-nov', 'hora': '13:00', 'lugar': 'Al Bayt', 'pais_1': 'España', 'pais_2': 'Alemania'},
        {'fecha': '27-nov', 'hora': '04:00', 'lugar': 'Ahmad Bin Ali', 'pais_1': 'Japón', 'pais_2': 'Costa Rica'},
        {'fecha': '01-dic', 'hora': '13:00', 'lugar': 'Khalifa International', 'pais_1': 'Japón', 'pais_2': 'España'},
        {'fecha': '01-dic', 'hora': '13:00', 'lugar': 'Al Bayt', 'pais_1': 'Costa Rica', 'pais_2': 'Alemania'}
    ],
    'Grupo F': [
        {'fecha': '23-nov', 'hora': '13:00', 'lugar': 'Ahmad Bin Ali', 'pais_1': 'Bélgica', 'pais_2': 'Canadá'},
        {'fecha': '23-nov', 'hora': '04:00', 'lugar': 'Al Bayt', 'pais_1': 'Marruecos', 'pais_2': 'Croacia'},
        {'fecha': '27-nov', 'hora': '07:00', 'lugar': 'Al Thumama', 'pais_1': 'Bélgica', 'pais_2': 'Marruecos'},
        {'fecha': '27-nov', 'hora': '10:00', 'lugar': 'Khalifa International', 'pais_1': 'Croacia', 'pais_2': 'Canadá'},
        {'fecha': '01-dic', 'hora': '09:00', 'lugar': 'Ahmad Bin Ali', 'pais_1': 'Croacia', 'pais_2': 'Bélgica'},
        {'fecha': '01-dic', 'hora': '09:00', 'lugar': 'Al Thumama', 'pais_1': 'Canadá', 'pais_2': 'Marruecos'}
    ],
    'Grupo G': [
        {'fecha': '24-nov', 'hora': '13:00', 'lugar': 'Lusail Iconic Stadium', 'pais_1': 'Brasil', 'pais_2': 'Serbia'},
        {'fecha': '24-nov', 'hora': '04:00', 'lugar': 'Al Janoub', 'pais_1': 'Suiza', 'pais_2': 'Camerún'},
        {'fecha': '28-nov', 'hora': '10:00', 'lugar': 'Stadium 974', 'pais_1': 'Brasil', 'pais_2': 'Suiza'},
        {'fecha': '28-nov', 'hora': '04:00', 'lugar': 'Al Janoub', 'pais_1': 'Camerún', 'pais_2': 'Serbia'},
        {'fecha': '02-dic', 'hora': '13:00', 'lugar': 'Lusail Iconic', 'pais_1': 'Camerún', 'pais_2': 'Brasil'},
        {'fecha': '02-dic', 'hora': '13:00', 'lugar': 'Stadium 974', 'pais_1': 'Serbia', 'pais_2': 'Suiza'}
    ],
    'Grupo H': [
        {'fecha': '24-nov', 'hora': '10:00', 'lugar': 'Stadium 974', 'pais_1': 'Portugal', 'pais_2': 'Ghana'},
        {'fecha': '24-nov', 'hora': '07:00', 'lugar': 'Education City', 'pais_1': 'Uruguay', 'pais_2': 'Corea del Sur'},
        {'fecha': '28-nov', 'hora': '13:00', 'lugar': 'Lusail Iconic', 'pais_1': 'Portugal', 'pais_2': 'Uruguay'},
        {'fecha': '28-nov', 'hora': '07:00', 'lugar': 'Education City', 'pais_1': 'Corea del Sur', 'pais_2': 'Ghana'},
        {'fecha': '02-dic', 'hora': '09:00', 'lugar': 'Education City', 'pais_1': 'Corea del Sur', 'pais_2': 'Portugal'},
        {'fecha': '02-dic', 'hora': '09:00', 'lugar': 'Al Janoub', 'pais_1': 'Ghana', 'pais_2': 'Uruguay'}
    ]
}

fifa_rank = [
    {'nro': 1, 'pais': 'BelgiumBEL', 'puntos': 1783.38},
    {'nro': 2, 'pais': 'BrazilBRA', 'puntos': 1743.45},
    {'nro': 3, 'pais': 'EnglandENG', 'puntos': 1670.5},
    {'nro': 4, 'pais': 'FranceFRA', 'puntos': 1659.22},
    {'nro': 5, 'pais': 'ItalyITA', 'puntos': 1643.82},
    {'nro': 6, 'pais': 'ArgentinaARG', 'puntos': 1642.65},
    {'nro': 7, 'pais': 'PortugalPOR', 'puntos': 1631.05},
    {'nro': 8, 'pais': 'SpainESP', 'puntos': 1617.14},
    {'nro': 9, 'pais': 'MexicoMEX', 'puntos': 1608.94},
    {'nro': 10, 'pais': 'DenmarkDEN', 'puntos': 1604.58},
    {'nro': 11, 'pais': 'GermanyGER', 'puntos': 1602.98},
    {'nro': 12, 'pais': 'NetherlandsNED', 'puntos': 1597.32},
    {'nro': 13, 'pais': 'UruguayURU', 'puntos': 1594.23},
    {'nro': 14, 'pais': 'CroatiaCRO', 'puntos': 1589.93},
    {'nro': 15, 'pais': 'ColombiaCOL', 'puntos': 1575.81},
    {'nro': 16, 'pais': 'SwitzerlandSUI', 'puntos': 1568.88},
    {'nro': 17, 'pais': 'ChileCHI', 'puntos': 1559.19},
    {'nro': 18, 'pais': 'SwedenSWE', 'puntos': 1552.12},
    {'nro': 19, 'pais': 'PeruPER', 'puntos': 1549.09},
    {'nro': 20, 'pais': 'WalesWAL', 'puntos': 1539.55},
    {'nro': 21, 'pais': 'JapanJPN', 'puntos': 1530.39},
    {'nro': 22, 'pais': 'UkraineUKR', 'puntos': 1517.02},
    {'nro': 23, 'pais': 'AustriaAUT', 'puntos': 1507.33},
    {'nro': 24, 'pais': 'TurkeyTUR', 'puntos': 1500.6},
    {'nro': 25, 'pais': 'SenegalSEN', 'puntos': 1496.67},
    {'nro': 26, 'pais': 'USAUSA', 'puntos': 1493.83},
    {'nro': 27, 'pais': 'SerbiaSRB', 'puntos': 1488.35},
    {'nro': 28, 'pais': 'PolandPOL', 'puntos': 1483.29},
    {'nro': 29, 'pais': 'ParaguayPAR', 'puntos': 1473.62},
    {'nro': 30, 'pais': 'NigeriaNGA', 'puntos': 1466.9},
    {'nro': 31, 'pais': 'AlgeriaALG', 'puntos': 1463.24},
    {'nro': 32, 'pais': 'GreeceGRE', 'puntos': 1462.48},
    {'nro': 33, 'pais': 'VenezuelaVEN', 'puntos': 1455.67},
    {'nro': 34, 'pais': 'SlovakiaSVK', 'puntos': 1443.41},
    {'nro': 35, 'pais': 'Czech RepublicCZE', 'puntos': 1442.61},
    {'nro': 36, 'pais': 'IranIRN', 'puntos': 1439.33},
    {'nro': 37, 'pais': 'HungaryHUN', 'puntos': 1437.68},
    {'nro': 38, 'pais': 'EcuadorECU', 'puntos': 1435.68},
    {'nro': 39, 'pais': 'Costa RicaCRC', 'puntos': 1432.79},
    {'nro': 40, 'pais': 'SloveniaSVN', 'puntos': 1431.06},
    {'nro': 41, 'pais': 'IsraelISR', 'puntos': 1425.41},
    {'nro': 42, 'pais': 'MontenegroMNE', 'puntos': 1421.91},
    {'nro': 43, 'pais': 'China PRCHN', 'puntos': 1421.07},
    {'nro': 44, 'pais': 'PanamaPAN', 'puntos': 1420.16},
    {'nro': 45, 'pais': 'FinlandFIN', 'puntos': 1419.45},
    {'nro': 46, 'pais': 'HondurasHON', 'puntos': 1418.44},
    {'nro': 47, 'pais': 'AlbaniaALB', 'puntos': 1413.91},
    {'nro': 48, 'pais': 'Bosnia and HerzegovinaBIH', 'puntos': 1411.56},
    {'nro': 49, 'pais': 'JamaicaJAM', 'puntos': 1408.86},
    {'nro': 50, 'pais': 'UzbekistanUZB', 'puntos': 1407.45},
    {'nro': 51, 'pais': 'RomaniaROU', 'puntos': 1403.23},
    {'nro': 52, 'pais': 'United Arab EmiratesUAE', 'puntos': 1396.59},
    {'nro': 53, 'pais': 'Northern IrelandNIR', 'puntos': 1392.24},
    {'nro': 54, 'pais': 'SyriaSYR', 'puntos': 1391.93},
    {'nro': 55, 'pais': 'GeorgiaGEO', 'puntos': 1391.47},
    {'nro': 56, 'pais': 'El SalvadorSLV', 'puntos': 1391.41},
    {'nro': 57, 'pais': 'MadagascarMAD', 'puntos': 1390.96},
    {'nro': 58, 'pais': 'LithuaniaLTU', 'puntos': 1387.9},
    {'nro': 59, 'pais': 'KosovoKVX', 'puntos': 1385.85},
    {'nro': 60, 'pais': 'MoroccoMAR', 'puntos': 1384.57},
    {'nro': 61, 'pais': 'Trinidad and TobagoTRI', 'puntos': 1381.26},
    {'nro': 62, 'pais': 'EgyptEGY', 'puntos': 1380.17},
    {'nro': 63, 'pais': 'TunisiaTUN', 'puntos': 1376.48},
    {'nro': 64, 'pais': 'MaliMLI', 'puntos': 1375.42},
    {'nro': 65, 'pais': 'South AfricaRSA', 'puntos': 1375.21},
    {'nro': 66, 'pais': 'Cape VerdeCPV', 'puntos': 1373.67},
    {'nro': 67, 'pais': 'QatarQAT', 'puntos': 1373.53},
    {'nro': 68, 'pais': 'IraqIRQ', 'puntos': 1368.41},
    {'nro': 69, 'pais': 'MoldovaMDA', 'puntos': 1368.32},
    {'nro': 70, 'pais': 'BoliviaBOL', 'puntos': 1365.17},
    {'nro': 71, 'pais': 'JordanJOR', 'puntos': 1364.11},
    {'nro': 72, 'pais': 'Korea RepublicKOR', 'puntos': 1360.66},
    {'nro': 73, 'pais': 'BulgariaBUL', 'puntos': 1360.47},
    {'nro': 74, 'pais': 'AzerbaijanAZE', 'puntos': 1359.15},
    {'nro': 75, 'pais': 'ScotlandSCO', 'puntos': 1356.56},
    {'nro': 76, 'pais': 'MacedoniaMKD', 'puntos': 1354.86},
    {'nro': 77, 'pais': 'CongoCGO', 'puntos': 1353.62},
    {'nro': 78, 'pais': 'GuineaGIN', 'puntos': 1353.47},
    {'nro': 79, 'pais': 'Sierra LeoneSLE', 'puntos': 1352.99},
    {'nro': 80, 'pais': 'CyprusCYP', 'puntos': 1352.76},
    {'nro': 81, 'pais': 'CuraçaoCUW', 'puntos': 1351.69},
    {'nro': 82, 'pais': 'EstoniaEST', 'puntos': 1348.66},
    {'nro': 83, 'pais': 'ArmeniaARM', 'puntos': 1346.56},
    {'nro': 84, 'pais': 'KuwaitKUW', 'puntos': 1346.2},
    {'nro': 85, 'pais': 'Faroe IslandsFRO', 'puntos': 1345.44},
    {'nro': 86, 'pais': 'IndiaIND', 'puntos': 1345.16},
    {'nro': 87, 'pais': 'BermudaBER', 'puntos': 1344.56},
    {'nro': 88, 'pais': 'GambiaGAM', 'puntos': 1344.5},
    {'nro': 89, 'pais': 'KazakhstanKAZ', 'puntos': 1343.36},
    {'nro': 90, 'pais': 'ZambiaZAM', 'puntos': 1341.74},
    {'nro': 91, 'pais': 'SurinameSUR', 'puntos': 1340.68},
    {'nro': 92, 'pais': 'BotswanaBOT', 'puntos': 1340.24},
    {'nro': 93, 'pais': 'LebanonLBN', 'puntos': 1339.84},
    {'nro': 94, 'pais': 'ThailandTHA', 'puntos': 1339.65},
    {'nro': 95, 'pais': 'Saint Kitts and NevisSKN', 'puntos': 1339.45},
    {'nro': 96, 'pais': 'Hong KongHKG', 'puntos': 1339.34},
    {'nro': 97, 'pais': 'EthiopiaETH', 'puntos': 1337.3},
    {'nro': 98, 'pais': 'LiberiaLBR', 'puntos': 1337.19},
    {'nro': 99, 'pais': 'BarbadosBRB', 'puntos': 1337.04},
    {'nro': 100, 'pais': 'MalawiMWI', 'puntos': 1336.54},
    {'nro': 101, 'pais': 'HaitiHAI', 'puntos': 1336.15},
    {'nro': 102, 'pais': 'KenyaKEN', 'puntos': 1335.96},
    {'nro': 103, 'pais': 'LatviaLVA', 'puntos': 1335.36},
    {'nro': 104, 'pais': 'AngolaANG', 'puntos': 1334.85},
    {'nro': 105, 'pais': 'IndonesiaIDN', 'puntos': 1334.39},
    {'nro': 106, 'pais': 'MalaysiaMAS', 'puntos': 1334.19},
    {'nro': 107, 'pais': 'Equatorial GuineaGEQ', 'puntos': 1332.72},
    {'nro': 108, 'pais': 'MozambiqueMOZ', 'puntos': 1332.37},
    {'nro': 109, 'pais': 'LithuaniaLTU', 'puntos': 1332.17},
    {'nro': 110, 'pais': 'CubaCUB', 'puntos': 1331.56},
    {'nro': 111, 'pais': 'RwandaRWA', 'puntos': 1331.19},
    {'nro': 112, 'pais': 'BahrainBHR', 'puntos': 1327.95},
    {'nro': 113, 'pais': 'GuatemalaGUA', 'puntos': 1327.66},
    {'nro': 114, 'pais': 'ZimbabweZIM', 'puntos': 1327.39},
    {'nro': 115, 'pais': 'GrenadaGRN', 'puntos': 1327.27},
    {'nro': 116, 'pais': 'NamibiaNAM', 'puntos': 1326.47},
    {'nro': 117, 'pais': 'TajikistanTJK', 'puntos': 1326.2},
    {'nro': 118, 'pais': 'Dominican RepublicDOM', 'puntos': 1326.1},
    {'nro': 119, 'pais': 'KosovoKVX', 'puntos': 1325.97},
    {'nro': 120, 'pais': 'PalestinePLE', 'puntos': 1325.92},
    {'nro': 121, 'pais': 'CongoDR CongoCOD', 'puntos': 1325.9},
    {'nro': 122, 'pais': 'Central African RepublicCTA', 'puntos': 1325.83},
    {'nro': 123, 'pais': 'BeninBEN', 'puntos': 1325.77},
    {'nro': 124, 'pais': 'NigerNGR', 'puntos': 1325.56},
    {'nro': 125, 'pais': 'Antigua and BarbudaANT', 'puntos': 1325.36},
    {'nro': 126, 'pais': 'TanzaniaTAN', 'puntos': 1324.64},
    {'nro': 127, 'pais': 'Guinea-BissauGBS', 'puntos': 1324.34},
    {'nro': 128, 'pais': 'VietnamVIE', 'puntos': 1324.29},
    {'nro': 129, 'pais': 'LaosLAO', 'puntos': 1324.24},
    {'nro': 130, 'pais': 'LiechtensteinLIE', 'puntos': 1324.22},
    {'nro': 131, 'pais': 'SwazilandSWZ', 'puntos': 1324.08},
    {'nro': 132, 'pais': 'GuamGUM', 'puntos': 1324.04},
    {'nro': 133, 'pais': 'ComorosCOM', 'puntos': 1323.89},
    {'nro': 134, 'pais': 'São Tomé and PríncipeSTP', 'puntos': 1323.81},
    {'nro': 135, 'pais': 'FijiFIJ', 'puntos': 1323.8},
    {'nro': 136, 'pais': 'LuxembourgLUX', 'puntos': 1323.67},
    {'nro': 137, 'pais': 'AndorraAND', 'puntos': 1323.61},
    {'nro': 138, 'pais': 'SurinameSUR', 'puntos': 1323.6},
    {'nro': 139, 'pais': 'BotswanaBOT', 'puntos': 1323.59},
    {'nro': 140, 'pais': 'VanuatuVAN', 'puntos': 1323.47},
    {'nro': 141, 'pais': 'CambodiaCAM', 'puntos': 1323.39},
    {'nro': 142, 'pais': 'LesothoLES', 'puntos': 1323.38},
    {'nro': 143, 'pais': 'BhutanBHU', 'puntos': 1323.34},
    {'nro': 144, 'pais': 'SeychellesSEY', 'puntos': 1323.33},
    {'nro': 145, 'pais': 'MacauMAC', 'puntos': 1323.24},
    {'nro': 146, 'pais': 'DominicaDMA', 'puntos': 1323.23},
    {'nro': 147, 'pais': 'Turks and Caicos IslandsTCA', 'puntos': 1323.19},
    {'nro': 148, 'pais': 'MyanmarMYA', 'puntos': 1323.18},
    {'nro': 149, 'pais': 'TahitiTAH', 'puntos': 1323.15}, 
    {'nro': 150, 'pais': 'MaldivesMDV', 'puntos': 1323.1},
    {'nro': 151, 'pais': 'South SudanSSD', 'puntos': 1323.09},
    {'nro': 152, 'pais': 'BruneiBNR', 'puntos': 1323.08},
    {'nro': 153, 'pais': 'East TimorTLS', 'puntos': 1323.08},
    {'nro': 154, 'pais': 'US Virgin IslandsVIR', 'puntos': 1323.08},
    {'nro': 155, 'pais': 'AnguillaAIA', 'puntos': 1323.08},
    {'nro': 156, 'pais': 'SamoaSAM', 'puntos': 1323.08},
    {'nro': 157, 'pais': 'Papua New GuineaPNG', 'puntos': 1323.08},
    {'nro': 158, 'pais': 'San MarinoSMR', 'puntos': 1323.08},
    {'nro': 159, 'pais': 'American SamoaASA', 'puntos': 1323.08},
    {'nro': 160, 'pais': 'TongaTGA', 'puntos': 1323.08},
    {'nro': 161, 'pais': 'EritreaERI', 'puntos': 1323.08},
    {'nro': 162, 'pais': 'Cook IslandsCOK', 'puntos': 1323.08},
    {'nro': 163, 'pais': 'MontserratMNT', 'puntos': 1323.08},
    {'nro': 164, 'pais': 'BelizeBLZ', 'puntos': 1323.08},
    {'nro': 165, 'pais': 'GibraltarGIB', 'puntos': 1323.08},
    {'nro': 166, 'pais': 'Sint MaartenSXM', 'puntos': 1323.08},
    {'nro': 167, 'pais': 'British Virgin IslandsVGB', 'puntos': 1323.08},
    {'nro': 168, 'pais': 'TurkmenistanTKM', 'puntos': 1323.08},
    {'nro': 169, 'pais': 'Isle of ManIOM', 'puntos': 1323.08},
    {'nro': 170, 'pais': 'GuernseyGCI', 'puntos': 1323.08},
    {'nro': 171, 'pais': 'JerseyJEY', 'puntos': 1323.08},
    {'nro': 172, 'pais': 'Faroe IslandsFRO', 'puntos': 1323.08},
    {'nro': 173, 'pais': 'MonacoMON', 'puntos': 1323.08},
    {'nro': 174, 'pais': 'LiechtensteinLIE', 'puntos': 1323.08},
    {'nro': 175, 'pais': 'SeychellesSEY', 'puntos': 1323.08},
    {'nro': 176, 'pais': 'AndorraAND', 'puntos': 1323.08},
    {'nro': 177, 'pais': 'San MarinoSMR', 'puntos': 1323.08},
    {'nro': 178, 'pais': 'MongoliaMNG', 'puntos': 1323.08},
    {'nro': 179, 'pais': 'Turks and Caicos IslandsTCA', 'puntos': 1323.08},
    {'nro': 180, 'pais': 'British Virgin IslandsVGB', 'puntos': 1323.08},
    {'nro': 181, 'pais': 'ComorosCOM', 'puntos': 1323.08},
    {'nro': 182, 'pais': 'MontserratMNT', 'puntos': 1323.08},
    {'nro': 183, 'pais': 'Cayman IslandsCAY', 'puntos': 1323.08},
    {'nro': 184, 'pais': 'Northern Mariana IslandsNMI', 'puntos': 1323.08},
    {'nro': 185, 'pais': 'BahamasBAH', 'puntos': 1323.08},
    {'nro': 186, 'pais': 'Saint LuciaLCA', 'puntos': 1323.08},
    {'nro': 187, 'pais': 'ArubaARU', 'puntos': 1323.08},
    {'nro': 188, 'pais': 'GrenadaGRN', 'puntos': 1323.08},
    {'nro': 189, 'pais': 'BermudaBER', 'puntos': 1323.08},
    {'nro': 190, 'pais': 'Saint Vincent and the GrenadinesVIN', 'puntos': 1323.08},
    {'nro': 191, 'pais': 'São Tomé and PríncipeSTP', 'puntos': 1323.08},
    {'nro': 192, 'pais': 'DominicaDMA', 'puntos': 1323.08},
    {'nro': 193, 'pais': 'AnguillaAIA', 'puntos': 1323.08},
    {'nro': 194, 'pais': 'TurkmenistanTKM', 'puntos': 1323.08},
    {'nro': 195, 'pais': 'GuamGUM', 'puntos': 1323.08},
    {'nro': 196, 'pais': 'American SamoaASA', 'puntos': 1323.08},
    {'nro': 197, 'pais': 'US Virgin IslandsVIR', 'puntos': 1323.08},
    {'nro': 198, 'pais': 'SamoaSAM', 'puntos': 1323.08},
    {'nro': 199, 'pais': 'Papua New GuineaPNG', 'puntos': 1323.08},
    {'nro': 200, 'pais': 'TongaTGA', 'puntos': 1323.08},
    {'nro' : 201, 'pais' : 'GibraltarGIB', 'puntos' : 856.55},
	{'nro' : 202, 'pais' : 'EritreaERI', 'puntos' : 855.56},
	{'nro' : 203, 'pais' : 'ArubaARU', 'puntos' : 855.37},
	{'nro' : 204, 'pais' : 'BahamasBAH', 'puntos' : 854.8},
	{'nro' : 205, 'pais' : 'GuamGUM', 'puntos' : 838.33},
	{'nro' : 206, 'pais' : 'Turks and Caicos IslandsTCA', 'puntos' : 832},
	{'nro' : 207, 'pais' : 'Sri LankaSRI', 'puntos' : 825.25},
	{'nro' : 208, 'pais' : 'US Virgin IslandsVIR', 'puntos' : 823.97},
	{'nro' : 209, 'pais' : 'British Virgin IslandsVGB', 'puntos' : 809.32},
	{'nro' : 210, 'pais' : 'AnguillaAIA', 'puntos' : 790.74},
	{'nro' : 211, 'pais' : 'San MarinoSMR', 'puntos' : 763.82},
]

resultado = [
	{'nro': 1, 'pais1': 'ArgentinaARG', 'puntos1': 1770.65, 'pais2': 'BrazilBRA', 'puntos2': 1837.56},
	{'nro': 2, 'pais1': 'BrazilBRA', 'puntos1': 990.5, 'pais2': 'UruguayURU', 'puntos2': 1643.71},
	{'nro': 3, 'pais1': 'UruguayURU', 'puntos1': 1643.71, 'pais2': 'EnglandENG', 'puntos2': 1737.46},
	{'nro': 4, 'pais1': 'EnglandENG', 'puntos1': 1737.46, 'pais2': 'SpainESP', 'puntos2': 1716.93},
	{'nro': 5, 'pais1': 'SpainESP', 'puntos1': 1716.93, 'pais2': 'GermanyGER', 'puntos2': 1658.96},
	{'nro': 6, 'pais1': 'GermanyGER', 'puntos1': 1658.96, 'pais2': 'NetherlandsNED', 'puntos2': 1679.41},
	{'nro': 7, 'pais1': 'NetherlandsNED', 'puntos1': 1679.41, 'pais2': 'BelgiumBEL', 'puntos2': 1821.92},
	{'nro': 8, 'pais1': 'BelgiumBEL', 'puntos1': 1821.92, 'pais2': 'PortugalPOR', 'puntos2': 1678.65},
	{'nro': 9, 'pais1': 'PortugalPOR', 'puntos1': 1678.65, 'pais2': 'ItalyITA', 'puntos2': 1713.86},
	{'nro': 10, 'pais1': 'ItalyITA', 'puntos1': 1713.86, 'pais2': 'SwitzerlandSUI', 'puntos2': 1621.43},
	{'nro': 11, 'pais1': 'SwitzerlandSUI', 'puntos1': 1621.43, 'pais2': 'FranceFRA', 'puntos2': 1764.85},
	{'nro': 12, 'pais1': 'FranceFRA', 'puntos1': 1764.85, 'pais2': 'WalesWAL', 'puntos2': 1582.13},
	{'nro': 13, 'pais1': 'WalesWAL', 'puntos1': 1582.13, 'pais2': 'BhutanBHU', 'puntos2': 910.96},
	{'nro': 14, 'pais1': 'BhutanBHU', 'puntos1': 910.96, 'pais2': 'NigeriaNGA', 'puntos2': 1504.7},
	{'nro': 15, 'pais1': 'NigeriaNGA', 'puntos1': 1504.7, 'pais2': 'IcelandISL', 'puntos2': 1379.61},
	{'nro': 16, 'pais1': 'IcelandISL', 'puntos1': 1379.61, 'pais2': 'SwedenSWE', 'puntos2': 1563.44},
	{'nro': 17, 'pais1': 'SwedenSWE', 'puntos1': 1563.44, 'pais2': 'BelarusBLR', 'puntos2': 1226.55},
	{'nro': 18, 'pais1': 'BelarusBLR', 'puntos1': 1226.55, 'pais2': 'AlbaniaALB', 'puntos2': 1361.81},
	{'nro': 19, 'pais1': 'AlbaniaALB', 'puntos1': 1361.81, 'pais2': 'AustriaAUT', 'puntos2': 1502.47},
	{'nro': 20, 'pais1': 'AustriaAUT', 'puntos1': 1502.47, 'pais2': 'RussiaRUS', 'puntos2': 1493.42},
	{'nro': 21, 'pais1': 'RussiaRUS', 'puntos1': 1493.42, 'pais2': 'PolandPOL', 'puntos2': 1546.18},
	{'nro': 22, 'pais1': 'PolandPOL', 'puntos1': 1546.18, 'pais2': 'SenegalSEN', 'puntos2': 1593.45},
	{'nro': 23, 'pais1': 'SenegalSEN', 'puntos1': 1593.45, 'pais2': 'ColombiaCOL', 'puntos2': 1604.07},
	{'nro': 24, 'pais1': 'ColombiaCOL', 'puntos1': 1604.07, 'pais2': 'CameroonCMR', 'puntos2': 1484.95},
	{'nro': 25, 'pais1': 'CameroonCMR', 'puntos1': 1484.95, 'pais2': 'MoroccoMAR', 'puntos2': 1558.9},
	{'nro': 26, 'pais1': 'MoroccoMAR', 'puntos1': 1558.9, 'pais2': 'IranIRN', 'puntos2': 1558.64},
	{'nro': 27, 'pais1': 'IranIRN', 'puntos1': 1558.64, 'pais2': 'CameroonCMR', 'puntos2': 1484.95},
	{'nro': 28, 'pais1': 'CameroonCMR', 'puntos1': 1484.95, 'pais2': 'AustraliaAUS', 'puntos2': 1483.73},
	{'nro': 29, 'pais1': 'AustraliaAUS', 'puntos1': 1483.73, 'pais2': 'GhanaGHA', 'puntos2': 1389.68},
	{'nro': 30, 'pais1': 'GhanaGHA', 'puntos1': 1389.68, 'pais2': 'AlgeriaALG', 'puntos2': 1480.59},
	{'nro': 31, 'pais1': 'AlgeriaALG', 'puntos1': 1480.59, 'pais2': 'EgyptEGY', 'puntos2': 1482.63},
	{'nro': 32, 'pais1': 'EgyptEGY', 'puntos1': 1482.63, 'pais2': 'AustriaAUT', 'puntos2': 1502.47},
	{'nro': 33, 'pais1': 'AustriaAUT', 'puntos1': 1502.47, 'pais2': 'MexicoMEX', 'puntos2': 990.5},
	{'nro': 34, 'pais1': 'MexicoMEX', 'puntos1': 990.5, 'pais2': 'CoteDivoireCOD', 'puntos2': 990.5},
	{'nro': 35, 'pais1': 'CoteDivoireCOD', 'puntos1': 990.5, 'pais2': 'NetherlandsNED', 'puntos2': 1679.41},
	{'nro': 36, 'pais1': 'NetherlandsNED', 'puntos1': 1679.41, 'pais2': 'SenegalSEN', 'puntos2': 1593.45},
	{'nro': 37, 'pais1': 'SenegalSEN', 'puntos1': 1593.45, 'pais2': 'BelgiumBEL', 'puntos2': 1821.92},
	{'nro': 38, 'pais1': 'BelgiumBEL', 'puntos1': 1821.92, 'pais2': 'TunisiaTUN', 'puntos2': 990.5},
	{'nro': 39, 'pais1': 'TunisiaTUN', 'puntos1': 990.5, 'pais2': 'PanamaPAN', 'puntos2': 990.5},
	{'nro': 40, 'pais1': 'PanamaPAN', 'puntos1': 990.5, 'pais2': 'SwitzerlandSUI', 'puntos2': 1621.43},
	{'nro': 41, 'pais1': 'SwitzerlandSUI', 'puntos1': 1621.43, 'pais2': 'SenegalSEN', 'puntos2': 1593.45},
	{'nro': 42, 'pais1': 'SenegalSEN', 'puntos1': 1593.45, 'pais2': 'BelgiumBEL', 'puntos2': 1821.92},
	{'nro': 43, 'pais1': 'BelgiumBEL', 'puntos1': 1821.92, 'pais2': 'TunisiaTUN', 'puntos2': 990.5},
]

"""

 Pronosticador de resultados de fase de grupos - Mundial Qatar 2022
 datos obtenidos de https://www.fifa.com/

 Elaborar un algoritmos que simule el resultado de cada partido en cada 
 grupo. 
 El resultado de un partido es determinado al azar pero basado en una probabilidad
 ponderada en la puntuación del país en el rank de la FIFA. Por ejemplo si juega
 Bélgica (1821.92 puntos) con Tonga (861.81 puntos) considerar que Bélgica tiene
 68% de ganar el partido. Este porcentaje se obtiene de la porción que representa
 los puntos de cada país respecto a la sumatoria de ambos. El cálculo de azar
 debe darle el 68% probabilidad de ganar a Bélgica.
 Luego de la simulación mostrar como queda conformado el resultado de cada grupos
 ordenados (usar algoritmo explícito de ordenación, no usar las funciones de PHP)
 según los puntos obtenidos en cada partido de mayor a menor.
 Agregar lo que considere necesario a los arrays
 
"""

#calculo de probabilidad

rand = random.randint(0, len(fifa_rank) - 1)
pais1 = fifa_rank[rand]['pais']
puntos1 = fifa_rank[rand]['puntos']

probabilidad = puntos1 / 10000
probabilidad = probabilidad * 100
probabilidad = round(probabilidad, 2)
probabilidad = str(probabilidad)

#calculo de puntos ganados por el equipo 1

puntos_ganados = puntos1 / 2
puntos_ganados = round(puntos_ganados, 2)

#resultado del partido
rand = random.randint(0, len(resultado) - 1)
pais1 = resultado[rand]['pais1']
puntos_1 = resultado[rand]['puntos1']
pais2 = resultado[rand]['pais2']
puntos_2 = resultado[rand]['puntos2']

#ganador del partido

def ganador(puntos_1, puntos_2):
    if puntos_1 > puntos_2:
        return pais1
    elif puntos_1 < puntos_2:
        return pais2
    else:
        return 'empate'

print(f"El ganador es: {ganador(puntos_1, puntos_2)}")


print(pais1 + ' ' + str(puntos_1) + ' vs ' + pais2 + ' ' + str(puntos_2))
print(f"El ganador es: {ganador(puntos_1, puntos_2)}")
print("Probabilidad de ganar el partido: " + str(probabilidad) + "%")
print("Puntos: " + str(puntos_ganados))

"""

$rand = rand(0, count($fifa_rank) - 1);
$pais1 = $fifa_rank[$rand]['pais'];
$puntos1 = $fifa_rank[$rand]['puntos'];

//calculo de probabilidad
$probabilidad = $puntos1 / 1000;
$probabilidad = $probabilidad * 100;
$probabilidad = round($probabilidad, 2);
$probabilidad = $probabilidad . '%';

//calculo de puntos ganados por el equipo 1
$puntos_ganados = $puntos1 / 2;
$puntos_ganados = round($puntos_ganados, 2);

//resultado del partido
$rand = rand(0, count($resultado) - 1);
$pais1 = $resultado[$rand]['pais1'];
$puntos_1 = $resultado[$rand]['puntos1'];
$pais2 = $resultado[$rand]['pais2'];
$puntos_2 = $resultado[$rand]['puntos2'];


//ganador del partido
$ganador = '';
if ($puntos_1 > $puntos_2) {
	$ganador = $pais1;
} else {
	$ganador = $pais2;
}

echo $pais1 . ' ' . $puntos_1 . ' vs ' . $pais2 . ' ' . $puntos_2. "\n";
echo "El ganador es: " . $ganador . "\n";
echo "Probabilidad de ganar el partido: " . $probabilidad. "\n";
echo "Puntos: " . $puntos_ganados. "\n";

"""

# Imprimir los países y sus puntos
# for equipo in fifa_rank:
#     print(f"País: {equipo['pais'].split(equipo['pais'][-3:])[-2]}\tPuntos: {equipo['puntos']}")

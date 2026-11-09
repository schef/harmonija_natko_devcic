"""Source-only rectangles individually selected from visual page inspection.
Coordinates in the 2000-pixel-height inspection view; manifest uses source pixels.
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'images/02-dijatonika-b'
HERE = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
rows = []

def crop(page, label, box, note='', kind='example'):
    source = f'sources/pages/page-{page:03}.png'
    im = Image.open(ROOT / source)
    scale = im.height / 2000
    rect = [round(v * scale) for v in box]
    stem = f'primjer-2-{label}' if kind == 'example' else f'zadatak-2-{page}-{label}'
    path = f'images/02-dijatonika-b/{stem}.png'
    im.crop(rect).save(ROOT / path)
    rows.append(dict(id=stem, example=f'2.{label}' if kind == 'example' else label,
                     kind=kind, printed_page=page, pdf_page=page//2+1,
                     source_image=source, rect=rect, image=path,
                     review_status='pending_independent_review', review_note=note,
                     caption=f'Primjer 2.{label}. Tiskana str. {page}.' if kind == 'example' else f'Zadatak {label}. Tiskana str. {page}.'))

crop(64,'134',(470,680,950,835))
crop(65,'135',(166,77,1343,730),'Cleanup required: handwriting above/among variants a–d; retained original pixels.')
crop(65,'136',(208,1075,1243,1404))
crop(65,'137',(428,1509,1090,1839))
crop(66,'138',(125,282,1300,608),'Cleanup required: pencil marks among lower figures.')
crop(66,'139',(294,833,1135,1154))
crop(66,'140-p66',(123,1498,1300,1823),'Cross-page example, variants a–b. Cleanup required: pencil marks among lower figures.')
crop(67,'140-p67',(457,92,1086,398),'Cross-page continuation c; number printed on preceding page. Pencil analysis below bass overlaps crop.')
crop(67,'141',(300,425,1235,742),'Cleanup required: pencil circle around NE and analysis among lower figures.')
crop(67,'142',(504,1190,1042,1484))
crop(67,'143-p67',(185,1512,1357,1847),'Cross-page example a–b; pencil annotations overlap original example.')
crop(68,'143-p68',(115,96,1305,545),'Cross-page continuation c; number printed on preceding page. Pencil marks below staff.')
crop(68,'144',(110,904,1303,1552),'Cleanup required: pencil harmonic annotations among figures.')
crop(68,'1',(133,1640,1093,1849),'Typeset progression exercise includes its instruction, inseparable from inline figures.','exercise')
crop(69,'145',(252,598,1279,934),'Cleanup required: handwritten analysis between labels/staves.')
crop(69,'146',(490,1187,1060,1497),'Cleanup required: pencil wavy line beside printed NE.')
crop(69,'147',(178,1511,1356,1830),'Cleanup required: pencil analysis under figures.')

crop(70,'148',(130,579,1326,1231),'Cleanup required: faint pencil annotations among figured bass.')
crop(71,'149',(336,88,1187,416))
crop(71,'150',(336,803,1187,1123),'Cleanup required: pencil check mark beside b and marks among notes.')
crop(71,'151-p71',(180,1519,1356,1847),'Cross-page a–d. Pencil analysis below figures.')
crop(72,'151-p72',(298,104,1106,430),'Cross-page e–g; number on preceding page. Pencil analysis below figures.')
crop(72,'152',(140,1076,1306,1387))
crop(72,'1',(140,1558,1305,1689),kind='exercise')
crop(72,'2',(140,1703,1305,1844),kind='exercise')
crop(73,'3',(171,103,1337,232),kind='exercise')
crop(73,'4',(175,248,1336,384),kind='exercise')
crop(73,'5',(175,400,1337,539),kind='exercise')
crop(73,'6',(175,563,1336,701),kind='exercise')
crop(73,'7',(175,704,1337,842),kind='exercise')
crop(73,'8',(175,856,1337,1003),kind='exercise')
crop(73,'9',(175,1009,1337,1108),kind='exercise')
crop(73,'10',(170,1161,1337,1286),kind='exercise')
crop(73,'11',(170,1308,1335,1413),kind='exercise')
crop(73,'12',(170,1454,1336,1575),kind='exercise')
crop(73,'13',(169,1590,1335,1856),kind='exercise')
crop(74,'14',(137,91,1319,208),kind='exercise')
crop(74,'15',(137,240,1318,363),kind='exercise')
crop(74,'16',(138,384,1319,515),kind='exercise')
crop(74,'17',(137,541,1318,663),kind='exercise')
crop(74,'18',(138,682,1319,810),kind='exercise')
crop(74,'19',(138,828,1319,955),kind='exercise')
crop(74,'20',(137,979,1317,1108),kind='exercise')
crop(74,'21',(137,1128,1315,1254),kind='exercise')
crop(74,'22',(137,1273,1315,1402),kind='exercise')
crop(74,'8-realizacija',(122,1508,1318,1843),'Realizacija zadatka 8; identifying heading is transcribed by parent, excluded from score-only crop.','exercise')

crop(75,'13-realizacija',(152,175,1348,781),'Identifying heading excluded from score-only crop.','exercise')
crop(76,'153',(151,836,1317,1001),'Cleanup required: handwritten chord names above notes and analysis below.')
crop(76,'154-p76',(138,1514,1318,1842),'Cross-page a–e. Cleanup required: handwriting around labels and circled analysis.')
crop(77,'154-p77',(451,78,1088,397),'Cross-page f–g, number on preceding page. Handwriting near labels.')
crop(77,'155',(424,615,1088,908),'Cleanup required: handwritten chord labels above printed variants.')
crop(77,'156',(311,1141,1157,1457),'Cleanup required: handwriting beside labels.')
crop(78,'157',(141,313,1317,610),'Cleanup required: handwriting intersects notes and bass, not removable by rectangle.')
crop(78,'158',(140,819,1315,1104),'Cleanup required: pencil harmonic annotations around notation.')
crop(78,'159',(127,1565,768,1833),'Cleanup required: pencil arrow near b.')
crop(78,'160',(808,1582,1303,1824),'Cleanup required: pencil writing above soprano.')
crop(79,'161',(158,331,1331,624),'Cleanup required: handwritten analysis between staves.')
crop(79,'162',(437,1060,1013,1323),'Cleanup required: handwritten chord names near variants.')
crop(80,'163',(144,100,1315,774),'Cleanup required: handwriting near labels and harmonic analysis.')
crop(80,'164',(207,1053,1185,1388),'Cleanup required: handwritten chord names over bracket and analysis below.')
crop(80,'165',(151,1441,807,1788),'Cleanup required: pencil circles on bass notes.')
crop(80,'166',(835,1440,1325,1835),'Cleanup required: handwriting between attribution and staff.')

if __name__ == '__main__':
    (HERE / 'images.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')

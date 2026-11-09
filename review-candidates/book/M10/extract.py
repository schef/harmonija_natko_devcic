"""Individually selected source crop rectangles, in a 1456x2000 viewing frame.
Output uses original pixels only; rect records actual source pixel coordinates.
"""
import json
from pathlib import Path
from PIL import Image

OUT = Path('images/04-neakordicki-c')
HERE = Path('review-candidates/book/M10')
OUT.mkdir(parents=True, exist_ok=True)
rows = []

def crop(page, number, box, kind='example', part='', note=''):
    source = f'sources/pages/page-{page:03}.png'
    im = Image.open(source)
    x0,y0,x1,y1 = box
    rect = [round(x0*im.width/1456),round(y0*im.height/2000),round(x1*im.width/1456),round(y1*im.height/2000)]
    stem = f'primjer-4-{number}' if kind == 'example' else f'zadatak-4-{page}-{number}'
    if part: stem += '-'+part
    path = OUT / (stem+'.png')
    im.crop(rect).save(path)
    label = f'4.{number}' if kind == 'example' else str(number)
    rows.append(dict(id=stem, example=label, kind=kind, printed_page=page, pdf_page=page//2+1,
                     source_image=source, rect=rect, image=str(path), review_status='pending_independent_review',
                     review_note=note or 'Source-only crop; independent visual review required.',
                     caption=f'{"Primjer" if kind == "example" else "Zadatak"} {label}. Izvor: str. {page}.' + (f' Dio: {part}.' if part else '')))

crop(349,143,(245,720,1280,1027))
crop(349,144,(360,1033,1170,1310))
crop(349,145,(413,1603,1085,1900))
crop(350,146,(383,292,1014,580))
crop(350,147,(123,886,669,1175))
crop(350,148,(671,881,1305,1170))
crop(350,149,(120,1225,1160,1533))
crop(351,150,(432,274,1060,601))
crop(351,151,(520,920,1006,1202))
crop(351,152,(164,1545,1346,1826),part='a')
crop(352,152,(122,70,1320,355),part='b',note='Continuation d–g; number occurs in preceding part on p.351.')
crop(352,153,(140,455,1320,730))
crop(352,154,(139,772,1318,1050))
crop(352,155,(393,1076,1066,1475))
crop(352,156,(187,1490,1272,1842))
crop(353,157,(333,80,1205,395))
crop(353,158,(171,509,1345,900))
crop(353,159,(330,1042,1189,1395))
crop(354,160,(120,76,1320,798))
crop(354,161,(346,1114,1112,1455))
crop(355,162,(375,142,1141,447))
crop(355,163,(347,647,1207,929))
crop(355,1,(179,1400,1352,1535),'exercise')
crop(355,2,(180,1556,1354,1690),'exercise')
crop(355,3,(177,1717,1355,1845),'exercise')
crop(356,4,(125,145,1308,671),'exercise')
crop(356,5,(126,681,1306,1136),'exercise')
crop(356,6,(128,1348,1304,1494),'exercise')
crop(356,7,(129,1505,1303,1640),'exercise')
crop(356,8,(127,1671,1306,1795),'exercise',part='a')
crop(357,8,(173,109,1354,228),'exercise',part='b',note='Continuation of exercise 8 on p.356; no repeated number.')
crop(357,9,(174,324,1354,1046),'exercise')
crop(357,10,(171,1065,1354,1598),'exercise')
crop(357,11,(173,1617,1353,1780),'exercise',part='a')
crop(358,11,(143,142,1319,488),'exercise',part='b',note='Continuation of exercise 11 on p.357; no repeated number.')
crop(358,12,(143,497,1328,934),'exercise')
crop(358,13,(144,962,1325,1259),'exercise')
crop(358,14,(144,1270,1325,1546),'exercise')

crop(359,9,(154,184,1351,1340),'exercise',part='realizacija')
crop(360,12,(119,194,1317,1593),'exercise',part='realizacija')
crop(361,164,(176,934,1351,1250))
crop(361,165,(176,1517,965,1825))
crop(361,166,(970,1536,1350,1825))
crop(362,167,(134,93,1316,468))
crop(362,168,(404,517,1033,804))
crop(362,169,(130,841,1314,1210),note='cleanup-required: footnote starts level with lowest beamed bass notation; preserve beam with unavoidable partial footnote ink. No retouch applied.')
crop(362,170,(247,1555,1176,1852))
crop(363,171,(173,99,839,508))
crop(363,172,(840,99,1352,452))
crop(363,173,(167,616,1353,1026))
crop(363,174,(163,1294,1347,1680))
crop(364,175,(297,93,1156,453))
crop(364,176,(127,872,703,1226))
crop(364,177,(703,911,1309,1179))
crop(364,1,(128,1440,1310,1691),'exercise')
crop(364,2,(136,1737,1312,1847),'exercise',part='a')
crop(365,2,(166,90,1347,208),'exercise',part='b',note='Continuation of exercise 2 on p.364; no repeated number.')
crop(365,3,(166,219,1347,492),'exercise')
crop(365,4,(166,516,1343,801),'exercise')

crop(366,178,(128,1411,1305,1800),part='a',note='Source contains circled bass notes (handwritten); cleanup-required, no retouch applied.')
crop(367,178,(133,83,1329,819),part='b',note='Continuation from p.366. Source contains handwritten circles; cleanup-required, no retouch applied.')
crop(367,179,(151,830,1336,1184))
crop(367,180,(146,1193,1325,1507))
crop(368,181,(119,371,1321,1003))
crop(368,182,(145,1419,1326,1791),part='a')
crop(369,182,(155,145,1347,469),part='b',note='Continuation of example 4.182 on p.368; no repeated number.')
crop(369,183,(170,478,1351,842))
crop(369,184,(155,1461,1335,1838))
crop(370,185,(227,106,1222,476))
crop(370,186,(130,533,1320,1513))
crop(370,187,(133,1533,1316,1855))
crop(371,1,(166,206,1357,1055),'exercise')
crop(371,2,(164,1161,1357,1760),'exercise',part='a')
crop(372,2,(122,89,1324,726),'exercise',part='b',note='Continuation of exercise 2 on p.371; no repeated number.')
crop(372,3,(139,921,1336,1805),'exercise')
crop(373,4,(155,101,1357,1350),'exercise')
crop(373,5,(164,1451,1356,1707),'exercise',part='a')
crop(374,5,(128,105,1335,1310),'exercise',part='b',note='Continuation of exercise 5 on p.373; no repeated number.')
crop(374,1,(128,1517,1333,1828),'exercise',part='realizacija-a')
crop(375,1,(156,96,1359,1103),'exercise',part='realizacija-b',note='Continuation of realization of exercise 1 from p.374; no repeated number.')
crop(376,188,(127,669,1311,1063))
crop(377,189,(163,100,1354,750))
crop(377,190,(160,956,1352,1657))
crop(378,191,(122,101,1300,463))
crop(378,192,(122,996,1304,1505),note='cleanup-required: Beethoven attribution top overlaps preceding prose baseline; bottom slur overlaps following Ravel attribution. Preserve all example content with unavoidable foreign prose/attribution fragments. No retouch applied.')
crop(378,193,(124,1497,1302,1885),note='cleanup-required: Ravel attribution overlaps preceding example bottom slur; preserve attribution with unavoidable foreign slur ink. No retouch applied.')

if __name__ == '__main__':
    (HERE/'images.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

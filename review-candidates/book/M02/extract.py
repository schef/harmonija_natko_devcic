"""Explicit independently selected source rectangles (visual reference 1450x2000)."""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
records = []

def crop(page, name, box, note='', caption=None):
    source = f'sources/pages/page-{page:03}.png'
    image = f'images/02-dijatonika-a/{name}.png'
    with Image.open(ROOT / source) as im:
        w, h = im.size
        rect = [round(box[0]*w/1450), round(box[1]*h/2000), round(box[2]*w/1450), round(box[3]*h/2000)]
        out = ROOT / image
        if out.exists():
            raise RuntimeError(f'Refusing to overwrite {image}')
        im.crop(rect).save(out)
    example = name.replace('primjer-2-', '2.') if name.startswith('primjer') else name
    records.append(dict(id=name, example=example, kind='example' if name.startswith('primjer') else 'exercise', printed_page=page, pdf_page=page//2+1, source_image=source, rect=rect, image=image, review_status='pending_independent_review', review_note=note or 'Source-only provisional crop; independent review required.', caption=caption or example))

crop(47,'primjer-2-98',(148,96,1330,412),'cleanup-required: faint handwritten analytical marks below notation preserved.')
crop(47,'primjer-2-99',(268,418,1185,694))
crop(47,'zadatak-2-47-1',(155,931,1323,1077))
crop(47,'zadatak-2-47-2',(155,1098,1320,1237))
crop(47,'zadatak-2-47-3',(155,1276,1320,1398))
crop(47,'zadatak-2-47-4',(156,1418,1318,1534))
crop(47,'zadatak-2-47-5',(155,1580,1317,1707))
crop(47,'zadatak-2-47-6',(155,1730,1316,1856))
crop(48,'primjer-2-100',(450,573,972,735),'cleanup-required: pencil marks adjacent to printed brackets preserved.')
crop(48,'primjer-2-101',(159,1084,1324,1280),'cleanup-required: handwriting above/below chords preserved.')
crop(48,'primjer-2-102',(481,1572,873,1847))
crop(49,'primjer-2-103',(169,537,902,850),'cleanup-required: pencil marks near notes preserved.')
crop(49,'primjer-2-104',(928,543,1341,835),'cleanup-required: pencil marks near notes preserved.')
crop(49,'primjer-2-105',(541,1666,970,1812))
crop(50,'primjer-2-106',(126,762,607,1042),'cleanup-required: handwriting within system preserved.')
crop(50,'primjer-2-107',(668,758,1301,1022),'cleanup-required: handwriting within system preserved.')
crop(50,'primjer-2-108',(108,1053,1302,1683),'cleanup-required: handwritten marks below systems preserved; printed footnotes excluded for text transcription.')
crop(51,'primjer-2-109',(155,424,1329,785),'cleanup-required: handwritten analysis under system preserved.')
crop(51,'primjer-2-110',(491,1099,955,1237))
crop(51,'primjer-2-111',(147,1558,1315,1876),'Part a; continuation b–d on printed52. cleanup-required: faint marks below system preserved.')
crop(52,'primjer-2-111-nastavak',(130,100,1321,723),'Continuation b–d; number appears on printed51 only. cleanup-required: handwriting preserved. Footnote excluded for text transcription.')
crop(52,'primjer-2-112',(491,1070,922,1239))
crop(52,'primjer-2-113',(141,1522,1314,1868),'cleanup-required: handwritten analysis within/below system preserved.')
crop(53,'primjer-2-114',(317,446,1160,814),'cleanup-required: handwriting above system preserved.')
crop(53,'primjer-2-115',(304,1402,1146,1695))
crop(54,'primjer-2-116',(149,832,753,1173),'cleanup-required: handwriting below system preserved.')
crop(54,'primjer-2-117',(789,824,1324,1180),'cleanup-required: handwritten analysis below system preserved.')
crop(54,'primjer-2-118',(158,1547,1328,1888),'First system; continuation on printed55. cleanup-required: handwritten marks preserved.')
crop(55,'primjer-2-118-nastavak',(156,86,1343,359),'Continuation of2.118; number on printed54 only.')
crop(55,'primjer-2-119',(397,364,1054,734),'cleanup-required: handwritten analysis above/below system preserved.')
crop(55,'primjer-2-120',(254,987,1280,1295))
crop(55,'primjer-2-121',(169,1548,1344,1848))
crop(56,'primjer-2-122',(130,459,1307,773))
crop(56,'primjer-2-123',(507,1034,890,1309))
crop(57,'primjer-2-124',(148,251,1341,901),'cleanup-required: handwritten analysis below both systems preserved.')
crop(57,'primjer-2-125',(171,1146,1340,1508),'cleanup-required: handwriting below notation preserved.')
crop(58,'primjer-2-126',(353,100,1100,401))
crop(58,'primjer-2-127',(136,1475,839,1843),'cleanup-required: faint pencil marks below system preserved.')
crop(58,'primjer-2-128',(856,1512,1306,1844),'cleanup-required: pencil analysis below system preserved.')
crop(59,'primjer-2-129',(178,95,1359,718),'cleanup-required: pencil marks below systems preserved. Lower crop stops before body paragraph.')
crop(60,'primjer-2-130',(100,542,577,841))
crop(60,'primjer-2-131',(639,540,1276,837))
crop(60,'primjer-2-132',(111,862,577,1025))
crop(60,'primjer-2-133',(635,865,1119,1150))
crop(60,'zadatak-2-60-1',(105,1420,1268,1534))
crop(60,'zadatak-2-60-2',(103,1576,1266,1698))
crop(60,'zadatak-2-60-3',(101,1726,1264,1844))
crop(61,'zadatak-2-61-4',(185,111,1346,240))
crop(61,'zadatak-2-61-5',(185,282,1346,393))
crop(61,'zadatak-2-61-6',(185,449,1346,569))
crop(61,'zadatak-2-61-7',(185,594,1344,709))
crop(61,'zadatak-2-61-8',(183,740,1348,836))
crop(61,'zadatak-2-61-9',(179,885,1343,980))
crop(61,'zadatak-2-61-10',(174,1027,1345,1118))
crop(61,'zadatak-2-61-11',(175,1169,1345,1258))
crop(61,'zadatak-2-61-12',(175,1277,1346,1401))
crop(61,'zadatak-2-61-13',(174,1432,1345,1564))
crop(61,'zadatak-2-61-14',(174,1591,1345,1715))
crop(61,'zadatak-2-61-15',(174,1739,1345,1865))
crop(62,'zadatak-2-62-16',(112,101,1280,220))
crop(62,'zadatak-2-62-17',(112,262,1280,370))
crop(62,'zadatak-2-62-18',(109,410,1278,532))
crop(62,'zadatak-2-62-19',(109,572,1278,695))
crop(62,'zadatak-2-62-20',(110,709,1277,832))
crop(62,'zadatak-2-62-21',(111,873,1277,993))
crop(62,'zadatak-2-62-22',(105,1022,1278,1141))
crop(62,'zadatak-2-62-23',(108,1182,1277,1329))
crop(62,'zadatak-2-62-12-realizacija',(88,1520,1275,1840),'Realizacija zadatka12; identity heading is transcribed separately, no printed number within notation.', 'Realizacija zadatka12')
crop(63,'zadatak-2-63-13-realizacija',(129,203,1317,840),'Realizacija zadatka13; identity heading is transcribed separately, no printed number within notation.', 'Realizacija zadatka13')
(ROOT/'review-candidates/book/M02/images.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'{len(records)} source-only crops saved, pending independent review')

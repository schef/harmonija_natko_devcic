"""Individually selected source-only rectangles, printed 309–328.

View coordinates refer to a 2000-high page display. Manifest rectangles are
original source pixels, exclusive right/bottom. Run from repository root.
No importing or execution of the old extract.py is involved.
"""
import json
from pathlib import Path
from PIL import Image

OUT = Path('images/04-neakordicki-b')
MANIFEST = Path('review-candidates/book/M09/images-309-328.json')
# page, slot, kind, four separately selected edges, source caveat
SELECTIONS = [
 (309,'53','example',(168,744,1342,1158),'cleanup: pencil labels and analysis.'),
 (309,'54','example',(168,1460,1340,1810),'cleanup: pencil labels above variants.'),
 (310,'55','example',(136,951,723,1268),'cleanup: pencil circles and annotations.'),
 (310,'56','example',(733,949,1317,1263),'cleanup: pencil circles.'),
 (310,'57','example',(136,1270,723,1580),'cleanup: pencil circles.'),
 (310,'58','example',(732,1268,1317,1580),'cleanup: pencil circles.'),
 (311,'59','example',(231,83,1290,380),''),
 (311,'60','example',(166,1003,1346,1666),'cleanup: handwriting throughout; right marginal handwriting touches staff ending and cannot be wholly excluded by rectangle without losing notation.'),
 (312,'61','example',(143,130,1308,296),'cleanup: faint pencil marks near DA.'),
 (312,'62','example',(223,476,1220,744),''),
 (312,'63','example',(207,906,1223,1268),'cleanup: pencil circle and marks.'),
 (312,'64','example',(352,1589,1097,1888),'cleanup: pencil marks at b and bass note.'),
 (313,'65','example',(397,335,1141,664),'cleanup: handwritten harmonic analysis below bass retained.'),
 (313,'66','example',(182,663,1366,1016),'cleanup: pencil marks within and below notation; attribution retained.'),
 (313,'67','example',(247,1010,1233,1372),'footnote_overlap: lowest printed fermata and first footnote ink overlap vertically in this skewed scan, so a rectangular score-only crop cannot retain the complete fermata while excluding the footnote. Full footnote retained rather than partial prose or clipped notation. Printed score asterisk retained. cleanup: handwritten analysis below bass.'),
 (313,'68','example',(414,1540,1120,1877),'cleanup: pencil mark adjacent to upper notation. Tight upper source separation from preceding paragraph underline; no notation removed.'),
 (314,'69','example',(129,268,1310,581),''),
 (314,'70','example',(242,784,1168,1160),'source_layout: open staff ends preserved as printed.'),
 (314,'71','example',(237,1199,1075,1614),'cleanup: handwritten analysis below bass; lower fermata retained.'),
 (315,'1','exercise',(174,638,1348,779),''),
 (315,'2','exercise',(174,812,1348,1145),''),
 (315,'3','exercise',(173,1280,1346,1567),''),
 (315,'4','exercise',(171,1582,1346,1706),''),
 (315,'5','exercise',(173,1723,1347,1858),''),
 (316,'6','exercise',(145,92,1323,365),''),
 (316,'7','exercise',(123,715,1320,1291),''),
 (316,'8','exercise',(135,1346,1318,1785),''),
 (317,'9','exercise',(151,100,1350,686),''),
 (317,'3-realizacija','realization',(158,813,1351,1571),'Printed realization title included.'),
 (318,'72','example',(128,243,1310,519),''),
 (318,'73','example',(127,573,1311,850),''),
 (318,'74','example',(129,905,1310,1191),'source_layout/source_damage: irregular open staff endpoints of variant c retained without repair.'),
 (318,'75','example',(129,1230,1311,1507),''),
 (319,'76','example',(458,79,1067,341),''),
 (319,'77','example',(168,551,1350,837),''),
 (319,'78','example',(170,884,685,1175),''),
 (319,'79','example',(687,885,1352,1159),''),
 (319,'80','example',(257,1200,1280,1489),''),
 (320,'81','example',(127,209,1311,500),''),
 (320,'82','example',(107,831,1306,1796),''),
 (321,'1','exercise',(169,207,1344,449),''),
 (321,'2','exercise',(167,492,1343,882),''),
 (321,'3','exercise',(168,905,1343,1181),''),
 (321,'4','exercise',(168,1199,1342,1469),''),
 (321,'5','exercise',(169,1481,1343,1762),''),
 (322,'4-realizacija','realization',(111,97,1298,841),'Printed realization title included.'),
 (322,'83','example',(141,1311,1301,1479),''),
 (322,'84','example',(139,1516,1300,1843),''),
 (323,'85','example',(303,278,1166,459),''),
 (323,'86','example',(312,479,1169,666),''),
 (323,'87','example',(160,938,1328,1217),'source_layout: open staff endpoints at right are present in source.'),
 (323,'88','example',(465,1560,1021,1834),''),
 (324,'89','example',(139,484,1315,667),''),
 (324,'90','example',(245,1037,1219,1321),''),
 (324,'91','example',(242,1367,1219,1655),''),
 (325,'92','example',(164,74,1349,359),''),
 (325,'93','example',(546,672,971,932),''),
 (325,'94','example',(342,1298,1177,1622),'source_layout: open staff endpoints retained as printed.'),
 (326,'95','example',(139,329,694,605),'source_layout: open staff endpoints retained as printed.'),
 (326,'96','example',(699,300,1322,596),'source_layout: open staff endpoints retained as printed.'),
 (326,'97','example',(125,847,1321,1477),''),
 (326,'98-a','example',(134,1538,1321,1842),'First part, variants a–c; printed number present. Continues on printed 327.'),
 (327,'98-b','example',(167,102,1365,391),'Continuation, variants d–e; no printed example number on this part. No number added.'),
 (327,'99','example',(174,779,1357,1088),''),
 (327,'100','example',(339,1465,1209,1738),'source_layout: open staff endpoints retained as printed.'),
 (328,'101','example',(241,636,1183,1019),'Bach attribution and lower fermata included.'),
 (328,'102','example',(233,1101,1179,1468),'Bach attribution and lower fermata included.'),
 (328,'103','example',(238,1584,1091,1973),'Left edge excludes printed page number; complete lower fermata retained with genuine source margin.'),
]


def main():
    assert len(SELECTIONS) == 68
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for page, slot, kind, box, note in SELECTIONS:
        assert 309 <= page <= 328
        source = Path(f'sources/pages/page-{page:03}.png')
        with Image.open(source) as im:
            rect = [round(v * im.height / 2000) for v in box]
            assert 0 <= rect[0] < rect[2] <= im.width
            assert 0 <= rect[1] < rect[3] <= im.height
            if kind == 'example':
                name = f'primjer-4-{slot}'
                example = '4.' + slot.split('-')[0]
                label = f'Primjer {example}'
            else:
                name = f'zadatak-4-{page}-{slot}'
                example = slot.split('-')[0]
                label = f'Realizacija zadatka {example}' if kind == 'realization' else f'Zadatak {example}'
            image = OUT / f'{name}.png'
            cropped = im.crop(tuple(rect))
            if image.exists():
                with Image.open(image) as old:
                    if old.mode != cropped.mode or old.size != cropped.size or old.tobytes() != cropped.tobytes():
                        raise FileExistsError(f'Refusing to overwrite existing image: {image}')
            else:
                cropped.save(image)
        rows.append(dict(id=name, example=example, kind=kind, slot_label=slot,
                         printed_page=page, pdf_page=page // 2 + 1,
                         source_image=source.as_posix(), rect=rect,
                         image=image.as_posix(), review_status='pending_independent_review',
                         review_note=note, caption=f'{label}. Izvor: tiskana str. {page}.'))
    MANIFEST.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(rows)} source-only crops; all pending independent review.')


if __name__ == '__main__':
    main()

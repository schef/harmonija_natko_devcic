"""M09 printed 329–348: separately chosen four-edge source rectangles.

Selection coordinates refer to the 2000-high visual display; manifest rects
are local original PNG pixels, [left, top, right, bottom), not spread pixels.
No old extraction plan is imported. Run from repository root.
"""
import json
from pathlib import Path
from PIL import Image

OUT = Path('images/04-neakordicki-b')
MANIFEST = Path('review-candidates/book/M09/images-329-348.json')
# printed page, slot, kind, individually selected L/T/R/B, source caveat
SELECTIONS = [
    (329, '1', 'exercise', (158, 168, 1350, 1064), ''),
    (329, '2', 'exercise', (179, 1121, 1349, 1230), ''),
    (329, '3', 'exercise', (180, 1257, 1347, 1387), ''),
    (329, '4', 'exercise', (181, 1412, 1349, 1700), ''),
    (329, '5-a', 'exercise', (182, 1731, 1348, 1858), 'First part; printed exercise 5 present. Continues on 330.'),
    (330, '5-b', 'exercise', (139, 96, 1316, 371), 'Continuation of exercise 5 on 329; no repeated number printed. No number added.'),
    (330, '3-realizacija', 'realization', (118, 397, 1318, 1150), 'Printed realization title retained.'),
    (331, '104', 'example', (177, 81, 1355, 372), ''),
    (331, '105', 'example', (230, 410, 1311, 685), ''),
    (331, '106', 'example', (477, 1543, 1092, 1849), 'Bach attribution retained; open staff ends as printed.'),
    (332, '107', 'example', (134, 107, 1316, 442), 'Bach attribution and lower fermata retained; open staff ends as printed.'),
    (332, '1', 'exercise', (114, 531, 1310, 1130), ''),
    (332, '2', 'exercise', (115, 1162, 1306, 1781), 'Lowest bass ledger note and stem retained.'),
    (333, '3', 'exercise', (190, 101, 1354, 225), ''),
    (333, '4', 'exercise', (185, 246, 1354, 511), ''),
    (333, '3-realizacija', 'realization', (164, 594, 1355, 1299), 'Printed title and score *) retained; explanatory footnote is transcribed separately in text-319-333.md.'),
    (334, '108', 'example', (113, 394, 1294, 684), 'cleanup: pencil circles retained. C-dur title and both staves retained.'),
    (334, '109', 'example', (113, 721, 1293, 1009), 'cleanup: pencil circles retained. c-mol title and both staves retained.'),
    (334, '110', 'example', (306, 1674, 1101, 1812), ''),
    (335, '111', 'example', (233, 98, 1270, 386), ''),
    (335, '112', 'example', (347, 779, 1183, 1095), 'All lower asterisk markers retained.'),
    (335, '1', 'exercise', (144, 1277, 1340, 1839), ''),
    (336, '2', 'exercise', (146, 124, 1322, 691), 'source_layout: exceptionally narrow lower separation from exercise 3 slur; lowest parenthesized figures retained.'),
    (336, '3', 'exercise', (148, 692, 1322, 1253), 'source_layout: upper edge follows narrow source gap after exercise 2 figures; full opening slur retained.'),
    (336, '1-realizacija-a', 'realization', (126, 1450, 1321, 1844), 'First part, printed realization title retained; continues on 337. Lower page number excluded.'),
    (337, '1-realizacija-b', 'realization', (145, 80, 1340, 760), 'Continuation of realization 1 on 336, two systems; no repeated title printed.'),
    (337, '113', 'example', (494, 1356, 1022, 1718), 'cleanup/source_damage/layout_overlap: pencil analysis below score and faint pencil pointer above first asterisk retained. Pointer meets handwriting under preceding prose; some source pencil underline remains at upper edge, but no printed prose. No retouching.'),
    (338, '114', 'example', (137, 351, 1083, 698), 'cleanup: handwritten harmonic analysis beneath bass retained; open staff ends as printed.'),
    (338, '115', 'example', (135, 702, 995, 1050), 'Beethoven attribution and lowest bass stems retained; open staff ends as printed.'),
    (338, '116', 'example', (135, 1084, 1314, 1391), 'source_layout: narrow lower gap before prose; all three lower asterisks retained.'),
    (338, '117', 'example', (356, 1559, 1070, 1850), ''),
    (339, '118', 'example', (178, 241, 706, 542), ''),
    (339, '119', 'example', (707, 220, 1361, 559), 'Haydn attribution and score *) retained; footnote separately transcribed in text-334-348.md.'),
    (339, '120', 'example', (370, 614, 1134, 911), ''),
    (339, '121', 'example', (170, 1180, 837, 1464), ''),
    (339, '122', 'example', (839, 1169, 1351, 1480), 'Lowest asterisk retained.'),
    (339, '123', 'example', (373, 1525, 1135, 1830), 'Lowest bass stems retained.'),
    (340, '124', 'example', (289, 80, 1090, 429), 'Beethoven attribution and lowest staccato retained.'),
    (340, '125', 'example', (288, 429, 1183, 763), 'source_layout: exceptionally narrow lower source gap between bass ledger note and following prose; Chopin attribution retained.'),
    (340, '126', 'example', (131, 1125, 1305, 1410), 'Open staff ends retained as printed.'),
    (340, '127', 'example', (131, 1475, 1308, 1837), 'Chopin attribution and complete lowest figures 7/4—3 retained.'),
    (341, '128', 'example', (537, 88, 978, 373), 'Footnote prose separately transcribed in text-334-348.md; printed score has asterisks, no added marker.'),
    (341, '129', 'example', (311, 442, 1204, 845), 'Bach attribution and lowest figures retained.'),
    (341, '130', 'example', (329, 996, 1174, 1270), ''),
    (341, '131', 'example', (170, 1315, 1346, 1675), 'Chopin attribution and all score *, **, *** markers retained; three footnotes separately transcribed in text-334-348.md.'),
    (342, '132', 'example', (268, 428, 1171, 744), 'NE, DA and asterisk retained; open staff ends as printed.'),
    (342, '133', 'example', (127, 767, 1310, 1242), 'Lowest bass ledger notes retained; open staff ends as printed.'),
    (342, '134', 'example', (363, 1597, 1074, 1898), 'Lowest figures retained; crop shifted right of printed page number.'),
    (343, '135', 'example', (364, 106, 1178, 418), ''),
    (343, '136', 'example', (174, 456, 1354, 755), 'Printed itd. and complete open staff ends retained.'),
    (343, '137', 'example', (157, 1088, 1355, 1722), 'Both systems a–f and lowest figures retained.'),
    (344, '138', 'example', (137, 398, 1311, 682), ''),
    (344, '139', 'example', (125, 721, 1314, 1364), 'Both systems a–e plus itd. retained. Source prose says d–f, but no f is printed in the score.'),
    (345, '140', 'example', (178, 86, 1356, 380), 'source_layout: close lower separation from prose; all lower beams and slurs retained.'),
    (345, '141', 'example', (178, 957, 708, 1252), 'Printed CAMBIATA title and bracket retained.'),
    (345, '142', 'example', (177, 1257, 1355, 1575), 'Marx–Bayer attribution retained; open staff ends as printed.'),
    (346, '1', 'exercise', (128, 168, 1307, 543), 'Complete figured bass through lowest altered figures retained.'),
    (346, '2', 'exercise', (128, 548, 1307, 932), 'Complete figured bass retained.'),
    (346, '3', 'exercise', (128, 935, 1307, 1207), ''),
    (346, '4', 'exercise', (128, 1238, 1307, 1493), ''),
    (346, '5', 'exercise', (128, 1499, 1308, 1828), 'Printed Allegretto retained.'),
    (347, '6', 'exercise', (181, 128, 1363, 405), ''),
    (347, '7', 'exercise', (182, 419, 1363, 697), ''),
    (347, '8', 'exercise', (180, 720, 1360, 999), ''),
    (347, '9', 'exercise', (179, 1013, 1361, 1439), 'All three staves, changing time signatures and lowest ledger note retained.'),
    (348, '3-realizacija', 'realization', (123, 96, 1320, 878), 'Printed title and brackets with *) and **) retained. Both explanatory footnotes separately transcribed in text-334-348.md.'),
]


def main():
    assert len(SELECTIONS) == 66
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for page, slot, kind, box, note in SELECTIONS:
        assert 329 <= page <= 348
        source = Path(f'sources/pages/page-{page}.png')
        with Image.open(source) as original:
            rect = [round(v * original.height / 2000) for v in box]
            assert 0 <= rect[0] < rect[2] <= original.width
            assert 0 <= rect[1] < rect[3] <= original.height
            if kind == 'example':
                name = f'primjer-4-{slot}'
                example = f'4.{slot}'
                label = f'Primjer {example}'
            else:
                name = f'zadatak-4-{page}-{slot}'
                example = slot.split('-')[0]
                label = (f'Realizacija zadatka {example}' if kind == 'realization'
                         else f'Zadatak {example}')
            if slot.endswith('-a'):
                label += ' — početak'
            elif slot.endswith('-b'):
                label += ' — nastavak'
            image = OUT / f'{name}.png'
            crop = original.crop(tuple(rect))
            if image.exists():
                with Image.open(image) as old:
                    if old.mode != crop.mode or old.size != crop.size or old.tobytes() != crop.tobytes():
                        raise FileExistsError(f'Refusing to overwrite differing existing image: {image}')
            else:
                crop.save(image)
        records.append(dict(id=name, example=example, kind=kind,
                            printed_page=page, pdf_page=page // 2 + 1,
                            source_image=source.as_posix(), rect=rect,
                            image=image.as_posix(),
                            review_status='pending_independent_review',
                            review_note=note,
                            caption=f'{label}. Izvor: tiskana str. {page}.'))
    MANIFEST.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(records)} source-pixel crops, pending independent review.')


if __name__ == '__main__':
    main()

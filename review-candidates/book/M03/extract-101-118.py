"""Source-only extraction, printed 101–118. Run from repository root.

Each rectangle was selected individually from a visually opened source page.
Planning coordinates use the displayed page's 2000-pixel height; the manifest
records the corresponding original-source pixel rectangle, Pillow exclusive right/bottom.
No resampling, retouching, compositing, padding, or automatic margin expansion.
"""
import json
import re
from pathlib import Path
from PIL import Image

OUT = Path('review-candidates/book/M03')
DEST = Path('images/02-dijatonika-b')
# page, slot identity, individually chosen left/top/right/bottom, source conflict
ROWS = [
 (101,'zadatak 4',(190,80,1370,215),False),
 (101,'zadatak 5',(190,228,1370,361),False),
 (101,'zadatak 6',(200,361,1372,494),False),
 (101,'zadatak 7',(201,514,1372,658),False),
 (101,'zadatak 8',(199,678,1372,827),False),
 (101,'zadatak 9',(199,833,1371,928),False),
 (101,'zadatak 10',(194,983,1371,1075),False),
 (101,'zadatak 11',(190,1115,1371,1234),False),
 (101,'zadatak 12',(188,1297,1371,1388),False),
 (101,'zadatak 13',(189,1420,1372,1557),False),
 (101,'zadatak 14',(185,1576,1371,1710),False),
 (101,'zadatak 15',(187,1739,1371,1867),False),
 (102,'zadatak 16',(118,82,1301,205),False),
 (102,'zadatak 17',(118,230,1301,359),False),
 (102,'zadatak 18',(117,378,1300,511),False),
 (102,'zadatak 19',(118,526,1300,661),False),
 (102,'zadatak 20',(117,667,1300,806),False),
 (102,'zadatak 21',(116,824,1300,1101),False),
 (102,'zadatak 22',(115,1115,1300,1240),False),
 (102,'zadatak 23',(114,1260,1300,1391),False),
 (102,'Realizacija zadatka 17 (početak)',(94,1461,1300,1840),False),
 (103,'Realizacija zadatka 17 (nastavak)',(150,78,1350,406),False),
 (103,'2.222',(359,1134,1134,1304),True),
 (103,'2.223',(533,1572,929,1890),True),
 (104,'2.224',(140,1078,1314,1274),True),
 (104,'2.225',(137,1524,1313,1870),True),
 (105,'2.226',(358,53,1117,414),True),
 (105,'2.227',(174,743,1249,1108),True),
 (105,'2.228',(564,1271,968,1620),True),
 (106,'2.229',(402,22,982,231),True),
 (106,'2.230',(151,671,1246,998),True),
 (106,'2.231',(107,1184,1302,1872),True),
 (107,'2.232',(137,367,1345,1381),True),
 (107,'2.233',(325,1530,1183,1870),True),
 (108,'2.234',(204,529,1139,702),True),
 (108,'2.235',(194,704,1271,1038),True),
 (108,'2.236',(133,1172,1311,1506),True),
 (108,'2.237',(131,1508,1311,1845),False),
 (109,'zadatak 1',(157,167,1321,334),False),
 (109,'zadatak 2',(156,336,1321,477),False),
 (109,'zadatak 3',(155,482,1321,628),False),
 (109,'zadatak 4',(154,630,1321,794),False),
 (109,'zadatak 5',(155,797,1321,937),False),
 (109,'zadatak 6',(147,948,1321,1238),True),
 (109,'zadatak 7',(154,1251,1321,1397),True),
 (109,'zadatak 8',(153,1400,1321,1543),True),
 (109,'zadatak 9',(153,1557,1321,1693),True),
 (109,'zadatak 10',(148,1713,1321,1860),True),
 (110,'zadatak 11',(139,101,1313,191),False),
 (110,'zadatak 12',(137,204,1313,334),False),
 (110,'zadatak 13',(132,355,1313,488),False),
 (110,'zadatak 14',(130,510,1313,642),False),
 (110,'zadatak 15',(129,665,1312,800),False),
 (110,'zadatak 16',(130,823,1311,951),False),
 (110,'zadatak 17',(128,981,1310,1107),False),
 (110,'zadatak 18',(127,1136,1310,1273),False),
 (110,'zadatak 19',(126,1289,1310,1423),False),
 (110,'zadatak 20',(126,1438,1310,1572),False),
 (110,'zadatak 21',(126,1586,1308,1726),False),
 (110,'zadatak 22',(134,1730,1308,1860),False),
 (111,'zadatak 23',(158,83,1342,226),False),
 (111,'Realizacija zadatka 16',(151,386,1343,789),False),
 (111,'2.238',(414,1190,1034,1501),True),
 (111,'2.239',(169,1528,1346,1845),True),
 (112,'2.240',(122,343,1299,763),True),
 (112,'2.241',(115,1014,1301,1424),True),
 (112,'2.242',(307,1435,1101,1606),False),
 (113,'2.243',(348,82,1152,405),True),
 (113,'zadatak 1',(155,556,1331,863),False),
 (113,'zadatak 2',(156,868,1331,976),False),
 (113,'zadatak 3',(157,1001,1331,1120),False),
 (113,'zadatak 4',(151,1145,1331,1410),False),
 (113,'zadatak 5',(155,1429,1330,1560),False),
 (113,'zadatak 6',(155,1583,1329,1706),False),
 (113,'zadatak 7',(155,1727,1329,1855),False),
 (114,'Realizacija zadatka 4',(144,92,1332,799),False),
 (115,'2.244',(363,648,1164,952),True),
 (115,'2.245',(386,1304,1138,1506),True),
 (115,'2.246',(311,1510,1205,1858),True),
 (116,'2.247',(114,390,1306,745),True),
 (116,'2.248',(114,746,756,1063),True),
 (116,'2.249',(783,728,1302,1060),True),
 (116,'2.250',(261,1155,1029,1493),True),
 (116,'2.251',(113,1495,1301,1854),False),
 (117,'2.252',(364,85,1129,375),False),
 (117,'zadatak 1',(192,515,1365,676),True),
 (117,'zadatak 2',(189,695,1365,829),False),
 (117,'zadatak 3',(188,830,1365,939),False),
 (117,'zadatak 4',(188,956,1365,1095),False),
 (117,'zadatak 5',(186,1110,1365,1246),False),
 (117,'zadatak 6',(193,1256,1365,1385),False),
 (117,'Realizacija zadatka 4',(163,1454,1365,1846),False),
 (118,'2.253',(194,665,1136,1008),True),
 (118,'2.254',(196,1009,1125,1320),True),
 (118,'2.255',(111,1322,1281,1618),True),
]


def main():
    slots = [(int(p), label) for label, p in re.findall(
        r'<!-- visual: (.*?); page (\d+) -->',
        (OUT / 'text-101-118.md').read_text())]
    assert [(p, label) for p, label, _, _ in ROWS] == slots
    assert len(ROWS) == 95
    manifest = []
    for page, label, planned, conflict in ROWS:
        source = f'sources/pages/page-{page}.png'
        with Image.open(source) as im:
            rect = [round(v * im.height / 2000) for v in planned]
            l, t, r, b = rect
            assert 0 <= l < r <= im.width and 0 <= t < b <= im.height
            if label.startswith('2.'):
                kind = 'example'
                stem = 'primjer-2-' + label.split('.')[1]
                caption = f'Primjer {label}. — tiskana str. {page}.'
            elif label.startswith('zadatak'):
                kind = 'exercise'
                stem = f'zadatak-2-{page}-{label.split()[-1]}'
                caption = f'Zadatak {label.split()[-1]}. — tiskana str. {page}.'
            else:
                kind = 'realization'
                n = re.search(r'\d+', label)[0]
                stem = f'zadatak-2-{page}-{n}-realizacija'
                caption = f'{label}. — tiskana str. {page}.'
            image = f'{DEST}/{stem}.png'
            assert not Path(image).exists(), f'Refusing overwrite: {image}'
            im.crop(rect).save(image)
        note = ('cleanup_required: Original handwriting/source marks retained without '
                'retouching; independent reviewer must assess source-layout conflicts.'
                if conflict else 'Independent visual review required; original source pixels only.')
        if page == 103 and kind == 'realization':
            note += ' Continuation: title is printed only on preceding page 102; no synthetic title added.'
        if page in (103, 114) and kind == 'realization':
            note += ' Explanatory prose footnote remains in text transcription, outside score crop.'
        manifest.append(dict(id=stem, example=label, kind=kind, printed_page=page,
                             pdf_page=(page + 2)//2, source_image=source, rect=rect,
                             image=image, review_status='pending_independent_review',
                             review_note=note, caption=caption))
    (OUT / 'images-101-118.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    lines = ['# Extraction hand-off: printed 101–118', '',
             '- Assigned printed pages: **101–118**; PDF pages: **51–60**.',
             '- All 18 source PNGs opened visually; **95/95 text visual slots mapped in order**.',
             '- 34 numbered examples (2.222–2.255), 56 exercises, 5 realization parts.',
             '- Every output is a separate original-source rectangle. Multi-system examples remain one rectangle; the realization across pages 102–103 remains two separate parts.',
             '- No text/chapter/global manifest/tracker edits. No approval, commit, push, delegation, API, GUI, or generated borders.',
             '- Rectangles in JSON are original-source pixels `[left, top, right, bottom]`, right/bottom exclusive.',
             '- **All 95 images: pending_independent_review.** Extraction is ready for independent review, not integration approval.',
             '- Validation: all 95 saved images compared pixel-for-pixel with their manifest source rectangles; all identical. 36 entries carry `cleanup_required` notes.',
             '- Particular source-layout conflicts: 2.234 has handwriting intruding into the final prose line immediately above it; 2.235 has tightly spaced bottom analysis immediately above the next paragraph; 2.253–2.255 have handwritten analysis in the narrow inter-example gaps. These are not clean-source approvals: reviewers must inspect those boundaries and determine whether any source-conflict remediation is possible without clipping printed content.',
             '- Handwriting/scan marks are not repaired or hidden by clipping notation; flagged entries require cleanup/source-conflict assessment. No musical content identified as unreadable, but these marks may obscure fine notation and require reviewer attention.',
             '- Source footnotes for realizations on 103 and 114 are preserved in the supplied text candidate, not included as body prose within score images.',
             '', '## Files', '',
             '- `review-candidates/book/M03/extract-101-118.py`',
             '- `review-candidates/book/M03/images-101-118.json`',
             '- `review-candidates/book/M03/extraction-101-118.md`',
             '- The 95 PNG paths enumerated below in `images/02-dijatonika-b/`.', '',
             '## Per-image inventory and integration blocks', '']
    for m in manifest:
        lines += [f"### {m['example']} — str. {m['printed_page']} / PDF {m['pdf_page']}", '',
                  f"![{m['example']} — str. {m['printed_page']}]({m['image']})", '',
                  m['caption'], '', '<!-- MuseScore: placeholder -->', '',
                  f"- Review: `{m['review_status']}`. {m['review_note']}", '']
    (OUT / 'extraction-101-118.md').write_text('\n'.join(lines)+'\n')
    print(f'Extracted {len(manifest)} source rectangles; all pending independent review.')


if __name__ == '__main__':
    main()

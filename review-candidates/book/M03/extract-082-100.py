"""Individually sighted source-pixel rectangles; extraction only, no approval.

Coordinates below use the source-page viewer's 2000-pixel-high reference
frame, converted once to integer original pixels. Manifest rect is Pillow
[left, top, right, bottom), in original source pixels. No resampling of crops.
Existing images are never overwritten unless already byte-identical.
"""
import hashlib
import io
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
LOCAL = ROOT / 'review-candidates/book/M03'
OUT = 'images/02-dijatonika-b'

# Each rectangle was selected individually after opening its source PNG.
# Order on each page is the exact order of local text visual slots.
BOXES = {
    82: [(140,80,1310,350), (145,370,1310,495), (145,505,1310,640), (120,820,1310,1600)],
    83: [(430,600,1085,735), (160,1220,530,1500), (580,1210,1330,1520), (295,1550,1180,1840)],
    84: [(145,445,625,650), (670,405,1320,745), (125,1200,1320,1870)],
    85: [(170,395,550,555), (555,395,1340,725), (530,1300,975,1465), (165,1510,1340,1875)],
    86: [(520,85,935,395), (135,755,455,890), (500,745,1320,1055), (130,1350,1310,1675)],
    87: [(175,75,1355,425), (155,568,1355,1240), (170,1430,1350,1765)],
    88: [(120,550,965,890), (995,580,1305,705), (120,867,1305,1200), (125,1555,1310,1895)],
    89: [(315,280,1165,625), (160,835,955,1190), (985,825,1340,1155), (555,1525,965,1885)],
    90: [(125,105,1300,525), (405,735,1020,1090), (525,1310,935,1645)],
    91: [(350,85,1150,420), (290,421,1220,760), (170,754,1340,1085), (190,1150,1360,1298), (190,1303,1360,1454.5), (190,1454.5,1360,1592), (190,1592,1360,1737), (190,1728,1360,1835)],
    92: [(130,100,1305,230), (130,265,1305,375), (130,395,1305,500), (130,525,1305,655), (125,680,1305,805), (120,825,1305,950), (125,975,1305,1100), (120,1115,1305,1390), (120,1398,1305,1540), (120,1560,1305,1688), (120,1710,1305,1835)],
    93: [(155,85,1355,820), (310,1140,1180,1310), (170,1588,1350,1880)],
    94: [(120,330,835,710), (845,335,1305,710), (120,1210,655,1545), (760,1180,1305,1555)],
    95: [(305,260,1160,570), (155,580,1345,960), (275,1435,1225,1860)],
    96: [(335,85,1140,400), (120,775,1320,1440)],
    97: [(305,70,1190,420), (145,835,715,1038), (125,1038,1325,1725)],
    98: [(120,85,1320,443), (390,845,1060,1255), (250,1255,1225,1668)],
    99: [(155,315,1360,1075), (275,1505,1360,1875)],
    100: [(115,85,1305,425), (115,425,665,742), (675,425,1305,730), (440,740,1070,1035), (115,1035,1305,1360), (125,1420,1305,1563), (125,1568,1305,1705), (120,1715,1305,1855)],
}

# Pencil marks intersect notation/printed analysis or share its bounding box.
CONFLICTS = {
    '2.169', '2.170', '2.171', '2.172', '2.173', '2.174',
    '2.175', '2.176', '2.177', '2.178', '2.179', '2.182',
    '2.183', '2.184', '2.185', '2.186', '2.188', '2.189',
    '2.190', '2.191', '2.192', '2.193', '2.194', '2.195',
    '2.196', '2.197', '2.198', '2.199', '2.201', '2.202',
    '2.203', '2.204', '2.205', '2.206', '2.207', '2.208',
    '2.209', '2.210', '2.211', '2.212', '2.213.a—m',
    '2.213.n—t (nastavak)', '2.214.a', '2.214.b', '2.215', '2.216', '2.217',
}


def main():
    text = (LOCAL / 'text-082-100.md').read_text()
    slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->', text)
    assert len(slots) == 80
    records = []
    counters = {}
    for example, page_s in slots:
        page = int(page_s)
        index = counters.get(page, 0)
        counters[page] = index + 1
        ref_rect = BOXES[page][index]
        source = f'sources/pages/page-{page:03}.png'
        im = Image.open(ROOT / source)
        scale = im.height / 2000
        rect = [round(v * scale) for v in ref_rect]
        if example.startswith('zadatak '):
            kind = 'exercise'
            stem = f'zadatak-2-{page}-{example.split()[-1]}'
            caption = f'Zadatak {example.split()[-1]}. — str. {page}.'
        elif example.startswith('Realizacija'):
            kind = 'realization'
            n = re.search(r'\d+', example).group()
            stem = f'zadatak-2-{page}-{n}-realizacija'
            caption = f'Realizacija zadatka {n}. — str. {page}.'
        else:
            kind = 'example'
            n = re.search(r'2\.(\d+)', example).group(1)
            suffix = '-p97' if page == 97 and n == '213' else '-p98' if page == 98 and n == '213' else '-a' if example == '2.214.a' else '-b' if example == '2.214.b' else ''
            stem = f'primjer-2-{n}{suffix}'
            caption = f'Primjer {example}. — str. {page}.'
        image = f'{OUT}/{stem}.png'
        buffer = io.BytesIO()
        im.crop(rect).save(buffer, format='PNG')
        content = buffer.getvalue()
        target = ROOT / image
        if target.exists():
            assert hashlib.sha256(target.read_bytes()).digest() == hashlib.sha256(content).digest(), f'Refusing to overwrite {image}'
        else:
            target.write_bytes(content)
        note = 'Source-pixel crop; independently selected edges. Independent visual review required.'
        if example in CONFLICTS:
            note += ' cleanup_required: original pencil marks/scan interference within or immediately adjoining notation and analysis; preserved, not retouched or clipped to hide them.'
        if example == '2.213.n—t (nastavak)':
            note += ' Cross-page continuation: printed example number occurs only in the p97 part; no number fabricated here. Printed variant sequence n,o,p,r,s,t retained.'
        if example == '2.214.b':
            note += ' Printed shared example number is in part a; part b retains its own variant label and Bach attribution.'
        if example == '2.210':
            note += ' Source includes variants a–h, although prose references only a–g; h is retained.'
        if page == 91 and example in {'zadatak 4', 'zadatak 5'}:
            note += ' cleanup_required: source layout conflict: exercise 4 lowest figured-bass line and exercise 5 highest ledger note overlap vertically. Both intended contents retained; rectangular crops necessarily retain a fragment of the neighbouring exercise. No clipping of intended notation or retouching used.'
        if page == 91 and example == '2.199':
            note += ' Source layout conflict: pencil analysis from 2.198 adjoins the Schumann attribution at this crop top; preserved original pixels.'
        records.append(dict(id=f'p{page:03}:{example}', example=example, kind=kind,
                            printed_page=page, pdf_page=page//2+1,
                            source_image=source, rect=rect, image=image,
                            review_status='pending_independent_review',
                            review_note=note, caption=caption))
    assert all(counters[p] == len(BOXES[p]) for p in BOXES)
    assert len({r['image'] for r in records}) == 80
    (LOCAL / 'images-082-100.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    print(f'Extracted {len(records)} distinct source-pixel crops across {len(counters)} pages; {sum("cleanup_required" in r["review_note"] for r in records)} flagged cleanup_required.')


if __name__ == '__main__':
    main()

"""Individually selected source rectangles; no resampling, retouching or borders.

Coordinates below refer to the visually inspected 2000-pixel-high display.
Manifest rect is the resulting original-source [left, top, right, bottom].
Run from repository root. This script writes only this worker's assigned files.
"""
import json
import re
from pathlib import Path
from PIL import Image

BASE = Path('review-candidates/book/M06')
OUT = Path('images/03-kromatika-b')
# page, exact visual-slot label, display rectangle, display width
SPECS = [
 (224,'3.117',(120,92,1320,800),1459),
 (224,'3.118',(130,913,1320,1284),1459),
 (224,'3.119',(130,1380,1320,1818),1459),
 (225,'3.120',(165,111,1346,523),1459),
 (225,'ZADACI 2',(175,738,1345,903),1459),
 (225,'ZADACI 3',(174,926,1345,1074),1459),
 (225,'ZADACI 4',(175,1100,1345,1266),1459),
 (225,'ZADACI 5',(176,1287,1345,1459),1459),
 (225,'ZADACI 6',(177,1474,1346,1637),1459),
 (225,'ZADACI 7',(176,1658,1346,1751),1459),
 (226,'ZADACI 8',(139,107,1314,205),1459),
 (226,'ZADACI 9',(139,250,1314,342),1459),
 (226,'ZADACI 10',(131,382,1314,490),1459),
 (226,'ZADACI 11',(135,539,1314,641),1459),
 (226,'ZADACI 12',(134,665,1314,792),1459),
 (226,'ZADACI 13',(134,813,1314,937),1459),
 (226,'ZADACI 14',(132,960,1314,1090),1459),
 (226,'ZADACI 15',(130,1107,1314,1240),1459),
 (226,'ZADACI 16',(132,1255,1314,1378),1459),
 (226,'ZADACI 17',(132,1398,1314,1525),1459),
 (226,'ZADACI 18',(132,1546,1314,1675),1459),
 (226,'ZADACI 19',(127,1690,1314,1817),1459),
 (227,'Realizacija zadatka 7.',(164,83,1366,789),1459),
 (227,'Realizacija zadatka 12.',(170,1011,1370,1401),1459),
 (229,'3.121 a), b)',(180,70,1350,296),1459),
 (229,'3.122 a), b)',(173,821,1347,1206),1459),
 (229,'3.123',(400,1214,1111,1605),1459),
 (230,'3.124',(231,141,1178,487),1459),
 (230,'3.125 a), b), c)',(112,514,1307,1259),1459),
 (230,'3.126',(135,1529,733,1875),1459),
 (230,'3.127 a), b)',(744,1509,1309,1848),1459),
 (231,'3.128 a), b)',(198,611,1360,829),1459),
 (231,'3.129',(326,1192,1220,1584),1459),
 (232,'3.130 a)',(432,130,1008,483),1456),
 (232,'3.130 b)',(116,488,1312,843),1456),
 (232,'3.130 c)',(119,850,1313,1247),1456),
 (232,'3.131',(449,1359,977,1718),1456),
 (233,'3.132 a), b)',(173,303,1351,709),1456),
 (233,'3.133',(157,738,1352,1531),1456),
 (234,'3.134 a), b), c)',(126,131,1301,486),1456),
 (234,'3.135 a), b)',(96,687,1308,1446),1456),
 (235,'3.136 a), b), c), d), e), f)',(181,709,1354,885),1456),
 (235,'3.137 a), b)',(173,1178,1351,1569),1456),
 (236,'3.138 a), b)',(123,215,1293,625),1450),
 (236,'3.139 a)',(102,980,1287,1740),1450),
 (237,'3.139 b)',(395,125,1128,574),1450),
 (237,'ZADACI 2',(164,1518,1330,1703),1450),
 (237,'ZADACI 3',(164,1704,1328,1870),1450),
 (238,'ZADACI 4',(126,117,1297,283),1455),
 (238,'ZADACI 5',(130,285,1299,455),1455),
 (238,'ZADACI 6',(129,461,1304,806),1455),
 (238,'ZADACI 7',(140,785,1307,903),1455),
 (238,'ZADACI 8',(144,947,1309,1054),1455),
 (238,'ZADACI 9',(144,1098,1309,1205),1455),
 (238,'ZADACI 10',(139,1240,1313,1341),1455),
 (238,'ZADACI 11',(143,1364,1316,1644),1455),
 (238,'ZADACI 12',(142,1664,1320,1806),1455),
 (239,'ZADACI 13',(159,99,1336,230),1455),
 (239,'ZADACI 14',(159,250,1334,373),1455),
 (239,'ZADACI 15',(159,391,1334,518),1455),
 (239,'ZADACI 16',(159,535,1336,663),1455),
 (239,'ZADACI 17',(155,687,1338,968),1455),
 (239,'Realizacija zadatka 7.',(141,1120,1338,1821),1455),
 (240,'Realizacija zadatka 11.',(133,93,1331,1194),1459),
]

def main():
    source_index = {r['printed_page']: r for r in json.loads(Path('sources/index.json').read_text())['pages']
                    if isinstance(r['printed_page'], int) and 224 <= r['printed_page'] <= 240}
    text = (BASE / 'text-224-240.md').read_text()
    slots = [(int(p), label) for label,p in re.findall(r'<!-- visual: (.*?); page (\d+) -->',text)]
    assert [(p,label) for p,label,_,_ in SPECS] == slots
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for index,(page,label,box,display_width) in enumerate(SPECS,1):
        source = Path(source_index[page]['image'])
        with Image.open(source) as im:
            rect = [round(box[0]*im.width/display_width),round(box[1]*im.height/2000),
                    round(box[2]*im.width/display_width),round(box[3]*im.height/2000)]
            if label.startswith('3.'):
                number = re.match(r'3\.(\d+)', label)[1]
                variant = re.search(r'3\.130 ([abc])',label)
                suffix = '-' + variant[1] if variant else ''
                if number == '139': suffix = '-a' if page == 236 else '-b'
                name = f'primjer-3-{number}{suffix}.png'
                kind = 'musical_example'
                caption = f'Primjer {label}. Tiskana str. {page}.'
            else:
                num = re.search(r'\d+',label)[0]
                kind = 'realization' if label.startswith('Realizacija') else 'exercise'
                section = '3-6' if page <= 227 else '3-7-1'
                name = f'{"realizacija" if kind == "realization" else "zadatak"}-{section}-{num}.png'
                caption = f'{label.rstrip(".")}. Tiskana str. {page}.'
            target = OUT / name
            im.crop(rect).save(target)
        note = 'Source-only crop; individually selected four edges. Independent visual review required.'
        cleanup = page == 238 and label in ('ZADACI 6','ZADACI 7')
        if cleanup:
            note += ' cleanup_required: inseparable rectangular source layout. Lowest figures of exercise 6 overlap vertically with highest accidental of exercise 7. All intended notation retained, with unavoidable foreign ink at the shared edge; no retouching. This crop cannot pass the clean-edge checklist as-is.'
        if label in ('3.130 b)','3.130 c)','3.139 b)'):
            note += ' Variant-only source part: example number occurs on preceding part; no number synthesized.'
        if page == 236 and label == '3.139 a)':
            note += ' Attribution is in adjacent prose, not printed within this score block; retained in text, not copied into image.'
        records.append(dict(id=f'M06-p{page}-slot-{index:02d}',example=label,kind=kind,
            printed_page=page,pdf_page=source_index[page]['pdf_page'],source_image=source.as_posix(),rect=rect,
            image=target.as_posix(),review_status='pending_independent_review',review_note=note,caption=caption,
            cleanup_required=cleanup))
    (BASE/'images-224-240.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    lines = ['# Extraction hand-off: printed pages 224–240', '',
        '- Assigned source: printed pages 224–240; PDF pages 113–121 (1-based).',
        '- All 17 source PNGs opened visually. Page 228 has no visual slot.',
        '- 64 slots map one-to-one to 64 source-pixel PNG crops; no stitching, borders, retouching or resampling.',
        '- `rect` is local source PNG `[left, top, right, bottom]`, right/bottom exclusive; paths are repository-root-relative.',
        '- Cross-page example 3.139 has separate a/b files (236/237). Example 3.130 has separate a/b/c files matching its three slots.',
        '- Multisystem examples/exercises retain their full same-page systems in one source rectangle.',
        '- Realization titles are inside their crops; prose footnotes remain in the verified text.',
        '- No chapter, verified prose, global manifest, tracker, earlier crop, or other worker output changed.',
        '- No unreadable musical material identified. cleanup_required: page 238 exercises 6 and 7 have vertically overlapping figure/accidental extents; original pixels preserved with unavoidable foreign ink at the shared edge. These two crops cannot pass the clean-edge checklist as-is.',
        '- Each resulting crop was opened individually for extraction edge inspection; this is not independent approval.',
        '- Every image is pending_independent_review, not self-approved. Ready for independent image review, NOT final integration.',
        '', '## Slot / image hand-off', '', '| Page | Slot | Image | Review |', '| --- | --- | --- | --- |']
    for r in records:
        flag = '; cleanup_required' if r['cleanup_required'] else ''
        lines.append(f'| {r["printed_page"]} | {r["example"]} | `{r["image"]}` | pending_independent_review{flag} |')
    (BASE/'extraction-224-240.md').write_text('\n'.join(lines)+'\n')
    print(f'Wrote {len(records)} crops and assigned manifest/report.')

if __name__ == '__main__':
    main()

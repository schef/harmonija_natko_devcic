"""Reproducible original-pixel crops, individually chosen from visually opened pages.

SPECS use the 2000-high source display coordinates, not fixed crop margins.
Manifest rectangles are local original PNG coordinates, right/bottom exclusive.
Run from repository root. No retouching, stitching, resampling or added borders.
"""
import json
import re
from pathlib import Path
from PIL import Image

BASE = Path('review-candidates/book/M06')
OUT = Path('images/03-kromatika-b')
SPECS = [
 (241,'3.140',(172,248,1345,679)),
 (241,'3.141',(171,709,1344,1126)),
 (241,'3.142',(177,1695,1346,1848)),
 (242,'3.143',(156,809,1309,1080)),
 (242,'3.144 a–b',(133,1511,1310,1863)),
 (243,'3.144 c',(426,92,1105,433)),
 (243,'3.145',(174,462,1348,835)),
 (243,'3.146',(328,976,1183,1299)),
 (243,'3.147',(170,1311,1348,1677)),
 (244,'3.148',(125,1033,1160,1370)),
 (244,'3.149',(128,1396,1308,1713)),
 (245,'3.150',(176,104,1354,402)),
 (245,'3.151',(372,594,1127,949)),
 (245,'3.152',(174,958,1350,1679)),
 (246,'3.153',(435,91,1010,440)),
 (246,'3.154',(132,852,1305,1085)),
 (246,'3.155',(132,1074,1306,1330)),
 (246,'3.156',(122,1545,1306,1865)),
 (247,'ZADACI 2',(181,252,1358,419)),
 (247,'ZADACI 3',(179,435,1358,788)),
 (247,'ZADACI 4',(180,796,1357,1037)),
 (247,'ZADACI 5',(184,1063,1356,1305)),
 (247,'ZADACI 6',(185,1321,1356,1577)),
 (247,'ZADACI 7',(185,1590,1357,1868)),
 (248,'ZADACI 8',(159,98,1321,226)),
 (248,'ZADACI 9',(150,232,1321,521)),
 (248,'Realizacija zadatka 7.',(115,530,1320,1658)),
 (249,'3.157',(177,873,1350,1098)),
 (249,'3.158',(178,1110,1350,1320)),
 (249,'3.159',(180,1343,1351,1497)),
 (250,'3.160',(377,118,1036,283)),
 (250,'3.161',(201,653,1232,878)),
 (250,'3.162',(131,1127,665,1475)),
 (250,'3.163',(668,1128,1307,1473)),
 (250,'3.164',(132,1478,1307,1880)),
 (251,'3.165',(284,205,1227,555)),
 (251,'3.166',(216,557,1290,962)),
 (251,'3.167',(341,1154,1152,1503)),
 (251,'3.168',(163,1512,1356,1875)),
 (252,'3.169',(106,121,1309,866)),
 (252,'3.170 a–c',(123,1452,1310,1842)),
 (253,'3.170 d',(453,98,1049,453)),
 (253,'ZADACI 2',(169,1038,1350,1408)),
 (253,'ZADACI 3',(171,1409,1350,1596)),
 (253,'ZADACI 4',(172,1605,1350,1704)),
 (253,'ZADACI 5',(171,1726,1351,1863)),
 (254,'ZADACI 6',(120,85,1294,201)),
 (254,'Realizacija zadatka 5.',(104,210,1306,899)),
 (255,'3.171',(157,61,1340,351)),
 (255,'3.172',(146,363,1340,977)),
 (255,'3.173',(158,983,1340,1385)),
 (255,'3.174',(158,1385,1338,1800)),
 (256,'3.175',(115,356,1307,1342)),
]

def main():
    pages = {r['printed_page']: r for r in json.loads(Path('sources/index.json').read_text())['pages']
             if isinstance(r['printed_page'], int) and 241 <= r['printed_page'] <= 256}
    text = (BASE/'text-241-256.md').read_text()
    slots = [(int(p),label) for label,p in re.findall(r'<!-- visual: (.*?); page (\d+) -->',text)]
    assert [(p,label) for p,label,_ in SPECS] == slots
    assert len(slots) == 53
    records = []
    for i,(page,label,box) in enumerate(SPECS,1):
        source = Path(pages[page]['image'])
        with Image.open(source) as im:
            width = round(im.width/im.height*2000)
            rect = [round(box[0]*im.width/width),round(box[1]*im.height/2000),
                    round(box[2]*im.width/width),round(box[3]*im.height/2000)]
            if label.startswith('3.'):
                number = re.match(r'3\.(\d+)',label)[1]
                suffix = { (242,'144'):'-ab',(243,'144'):'-c',
                           (252,'170'):'-abc',(253,'170'):'-d' }.get((page,number),'')
                name = f'primjer-3-{number}{suffix}.png'
                kind = 'musical_example'
                caption = f'Primjer {label}. Tiskana str. {page}.'
            else:
                num = re.search(r'\d+',label)[0]
                kind = 'realization' if label.startswith('Realizacija') else 'exercise'
                section = '3-7-2' if page <= 248 else '3-7-3'
                name = f'{"realizacija" if kind == "realization" else "zadatak"}-{section}-{num}.png'
                caption = f'{label.rstrip(".")}. Tiskana str. {page}.'
            target = OUT/name
            im.crop(rect).save(target)
        note = 'Original source pixels only; four edges individually selected. Independent visual review required.'
        if (page,label) in ((243,'3.144 c'),(253,'3.170 d')):
            note += ' Continuation part: printed example number occurs only in preceding part; not synthesized or repeated.'
        if (page,label) in ((246,'3.154'),(246,'3.155'),(255,'3.173'),(255,'3.174')):
            note += ' Tight natural separation from adjacent example; inspect shared horizontal edge particularly closely.'
        cleanup = page == 246 and label in ('3.154','3.155')
        if cleanup:
            note += ' cleanup_required: lowest figures of 3.154 and highest variant label of 3.155 have inseparable rectangular extents. Preserve original notation and unavoidable adjacent ink; no painting or clipping to hide it.'
        records.append(dict(id=f'M06-p{page}-slot-{i:02d}',example=label,kind=kind,
            printed_page=page,pdf_page=pages[page]['pdf_page'],source_image=source.as_posix(),rect=rect,
            image=target.as_posix(),review_status='pending_independent_review',review_note=note,
            caption=caption,cleanup_required=cleanup))
    (BASE/'images-241-256.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    lines = ['# Extraction hand-off: printed pages 241–256','',
        '- Assigned source: printed pages 241–256; PDF pages 121–129 (1-based).',
        '- Every assigned source PNG opened visually; 53 visual slots map one-to-one to 53 separate crops.',
        '- Original pixels only: no resampling, artificial margin, retouching, repeated labels, or stitching.',
        '- Manifest paths are repository-root-relative; rect is local source PNG [left, top, right, bottom], right/bottom exclusive.',
        '- Examples 3.144 and 3.170 retain separate cross-page parts. Continuation parts have no synthesized example number.',
        '- Attributions and realization titles retained inside crops; prose footnotes remain in verified text.',
        '- Every resulting crop was opened individually for extraction inspection (not independent approval).',
        '- All 53 images: pending_independent_review. No extractor self-approval.',
        '- Tight shared edges: 3.154/3.155 (246), 3.173/3.174 (255); reviewer should verify full-resolution separation.',
        '- cleanup_required: 3.154 and 3.155 have inseparable rectangular figure/variant extents; intended content retained with unavoidable adjacent ink. No source cleanup applied. These cannot pass the clean-edge checklist as-is.',
        '- Earlier pages, other workers, chapter files, global trackers and raw manifests unchanged.',
        '- Ready for independent visual review, NOT final integration.','',
        '## Complete slot identity mapping','',
        '| Printed page | PDF page | Slot | Image | Review |',
        '| --- | --- | --- | --- | --- |']
    for r in records:
        flag = '; cleanup_required' if r['cleanup_required'] else ''
        lines.append(f'| {r["printed_page"]} | {r["pdf_page"]} | {r["example"]} | `{r["image"]}` | pending_independent_review{flag} |')
    (BASE/'extraction-241-256.md').write_text('\n'.join(lines)+'\n')
    print(f'Wrote {len(records)} crops, manifest and hand-off.')

if __name__ == '__main__':
    main()

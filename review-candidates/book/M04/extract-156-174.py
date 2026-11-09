"""Source-pixel crops for printed 156–174 only; no retouching or resampling.

Each rectangle was individually selected from a source-page view at height
2000. Only the coordinate system is scaled; output is an original PNG crop.
Run from repository root. No shared manifest or chapter files are changed.
"""
import json
import re
from pathlib import Path
from PIL import Image

BASE = Path('review-candidates/book/M04')
OUT = Path('images/02-dijatonika-c')
# page, example number (exercise numbers prefixed z), independently chosen bounds
PLAN = [
    [156, '373', [267, 593, 1126, 920]],
    [157, '374', [186, 75, 1377, 420]],
    [157, '375', [277, 433, 1273, 785]],
    [157, '376', [173, 1072, 1364, 1430]],
    [157, '377', [173, 1430, 1365, 1827]],
    [158, '378', [99, 587, 1294, 1246]],
    [158, '379', [109, 1235, 1293, 1853]],
    [159, '380', [135, 975, 1326, 1818]],
    [160, 'z2', [128, 296, 1300, 448]],
    [160, 'z3', [127, 471, 1299, 633]],
    [160, 'z4', [124, 642, 1299, 961]],
    [160, 'z5', [126, 982, 1299, 1308]],
    [160, 'z6', [127, 1315, 1295, 1413]],
    [160, 'z7', [129, 1457, 1295, 1561]],
    [160, 'z8', [128, 1572, 1295, 1710]],
    [161, 'z9', [177, 117, 1345, 244]],
    [161, 'z10', [174, 252, 1344, 391]],
    [161, 'z11', [175, 406, 1344, 537]],
    [161, 'z12', [174, 546, 1343, 674]],
    [161, 'z13', [171, 674, 1346, 1117]],
    [161, 'z14', [169, 1135, 1344, 1708]],
    [161, 'z15', [165, 1713, 1344, 1846]],
    [162, 'z15', [133, 115, 1310, 394]],
    [162, 'z16', [133, 413, 1309, 546]],
    [162, 'z17', [131, 548, 1310, 840]],
    [162, '381', [314, 1715, 1112, 1887]],
    [163, '382', [159, 435, 1344, 1389]],
    [164, '383', [130, 99, 1310, 823]],
    [164, '384', [209, 1081, 1243, 1467]],
    [165, '385', [162, 822, 1331, 1104]],
    [166, '386', [140, 260, 1321, 1247]],
    [167, '387', [175, 99, 761, 379]],
    [167, '388', [766, 100, 1354, 378]],
    [167, '389', [173, 478, 763, 758]],
    [167, '390', [769, 479, 1353, 758]],
    [168, '391', [127, 312, 1313, 644]],
    [168, '392', [128, 644, 1313, 921]],
    [168, '393', [128, 936, 1313, 1238]],
    [168, '394', [127, 1243, 1314, 1518]],
    [168, '395', [128, 1537, 1315, 1837]],
    [169, '396', [154, 80, 1351, 1129]],
    [169, '397', [153, 1134, 1350, 1853]],
    [170, '398', [121, 85, 1327, 820]],
    [171, '399', [169, 286, 1353, 660]],
    [171, '400', [169, 641, 1353, 1022]],
    [171, '401', [169, 978, 1354, 1322]],
    [171, '402', [172, 1542, 1354, 1857]],
    [172, '403', [288, 89, 1143, 410]],
    [172, '404', [121, 524, 1301, 880]],
    [172, '405', [120, 883, 1303, 1301]],
    [172, '406', [121, 1489, 1301, 1875]],
    [173, '407', [154, 35, 1351, 752]],
    [173, '408', [166, 967, 1349, 1297]],
    [173, '409', [167, 1291, 1351, 1618]],
    [173, '409b', [445, 1621, 1041, 1894]],
]

NOTES = {
    '378': 'cleanup_required: lowest stems of example 2.378 overlap the vertical band of the following boxed C–fis–C title. Complete example content retained; a rectangular crop includes the upper portion of that neighbouring title.',
    '379': 'cleanup_required: boxed C–fis–C identifying title shares its vertical band with lowest stems of preceding example 2.378; source pixels preserved.',
    '381': 'cleanup_required: faint handwritten chord labels/notes interleave printed variants and lower figures. No retouching; printed bottom 5 retained.',
    '382': 'cleanup_required: extensive faint handwritten annotations surround and interleave both printed variants and analyses; source pixels preserved.',
    '383': 'cleanup_required: handwriting above, below and between printed variants/analyses cannot be excluded while preserving the complete example.',
    '384': 'cleanup_required: faint handwritten harmonic labels interleave printed title and lower analysis; source pixels preserved.',
    '391': 'cleanup_required: handwritten chord names and Roman numerals interleave the example; source pixels preserved.',
    '392': 'cleanup_required: faint tail of handwritten analysis of preceding example lies in the same vertical band as the Frigijski identifying title.',
    '399': 'cleanup_required: complete lowest fermata shares vertical space with highest stems of following example 2.400; rectangular source crop retains a small neighbouring stem fragment.',
    '400': 'cleanup_required: highest stems share vertical space with preceding example 2.399 lowest fermata; lowest slur/fermata share vertical space with following example 2.401 attribution and upper slur. Neighbouring fragments preserved rather than clipping notation.',
    '401': 'cleanup_required: complete attribution shares vertical space with preceding example 2.400 lowest slur/fermata. Neighbouring fragments preserved rather than clipping the identifying title.',
    '408': 'cleanup_required: lowest staccato mark shares vertical space with highest stems of following example 2.409; rectangular crop preserves neighbouring stem tips.',
    '409': 'cleanup_required: highest stems share vertical space with lowest staccato mark of preceding example 2.408; neighbouring fragment retained rather than clipping notation.',
}


def main():
    pages = {p['printed_page']: p for p in json.loads(
        Path('sources/index.json').read_text())['pages'] if p['printed_page'] is not None}
    slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->',
                       (BASE / 'text-156-174.md').read_text())
    assert len(slots) == 54 and len(PLAN) == 55
    assert len({(p, n) for p, n, _ in PLAN}) == 55
    covered = set()
    OUT.mkdir(exist_ok=True, parents=True)
    records = []
    for page, num, view_rect in PLAN:
        slot_num = '409' if num == '409b' else num
        exercise = num.startswith('z')
        prefix = f'zadatak {slot_num[1:]}' if exercise else f'primjer 2.{slot_num}'
        matches = [(label, p) for label, p in slots if int(p) == page and
                   (label == prefix or label.startswith(prefix + ' ') or label.startswith(prefix + ','))]
        assert len(matches) == 1, (page, num, matches)
        label, slot_page = matches[0]
        covered.add((label, slot_page))
        ident = (f'zadatak-2-9-6-{num[1:]}' if exercise else f'primjer-2-{num}')
        if num == '409':
            ident += '-a'
        elif num == '409b':
            ident = 'primjer-2-409-b'
        if num == 'z15':
            ident += '-pocetak' if page == 161 else '-nastavak'
        target = OUT / f'{ident}.png'
        source = pages[page]['image']
        with Image.open(source) as im:
            rect = [round(v * im.height / 2000) for v in view_rect]
            assert 0 <= rect[0] < rect[2] <= im.width
            assert 0 <= rect[1] < rect[3] <= im.height
            im.crop(rect).save(target)
        note = NOTES.get(num, 'Individual source-only rectangle; all printed variants, analyses and identifying text retained. Independent full-resolution edge review required.')
        if num == '409b':
            note = 'Separate lower variant b of example 2.409; no repeated number/attribution in this source part. Pair with -a. Narrow source rectangle excludes bottom-right printed page number while preserving the complete lower bracket and genuine margin.'
        if num == 'z15':
            note = ('Cross-page exercise, separate source-only part; ' +
                    ('number printed here; continues on printed 162.' if page == 161 else 'no repeated number in source; pair with beginning on printed 161.'))
        caption = f'{label[0].upper() + label[1:]}. Tiskana str. {page}; PDF str. {pages[page]["pdf_page"]}.'
        if slot_num == '409':
            caption = f'Primjer 2.409, varijanta {"b" if num == "409b" else "a"}. Dvořak: Simfonija br. 9 u e-molu. Tiskana str. 173; PDF str. 87.'
        records.append(dict(id=ident, example=f'zadatak {num[1:]}' if exercise else f'2.{slot_num}',
                            kind='exercise' if exercise else ('diagram' if num == '385' else 'musical_example'),
                            printed_page=page, pdf_page=pages[page]['pdf_page'],
                            source_image=source, rect=rect, image=str(target),
                            review_status='pending_independent_review', review_note=note, caption=caption))
    assert len(covered) == 54
    (BASE / 'images-156-174.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    report = ['# Extraction hand-off: printed 156–174', '',
              '- Assigned: printed 156–174 inclusive (19 pages), PDF 79–88.',
              '- All 19 source pages opened visually; printed 174 confirmed blank (scan specks only).',
              '- All 54 visual slots matched: 37 numbered examples (2.373–2.409) plus 17 exercise parts (2–17, exercise 15 split at the page boundary). 55 PNGs because example 2.409 has separate a/b rectangles to exclude the page number without clipping its lower bracket. No stitching.',
              '- Source pixels cropped losslessly; no generated border, retouching, deskewing or output resizing.',
              '- Four edges of every crop inspected in native-resolution edge strips after initial source-page inspection; flagged overlaps are exceptions, not approvals. Corrected the 2.400 lowest slur and 2.401 attribution after this check.',
              '- Changed only this hand-off, `review-candidates/book/M04/images-156-174.json`, `review-candidates/book/M04/extract-156-174.py`, and the 55 listed PNGs in `images/02-dijatonika-c/`.',
              '- Earlier files through printed 155, chapter text, global manifests and trackers were not edited.',
              '- Every image is **pending_independent_review**; none is self-approved. Ready for independent review, **not final integration**.',
              '- Handwriting/layout exceptions are recorded per image below. No source passage in this assignment is missing; faint handwriting is not interpreted as printed analysis.', '',
              '## Image inventory and proposed integration blocks', '']
    for r in records:
        report += [f'### {r["id"]}', '', f'![{r["caption"]}]({r["image"]})', '',
                   r['caption'], '', f'<!-- MuseScore: {r["id"]}; pending -->', '',
                   f'- Review: `{r["review_status"]}`.', f'- Note: {r["review_note"]}', '']
    (BASE / 'extraction-156-174.md').write_text('\n'.join(report) + '\n')
    print(f'Wrote {len(records)} source-only crops and assigned manifest/hand-off.')


if __name__ == '__main__':
    main()

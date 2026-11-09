"""Source-only individually selected crops, printed 207–223; run at repo root.

Selection coordinates use the visually opened 2000-high source display.
Manifest rectangles use native local pixels (left/top inclusive, right/bottom
exclusive). No padding, resampling, cleaning, stitching, or generated pixels.
Existing different outputs are backed up rather than silently discarded.
"""
from pathlib import Path
from PIL import Image
import hashlib
import json
import re
import shutil


# page, identifier, four individually chosen display edges, special note
SPECS = [
    (207, '79', (330, 746, 1214, 938), ''),
    (207, '80', (254, 1104, 1274, 1440), ''),
    (208, '81', (137, 323, 1311, 989), 'Includes all eight printed variants a–h, not only those cited in prose.'),
    (208, '82', (143, 999, 1307, 1325), ''),
    (208, '83', (140, 1533, 1305, 1892), 'cleanup_required: printed page number begins above the bottom of the lowest figured-bass 4. A single intact rectangular crop cannot exclude it without clipping the figure or example number; page number retained whole, no retouching.'),
    (209, '84', (167, 379, 1333, 746), ''),
    (209, '85', (146, 783, 1327, 1495), ''),
    (210, '86', (136, 491, 1323, 1204), ''),
    (210, '87', (284, 1229, 1170, 1565), ''),
    (211, '88', (408, 75, 1156, 520), ''),
    (211, '89', (165, 800, 1363, 1468), 'Two systems retained with Beethoven attribution.'),
    (211, '90', (174, 1470, 1361, 1826), 'Schumann attribution retained.'),
    (212, '91', (125, 97, 1312, 459), 'Beethoven attribution retained.'),
    (212, '92', (259, 493, 1187, 900), 'Chopin attribution and lowest bass notes retained.'),
    (212, 'z2', (141, 1080, 1314, 1226), ''),
    (212, 'z3', (138, 1235, 1316, 1416), ''),
    (212, 'z4', (135, 1409, 1314, 1731), 'cleanup_required: both systems retained. Lowest figure ends at display y1726.6, while exercise 5 high note begins at y1724.3 in another column; a rectangular crop necessarily includes a tip of the adjacent high note.'),
    (212, 'z5', (140, 1722, 1314, 1918), 'cleanup_required: exercise 4 lowest figure overlaps the top band of exercise 5 high note; printed page number begins before the lowest exercise 5 figures end. Intact notation and complete page number retained; unavoidable foreign partial figure at top flagged, not retouched.'),
    (213, 'z6', (184, 65, 1360, 216), ''),
    (213, 'z7', (185, 217, 1359, 344), ''),
    (213, 'z8', (184, 365, 1360, 488), ''),
    (213, 'z9', (181, 510, 1357, 634), ''),
    (213, 'z10', (176, 663, 1359, 790), ''),
    (213, 'z11', (175, 805, 1358, 931), ''),
    (213, 'z12', (177, 953, 1359, 1077), ''),
    (213, 'z13', (175, 1098, 1359, 1218), ''),
    (213, 'r7', (158, 1228, 1360, 1876), 'Realizacija zadatka 7. title and both systems retained; page number excluded.'),
    (214, '93', (135, 1003, 1307, 1211), 'cleanup_required: source pencil marks among notation/figures, including below variant a; preserved without retouching.'),
    (214, '94', (208, 1620, 1217, 1840), ''),
    (215, '95', (300, 552, 710, 797), 'Bottom edge excludes pencil word below staff while retaining printed stems.'),
    (215, '96', (733, 553, 1222, 868), 'cleanup_required: handwriting alongside and beneath printed figures is inseparable in rectangular crop; retained.'),
    (215, '97', (255, 1357, 1266, 1512), ''),
    (216, '98', (342, 207, 1084, 362), 'cleanup_required: pencil circles around variant labels a and c retained.'),
    (216, '99', (294, 559, 1138, 882), 'cleanup_required: pencil analysis overlaps notation and figured bass; retained.'),
    (216, '100', (107, 888, 1300, 1543), 'cleanup_required: pencil analysis inside systems and beneath figures retained. All a–f and two systems included; exterior right-margin writing excluded where feasible.'),
    (216, '101-a-c', (125, 1562, 1306, 1882), 'cleanup_required: pencil analysis overlaps variant c and staff. First part only, a–c; printed example number retained.'),
    (217, '101-d-f', (163, 57, 1359, 416), 'cleanup_required: pencil marks near variant d and within staff retained. Continuation d–f; source does not repeat example number.'),
    (217, '102', (310, 731, 1209, 1065), 'cleanup_required: handwriting between staves and around notation/figures retained.'),
    (217, '103', (166, 1528, 1355, 1879), 'cleanup_required: pencil marks/circles intersect notation/figures; retained without retouching. Top handwriting meets boundary below preceding prose.'),
    (218, '104', (120, 392, 1307, 733), 'cleanup_required: pencil circle around first figured bass retained.'),
    (218, '105', (121, 1008, 1307, 1735), 'Both systems a–h and terminal itd. retained.'),
    (219, '106', (153, 773, 1353, 1598), 'cleanup_required: extensive source handwriting interleaved with labels, notation and figured bass; retained. Two systems a–e.'),
    (220, '107', (115, 337, 1305, 1376), 'cleanup_required: extensive handwriting interleaved with all three systems a–i. Source pencil strokes extend into preceding prose, so upper handwritten strokes meet crop boundary; printed prose excluded. Lowest printed figures retained; separate bottom pencil analysis omitted to avoid the next attribution.'),
    (220, '108', (129, 1376, 1306, 1740), 'cleanup_required: preceding-example pencil analysis occupies same top band as Chopin attribution; lower annotation is retained rather than erased. Attribution and a–c retained; explanatory prose footnotes remain in text, outside score crop.'),
    (221, '109', (451, 444, 1107, 659), 'cleanup_required: pencil analysis overlaps labels and notation; retained.'),
    (221, '110', (166, 681, 1340, 1030), 'cleanup_required: handwritten figures/circles interleaved with printed notation; retained.'),
    (221, '111', (438, 1250, 1105, 1614), 'cleanup_required: pencil analysis overlaps notation and printed figures; retained. Upper pencil marks meet boundary below preceding prose underline.'),
    (222, '112', (477, 62, 997, 371), 'cleanup_required: handwriting within and below staves; retained alongside complete figured bass.'),
    (222, '113', (125, 973, 1303, 1325), 'cleanup_required: pencil figures alongside printed analysis retained. Lowest printed 3 of variant c overlaps vertical band of following example title at another x-position; complete figure retained with unavoidable foreign title fragment at bottom left.'),
    (222, '114', (123, 1307, 1022, 1678), 'Top edge retains full C(c)–G(g) title; narrower right edge excludes preceding example c lowest figures.'),
    (223, '115', (163, 225, 1349, 909), 'All five variants a–e, both systems and lowest figures retained.'),
    (223, '116', (271, 1117, 1254, 1488), ''),
]


def preserve_write(path, data):
    if path.exists():
        old = path.read_bytes()
        if old == data:
            return
        digest = hashlib.sha256(old).hexdigest()[:12]
        backup = path.with_name(path.name + '.before-207-223-' + digest)
        if not backup.exists():
            shutil.copy2(path, backup)
    path.write_bytes(data)


def main():
    import io
    out = Path('images/03-kromatika-b')
    out.mkdir(parents=True, exist_ok=True)
    index = {p['printed_page']: p for p in json.loads(Path('sources/index.json').read_text())['pages']}
    slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->', Path('review-candidates/book/M06/text-207-223.md').read_text())
    assert len(slots) == len(SPECS) == 52
    records = []
    for (page, num, edges, note), (slot, slot_page) in zip(SPECS, slots):
        assert page == int(slot_page)
        if num.startswith('z'):
            kind, example = 'exercise', 'Zadatak ' + num[1:]
            stem = f'zadatak-3-{page}-{num[1:]}'
        elif num.startswith('r'):
            kind, example = 'realization', 'Realizacija zadatka ' + num[1:]
            stem = f'realizacija-3-{page}-zadatak-{num[1:]}'
        else:
            kind, example = 'example', '3.' + num.split('-')[0]
            stem = 'primjer-3-' + num
        source = index[page]['image']
        im = Image.open(source)
        scale = im.height / 2000
        rect = [round(v * scale) for v in edges]
        assert 0 <= rect[0] < rect[2] <= im.width
        assert 0 <= rect[1] < rect[3] <= im.height
        image = out / (stem + '.png')
        buf = io.BytesIO()
        im.crop(rect).save(buf, format='PNG')
        preserve_write(image, buf.getvalue())
        caption = (f'Primjer {slot}' if kind == 'example' else example) + f', str. {page}.'
        records.append(dict(id=stem, example=example, kind=kind,
            printed_page=page, pdf_page=index[page]['pdf_page'],
            source_image=source, rect=rect, image=str(image),
            review_status='pending_independent_review',
            review_note=(note + ' ' if note else '') + 'Source-only crop; independent full-resolution content and four-edge review required.',
            caption=caption))
    preserve_write(Path('review-candidates/book/M06/images-207-223.json'),
        (json.dumps(records, ensure_ascii=False, indent=2) + '\n').encode())
    report = [
        '# M06 extraction hand-off: printed pages 207–223',
        '',
        '- Assignment: 17 printed pages, 207–223; PDF pages 104–112 (1-based, taken from `sources/index.json`).',
        '- All 17 source PNGs opened visually. All 52 score crops opened separately for extractor content/edge checks; this is not independent approval.',
        '- Exact mapping: 52 visual slots → 52 PNGs. Example 3.101 remains two separate source-page parts (a–c on 216; d–f on 217). No stitching.',
        '- Image directory: `images/03-kromatika-b/` (only this assignment’s names).',
        '- Manifest: `review-candidates/book/M06/images-207-223.json`.',
        '- Reproduction script: `review-candidates/book/M06/crops-207-223.py`.',
        '- Existing partial script `review-candidates/book/M06/crops.py` preserved unchanged. Image directory was empty on initial inspection. Revised extraction outputs retain checksum-named `.before-207-223-*` backups.',
        '- Manifest `rect` is `[left, top, right, bottom]` in local native source pixels, right/bottom exclusive; paths are repository-root-relative. The script converts independently chosen visual coordinates to native pixels before direct PIL crop.',
        '- PDF-index discrepancy for integration: even-page comments in `review-candidates/book/M06/text-207-223.md` are one lower than `sources/index.json`. Manifest follows the required source index: printed 208→PDF105, 210→106, 212→107, 214→108, 216→109, 218→110, 220→111, 222→112. Text was not edited.',
        '- Validation: all 52 manifest links exist, all IDs/paths are unique, all slots map in order, and every PNG is pixel-identical to its native source rectangle. This mechanical validation does not constitute independent visual approval.',
        '- No scan resampling, generated borders, retouching, page stitching, chapter edits, shared tracker edits, global manifest edits, commits, pushes, or delegation.',
        '',
        '## Review disposition',
        '',
        '**Every image is `pending_independent_review`. None is self-approved. Not ready for integration.** Ready to hand off for independent review, including the explicitly unresolved cleanup/layout exceptions below.',
        '',
        'Source pencil analysis is inseparable from printed notation in a number of examples. It was preserved and flagged, not erased. A clean score-only result cannot be claimed for those images. No printed notation was intentionally omitted as a substitute for cleanup. Particularly crowded original layouts: 3.83/page 208 (page number overlaps the lowest figure band); exercises 4–5/page 212 (neighboring high note/lowest figure overlap, plus exercise 5 figures overlap the page-number band); 3.107–108/page 220 (pencil analysis overlaps attribution); 3.113–114/page 222 (lowest figure overlaps next title band). These require an independent decision, alternate source, or an explicitly authorized multi-part extraction; no fabricated separation was used.',
        '',
        'No unreadable printed passage was discovered in the assigned visuals. Pencil additions are not treated as authoritative text. Continuation 3.101 d–f has no repeated printed example number; this source fact is recorded rather than generating a number. Realization title and composer/work attributions are retained. Prose footnotes under 3.108 remain in the verified text; score asterisk markers remain in the image.',
        '',
        '## Per-slot image hand-off',
        '',
        '| Slot | Printed page | PDF page | Image | Review | Extraction note |',
        '| --- | ---: | ---: | --- | --- | --- |',
    ]
    for rec, (slot, _) in zip(records, slots):
        report.append(f"| {slot} | {rec['printed_page']} | {rec['pdf_page']} | `{rec['image']}` | pending_independent_review | {rec['review_note']} |")
    preserve_write(Path('review-candidates/book/M06/extraction-207-223.md'),
        ('\n'.join(report) + '\n').encode())
    print(f'Wrote {len(records)} crops and 52-slot manifest. No independent review claimed.')


if __name__ == '__main__':
    main()

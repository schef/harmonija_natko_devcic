"""Individual source-only rectangles; existing partial plan stays untouched.

View coordinates were chosen on separate page views at height 2000.
Conversion to source-local coordinates never resamples the saved image.
"""
import json
import re
import sys
from pathlib import Path
from PIL import Image

BASE = Path('review-candidates/book/M04')
OUT = Path('images/02-dijatonika-c')
ADDITIONS = [
    [149,339,[360,366,1166,713]],
    [149,340,[290,765,1231,1108]],
    [149,341,[315,1480,1169,1818]],
    [150,342,[300,116,1147,468]],
    [150,343,[144,889,744,1210]],
    [150,344,[756,887,1310,1214]],
    [150,345,[280,1225,1127,1551]],
    [150,346,[310,1554,1066,1860]],
    [151,347,[383,104,1140,399],'','cleanup_required: lower analysis interleaves following example 2.348 title; source pixels preserved.'],
    [151,348,[343,382,1190,674],'','cleanup_required: preceding example 2.347 lower analysis interleaves title; source pixels preserved.'],
    [151,349,[378,674,1133,974]],
    [151,350,[339,982,1184,1285]],
    [151,351,[339,1559,1140,1901]],
    [152,352,[165,88,1204,447]],
    [152,353,[225,640,1129,975]],
    [152,354,[185,987,1179,1332]],
    [153,355,[148,80,702,396]],
    [153,356,[713,86,1334,406]],
    [153,357,[147,406,727,719]],
    [153,358,[739,407,1335,717]],
    [153,359,[146,725,771,1038]],
    [153,360,[781,719,1335,1037]],
    [153,361,[146,1038,810,1366]],
    [153,362,[812,1041,1335,1355]],
    [153,363,[294,1366,1153,1679]],
    [154,364,[324,352,1157,683]],
    [154,365,[323,690,1156,1013]],
    [154,366,[320,1017,1155,1335]],
    [154,367,[315,1340,1153,1673]],
    [155,368,[195,484,1352,840]],
    [155,369,[194,924,823,1258]],
    [155,370,[829,907,1352,1265]],
    [155,371,[190,1502,823,1834]],
    [155,372,[829,1485,1349,1827]],
]


def main():
    mapping = {p['printed_page']: p for p in json.loads(
        Path('sources/index.json').read_text())['pages'] if p['printed_page'] is not None}
    original = json.loads((BASE / 'crop-plan.json').read_text())
    plan = [r for r in original if 137 <= r[0] <= 148] + ADDITIONS
    # Individually inspected corrections to inherited rectangles, not padding.
    # The lowest stem and first analysis line share a horizontal scan row:
    # keep that whole line with the score, remaining analysis separately.
    for row in plan:
        if row[1] == 325 and row[3] == '-score':
            row[2][3] = 1844
            row[4] += ' First analysis line retained with score so lowest bass stem is complete.'
        if row[1] == 325 and row[3] == '-analysis':
            row[2][1] = 1844
            row[4] = 'Remaining lower analysis; first analysis line is in -score. No repeated number in this source part; pair with -score. Separate rectangle excludes running footer.'
        if row[1] == 321:
            row.extend(['', 'cleanup_required: faint handwritten marks alongside the lower analysis cannot be excluded by a rectangular crop while retaining the complete example; source pixels preserved.'])
    slots = re.findall(r'<!-- visual: primjer 2\.(\d+).*?; page (\d+) -->',
                       (BASE / 'text-137-155.md').read_text())
    assert len(slots) == 72
    assert {(int(n), int(p)) for n, p in slots} == {(r[1], r[0]) for r in plan}
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for p, num, view_rect, *extra in plan:
        suffix = extra[0] if extra else ''
        note = extra[1] if len(extra) > 1 else ''
        note = note.replace('cleanup-required:', 'cleanup_required:')
        source = mapping[p]['image']
        with Image.open(source) as im:
            rect = [round(v * im.height / 2000) for v in view_rect]
            assert 0 <= rect[0] < rect[2] <= im.width
            assert 0 <= rect[1] < rect[3] <= im.height
            name = f'primjer-2-{num}{suffix}'
            target = OUT / f'{name}.png'
            crop = im.crop(rect)
            if target.exists():
                with Image.open(target) as old:
                    same = old.size == crop.size and old.tobytes() == crop.tobytes()
                if not same:
                    assert '--recrop-own-generated' in sys.argv and num == 325, f'Existing different crop: {target}'
                    crop.save(target)
            else:
                crop.save(target)
        caption = f'Primjer 2.{num} — tiskana str. {p}' + (f' ({suffix[1:]})' if suffix else '') + '.'
        records.append(dict(id=name, example=f'2.{num}', kind='example',
                            printed_page=p, pdf_page=mapping[p]['pdf_page'],
                            source_image=source, rect=rect, image=str(target),
                            review_status='pending_independent_review',
                            review_note=note or 'Source-only candidate; independent four-edge/source review required.',
                            caption=caption))
    (BASE / 'images-137-155.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    report = [
        '# Extraction hand-off: printed pages 137–155',
        '',
        '- Assignment: 19 printed pages, 137–155; PDF pages 69–78, read from `sources/index.json`.',
        '- All 19 original source PNGs were opened visually. Individual four-edge bounds were checked with native-resolution edge strips; this is extractor quality control, not independent approval.',
        '- Exactly 72 verified text slots map to 73 source-only PNG rectangles, covering examples 2.302–2.372 (71 distinct numbers). Example 2.305 occupies two cross-page slots (a–b on 139, c on 140), without stitching. Example 2.325 occupies one slot with two separate parts to exclude the running footer and retain its complete lowest stem.',
        '- Every crop remains `pending_independent_review`; no pass/self-approval is asserted.',
        '- Source pixels only: no retouching, border generation, padding, deskewing, stitching, or resampling of outputs. Rectangles are source-local `[left, top, right, bottom)` pixels.',
        '- Created: `review-candidates/book/M04/extract-137-155.py`, `review-candidates/book/M04/images-137-155.json`, this report, and the 73 images listed below in `images/02-dijatonika-c/`.',
        '- Preserved untouched: existing `crop-plan.json`, `crop.py`, verified text, chapter files, shared manifests, milestone tracker, and all other assigned ranges.',
        '- Readiness: ready for independent visual review; NOT ready for final integration. Flagged layout/handwriting cases require reviewer disposition. No unreadable example was omitted. Continuation 2.305 c and the second part of 2.325 have no repeated source number; none was fabricated.',
        '',
        '## Flagged source-layout / handwriting cases',
        '',
    ]
    report += [f"- **{r['id']}**, printed {r['printed_page']}: {r['review_note']}" for r in records if 'cleanup_required:' in r['review_note']]
    report += ['', '## Slot-by-slot mapping and pending review', '',
               'All paths below are repository-root-relative, matching the JSON manifest. Each image group belongs to one original verified-text slot.', '']
    for i, (n, p) in enumerate(slots, 1):
        group = [r for r in records if r['example'] == f'2.{n}' and r['printed_page'] == int(p)]
        report += [f'### Slot {i:02}: primjer 2.{n}, tiskana str. {p}', '']
        for r in group:
            report += [f"![{r['caption']}]({r['image']})", '', r['caption'], '',
                       f"- Source: `{r['source_image']}`, PDF page {r['pdf_page']}, local rectangle `{r['rect']}`.",
                       f"- Image review: **pending_independent_review**. {r['review_note']}", '']
        report += ['<!-- MuseScore: pending -->', '']
    (BASE / 'extraction-137-155.md').write_text('\n'.join(report) + '\n')
    print(f'{len(slots)} slots mapped to {len(records)} source-only rectangles; all pending independent review.')


if __name__ == '__main__':
    main()

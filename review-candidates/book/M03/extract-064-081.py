"""Extract 68 individually inspected visual slots, without modifying source pixels.

The previous extract.py is read as data (never imported/executed). Its 62
individually specified rectangles are retained except for the explicit changes
below. Rectangles there and here use the 2000-high inspection view; the manifest
records the actual, unresized source-pixel rectangles (Pillow exclusive edges).
Different pre-existing output pixels are preserved in snapshots-064-081/.
"""
import ast
import hashlib
import io
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT = ROOT / 'images/02-dijatonika-b'


def definitions():
    tree = ast.parse((HERE / 'extract.py').read_text())
    result = []
    for node in tree.body:
        if not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and getattr(node.value.func, 'id', '') == 'crop'):
            continue
        args = [ast.literal_eval(v) for v in node.value.args]
        kw = {v.arg: ast.literal_eval(v.value) for v in node.value.keywords}
        page, label, box = args[:3]
        note = args[3] if len(args) > 3 else ''
        kind = args[4] if len(args) > 4 else kw.get('kind', 'example')
        if (page, label) == (68, '1'):
            # Two separate inline formulae, excluding surrounding instruction
            # and the conjunction following the first formula.
            result.extend([
                (68, 'progresija-1', (560, 1644, 801, 1726), '', 'exercise'),
                (68, 'progresija-2', (276, 1728, 711, 1807), '', 'exercise'),
            ])
            continue
        if (page, label) == (74, '8-realizacija'):
            box = (122, 1466, 1318, 1843)
            kind, note = 'realization', 'Identifying title retained above the complete realization.'
        if (page, label) == (75, '13-realizacija'):
            box = (152, 84, 1348, 781)
            kind, note = 'realization', 'Identifying title and both systems retained.'
        result.append((page, label, box, note, kind))
    # Individually selected bounds on the final assigned page. Exercise 2 and
    # exercise 4 each occupy two systems and are not split into separate images.
    result.extend([
        (81, '167', (168, 329, 1334, 729), '', 'example'),
        (81, '1', (170, 940, 1328, 1075), '', 'exercise'),
        (81, '2', (163, 1081, 1328, 1438), '', 'exercise'),
        (81, '3', (168, 1451, 1328, 1559), '', 'exercise'),
        (81, '4', (162, 1578, 1328, 1840), '', 'exercise'),
    ])
    return result


def save_preserving(path, image):
    data = io.BytesIO()
    image.save(data, format='PNG')
    payload = data.getvalue()
    if path.exists():
        with Image.open(path) as old:
            same = old.mode == image.mode and old.size == image.size and old.tobytes() == image.tobytes()
        if same:
            return 'reused'
        previous = path.read_bytes()
        digest = hashlib.sha256(previous).hexdigest()[:12]
        snapshot = OUT / 'snapshots-064-081' / f'{path.stem}-{digest}.png'
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        if not snapshot.exists():
            snapshot.write_bytes(previous)
    path.write_bytes(payload)
    return 'created_or_updated'


def main():
    slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->',
                       (HERE / 'text-064-081.md').read_text())
    specs = definitions()
    assert len(specs) == len(slots) == 68
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for (page, label, box, note, kind), (identity, slotpage) in zip(specs, slots):
        assert page == int(slotpage), (page, identity, slotpage)
        if kind == 'example':
            assert identity.startswith('2.' + label.split('-')[0]), (identity, label)
        elif kind == 'realization':
            assert identity == f'Realizacija zadatka {label.split("-")[0]}.'
        elif label.isdigit():
            assert identity == f'ZADACI {label}'
        source = f'sources/pages/page-{page:03}.png'
        with Image.open(ROOT / source) as image:
            scale = image.height / 2000
            rect = [round(v * scale) for v in box]
            assert 0 <= rect[0] < rect[2] <= image.width
            assert 0 <= rect[1] < rect[3] <= image.height
            stem = (f'primjer-2-{label}' if kind == 'example'
                    else f'zadatak-2-{page}-{label}')
            target = f'images/02-dijatonika-b/{stem}.png'
            save_preserving(ROOT / target, image.crop(rect))
        if 'pencil' in note.lower() or 'handwrit' in note.lower():
            note = 'cleanup_required: original source handwriting/layout retained without retouching. ' + note
        if page == 67 and label == '142':
            note = 'cleanup_required: faint source handwriting above the staff; no pixel alteration.'
        if (page, label) in [(71, '149'), (72, '152')]:
            note = 'cleanup_required: original faint handwritten analysis near the lower edge; printed notation intact.'
        caption = (f'Primjer {identity}. Tiskana str. {page}.' if kind == 'example'
                   else f'{identity} Tiskana str. {page}.')
        rows.append(dict(id=stem, example=identity, kind=kind,
                         printed_page=page, pdf_page=page // 2 + 1,
                         source_image=source, rect=rect, image=target,
                         review_status='pending_independent_review',
                         review_note=note or 'Source-only crop; independent visual review required.',
                         caption=caption))
    assert len({r['id'] for r in rows}) == 68
    (HERE / 'images-064-081.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    report = [
        '# M03 extraction hand-off: printed 64–81 / PDF 33–41', '',
        '- Extraction only; all 18 source PNGs visually inspected. No chapter text or global manifests changed.',
        '- Extractor inspected native-resolution strips of all four edges of all 68 output crops, in addition to the source-page inspection. This is extraction QA only, not the mandatory independent review.',
        '- 68 source-only crops match the 68 visual slots in `review-candidates/book/M03/text-064-081.md`, in source order. No count discrepancy.',
        '- The old 62 definitions become 68: split the combined page-68 progression into two (+1), and add example 2.167 plus four page-81 exercises (+5).',
        '- Retained identifying titles in the realizations on pages 74 and 75. Cross-page examples remain separate page-specific parts; exercises 13 (p.73), 2 and 4 (p.81), and realization 13 retain both systems in one crop.',
        '- `rect` is `[left, top, right, bottom]` in the original source PNG pixels, with right/bottom exclusive. No resizing, painting, generated borders, or other retouching was applied to output crops.',
        '- Prior `extract.py` and any prior manifests are unchanged. Identical existing pixels are reused; differing prior images are snapshotted inside `images/02-dijatonika-b/snapshots-064-081/` before replacement.',
        '- Every crop is **pending_independent_review**; this extractor has not approved any image. Parent must inspect all four edges against the source and give pass/recrop decisions.',
        '- Source handwriting frequently overlaps labels, notes, and analysis, or obstructs clean whitespace. `cleanup_required` notes identify these original-pixel limitations; they are not passes. No printed music was deliberately omitted to hide handwriting.',
        '- Continuation crops 2.140.c, 2.143.c, 2.151.e–g, and 2.154.f–g have their example number only on the preceding source page; no number has been synthesized.',
        '- No unreadable printed example was omitted. Handwritten additions are not authoritative notation; independent review may require a cleaner source for affected images.',
        '- Ready for independent image review, **not ready for final integration approval**.', '',
        '## Files', '',
        '- `review-candidates/book/M03/images-064-081.json`',
        '- `review-candidates/book/M03/extraction-064-081.md`',
        '- `review-candidates/book/M03/extract-064-081.py`',
        '- The 68 PNG paths listed below in `images/02-dijatonika-b/`.', '',
        '## Per-image hand-off', '',
        '| Source identity | Printed / PDF page | Image | Review / limitation |',
        '| --- | --- | --- | --- |',
    ]
    for r in rows:
        report.append(f"| {r['example']} | {r['printed_page']} / {r['pdf_page']} | `{r['image']}` | pending_independent_review — {r['review_note']} |")
    (HERE / 'extraction-064-081.md').write_text('\n'.join(report) + '\n')
    print(f'Created manifest and hand-off for {len(rows)} crops across {len(set(r["printed_page"] for r in rows))} printed pages.')


if __name__ == '__main__':
    main()

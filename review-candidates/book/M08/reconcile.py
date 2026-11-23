"""M08 source-only additions and slot reconciliation; raw inputs are read-only."""
import copy
import json
import re
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'review-candidates/book/M08'

# Individually selected from the source pages, not fixed-margin expansions.
RECROPS = {
    '4.13': [512, 2021, 1461, 2400],
    '4.z289-9-realizacija': [197, 1925, 1748, 2381],
    '4.z294-5-realizacija': [150, 780, 1705, 1799],
    '4.z297-3-realizacija': [195, 965, 1745, 2354],
    '4.z303-3-realizacija': [190, 1880, 1740, 2341],
    '4.z308-3-realizacija': [145, 110, 1709, 2355],
    '4.z303-3': [217, 543, 1738, 699],
    '4.z306-1': [192, 1473, 1718, 1913],
    '4.z306-2': [192, 1913, 1719, 2366],
}


def main():
    raw = json.loads((BASE / 'images.json').read_text())
    assert len(raw) == 103
    records = copy.deepcopy(raw)
    for r in records:
        if r['id'] in RECROPS:
            r['original_image'] = r['image']
            r['original_rect'] = r['rect']
            r['rect'] = RECROPS[r['id']]
            title = r['kind'] == 'realization'
            r['image'] = r['image'].replace('.png', '-naslov-recrop.png' if title else '-coverage-recrop.png')
            reason = ('restores the printed realization title' if title else {
                '4.13': 'restores the complete lowest bass stem and genuine lower whitespace',
                '4.z303-3': 'restores the upper slur; unavoidable preceding figured-bass fragments remain flagged cleanup_required',
                '4.z306-1': 'excludes the top of exercise 2 while retaining all final figures of exercise 1',
                '4.z306-2': 'restores the top note and a small genuine upper gap below exercise 1',
            }[r['id']])
            r['review_note'] += f' Separate recrop {reason}; original image and rectangle retained unchanged.'
            Image.open(ROOT / r['source_image']).crop(r['rect']).save(ROOT / r['image'])
        r['cleanup_required'] = 'cleanup-required' in r['review_note']
        if r['id'] in ('4.z303-2-cont', '4.z303-3'):
            r['cleanup_required'] = True
            r['review_note'] += ' cleanup_required: on page 303 the lowest figures of exercise 2 and the upper slur of exercise 3 occupy overlapping vertical ranges. Rectangular source-only isolation cannot provide a clean horizontal separation without losing notation; preserve source layout for independent decision, no retouching.'
        if r['id'] in ('4.z290-9-realizacija-cont', '4.31'):
            r['source_condition_note'] = 'Visible loss/white abrasion in original scan intersects notation (page 290: lower staff of first system near second measure; page 295: upper staff in variant c). Preserved exactly; independent notation interpretation needed, not a crop defect and not repaired.'
            r['review_note'] += ' ' + r['source_condition_note']
    records += json.loads((BASE / 'inline-progression.json').read_text())
    symbol = {
        'id': 'sifra-appoggiature-304',
        'example': 'Nenumerirana šifra trostruke appoggiature',
        'kind': 'diagram', 'printed_page': 304, 'pdf_page': 153,
        'source_image': 'sources/pages/page-304.png',
        'rect': [1278, 958, 1373, 1048],
        'image': 'images/04-neakordicki-a/sifra-appoggiature-304.png',
        'review_status': 'pending_independent_review',
        'review_note': 'Separate inline figured symbol in footnote **: stacked 9/7/4 resolving to 8/3. No printed example ID; descriptive manifest ID only. Source-only rectangular crop, independently selected four edges.',
        'caption': 'Nenumerirana šifra trostruke appoggiature (9/7/4 > 8/3) u bilješci ** uz realizaciju zadatka 3 iz odsjeka 4.1.6. Tiskana str. 304.',
        'cleanup_required': False,
    }
    Image.open(ROOT / symbol['source_image']).crop(symbol['rect']).save(ROOT / symbol['image'])
    records.append(symbol)
    records.sort(key=lambda r: (r['printed_page'], r['rect'][1]))
    slots = []
    for name in ('text-277-292.md', 'text-293-308.md'):
        text = (BASE / name).read_text()
        found = list(re.finditer(r'<!-- visual: (.*?); page (\d+) -->', text))
        assert len(found) == (49 if name == 'text-277-292.md' else 56)
        slots.extend((name, m.group(1), int(m.group(2)), text[:m.start()].count('\n') + 1) for m in found)
    assert len(slots) == len(records) == 105
    for index, (r, slot) in enumerate(zip(records, slots), 1):
        name, label, page, line = slot
        assert page == r['printed_page'], (r['id'], slot)
        r['slot_index'] = index
        r['slot_label'] = label
        r['slot_source'] = f'review-candidates/book/M08/{name}'
        r['slot_line'] = line
        r['review_status'] = 'pending_independent_review'
        r.setdefault('cleanup_required', False)
        r['musescore_hint'] = ('Unnumbered graphic: recreate only this inline progression/figured symbol; do not assign a printed example number.' if r['kind'] == 'diagram' else 'MuseScore transcription pending; retain all printed variants, analysis and continuation relationships.')
        src = Image.open(ROOT / r['source_image']).crop(r['rect']).convert('RGB')
        dst = Image.open(ROOT / r['image']).convert('RGB')
        assert src.size == dst.size and ImageChops.difference(src, dst).getbbox() is None, r['id']
        assert r['pdf_page'] == (r['printed_page'] // 2 + 1)
    # Verify originals as well, including superseded title-less crops.
    for r in raw:
        src = Image.open(ROOT / r['source_image']).crop(r['rect']).convert('RGB')
        dst = Image.open(ROOT / r['image']).convert('RGB')
        assert src.size == dst.size and ImageChops.difference(src, dst).getbbox() is None
    (BASE / 'images-complete.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(records)} slots; {len(RECROPS)} separate recrops; all 103 originals and 105 candidates pixel-exact.')
    print('cleanup_required:', [r['id'] for r in records if r['cleanup_required']])


if __name__ == '__main__':
    main()

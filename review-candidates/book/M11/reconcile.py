"""M11 bounded extraction reconciliation. Never overwrite raw candidates or text."""
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'review-candidates/book/M11'

# Original-source pixels; individually chosen, not padded or resampled.
RECROPS = {
    'slika-386-1': (1047, 1038, 1148, 1089),
    'slika-386-2': (1064, 1122, 1086, 1178),
    'slika-386-3': (1007, 1199, 1094, 1245),
    'slika-386-4': (485, 1681, 506, 1732),
    'slika-386-5': (858, 1725, 879, 1778),
    'slika-387-13': (1438, 995, 1484, 1060),
    'slika-387-14': (652, 1146, 689, 1189),
}
BLOCKERS = {
    'primjer-5-9': 'Source-layout cleanup required: exercise 10 title Andantino overlaps the vertical range of the final lower slur of exercise 9. Existing rectangle retains partial foreign title. Do not clip the slur.',
    'primjer-5-10-part-1': 'Source-layout cleanup required: Andantino belongs here, but neighboring exercise 9 lower slur intrudes at upper right. A single full-width rectangle cannot exclude it while retaining this title.',
    'primjer-5-11': 'Source-layout cleanup required: low ending reduction of exercise 11 extends below the adjacent Risoluto title of exercise 12. Existing rectangle contains that unrelated title; do not clip reduction.',
    'primjer-5-12': 'Source-layout cleanup required: Risoluto belongs here, but exercise 11 lower reduction intrudes at upper right. Do not remove the title to hide this conflict.',
    'slika-386-1': 'Source-layout cleanup required: removed upper-right preceding-line ink, but full sharp descends to y=1088 while next prose under the 4 begins at y=1087. Single rectangle still retains tiny lower-right foreign ink. A separately embedded sharp and 4 may resolve this; no stitching authorized.',
    'slika-386-2': 'Source-layout cleanup required: full slashed 4 extends through y=1175; old crop clipped its lower tip. Parenthesis begins at x=1084 while glyph extends through x=1084, so the new rectangle preserves glyph but retains parenthesis fragments. Do not clip slash or paint out punctuation.',
    'slika-386-5': 'Uncertified source separation: restored lower slash beyond old bottom y=1772. Neighboring prose above and tiny ink below slash leave essentially no margin; independent reviewer must distinguish slash tip from next-line ink. Cleanup required if foreign ink remains.',
    'slika-387-14': 'Source-layout cleanup required: complete overbar of 5 extends to x=686, but sentence period occupies x=680..685 at y=1178..1185. A rectangle retaining full figure also contains period already transcribed in text. Do not clip overbar or lower 5 to remove period.',
}


def main():
    raw_path = OUT / 'images.json'
    before = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    records = json.loads(raw_path.read_text())
    text = (OUT / 'text-379-387.md').read_text()
    assert len(records) == text.count('<!-- visual:') == 44
    report = [
        '# M11 extraction / coverage hand-off',
        '',
        '- Assigned: printed 379–411; PDF 190–206 (1-based). Visuals: printed 379–387, PDF 190–194 only.',
        '- Exact mapping: 44 records in verified-text slot order: 19 exercise/realization parts, 25 inline notation glyphs. No extra page-image slots.',
        '- Opened every source PNG 379–387. Inspected all 44 old crops on four native-resolution edge strips / native glyph contact sheets against source pages; realization 384 additionally opened in full. This is extractor inspection, NOT independent approval.',
        '- Every image remains pending_independent_review. Explicit blockers below are NOT acceptable clean crops and must not be integrated as approved images.',
        '- Original images.json and all 44 original PNGs preserved. Seven separate -recrop-m11.png candidates made only by source cropping; no paint, border, stitch, resize, or retouch.',
        '- The original p.384 and p.385 crops ALREADY retain the full printed titles “Realizacija zadatka 4.” and “Realizacija zadatka 9.”; no replacement needed.',
        '- Exercise 10 crosses 381/382 and exercise 13 crosses 382/383. Number appears only in first part as printed; do not invent a repeated number.',
        '- Coverage 388–411: checked all remaining verified-text shards for source-page markers, structure and visual slots. They contain blank pages, structured multilingual terminology, subject/name indexes and contents; zero visual slots. No page-image crops were added and no text changed.',
        '- Coordinates below are [left, top, right, bottom], source PNG pixels, right/bottom exclusive. Paths are repository-root-relative.',
        '',
    ]
    for page in range(379, 388):
        report += [f'## Printed page {page}', '']
        for row in [r for r in records if r['printed_page'] == page]:
            stem = Path(row['image']).stem
            row['original_image'] = row['image']
            row['original_rect'] = row['rect'].copy()
            row['slot_index'] = records.index(row) + 1
            row['review_status'] = 'pending_independent_review'
            row['source_damage'] = None
            if stem in RECROPS:
                row['rect'] = list(RECROPS[stem])
                row['image'] = str(Path(row['image']).with_name(stem + '-recrop-m11.png'))
                dest = ROOT / row['image']
                assert not dest.exists(), f'Will not overwrite {dest}'
                with Image.open(ROOT / row['source_image']) as source:
                    source.crop(row['rect']).save(dest)
            row['review_note'] = 'Extractor inspected source and all four old-crop edges; independent review required. '
            if stem in BLOCKERS:
                row['source_damage'] = BLOCKERS[stem]
                row['review_note'] += BLOCKERS[stem]
            elif 'part-2' in stem:
                row['review_note'] += 'Continuation has no repeated printed number; source is complete as printed.'
            else:
                row['review_note'] += 'No known source-layout blocker; not self-approved.'
            if stem == 'slika-386-3':
                row['review_note'] += ' Removed surrounding parentheses and lower-line prose; retains all four slash strokes.'
            if stem == 'slika-386-4':
                row['review_note'] += ' Removed both surrounding parentheses; near-zero lateral whitespace is source-imposed.'
            if stem == 'slika-387-13':
                row['review_note'] += ' Excludes sentence period at right; retains full two-level resolution figure.'
            report += [
                f"- **{row['slot_index']}. {row['id']}** — {row['caption']} PDF {row['pdf_page']}; source `{row['source_image']}`; rect `{row['rect']}`; image `{row['image']}`.",
                f"  - Original: `{row['original_image']}`; rect `{row['original_rect']}`.",
                f"  - Review: **pending_independent_review**. {row['review_note']}",
            ]
        report.append('')
    report += [
        '## Integration readiness',
        '',
        'NOT ready for final integration. Independent visual review is still required for all 44 records. Eight records carry explicit source-layout/separation blockers, including old crops retained as evidence; resolve those by an independently reviewed multipart representation or another authorized source-only solution. No missing/unreadable musical identity was invented. No chapter, verified text, global tracker, raw manifest or original PNG was edited. No commit/push.',
        '',
    ]
    (OUT / 'images-complete.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    (OUT / 'extraction-complete.md').write_text('\n'.join(report))
    assert hashlib.sha256(raw_path.read_bytes()).hexdigest() == before
    for row in records:
        with Image.open(ROOT / row['source_image']) as source, Image.open(ROOT / row['image']) as crop:
            assert source.crop(row['rect']).tobytes() == crop.tobytes(), row['id']
    print('44 exact slots; 7 separate recrops; 8 explicit blockers; raw manifest unchanged; all crop pixels match source.')


if __name__ == '__main__':
    main()

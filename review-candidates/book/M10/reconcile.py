"""M10 extraction hand-off; never rewrites the original crops or images.json.

Run from the repository root. Rectangles are local, original PNG pixels,
not spread coordinates. Only four individually chosen replacements are made.
The extractor's observations are NOT independent crop approvals.
"""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from PIL import Image

HERE = Path('review-candidates/book/M10')
RAW = HERE / 'images.json'
OUT = Path('images/04-neakordicki-c')

# Each changed edge was selected separately against its source page.
# Values here use the source-view frame only to specify the selected edge;
# the delivered manifest records the resulting integer local pixel rectangle.
TOP_EDGES = {
    'zadatak-4-359-9-realizacija': (90, 'Restore the complete printed Realizacija zadatka 9. title; keep all three systems and lowest figures.'),
    'zadatak-4-360-12-realizacija': (98, 'Restore the complete printed Realizacija zadatka 12. title; keep all four systems and lowest stem.'),
    'zadatak-4-374-1-realizacija-a': (1460, 'Restore the complete printed Realizacija zadatka 1. title; keep the opening system, tied bass and source margin.'),
    'primjer-4-192': (999, 'Restore the very top of the Beethoven attribution, clipped by the old top edge. The preceding prose descenders overlap its vertical range: cleanup_required/layout_conflict, no masking or retouch.'),
}

DETAILS = {
    143: 'Variants a/b/c, stars and bass figures 4–3 and 7–6.',
    144: 'Variants a/b and all lower stems.',
    145: 'Variants a/b, connecting lines and figures 4–3 / 7–6; page number excluded.',
    146: 'Variants a/b and both NE labels.',
    147: 'Variants a/b; right edge stops before the neighbouring 4.148 number.',
    148: 'Variants a/b including raised accidentals; left edge excludes 4.147.',
    149: 'Variants a/b/c, DA/DA/NE, brackets and bottom *) marker; explanation separately transcribed.',
    150: 'Variants a/b and both complete stacked figured-bass groups, including parentheses.',
    151: 'Star above the beamed soprano and complete final barline.',
    152: 'First part a–c on351; continuation d–g on352, including *) marker. Printed number only on351; explanation separately transcribed.',
    153: 'All five variants a–e, including cross-staff diagonal in d.',
    154: 'All three variants a–c, accidentals and connecting lines.',
    155: 'Complete two-line Beethoven concerto attribution, fermata/star, tuplets and lower slur.',
    156: 'Complete Chopin op.59 no.1 attribution, long upper/lower slurs, lowest beam and staccato dots; open right endpoint is printed.',
    157: 'Chopin op.7 no.1 attribution and *) marker; separate prose footnote excluded.',
    158: 'Schumann op.21 no.6 attribution, both excerpts and i dalje: label, single/double-star markers and bottom slur; prose explanations excluded.',
    159: 'Chopin op.50 no.1 attribution, *) marker and complete low stems/slurs; explanation excluded.',
    160: 'Variant a spans both left-hand systems; b/c occupy lower right. All belong to this single numbered slot.',
    161: 'All overlapping upper/lower slurs and final low bass stem; attribution is in the surrounding verified prose, not printed as a separate score title.',
    162: 'Both fermatas, accidentals, bottom bass stem and complete final barline; Janacek attribution is in preceding prose on354.',
    163: 'All three stars, bass appoggiatura and final barline.',
    164: 'All variants a–d, stars and very lowest bass beam in c.',
    165: 'Complete Beethoven G-major op.49 no.2 attribution, both stars, low bass beams and printed open right endpoints.',
    166: 'Both stars and lower stems; no separate work attribution printed.',
    167: 'Complete Beethoven A-major op.2 no.2 attribution, *) marker, lowest bass beams/dots; explanation separately transcribed.',
    168: 'Star above soprano, lower flag and final barline.',
    169: 'Complete Beethoven c-minor op.111 attribution, all three *) markers and lowest bass beams. Related explanatory footnote touches the lowest-beam height: unavoidable partial footnote ink retained; cleanup_required/layout_conflict, no retouch.',
    170: 'Variants a/b, stars, all accidentals and lowest bass stem.',
    171: 'Complete Chopin Prelude op.28 no.2 attribution, star, arpeggiation, bottom fermata and very low bass note; narrow right margin is constrained by adjacent 4.172.',
    172: 'Complete Chopin Mazurka op.24 no.2 attribution, star and bass stems; left edge is the natural separation from 4.171.',
    173: 'Complete Schumann Carnaval op.9 attribution, stars, high ledger notes and lowest bass note. Source abrasion interrupts the right final barline; source_damage retained, not repaired.',
    174: 'Complete Chopin Prelude op.28 no.12 attribution, highest slur and lowest bass notes/staccato dots.',
    175: 'Complete Chopin Mazurka op.24 no.4 attribution, both single-star and double-star markers, lower staccato dot; explanations separately transcribed.',
    176: 'Complete J.S.Bach Koral br.8 attribution, fermatas above and below; narrow right separation from 4.177.',
    177: 'Separate unattributed numbered example; all accidentals and final barline.',
    178: 'First system and Chopin op.28 no.8 attribution on366; next two systems on367. Number only on366. Handwritten circles around bass notes preserved: cleanup_required/handwriting, no erasure.',
    179: 'Complete Bach b-minor Prelude / Wohltemperiertes Klavier I dio attribution and printed open right endpoints.',
    180: 'Complete Chopin Mazurka op.67 no.3 attribution, ornament, low bass stems and final barline; following prose excluded.',
    181: 'Complete Grieg Lirski komadi X,60 attribution and both grand-staff systems including low ledger notes.',
    182: 'Chopin Balada op.38 title and first system on368; one continuation system on369. Number/title occur only on368. Preserve long lower slurs and printed open endpoints.',
    183: 'Complete Chopin Mazurka op.17 no.4 attribution, ornaments, lower flags and final barline.',
    184: 'Complete Beethoven Sonata op.111 attribution, lowest left bass note, lowest right beam/slur and printed open endpoints; printer signature excluded.',
    185: 'Complete Schumann Albumblatter op.124,13 attribution and *) marker, lowest slur; explanation separately transcribed.',
    186: 'Complete R.Strauss Don Quichotte attribution and both three-staff systems, including lowest bass note and slurs.',
    187: 'Complete Schumann Papillons op.2 attribution and very lowest bass ledger notes.',
    188: 'Complete Beethoven f-minor op.57 attribution, dashed arrows, very low bass notes and lower/right slurs.',
    189: 'Complete Beethoven D-major op.10 no.3 attribution and both systems including lowest beam/accidental; printed open endpoints retained.',
    190: 'Complete Beethoven A-major op.2 no.2 attribution and both systems, star, low arpeggiations and bass stems; no separate explanation printed here.',
    191: 'Complete Beethoven Es-major op.81a attribution, both clef changes, lowest bass ledger note and bottom slur; following prose excluded.',
    192: 'Complete Beethoven Symphony9 attribution, trill, three staves, lowest bass ledger notes and long lower slurs. Prose descenders overlap attribution height; following Ravel attribution touches lowest-slur height. cleanup_required/layout_conflict; no clean rectangular separation at both edges, no clipping to conceal conflict.',
    193: 'Complete Ravel Rapsodie espagnole attribution, printed number, highest slurs and lowest bass ledger notes. Top includes unavoidable preceding 4.192 slur fragments: cleanup_required/layout_conflict. Open right endpoints are the actual end of this excerpt, not a lost final barline. Parent has checked379: chapter5 begins there, with no4.193 continuation;379 was not opened by this worker.',
}

EXERCISES = {
    355: ['One complete soprano row.', 'One complete soprano row.', 'One complete soprano row, including low accidentals.'],
    356: ['Three bass rows with every stacked figure and final barline.', 'Three bass rows with all star markers and final barline.', 'One soprano row including lowest slur.', 'One soprano row including lowest note.', 'First soprano row of8; printed number here, continuation on357.'],
    357: ['Continuation of8, one soprano row; no repeated number; final barline.', 'Four bass rows with all figures, accidentals and parentheses.', 'Three bass rows with all stacked figures and parentheses.', 'Opening bass row of11 with all figures; number here, continuation on358.'],
    358: ['Two bass rows finishing11, all stacked figures and final barline; no repeated number.', 'Three soprano rows with all accidentals and long slurs.', 'Two soprano rows, very low note, fermata and final barline.', 'Two soprano rows with all accidentals, lower notes and final barline.'],
    359: ['Realization of9; complete printed title and three grand-staff systems, including lowest figures.'],
    360: ['Realization of12; complete printed title and four grand-staff systems, including lowest bass stem.'],
    364: ['Two bass rows, printed1 and final barline.', 'First bass row of2; printed number here, continuation on365.'],
    365: ['Final bass row of2; no repeated number.', 'Two soprano rows and all slurs.', 'Two soprano rows, lower slur and final barline.'],
    371: ['Three complete grand-staff systems, printed1 and lowest ties.', 'Complete Allegro, ma non troppo instruction; two opening grand-staff systems of2. Number only here, continuation on372.'],
    372: ['Two grand-staff systems finishing2, no repeated number; lowest ties and final barline.', 'Three grand-staff systems of3; number, lowest ties and final barline.'],
    373: ['Complete Andantino grazioso instruction and four grand-staff systems of4, lowest bass ties and final barline.', 'Opening grand-staff system of5; printed number here, continuation on374.'],
    374: ['Four grand-staff systems finishing5; no repeated number, lowest ties and final barline.', 'Realization of1; complete printed title and first grand-staff system, continuation on375.'],
    375: ['Three grand-staff systems finishing realization1; no repeated title/number, lowest ties and final barline.'],
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    rows = json.loads(RAW.read_text())
    assert len(rows) == 86
    originals = {str(RAW): digest(RAW)}
    originals.update({r['image']: digest(r['image']) for r in rows})
    index = {p['printed_page']: p for p in json.loads(Path('sources/index.json').read_text())['pages'] if isinstance(p['printed_page'], int)}
    reviews = {}
    shards = {}
    for path in sorted(HERE.glob('text-*-review.json')):
        data = json.loads(path.read_text())
        text = path.with_name(path.name.replace('-review.json', '.md'))
        slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->', text.read_text())
        assert len(slots) == sum(len(p['visuals']) for p in data)
        for p in data:
            reviews[p['printed_page']] = p['visuals']
            shards[p['printed_page']] = str(text)
    assert sum(map(len, reviews.values())) == 86
    page_offsets = Counter()
    exercise_offsets = Counter()
    replacements = []
    for row in rows:
        p = row['printed_page']
        assert 349 <= p <= 378
        source = index[p]
        assert row['source_image'] == source['image']
        assert row['pdf_page'] == source['pdf_page']
        row['slot_label'] = reviews[p][page_offsets[p]]
        row['slot_markdown'] = shards[p]
        page_offsets[p] += 1
        old_image, old_rect = row['image'], list(row['rect'])
        if row['id'] in TOP_EDGES:
            edge, reason = TOP_EDGES[row['id']]
            im = Image.open(row['source_image'])
            row['rect'][1] = round(edge * im.height / 2000)
            row['image'] = str(OUT / (row['id'] + '-coverage-recrop.png'))
            assert row['image'] not in originals
            im.crop(row['rect']).save(row['image'])
            row['original_image'] = old_image
            row['original_rect'] = old_rect
            row['recrop_reason'] = reason
            replacements.append(row)
        if row['kind'] == 'example':
            number = int(row['example'].split('.')[1])
            detail = DETAILS[number]
        else:
            detail = EXERCISES[p][exercise_offsets[p]]
            exercise_offsets[p] += 1
        row['review_status'] = 'pending_independent_review'
        row['review_note'] = ('Extractor coverage reconciliation only: source page opened; printed identity, attribution/tempo where present, systems, variants, lowest notation and four native-resolution edges compared. ' + detail + ' Independent visual reviewer must decide pass/recrop required; this is not self-approval.')
        if 'realizacija' in row['slot_label']:
            row['caption'] = f"Realizacija zadatka {row['example']}. Izvor: str. {p}."
        row['cleanup_required'] = 'cleanup_required' in detail
        row['source_damage'] = 'source_damage' in detail
        row['source_endpoint_note'] = detail if row['kind'] == 'example' and row['example'] == '4.193' else ''
        im = Image.open(row['source_image'])
        crop = Image.open(row['image'])
        expected = im.crop(row['rect'])
        assert crop.mode == expected.mode and crop.size == expected.size
        assert crop.tobytes() == expected.tobytes(), row['image']
    assert page_offsets == Counter({p: len(v) for p, v in reviews.items()})
    assert len(set(r['id'] for r in rows)) == 86
    assert all(digest(p) == value for p, value in originals.items())
    (HERE / 'images-complete.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# M10 extraction / coverage hand-off', '',
        '- Assigned/opened: printed349–378, all30 source PNGs; PDF175–190 (1-based, checked against `sources/index.json`). No page outside this range opened.',
        '- Exact coverage: **86/86** positional slots =7+13+18+27+21 across the five verified Markdown shards and review JSONs. No new/missing slot or multipart-count difference.',
        '- Read all five text shards and all five review JSONs; verified text was not edited.',
        '- Deliverables: `review-candidates/book/M10/images-complete.json`, this report, `review-candidates/book/M10/reconcile.py`, and the four separate PNG replacements listed below.',
        '- Original `images.json` (86 records) and all86 original PNGs preserved byte-for-byte; SHA-256 compared before/after. All86 final candidates equal the exact source rectangle pixel-for-pixel.',
        '- Crop edges were examined individually, using source pages and native-resolution 40-pixel edge strips (temporary diagnostic sheets only, not score deliverables). No batch margin expansion, painting, synthetic border, resampling, joining or notation reconstruction.',
        '- **All86 candidates remain pending_independent_review.** Extractor observations are not independent image-review results or approvals. A separate reviewer must inspect every candidate against its source.', '',
        '## Separate recrops (original files retained)', '',
    ]
    for r in replacements:
        lines.append(f"- `{r['image']}`: {r['recrop_reason']} Original `{r['original_image']}`, local rect `{r['original_rect']}`; replacement local rect `{r['rect']}`.")
    lines += ['', '## Integration blockers / source limitations', '',
        '- 4.169 (362): lowest bass beam overlaps the explanatory footnote vertical range. Preserve the full beam; current source-only candidate contains partial related-footnote ink. cleanup_required/layout_conflict; not a pass.',
        '- 4.173 (363): abrasion interrupts the right final barline in the source itself. source_damage; no repair or concealed clipping.',
        '- 4.178 parts on366/367: handwritten bass-note circles are source ink. cleanup_required/handwriting; no erasure.',
        '- 4.192 (378): old top clipped the Beethoven attribution; replacement restores it but retains unavoidable preceding-prose descenders. Bottom slurs and next Ravel attribution share the same vertical range, leaving a constrained bottom margin. cleanup_required/layout_conflict; reviewer must not approve merely because notes are present.',
        '- 4.193 (378): complete Ravel attribution retained with unavoidable preceding-example slur fragments at top. cleanup_required/layout_conflict. Lowest bass notes retained and page number excluded.',
        '- 4.193 is an open-ended printed excerpt, NOT an incomplete extraction requiring an invented final barline. Parent reports379 starts5.REKAPITULACIJA and Zadaci1/2, with no4.193 continuation. This worker stopped at378; no379 crop/continuation added. Supersedes the earlier text-review suggestion to investigate a possible continuation; verified text remains untouched.',
        '- Multipart identities: 4.152351/352; exercise8356/357; exercise11357/358; exercise2364/365; 4.178366/367; 4.182368/369; exercise2371/372; exercise5373/374; realization1374/375. Keep separate images and actual printed number/title only where present, never repeat or synthesize labels.',
        '- Explanatory footnotes are already separately transcribed in the verified shards. Their score markers remain in crops. Realization titles are restored in the new PNGs; Allegro, ma non troppo and Andantino grazioso remain in the original complete score crops.',
        '- No unreadable prose discovered in this extraction task; no musical symbol repaired, inferred or replaced. The abrasion/handwriting/layout conflicts above require explicit reviewer/integrator disposition.',
        '- **Ready for independent review, not final integration or milestone completion.** No chapter Markdown, global tracker, raw manifest, commit or push changed.', '',
        '## Per-slot coverage and image-review state', '',
        '| Slot | Printed / PDF | Candidate | Image-review result | Extractor observation |',
        '|---|---|---|---|---|',
    ]
    for r in rows:
        detail = r['review_note'].split('edges compared. ', 1)[1].split(' Independent visual reviewer', 1)[0]
        lines.append(f"| {r['slot_label']} | {r['printed_page']} / {r['pdf_page']} | `{r['image']}` | pending independent review | {detail} |")
    (HERE / 'extraction-complete.md').write_text('\n'.join(lines) + '\n')
    print(f'86/86 slots; {len(replacements)} separate recrops; {sum(r["cleanup_required"] for r in rows)} cleanup-flagged candidates; {sum(r["source_damage"] for r in rows)} source-damage candidate; all pending independent review.')


if __name__ == '__main__':
    main()

"""M11 source-only crops; each rectangle was chosen separately by visual inspection.

Draft coordinates below refer to a proportional 2000px-high source preview.
The manifest records the corresponding integer coordinates in original PNG pixels.
No resampling, cleanup, stitching, padding, or pixel edits are performed.
"""
import json
from pathlib import Path
from PIL import Image

OUT = Path('review-candidates/book/M11')
SPECS = [
    # page, filename stem, printed identifier, preview rectangle, caption
    (379, 'primjer-5-1', '1', (155, 1024, 1333, 1436), 'Zadatak 1.'),
    (379, 'primjer-5-2', '2', (157, 1472, 1333, 1868), 'Zadatak 2.'),
    (380, 'primjer-5-3', '3', (136, 98, 1312, 505), 'Zadatak 3.'),
    (380, 'primjer-5-4', '4', (136, 514, 1308, 948), 'Zadatak 4.'),
    (380, 'primjer-5-5', '5', (134, 972, 1306, 1390), 'Zadatak 5.'),
    (380, 'primjer-5-6', '6', (126, 1405, 1304, 1842), 'Zadatak 6.'),
    (381, 'primjer-5-7', '7', (160, 105, 1333, 517), 'Zadatak 7.'),
    (381, 'primjer-5-8', '8', (163, 534, 1334, 980), 'Zadatak 8.'),
    (381, 'primjer-5-9', '9', (162, 982, 1334, 1419), 'Zadatak 9.'),
    (381, 'primjer-5-10-part-1', '10', (157, 1400, 1335, 1859), 'Zadatak 10., prvi dio.'),
    (382, 'primjer-5-10-part-2', '10', (131, 90, 1311, 222), 'Zadatak 10., nastavak sa str. 381.'),
    (382, 'primjer-5-11', '11', (127, 252, 1313, 875), 'Zadatak 11.'),
    (382, 'primjer-5-12', '12', (121, 836, 1305, 1578), 'Zadatak 12.'),
    (382, 'primjer-5-13-part-1', '13', (119, 1586, 1302, 1867), 'Zadatak 13., prvi dio.'),
    (383, 'primjer-5-13-part-2', '13', (168, 84, 1347, 373), 'Zadatak 13., nastavak sa str. 382.'),
    (383, 'primjer-5-14', '14', (168, 379, 1348, 1001), 'Zadatak 14.'),
    (383, 'primjer-5-15', '15', (168, 1020, 1349, 1737), 'Zadatak 15.'),
    (384, 'slika-384-1', None, (125, 82, 1331, 1563), 'Realizacija zadatka 4.'),
    (385, 'slika-385-1', None, (142, 82, 1340, 1183), 'Realizacija zadatka 9.'),
    # Appendix: isolated printed notation, not screenshots of surrounding prose.
    (386, 'slika-386-1', None, (810, 801, 897, 849), 'Oznaka povišene kvarte: ♯4.'),
    (386, 'slika-386-2', None, (824, 874, 848, 911), 'Brojka 4 precrtana kosim potezom.'),
    (386, 'slika-386-3', None, (778, 928, 850, 971), 'Kosi potezi za ponavljanje prethodne oznake.'),
    (386, 'slika-386-4', None, (375, 1306, 396, 1344), 'Precrtana brojka 5 u francuskom obilježavanju.'),
    (386, 'slika-386-5', None, (665, 1340, 685, 1376), 'Precrtana brojka 7 u francuskom obilježavanju.'),
    (386, 'slika-386-6', None, (211, 1480, 245, 1535), 'Francuska oznaka dominantnog septakorda.'),
    (386, 'slika-386-7', None, (214, 1538, 241, 1586), 'Francuska oznaka dominantnog kvintsekstakorda.'),
    (386, 'slika-386-8', None, (195, 1595, 241, 1633), 'Francuska oznaka dominantnog terckvartakorda.'),
    (386, 'slika-386-9', None, (193, 1645, 241, 1681), 'Francuska oznaka dominantnog sekundakorda.'),
    (386, 'slika-386-10', None, (196, 1688, 244, 1737), 'Francuska oznaka prvog obrata smanjenog septakorda.'),
    (386, 'slika-386-11', None, (192, 1740, 243, 1795), 'Francuska oznaka drugog obrata smanjenog septakorda.'),
    (387, 'slika-387-1', None, (486, 50, 534, 121), 'Varijanta oznake s razrješilicom.'),
    (387, 'slika-387-2', None, (660, 48, 711, 120), 'Varijanta oznake s povisilicom.'),
    (387, 'slika-387-3', None, (783, 48, 829, 107), 'Varijanta oznake sa snizilicom.'),
    (387, 'slika-387-4', None, (276, 145, 359, 220), 'Francuska oznaka dominantnog nonakorda.'),
    (387, 'slika-387-5', None, (276, 225, 306, 282), 'Francuska oznaka prvog obrata dominantnog nonakorda.'),
    (387, 'slika-387-6', None, (259, 292, 304, 363), 'Francuska oznaka drugog obrata dominantnog nonakorda.'),
    (387, 'slika-387-7', None, (258, 370, 304, 440), 'Francuska oznaka trećeg obrata dominantnog nonakorda.'),
    (387, 'slika-387-8', None, (226, 556, 277, 615), 'Francuska oznaka zaostajalice na basov ton kvintakorda.'),
    (387, 'slika-387-9', None, (226, 621, 278, 680), 'Francuska oznaka zaostajalice na basov ton sekstakorda.'),
    (387, 'slika-387-10', None, (225, 681, 279, 751), 'Francuska oznaka zaostajalice na basov ton kvintsekstakorda.'),
    (387, 'slika-387-11', None, (1110, 694, 1154, 749), 'Oznaka rješenja zaostajalice na basov ton kvintsekstakorda.'),
    (387, 'slika-387-12', None, (226, 762, 279, 832), 'Francuska oznaka zaostajalice na basov ton terckvartakorda.'),
    (387, 'slika-387-13', None, (1112, 771, 1159, 823), 'Oznaka rješenja zaostajalice na basov ton terckvartakorda.'),
    (387, 'slika-387-14', None, (504, 889, 535, 926), 'Alternativna oznaka smanjene kvinte odnosno smanjenog kvintakorda.'),
]

def main():
    source_index = {p['printed_page']: p for p in json.loads(Path('sources/index.json').read_text())['pages'] if p['printed_page'] is not None}
    records = []
    for page, stem, example, box, caption in SPECS:
        entry = source_index[page]
        source = Image.open(entry['image'])
        scale = source.height / 2000
        rect = [round(n * scale) for n in box]
        folder = '05-rekapitulacija' if page <= 385 else 'dodaci'
        dest = Path('images') / folder / (stem + '.png')
        dest.parent.mkdir(parents=True, exist_ok=True)
        source.crop(rect).save(dest)
        note = 'Source-only crop; requires independent comparison of all four edges.'
        if 'part-2' in stem:
            note += ' Continuation has no repeated printed exercise number in source; do not invent one.'
        if page == 382 and example in ('11', '12'):
            note += ' Closely adjacent exercise ending and following tempo indication require special boundary review.'
        records.append(dict(id='M11-' + stem, example=example, kind='score' if page <= 385 else 'notation', printed_page=page, pdf_page=entry['pdf_page'], source_image=entry['image'], rect=rect, image=str(dest), review_status='pending_independent_review', review_note=note, caption=caption))
    (OUT / 'images.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {len(records)} source-only crops and local images.json')

if __name__ == '__main__':
    main()

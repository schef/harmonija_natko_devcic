"""Individually selected rectangles, printed 119–136; no OCR or retouching.

Inspection coordinates below refer to 1000px-wide viewing copies of the source
pages. They are converted once to local ORIGINAL source pixels; only the original
PNG is cropped. Manifest rect is Pillow's [left, top, right, bottom), not xywh.
Do not run this script to overwrite subsequently independently corrected crops.
"""
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'images/02-dijatonika-b'
HANDOFF = ROOT / 'review-candidates/book/M03'

# Each edge chosen separately from its own source example. No margin expansion.
# page, identity, (left, top, right, bottom), cleanup flag
ROWS = [
 (119,'2.256',(108,735,913,962),True),
 (119,'2.257',(249,1045,739,1277),True),
 (120,'2.258',(82,26,891,279),True),
 (120,'2.259',(81,281,892,522),True),
 (120,'2.260',(173,746,789,989),True),
 (120,'2.261',(127,991,838,1240),True),
 (121,'2.262',(181,299,861,531),True),
 (121,'2.263',(109,633,958,855),True),
 (121,'2.264',(159,856,842,1066),True),
 (121,'2.265',(111,1067,924,1266),True),
 (122,'2.266',(83,331,897,680),True),
 (122,'2.267',(81,831,902,1280),False),
 (123,'2.268',(109,65,920,292),False),
 (123,'2.269',(105,395,918,616),True),
 (123,'2.270',(106,722,918,943),False),
 (124,'2.271',(179,730,762,909),True),
 (124,'2.272',(83,1057,390,1268),True),
 (124,'2.273',(437,1034,899,1283),True),
 (125,'2.274',(170,292,793,400),False),
 (125,'2.275',(210,985,733,1151),True),
 (126,'2.276',(87,43,898,299),True),
 (126,'2.277',(86,300,897,752),True),
 (126,'2.278',(82,760,894,1190),True),
 (127,'2.279',(113,65,925,300),False),
 (127,'2.280',(202,428,784,690),True),
 (127,'2.281',(109,912,925,1187),True),
 (128,'2.282',(81,59,895,314),True),
 (128,'2.283',(181,326,797,547),True),
 (128,'2.284',(74,550,896,1043),True),
 (129,'2.285',(288,14,751,210),True),
 (129,'2.286',(111,619,918,885),True),
 (129,'2.287',(109,887,917,1132),True),
 (130,'Zadatak 1',(95,132,898,242),False),
 (130,'Zadatak 2',(92,243,899,343),False),
 (130,'Zadatak 3',(94,344,899,448),False),
 (130,'Zadatak 4',(94,449,899,553),False),
 (130,'Zadatak 5',(91,557,899,653),True),
 (130,'Zadatak 6',(94,650,901,731),True),
 (130,'Zadatak 7',(96,739,900,828),False),
 (130,'Zadatak 8',(95,841,900,927),False),
 (130,'Zadatak 9',(91,941,900,1131),False),
 (130,'Zadatak 10',(89,1142,902,1235),False),
 (131,'Realizacija zadatka 6',(108,64,930,371),False),
 (131,'2.288',(108,763,927,1022),True),
 (132,'2.289',(90,72,902,298),False),
 (132,'2.290',(89,299,903,531),False),
 (132,'2.291',(208,765,788,922),True),
 (132,'2.292',(92,1007,904,1270),True),
 (133,'2.293',(123,187,933,452),True),
 (133,'2.294',(250,454,804,703),True),
 (133,'2.295',(121,942,586,1067),False),
 (133,'2.296',(589,922,927,1150),False),
 (134,'2.297',(86,244,468,369),True),
 (134,'2.298',(471,196,896,428),True),
 (134,'2.299',(258,448,725,713),True),
 (134,'2.300',(190,866,774,1004),False),
 (134,'2.301',(137,1014,821,1256),True),
 (135,'Zadatak 1',(116,147,926,247),False),
 (135,'Zadatak 2',(115,249,927,363),False),
 (135,'Zadatak 3',(115,373,927,477),False),
 (135,'Zadatak 4',(115,479,927,691),False),
 (135,'Zadatak 5',(115,697,926,790),False),
 (135,'Zadatak 6',(116,820,925,909),False),
 (135,'Zadatak 7',(116,918,927,1014),False),
 (135,'Zadatak 8',(115,1019,925,1107),False),
 (135,'Zadatak 9',(115,1123,924,1218),False),
 (136,'Realizacija zadatka 9',(79,67,899,342),False),
]

def main():
    slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->',
                       (HANDOFF / 'text-119-136.md').read_text())
    assert [(name, str(page)) for page,name,_,_ in ROWS] == slots
    assert len(ROWS) == 67
    manifest = []
    for page, name, view_rect, cleanup in ROWS:
        source = f'sources/pages/page-{page}.png'
        with Image.open(ROOT / source) as im:
            rect = [round(v * im.width / 1000) for v in view_rect]
            if name.startswith('2.'):
                ident = 'primjer-' + name.replace('.', '-')
                kind = 'example'
                caption = f'Primjer {name}. — tiskana str. {page}.'
            elif name.startswith('Zadatak'):
                ident = f'zadatak-2-{page}-{name.split()[-1]}'
                kind = 'exercise'
                caption = f'{name}. — tiskana str. {page}.'
            else:
                ident = f'realizacija-2-{page}-{name.split()[-1]}'
                kind = 'realization'
                caption = f'{name}. — tiskana str. {page}.'
            image = f'images/02-dijatonika-b/{ident}.png'
            target = ROOT / image
            if target.exists():
                raise FileExistsError(f'Refusing to overwrite existing work: {image}')
            im.crop(rect).save(target)
        note = 'Original source pixels only; pending independent visual review.'
        if cleanup:
            note += (' cleanup_required: source handwriting, pencil analysis, arrows, '
                     'or layout marks retained without retouching; inspect all edges '
                     'and authorize cleanup separately if needed.')
        if name in ('2.277','2.278','2.284','2.267') or (page,name) in ((130,'Zadatak 9'),(135,'Zadatak 4')):
            note += ' All same-page continuation systems retained in this single example.'
        if page == 130 and name in ('Zadatak 5', 'Zadatak 6'):
            note += (' Source-layout collision: lowest figures of exercise 5 and '
                     'upper slur of exercise 6 share vertical coordinates. '
                     'Rectangles overlap deliberately rather than clipping either '
                     'exercise; adjacent ink needs separately authorized cleanup.')
        if kind == 'realization':
            note += ' Identifying realization title retained; following prose/footnote excluded.'
        manifest.append(dict(id=ident, example=name, kind=kind, printed_page=page,
            pdf_page=(page+1)//2, source_image=source, rect=rect, image=image,
            review_status='pending_independent_review', review_note=note, caption=caption))
    (HANDOFF/'images-119-136.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print(f'Wrote {len(manifest)} original-pixel crops; exact ordered slot coverage confirmed.')

if __name__ == '__main__':
    main()

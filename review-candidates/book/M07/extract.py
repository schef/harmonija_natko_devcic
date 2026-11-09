"""M07: individually located source-pixel rectangles; no image alteration.

Coordinates below were chosen separately on each visually opened 2000-high
source preview. They are converted once to local original-pixel rectangles.
The output is always a direct PIL crop of the unmodified original PNG.
No automatic ink bounds, fixed padding, stitching, or retouching is used.
Run from the repository root. Existing outputs are refused.
"""
from pathlib import Path
from PIL import Image
import json
import re

OUT = Path('images/03-kromatika-c')
BASE = Path('review-candidates/book/M07')
# page, identifier, independently selected (left, top, right, bottom), source issue
CHOICES = [
 (257,'3.176',(180,807,1350,1066),'Handwritten marks near variant c and below figures.'),
 (257,'3.177',(168,1467,1344,1875),'Handwritten harmonic labels above and below systems.'),
 (258,'3.178',(184,86,1220,461),'Handwriting immediately below composer attribution.'),
 (258,'3.179',(206,614,1232,821),'Handwritten labels among variant letters.'),
 (258,'3.180',(112,831,1300,1868),''),
 (259,'3.181',(183,288,1370,993),''),
 (259,'3.182',(196,1071,1372,1798),''),
 (260,'3.183',(108,101,1287,508),''),
 (260,'3.184',(109,510,1289,975),''),
 (260,'3.185',(110,1281,1289,1638),''),
 (261,'3.186',(369,222,1168,446),''),
 (261,'3.187',(192,475,1371,821),''),
 (261,'3.188',(178,1232,1372,1832),''),
 (262,'3.189',(231,562,1173,764),''),
 (262,'3.190',(98,794,1301,1879),'Handwritten labels above variant a; preserved intact.'),
 (263,'3.191',(165,109,1368,711),''),
 (263,'3.192',(180,1183,1363,1658),''),
 (264,'3.193',(335,331,1082,461),''),
 (264,'ZADACI 1',(124,609,1298,972),''),
 (264,'ZADACI 2',(124,973,1298,1528),''),
 (264,'ZADACI 3',(126,1535,1300,1782),''),
 (265,'ZADACI 4',(160,107,1339,343),''),
 (265,'ZADACI 5',(158,384,1337,646),''),
 (265,'ZADACI 6',(163,667,1337,783),''),
 (265,'ZADACI 7',(165,806,1337,928),''),
 (265,'ZADACI 8',(163,953,1338,1092),''),
 (265,'ZADACI 9',(162,1098,1338,1355),''),
 (265,'ZADACI 10',(153,1381,1339,1670),''),
 (266,'Realizacija zadatka 6.',(125,83,1321,819),''),
 (267,'3.194',(151,910,1400,1201),'Pencil annotations touch/encircle printed figures and variant labels.'),
 (267,'3.195',(272,1548,1207,1818),'Pencil annotations overlap notation and extend above variants.'),
 (268,'3.196',(324,420,1179,742),'Small pencil marks inside the musical example.'),
 (268,'3.197',(143,1007,1316,1324),''),
 (268,'3.198',(142,1339,1314,1633),''),
 (269,'3.199',(138,207,1315,497),''),
 (269,'3.200',(127,547,1315,1183),''),
 (269,'3.201',(292,1189,1138,1558),'Handwritten labels above, inside, and below the example.'),
 (270,'3.202',(145,439,685,762),'Pencil labels within and below notation; narrow right separation from 3.203.'),
 (270,'3.203',(686,410,1324,802),'Handwriting above and below notation; narrow left separation from 3.202.'),
 (270,'3.204',(393,766,1063,1037),'Handwriting inside notation and beside the example.'),
 (270,'3.205',(325,1494,1130,1770),'Handwritten marks above and within the example.'),
 (271,'ZADACI 1',(155,221,1331,565),''),
 (271,'ZADACI 2',(155,585,1330,1116),''),
 (271,'ZADACI 3',(154,1117,1331,1224),''),
 (271,'ZADACI 4',(152,1254,1331,1520),''),
 (271,'ZADACI 5',(151,1544,1331,1824),''),
 (272,'Realizacija zadatka 3.',(132,82,1326,803),''),
 (273,'3.206',(285,733,1413,1080),'Handwritten labels and lines overlap slurs and notes; source marks extend right.'),
 (273,'3.207',(519,1597,1050,1809),'Handwritten harmonic label immediately above printed notation.'),
 (274,'3.208',(131,239,1309,811),'Pencil harmonic labels inside and below the three-staff example.'),
 (274,'3.209',(134,974,1309,1351),''),
 (274,'3.210',(185,1517,1262,1846),''),
 (275,'3.211',(252,190,1247,544),''),
 (275,'3.212',(165,685,1239,1027),''),
 (275,'3.213',(162,1059,1339,1571),''),
 (276,'3.214',(260,50,1191,279),'Handwritten harmonic labels directly above variant letters; unrelated marks at page top excluded.'),
 (276,'3.215',(127,546,1312,1318),'Handwritten analysis around variants b/c overlaps notation; retained without cleaning.'),
]

def main():
    assert len(CHOICES) == 57
    assert not (BASE/'images.json').exists(), 'Preserve existing manifest; inspect before rerun.'
    slots = re.findall(r'<!-- visual: (.*?); page (\d+) -->', (BASE/'text-257-276.md').read_text())
    assert [(e,str(p)) for p,e,_,_ in CHOICES] == slots
    source_index = {p['printed_page']: p for p in json.loads(Path('sources/index.json').read_text())['pages'] if p['printed_page'] is not None}
    OUT.mkdir(parents=True, exist_ok=True)
    rows=[]
    for slot,(page,example,preview_rect,issue) in enumerate(CHOICES,1):
        source=source_index[page]
        with Image.open(source['image']) as im:
            scale=im.height/2000
            rect=[round(c*scale) for c in preview_rect]
            if example.startswith('3.'):
                name='primjer-'+example.replace('.','-')+'.png'
                kind='example'
                caption=f'Primjer {example}. Izvor: tiskana str. {page}.'
            elif example.startswith('ZADACI'):
                chapter='3-8' if page<267 else '3-9'
                name=f'zadatak-{chapter}-{example.split()[-1]}.png'
                kind='exercise'
                caption=f'Zadatak {example.split()[-1]} (poglavlje {chapter.replace("-", ".")}). Izvor: tiskana str. {page}.'
            else:
                chapter='3-8' if page==266 else '3-9'
                number=6 if page==266 else 3
                name=f'realizacija-{chapter}-zadatak-{number}.png'
                kind='realization'
                caption=f'{example} Izvor: tiskana str. {page}.'
            image=OUT/name
            assert not image.exists(), f'Preserve existing output: {image}'
            assert 0<=rect[0]<rect[2]<=im.width and 0<=rect[1]<rect[3]<=im.height
            im.crop(tuple(rect)).save(image)
        rows.append(dict(id=f'M07-{slot:02d}',example=example,kind=kind,printed_page=page,pdf_page=source['pdf_page'],source_image=source['image'],rect=rect,image=str(image),review_status='pending_independent_review',cleanup_required=bool(issue),review_note=(('cleanup_required: '+issue+' ') if issue else '')+'Direct source-pixel crop; independent visual review required.',caption=caption))
    (BASE/'images.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(f'Created {len(rows)} individually specified crops and manifest; all pending independent review.')

def refine_boundaries():
    """Apply only the three documented extractor-edge corrections to our outputs."""
    rows=json.loads((BASE/'images.json').read_text())
    old_previews={19:(124,609,1298,968),20:(124,969,1298,1528),49:(519,1597,1006,1809)}
    for slot,old in old_previews.items():
        row=rows[slot-1]
        page,example,new,_=CHOICES[slot-1]
        assert row['example']==example and row['printed_page']==page
        with Image.open(row['source_image']) as im:
            scale=im.height/2000
            assert row['rect']==[round(c*scale) for c in old]
            with Image.open(row['image']) as prior:
                assert prior.tobytes()==im.crop(tuple(row['rect'])).tobytes()
            row['rect']=[round(c*scale) for c in new]
            im.crop(tuple(row['rect'])).save(row['image'])
        row['review_note']+=' Extractor edge refinement: '+('separated adjacent exercise figures at genuine source whitespace.' if slot in (19,20) else 'retained complete adjacent handwritten source label.')
    (BASE/'images.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print('Applied three validated source-boundary refinements; independent review remains pending.')

if __name__=='__main__':
    import sys
    if sys.argv[1:]==['--refine-boundaries']:
        refine_boundaries()
    else:
        main()

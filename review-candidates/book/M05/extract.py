"""Individually visually selected bounds, expressed in 2000-high page view.
Only a coordinate transform to native pixels is performed; no image resampling.
"""
from PIL import Image
import json
from pathlib import Path

OUT = Path('review-candidates/book/M05')
# page, example number, four independently chosen view bounds, limitation
CROPS = [
 (175,1,(275,650,1240,780),''),
 (175,2,(160,1512,655,1775),'cleanup-required: faint source handwriting near notation; retained without retouch.'),
 (175,3,(690,1445,1340,1800),'cleanup-required: faint source handwriting within score area; retained without retouch.'),
 (176,4,(215,400,1210,655),'cleanup-required: source pencil traces inside score; retained.'),
 (176,5,(215,705,1210,958),'cleanup-required: source pencil traces inside score; retained.'),
 (177,6,(174,910,1350,1230),'cleanup-required: faint pencil inside score area.'),
 (178,7,(135,467,1110,790),'cleanup-required: source handwriting beside second system.'),
 (178,8,(135,806,1110,1160),'cleanup-required: pencil analysis interleaved with systems.'),
 (178,9,(135,1160,1290,1328),'cleanup-required: source pencil analysis below notes.'),
 (178,10,(130,1328,1110,1510),'cleanup-required: pencil analysis below and near upper edge; neighbouring handwritten analysis cannot all be excluded.'),
 (179,11,(350,311,1105,470),'cleanup-required: source handwriting interleaved with variants.'),
 (179,12,(160,527,1320,735),'cleanup-required: source handwriting above and below variants.'),
 (179,13,(248,947,1240,1100),'cleanup-required: source handwriting alongside variant labels.'),
 (179,14,(424,1138,1050,1460),'cleanup-required: faint source pencil above attribution.'),
 (180,15,(413,153,1045,461),'cleanup-required: source pencil by Roman numerals.'),
 (180,16,(320,729,1132,1046),'cleanup-required: pencil analysis interleaved with notation.'),
 (180,17,(132,1455,1320,1818),'Footnote below example excluded for text transcription; asterisks retained.'),
 (181,18,(159,914,1348,1242),''),
 (182,19,(127,117,1318,1002),'cleanup-required: source pencil analysis interleaved with all three systems.'),
 (183,20,(170,110,1350,431),''),
 (183,21,(175,455,1350,790),'cleanup-required: pencil traces interleaved with notes and lower annotations.'),
 (183,22,(168,795,1350,1520),'cleanup-required: pencil analysis interleaved with both systems.'),
 (183,23,(171,1523,1350,1870),'cleanup-required: pencil analysis among variant labels and lower figures.'),
 (184,24,(131,464,1300,838),'cleanup-required: source handwritten analysis overlaps example.'),
 (184,25,(384,1130,1020,1480),'cleanup-required: source pencil within notation area.'),
 (185,26,(158,266,1328,610),'cleanup-required: pencil labels above printed score.'),
 (185,27,(158,612,1328,953),'cleanup-required: pencil labels interleaved with variant labels.'),
 (185,28,(149,1185,1328,1847),'cleanup-required: source pencil analysis within both systems. Continues p186; separate crop.'),
 (186,'28-p186',(142,109,1332,477),'Continuation of 3.28, variants e-f; number not repeated in source. cleanup-required: extensive pencil interleaved with notation.'),
 (186,29,(131,916,1330,1620),'cleanup-required: extensive source pencil among systems and lower annotations.'),
 (187,30,(184,425,1375,1092),''),
 (187,31,(189,1333,1375,1765),'Asterisk retained; associated prose footnote excluded for text transcription.'),
 (188,32,(120,437,1289,1075),'cleanup-required: pencil analysis within both variants.'),
 (188,33,(120,1080,1285,1380),'cleanup-required: source handwritten chord labels above score.'),
 (188,34,(118,1410,1284,1750),'cleanup-required: source handwritten analysis above and within score.'),
 (189,35,(178,102,1342,400),'cleanup-required: pencil analysis below score.'),
 (189,36,(165,409,1342,1008),'cleanup-required: pencil analysis inside both systems. Asterisk retained, footnote excluded for transcription.'),
 (189,'z2',(182,1323,1340,1475),''),
 (189,'z3',(180,1492,1340,1640),''),
 (189,'z4',(177,1651,1340,1806),''),
 (190,'z5',(127,86,1298,241),''),
 (190,'z6',(126,257,1298,399),''),
 (190,'z7',(130,408,1298,558),'Lower figures and next exercise slur nearly touch; natural separation used, independent edge review needed.'),
 (190,'z8',(130,558,1298,680),'Upper slur close to previous exercise figures; natural separation used, independent edge review needed.'),
 (190,'z9',(130,698,1295,824),''),
 (190,'z10',(122,847,1293,1117),'Both systems retained.'),
 (190,'z11',(120,1134,1292,1261),''),
 (190,'z12',(120,1277,1292,1412),''),
 (190,'z13',(119,1424,1288,1558),''),
 (190,'z14',(117,1569,1287,1840),'Both systems retained.'),
 (191,'z8-realizacija',(148,88,1335,485),'Realizacija zadatka 8: printed identifying label retained; no separate example number in source.'),
 (192,37,(136,1302,674,1657),'cleanup-required: handwritten analysis interleaved with score.'),
 (192,38,(706,1302,1319,1648),'cleanup-required: handwritten analysis interleaved with score.'),
 (193,39,(440,49,1090,368),'cleanup-required: handwritten chord names and traces within score.'),
 (193,40,(168,905,750,1223),'cleanup-required: handwritten chord names above score.'),
 (193,41,(750,904,1344,1221),'cleanup-required: handwritten chord names above score.'),
 (193,42,(284,1233,1205,1617),'cleanup-required: handwritten analysis above and below score.'),
 (194,43,(135,87,615,389),''),
 (194,44,(618,80,1309,388),''),
 (194,45,(202,565,1214,844),''),
 (194,46,(139,1078,769,1400),''),
 (194,47,(775,1084,1309,1409),''),
 (195,48,(175,104,735,406),''),
 (195,49,(741,108,1348,419),''),
 (195,50,(173,765,793,1071),''),
 (195,51,(801,770,1344,1070),''),
 (195,52,(165,1360,673,1666),''),
 (195,53,(697,1353,1340,1676),''),
 (196,54,(122,328,715,645),''),
 (196,55,(727,333,1307,641),''),
 (196,56,(130,1130,688,1422),''),
 (196,57,(700,1120,1310,1430),''),
 (196,58,(341,1476,1084,1725),''),
 (197,59,(154,101,1358,765),''),
 (197,60,(174,1045,1352,1462),''),
 (197,61,(174,1474,1354,1799),''),
 (198,62,(111,106,1311,1130),''),
 (199,63,(158,613,1353,1294),''),
 (199,64,(172,1537,1352,1865),''),
 (200,65,(134,240,1310,561),''),
 (200,66,(306,820,1090,1148),''),
 (200,67,(117,1234,1305,1872),'Continues on p201; separate original-pixel part.'),
 (201,'67-p201',(169,109,1357,421),'Continuation of 3.67 variants e-f; number not repeated in source.'),
 (201,68,(183,863,1358,1187),''),
 (201,69,(179,1212,1358,1537),''),
 (202,70,(368,123,1112,428),''),
 (202,71,(110,533,1301,1183),''),
 (202,72,(325,1433,1105,1576),''),
 (203,73,(175,178,791,504),''),
 (203,74,(798,181,1348,505),''),
 (203,75,(316,736,1197,1042),''),
 (204,76,(122,122,1304,787),''),
 (204,77,(125,1277,1293,1577),''),
 (205,78,(168,108,1335,400),''),
 (205,'z2',(174,679,1333,830),''),
 (205,'z3',(169,844,1333,1161),'Both systems retained.'),
 (205,'z4',(170,1165,1333,1408),'Both systems retained.'),
 (205,'z5',(169,1453,1333,1552),''),
 (205,'z6',(169,1596,1333,1845),'Both systems retained.'),
 (206,'z7',(125,100,1301,235),''),
 (206,'z8',(125,257,1301,381),''),
 (206,'z9',(123,399,1300,678),'Both systems retained.'),
 (206,'z10',(115,698,1300,827),''),
 (206,'z7-realizacija',(103,1116,1301,1832),'Realizacija zadatka 7: printed identifying label retained; both systems included.'),
]

def build():
    mapping = {p['printed_page']:p for p in json.loads(Path('sources/index.json').read_text())['pages']}
    entries=[]
    for page,num,view,note in CROPS:
        src=f'sources/pages/page-{page:03}.png'
        im=Image.open(src)
        factor=im.height/2000
        rect=[round(v*factor) for v in view]
        exercise = str(num).startswith('z')
        name=f'zadatak-3-{page}-{str(num)[1:]}' if exercise else f'primjer-3-{num}'
        path=f'images/03-kromatika-a/{name}.png'
        im.crop(rect).save(path)
        example=f'Zadatak {str(num)[1:]}' if exercise else f'3.{str(num).split("-")[0]}'
        caption=f'{example if exercise else "Primjer "+example}. Tiskana str. {page}.'
        entries.append(dict(id=name, example=example,kind='exercise' if exercise else 'example',printed_page=page,pdf_page=mapping[page]['pdf_page'],source_image=src,rect=rect,image=path,review_status='pending_independent_review',review_note=note or 'Original-pixel crop; independent four-edge review required.',caption=caption))
    (OUT/'images.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__': build()

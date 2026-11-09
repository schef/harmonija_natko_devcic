from PIL import Image
from pathlib import Path
import json

# Individually selected bounds, in thousandths of the displayed source page.
SPECS = [
 (207,'79',(225,373,832,470)),
 (207,'80',(175,552,872,719)),
 (208,'81',(93,162,903,494)),
 (208,'82',(99,500,903,661)),
 (208,'83',(98,766,900,934)),
 (209,'84',(115,189,917,372)),
 (209,'85',(103,391,916,747)),
 (210,'86',(95,248,905,601)),
 (210,'87',(196,612,799,782)),
]

def main():
    out=Path('images/03-kromatika-b'); out.mkdir(parents=True,exist_ok=True)
    index={p['printed_page']:p for p in json.loads(Path('sources/index.json').read_text())['pages']}
    records=[]
    for row in SPECS:
        page,num,bounds,*extra=row
        kind='exercise' if num.startswith('z') else 'example'
        stem=f'zadatak-3-{page}-{num[1:]}' if kind=='exercise' else f'primjer-3-{num}'
        source=f'sources/pages/page-{page:03d}.png'
        im=Image.open(source); w,h=im.size
        rect=[round(bounds[0]*w/1000),round(bounds[1]*h/1000),round(bounds[2]*w/1000),round(bounds[3]*h/1000)]
        path=out/(stem+'.png'); im.crop(rect).save(path)
        note=extra[0] if extra else 'Source-only crop; independent full-resolution edge/content review required.'
        example=f'Zadatak {num[1:]}' if kind=='exercise' else f'3.{num.split("-")[0]}'
        records.append(dict(id=stem,example=example,kind=kind,printed_page=page,pdf_page=index[page]['pdf_page'],source_image=source,rect=rect,image=str(path),review_status='pending_independent_review',review_note=note,caption=f'{example}, str. {page}.'))
    Path('review-candidates/book/M06/images.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__': main()

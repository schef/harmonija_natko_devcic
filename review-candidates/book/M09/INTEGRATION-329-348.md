# M09 — integracija tiskanih str. 329–348

## Ishod i granice

- Dodijeljeno i obrađeno: **20 tiskanih stranica 329–348**, **PDF str. 165–175** (indeks od 1), prema [izvornom indeksu](../../../sources/index.json). STOP 348; ništa sa str. 349 nije integrirano.
- [Poglavlju](../../../chapters/04-neakordicki-b.md) dodano 66 mjesta: **59 independent_pass, 7 cleanup_required**. Prethodni sadržaj kroz str. 328 očuvan je bajt-po-bajt, uključujući povijesni status na vrhu; dodana napomena izričito ga vremenski dopunjuje.
- [REVIEW.md](../../../images/04-neakordicki-b/REVIEW.md) samo dopunjen; [integriranom manifestu](images-integrated.json) dodano 66 na postojećih 68 zapisa: **134 ukupno, 111 independent_pass, 23 cleanup_required**. Svih prvih 68 objekata ostaje identično; sačuvan je i njihov izvorni serijalizirani sadržaj.
- Nisu stvarane ni mijenjane slike, sirovi manifesti, prijepisi, globalni tracker ni drugi dokumenti. Bez delegacije, retuširanja, ljudskog odobrenja, commita ili pusha. M09 nije označen dovršenim.

## Izvori i granice teksta

- [text-319-333.md](text-319-333.md), samo od oznake tiskane str. 329 nadalje; [pregled](text-319-333-review.json), samo zapisi 329–333.
- [text-334-348.md](text-334-348.md) u cijelosti, uz [pregled](text-334-348-review.json). Sve oznake source-page/pdf-page, naslovi, odlomci, fusnote, reference, bilješke i komentari nastavaka očuvani su bez tekstnih ispravaka. Nije bila potrebna ni normalizacija razmaka brojeva naslova.
- [Slikovni manifest](images-329-348.json) i [neovisni pregled](visual-review-329-348.json): točno 66 zapisa, 59 PASS i 7 RECROP_REQUIRED / source_limited. Integrator nije ponovno samoodobravao izreze.
- Povijesni završni komentar prijepisa 333/334, da je nastavak bio izvan tadašnjega tekstnog zadatka, ostaje doslovno sačuvan; iza njega slijedi drugi prijepis s nastavkom 334. Sadržaj nije izgubljen niti dupliran.
- Očuvana tiskana referenca `pr. 3.91.d` na 330; nije urednički prepravljena. Očuvana referenca `4.139.d—f` na 344, iako prikaz ima samo a–e i `itd.`; nema izmišljene varijante f. Očuvane su i tiskane atribucije/termini iz prijepisa, bez popravljanja.
- Rečenica na 337 prekinuta mjestom 4.113 između »koji« i »uokviruju« ostaje u izvornom slijedu. Završna dva objašnjenja realizacije na 348 prenesena su u cijelosti. Nema nedovršene rečenice ni nastavka na donjoj granici prema tekstnom pregledu.

## Validacija

- **Prethodno poglavlje:** bajtni prefiks neizmijenjen; prethodnih 68 manifestnih zapisa objektno identično i bez prepisivanja njihova izvornoga JSON sadržaja; prethodni REVIEW.md neizmijenjen prefiks.
- **Točan tekstni round-trip:** nakon uklanjanja točno 66 dodanih slikovnih blokova iz novoga dijela dobiva se točan spoj prijepisa 329–333 i 334–348 (samo separator između datoteka normaliziran na jedan prazan redak). Nema izostavljenih odlomaka, naslova, fusnota ili referenci.
- **66/66 mjesta:** točan redoslijed i stranica, identitet, tip/broj i izvorni visual label uspoređeni s manifestom, neovisnim pregledom i svim page.visual_ids tekstnih pregleda. Sve stranice 329–348 imaju potvrdu vizualne tekstne provjere.
- **134/134 izreza:** granice rect unutar izvornika; način boje, dimenzije i svi pikseli jednaki izvornom source_image.crop(rect). Ovo je dokaz podrijetla, ne prolaza vizualnoga pregleda.
- **134/134 indeksnih veza:** printed_page, pdf_page i source_image jednaki sources/index.json; novih 20 source-page oznaka pokriva točno 329–348.
- **59 ugrađenih slika / 7 blokiranih poveznica:** svako mjesto ima natpis sa stvarnom tiskanom stranicom i MuseScore placeholder; neuspjeli izrezi nisu ugrađeni kao odobrene slike. Razlozi i source_limited sačuvani pojedinačno.
- **Svi lokalni Markdown linkovi** u poglavlju, REVIEW.md i ovom izvještaju provjereni prema direktoriju sadržavajuće datoteke; svi postoje. JSON putanje ostaju pune putanje relativne korijenu repozitorija, chapter_link relativan poglavlju.
- **Opseg promjena:** provjerene hash-vrijednosti svih ostalih postojećih datoteka izvan .git; nema drugih promjena ovim poslom.

## Parovi preko stranica

- `zadatak-4-329-5-a` (početak, otisnut broj 5) ↔ `zadatak-4-330-5-b` (nastavak bez ponovljenoga broja). Oba PASS, dva izvorna mjesta, stvarne stranice u natpisima; a/b su samo identiteti datoteka, ne izmišljene tiskane varijante.
- `zadatak-4-336-1-realizacija-a` (početak s naslovom/brojem) ↔ `zadatak-4-337-1-realizacija-b` (nastavak bez ponovljenoga naslova/broja). Oba PASS; bez dodavanja oznaka u izvorne piksele.

## Potpuna mapa 66 novih mjesta / pojedinačni ishodi

| # | Identitet / točno izvorno mjesto | Tiskana / PDF str. | Izrez | Izvornik | Ishod |
| --- | --- | --- | --- | --- | --- |
| 69 | `zadatak-4-329-1` / zadatak 1 | 329 / 165 | [PNG](../../../images/04-neakordicki-b/zadatak-4-329-1.png) | [stranica](../../../sources/pages/page-329.png) | independent_pass |
| 70 | `zadatak-4-329-2` / zadatak 2 | 329 / 165 | [PNG](../../../images/04-neakordicki-b/zadatak-4-329-2.png) | [stranica](../../../sources/pages/page-329.png) | independent_pass |
| 71 | `zadatak-4-329-3` / zadatak 3 | 329 / 165 | [PNG](../../../images/04-neakordicki-b/zadatak-4-329-3.png) | [stranica](../../../sources/pages/page-329.png) | independent_pass |
| 72 | `zadatak-4-329-4` / zadatak 4 | 329 / 165 | [PNG](../../../images/04-neakordicki-b/zadatak-4-329-4.png) | [stranica](../../../sources/pages/page-329.png) | independent_pass |
| 73 | `zadatak-4-329-5-a` / zadatak 5 početak | 329 / 165 | [PNG](../../../images/04-neakordicki-b/zadatak-4-329-5-a.png) | [stranica](../../../sources/pages/page-329.png) | independent_pass |
| 74 | `zadatak-4-330-5-b` / zadatak 5 nastavak | 330 / 166 | [PNG](../../../images/04-neakordicki-b/zadatak-4-330-5-b.png) | [stranica](../../../sources/pages/page-330.png) | independent_pass |
| 75 | `zadatak-4-330-3-realizacija` / Realizacija zadatka 3 | 330 / 166 | [PNG](../../../images/04-neakordicki-b/zadatak-4-330-3-realizacija.png) | [stranica](../../../sources/pages/page-330.png) | independent_pass |
| 76 | `primjer-4-104` / 4.104 | 331 / 166 | [PNG](../../../images/04-neakordicki-b/primjer-4-104.png) | [stranica](../../../sources/pages/page-331.png) | independent_pass |
| 77 | `primjer-4-105` / 4.105 | 331 / 166 | [PNG](../../../images/04-neakordicki-b/primjer-4-105.png) | [stranica](../../../sources/pages/page-331.png) | independent_pass |
| 78 | `primjer-4-106` / 4.106 | 331 / 166 | [PNG](../../../images/04-neakordicki-b/primjer-4-106.png) | [stranica](../../../sources/pages/page-331.png) | independent_pass |
| 79 | `primjer-4-107` / 4.107 | 332 / 167 | [PNG](../../../images/04-neakordicki-b/primjer-4-107.png) | [stranica](../../../sources/pages/page-332.png) | independent_pass |
| 80 | `zadatak-4-332-1` / zadatak 1 | 332 / 167 | [PNG](../../../images/04-neakordicki-b/zadatak-4-332-1.png) | [stranica](../../../sources/pages/page-332.png) | independent_pass |
| 81 | `zadatak-4-332-2` / zadatak 2 | 332 / 167 | [PNG](../../../images/04-neakordicki-b/zadatak-4-332-2.png) | [stranica](../../../sources/pages/page-332.png) | independent_pass |
| 82 | `zadatak-4-333-3` / zadatak 3 | 333 / 167 | [PNG](../../../images/04-neakordicki-b/zadatak-4-333-3.png) | [stranica](../../../sources/pages/page-333.png) | independent_pass |
| 83 | `zadatak-4-333-4` / zadatak 4 | 333 / 167 | [PNG](../../../images/04-neakordicki-b/zadatak-4-333-4.png) | [stranica](../../../sources/pages/page-333.png) | independent_pass |
| 84 | `zadatak-4-333-3-realizacija` / Realizacija zadatka 3 | 333 / 167 | [PNG](../../../images/04-neakordicki-b/zadatak-4-333-3-realizacija.png) | [stranica](../../../sources/pages/page-333.png) | independent_pass |
| 85 | `primjer-4-108` / 4.108 | 334 / 168 | [PNG](../../../images/04-neakordicki-b/primjer-4-108.png) | [stranica](../../../sources/pages/page-334.png) | cleanup_required |
| 86 | `primjer-4-109` / 4.109 | 334 / 168 | [PNG](../../../images/04-neakordicki-b/primjer-4-109.png) | [stranica](../../../sources/pages/page-334.png) | cleanup_required |
| 87 | `primjer-4-110` / 4.110 a–c | 334 / 168 | [PNG](../../../images/04-neakordicki-b/primjer-4-110.png) | [stranica](../../../sources/pages/page-334.png) | independent_pass |
| 88 | `primjer-4-111` / 4.111 a–b | 335 / 168 | [PNG](../../../images/04-neakordicki-b/primjer-4-111.png) | [stranica](../../../sources/pages/page-335.png) | independent_pass |
| 89 | `primjer-4-112` / 4.112 | 335 / 168 | [PNG](../../../images/04-neakordicki-b/primjer-4-112.png) | [stranica](../../../sources/pages/page-335.png) | independent_pass |
| 90 | `zadatak-4-335-1` / zadatak 1 | 335 / 168 | [PNG](../../../images/04-neakordicki-b/zadatak-4-335-1.png) | [stranica](../../../sources/pages/page-335.png) | independent_pass |
| 91 | `zadatak-4-336-2` / zadatak 2 | 336 / 169 | [PNG](../../../images/04-neakordicki-b/zadatak-4-336-2.png) | [stranica](../../../sources/pages/page-336.png) | cleanup_required |
| 92 | `zadatak-4-336-3` / zadatak 3 | 336 / 169 | [PNG](../../../images/04-neakordicki-b/zadatak-4-336-3.png) | [stranica](../../../sources/pages/page-336.png) | cleanup_required |
| 93 | `zadatak-4-336-1-realizacija-a` / Realizacija zadatka 1 početak | 336 / 169 | [PNG](../../../images/04-neakordicki-b/zadatak-4-336-1-realizacija-a.png) | [stranica](../../../sources/pages/page-336.png) | independent_pass |
| 94 | `zadatak-4-337-1-realizacija-b` / Realizacija zadatka 1 nastavak | 337 / 169 | [PNG](../../../images/04-neakordicki-b/zadatak-4-337-1-realizacija-b.png) | [stranica](../../../sources/pages/page-337.png) | independent_pass |
| 95 | `primjer-4-113` / 4.113 a–b | 337 / 169 | [PNG](../../../images/04-neakordicki-b/primjer-4-113.png) | [stranica](../../../sources/pages/page-337.png) | cleanup_required |
| 96 | `primjer-4-114` / 4.114 a–b | 338 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-114.png) | [stranica](../../../sources/pages/page-338.png) | cleanup_required |
| 97 | `primjer-4-115` / 4.115 | 338 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-115.png) | [stranica](../../../sources/pages/page-338.png) | independent_pass |
| 98 | `primjer-4-116` / 4.116 a–b | 338 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-116.png) | [stranica](../../../sources/pages/page-338.png) | independent_pass |
| 99 | `primjer-4-117` / 4.117 a–b | 338 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-117.png) | [stranica](../../../sources/pages/page-338.png) | independent_pass |
| 100 | `primjer-4-118` / 4.118 a–b | 339 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-118.png) | [stranica](../../../sources/pages/page-339.png) | independent_pass |
| 101 | `primjer-4-119` / 4.119 | 339 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-119.png) | [stranica](../../../sources/pages/page-339.png) | independent_pass |
| 102 | `primjer-4-120` / 4.120 a–b | 339 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-120.png) | [stranica](../../../sources/pages/page-339.png) | independent_pass |
| 103 | `primjer-4-121` / 4.121 a–b | 339 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-121.png) | [stranica](../../../sources/pages/page-339.png) | independent_pass |
| 104 | `primjer-4-122` / 4.122 a–b | 339 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-122.png) | [stranica](../../../sources/pages/page-339.png) | independent_pass |
| 105 | `primjer-4-123` / 4.123 a–b | 339 / 170 | [PNG](../../../images/04-neakordicki-b/primjer-4-123.png) | [stranica](../../../sources/pages/page-339.png) | independent_pass |
| 106 | `primjer-4-124` / 4.124 | 340 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-124.png) | [stranica](../../../sources/pages/page-340.png) | independent_pass |
| 107 | `primjer-4-125` / 4.125 | 340 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-125.png) | [stranica](../../../sources/pages/page-340.png) | cleanup_required |
| 108 | `primjer-4-126` / 4.126 a–e | 340 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-126.png) | [stranica](../../../sources/pages/page-340.png) | independent_pass |
| 109 | `primjer-4-127` / 4.127 | 340 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-127.png) | [stranica](../../../sources/pages/page-340.png) | independent_pass |
| 110 | `primjer-4-128` / 4.128 | 341 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-128.png) | [stranica](../../../sources/pages/page-341.png) | independent_pass |
| 111 | `primjer-4-129` / 4.129 | 341 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-129.png) | [stranica](../../../sources/pages/page-341.png) | independent_pass |
| 112 | `primjer-4-130` / 4.130 a–b | 341 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-130.png) | [stranica](../../../sources/pages/page-341.png) | independent_pass |
| 113 | `primjer-4-131` / 4.131 | 341 / 171 | [PNG](../../../images/04-neakordicki-b/primjer-4-131.png) | [stranica](../../../sources/pages/page-341.png) | independent_pass |
| 114 | `primjer-4-132` / 4.132 a–b | 342 / 172 | [PNG](../../../images/04-neakordicki-b/primjer-4-132.png) | [stranica](../../../sources/pages/page-342.png) | independent_pass |
| 115 | `primjer-4-133` / 4.133 | 342 / 172 | [PNG](../../../images/04-neakordicki-b/primjer-4-133.png) | [stranica](../../../sources/pages/page-342.png) | independent_pass |
| 116 | `primjer-4-134` / 4.134 a–b | 342 / 172 | [PNG](../../../images/04-neakordicki-b/primjer-4-134.png) | [stranica](../../../sources/pages/page-342.png) | independent_pass |
| 117 | `primjer-4-135` / 4.135 a–b | 343 / 172 | [PNG](../../../images/04-neakordicki-b/primjer-4-135.png) | [stranica](../../../sources/pages/page-343.png) | independent_pass |
| 118 | `primjer-4-136` / 4.136 a–c | 343 / 172 | [PNG](../../../images/04-neakordicki-b/primjer-4-136.png) | [stranica](../../../sources/pages/page-343.png) | independent_pass |
| 119 | `primjer-4-137` / 4.137 a–f | 343 / 172 | [PNG](../../../images/04-neakordicki-b/primjer-4-137.png) | [stranica](../../../sources/pages/page-343.png) | independent_pass |
| 120 | `primjer-4-138` / 4.138 a–d | 344 / 173 | [PNG](../../../images/04-neakordicki-b/primjer-4-138.png) | [stranica](../../../sources/pages/page-344.png) | independent_pass |
| 121 | `primjer-4-139` / 4.139 a–e | 344 / 173 | [PNG](../../../images/04-neakordicki-b/primjer-4-139.png) | [stranica](../../../sources/pages/page-344.png) | independent_pass |
| 122 | `primjer-4-140` / 4.140 | 345 / 173 | [PNG](../../../images/04-neakordicki-b/primjer-4-140.png) | [stranica](../../../sources/pages/page-345.png) | independent_pass |
| 123 | `primjer-4-141` / 4.141 | 345 / 173 | [PNG](../../../images/04-neakordicki-b/primjer-4-141.png) | [stranica](../../../sources/pages/page-345.png) | independent_pass |
| 124 | `primjer-4-142` / 4.142 a–b | 345 / 173 | [PNG](../../../images/04-neakordicki-b/primjer-4-142.png) | [stranica](../../../sources/pages/page-345.png) | independent_pass |
| 125 | `zadatak-4-346-1` / zadatak 1 | 346 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-346-1.png) | [stranica](../../../sources/pages/page-346.png) | independent_pass |
| 126 | `zadatak-4-346-2` / zadatak 2 | 346 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-346-2.png) | [stranica](../../../sources/pages/page-346.png) | independent_pass |
| 127 | `zadatak-4-346-3` / zadatak 3 | 346 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-346-3.png) | [stranica](../../../sources/pages/page-346.png) | independent_pass |
| 128 | `zadatak-4-346-4` / zadatak 4 | 346 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-346-4.png) | [stranica](../../../sources/pages/page-346.png) | independent_pass |
| 129 | `zadatak-4-346-5` / zadatak 5 | 346 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-346-5.png) | [stranica](../../../sources/pages/page-346.png) | independent_pass |
| 130 | `zadatak-4-347-6` / zadatak 6 | 347 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-347-6.png) | [stranica](../../../sources/pages/page-347.png) | independent_pass |
| 131 | `zadatak-4-347-7` / zadatak 7 | 347 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-347-7.png) | [stranica](../../../sources/pages/page-347.png) | independent_pass |
| 132 | `zadatak-4-347-8` / zadatak 8 | 347 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-347-8.png) | [stranica](../../../sources/pages/page-347.png) | independent_pass |
| 133 | `zadatak-4-347-9` / zadatak 9 | 347 / 174 | [PNG](../../../images/04-neakordicki-b/zadatak-4-347-9.png) | [stranica](../../../sources/pages/page-347.png) | independent_pass |
| 134 | `zadatak-4-348-3-realizacija` / Realizacija zadatka 3 | 348 / 175 | [PNG](../../../images/04-neakordicki-b/zadatak-4-348-3-realizacija.png) | [stranica](../../../sources/pages/page-348.png) | independent_pass |

## Sedam izvorno ograničenih blokada

### primjer-4-108 — tiskana str. 334

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Rukopisni krugovi oko nota u oba sustava prepliću se s crtovljem; potpun primjer nije moguće odvojiti jednim sigurnim pravokutnikom prema neovisnom pregledu. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: Number, C-dur title and both scale staves are complete and outer edges are clean, but pencil circles around notes in both systems remain inside the image. They cross/interleave the staff area and are handwriting, not dust or printed notation. No source-only rectangle can remove them while retaining the complete example; source hold, not permission to retouch.

### primjer-4-109 — tiskana str. 334

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Rukopisni lukovi oko i ispod nota prvoga sustava ostaju unutar notacije; njihovo uklanjanje pravokutnim rezom izgubilo bi pripadnu notaciju. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: Number, c-mol title and both staves are complete, but handwritten curved marks around/below first-system notes remain, including beneath the opening low note and near the later chromatic notes. Not dust or printed slurs. Removing them with one rectangle would lose notation; no safe proposed rectangle.

### zadatak-4-336-2 — tiskana str. 336

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Donji rub y=892 reže donju povisilicu/brojku 4 šifriranoga basa (x=657–698). Te se oznake dodiruju s lukom zadatka 3; proširenje unosi tuđi luk, a sužavanje gubi šifražu. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: Bottom y=892 cuts the lower figured-bass sharp/4 beneath exercise 2; connected ink reaches the last crop row at source x=657-698. Enlarged source shows these figures meet the following exercise 3 slur at the same vertical boundary. Expanding bottom admits that foreign slur; shrinking loses figures. Four-edge review finds no safe complete rectangular recrop from this source.

### zadatak-4-336-3 — tiskana str. 336

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Gornji rub y=894 reže početni dugi luk (x=442–1661). Najniže brojke zadatka 2 dodiruju/preklapaju luk oko x=650–700; proširenje unosi tuđe brojke, a sužavanje dodatno reže luk. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: Top y=894 cuts the opening long slur: connected slur ink reaches the first crop row over source x=442-1661. Exercise 2's lowest figures meet/overlap this slur around x=650-700. Moving top upward imports those unrelated figures; moving down clips more slur. Number 3 and four systems otherwise retained. No fully safe rectangle can separate this printed-source collision.

### primjer-4-113 — tiskana str. 337

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Rukopisna podcrta/strelica spušta se do prve zvjezdice, a ispod basa ostaju rukopisne harmonijske oznake. Samo podizanje donjega ruba ne bi uklonilo strelicu uz notaciju. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: 4.113, actual a)/b), both score asterisks and notation retained, but the top contains handwritten underlining/arrow descending to the first asterisk, and below the bass are handwritten harmonic marks. Enlarged source confirms meaningful pencil strokes, not dust. A tighter bottom alone would not fix the arrow touching the upper score area; no complete handwriting-free source rectangle certified.

### primjer-4-114 — tiskana str. 338

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Rukopisna rimska i brojčana analiza ispod lijevoga i srednjega dijela basa prepliće se s otisnutim donjim zvjezdicama i dopire do crtovlja; nije dio tiskanoga primjera. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: 4.114, a)/b), staves and printed score stars retained, but handwritten Roman-numeral/figured analysis appears below the left and middle bass measures. It vertically interleaves the printed lower stars and reaches the staff area; not printed figures or dust. No rectangular source crop can discard all handwriting and preserve all notation/stars.

### primjer-4-125 — tiskana str. 340

**PROVISIONAL / cleanup_required; nije odobreno; source_limited.** Gornji rub y=555 reže završnu zagradu atribucije (počinje na y=553), a donji y=988 reže zadnju nisku basovu notu i uključuje vrhove proznih naglasaka od y=987. Prethodni primjer završava na y=552; siguran potpun pravokutnik bez susjedne proze nije utvrđen. BLOKIRANO: source_limited; siguran zamjenski izrez nije certificiran. Bez retuširanja ili odobrenja; potrebni su ručni pregled izvora i nova neovisna provjera.

Izvorni neovisni razlog: Top y=555 clips the closing attribution parenthesis, which begins at source y=553; bottom y=988 cuts the final low bass note, whose ink continues through y=988. The bottom also includes tops of prose accents beginning at y=987 (e.g. x=604), not dust. Above, 4.124's staccato ends at y=552. No single complete rectangular crop can include the low note while excluding the earlier-starting prose accents across its required width; no safe proposed rectangle.

## Predaja

Četiri izlazne datoteke navedene su gore; slike nisu izvlačene nanovo. Svi glazbeni primjeri, zadaci i realizacije s pojedinačnim tiskanim/PDF stranicama te ishodima nalaze se u punoj mapi. Nema nečitljivoga proznog teksta prema dostavljenim tekstnim pregledima. Nejasnoće/nepotpunosti odnose se na sedam navedenih izreznih blokada i dokumentiranu tiskanu diskrepanciju 4.139.d—f / a–e.

**Djelomična integracija spremna je za predaju, ne za konačno dovršenje M09.** Sedam novih neodobrenih slika zahtijeva rješavanje izvornoga ograničenja i novu neovisnu provjeru; ukupno u poglavlju ostaju 23 cleanup_required zapisa. Nema ljudskog odobrenja. Završetak ovoga zadatka: tiskana str. **348**.

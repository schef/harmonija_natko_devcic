# M09 — integracija samo tiskanih str. 309–328

## Ishod i granice

- Tiskane str. **309–328**, PDF str. **155–165**, indeksiranje od 1 prema [sources/index.json](../../../sources/index.json).
- [Poglavlje](../../../chapters/04-neakordicki-b.md) stvoreno; 68 točno uparenih mjesta: **52 independent_pass**, **16 cleanup_required**. Svaki pojedinačni ishod nalazi se u donjoj mapi.
- [Pregled slika](../../../images/04-neakordicki-b/REVIEW.md); [integrirani manifest](images-integrated.json), 68 zapisa.
- Nisu mijenjane slike, sirovi manifesti, izvorni prijepisi ni globalni tracker. Bez delegacije, ljudskog odobrenja, commita ili pusha; M09 nije označen dovršenim.
- Stranice 329–348 imaju provjeren tekst u zasebnim prijepisima, ali nisu slikovno integrirane ovim poslom. Integracija ovdje staje nakon 4.103 na str. 328; nije uključena proza ni slikovno mjesto sa str. 329.

## Dokazi o tekstu i provjeri slika

- [text-309-312.md](text-309-312.md) i [text-309-312-review.json](text-309-312-review.json).
- [text-313-316.md](text-313-316.md) i [text-313-316-review.json](text-313-316-review.json).
- [text-317-318.md](text-317-318.md) i [text-317-318-review.json](text-317-318-review.json).
- [text-319-333.md](text-319-333.md) i [text-319-333-review.json](text-319-333-review.json) — upotrijebljene samo str. 319–328.

[Izvorni slikovni manifest](images-309-328.json); [neovisni vizualni pregled](visual-review-309-328.json). Polja `verified` i `visually_verified` prihvaćena su kao potvrde pregleda pojedinih stranica; polje za svaku od 20 dodijeljenih stranica provjereno. Integracija ne ponavlja samoodobravanje slikovnih izreza.

## Validacija

- 68/68 mjesta spareno po točnom identitetu, izvornom nazivu i tiskanoj stranici; uspoređeni i popisi `visuals` / `visual_ids` iz tekstnih pregleda. Vježbe istih brojeva na različitim stranicama nisu zamijenjene.
- 68/68 izreza odgovara izvornim pikselima unutar `rect`; svi pravokutnici unutar izvornika. Podrijetlo nije vizualno odobrenje.
- 68/68 tiskana/PDF stranica i putanja izvornika odgovara indeksu. Izvorne oznake svih stranica 309–328 prisutne su, uključujući inline oznake.
- Točan povratni tekstualni test: uklanjanjem dodanih slikovnih blokova i korijenskog naslova/napomene dobiva se neizmijenjen spoj svih dodijeljenih prijepisa, s posljednjim odsječenim prije oznake stranice 329. Sva proza, naslovi, reference, bilješke i komentari nastavaka ostaju očuvani.
- Prijelaz 317/318 ostaje inline unutar spojenog odlomka; nije korišteno dijeljenje samo po samostalnim redcima oznaka stranica. Prijelaz os-/tvariti 327/328 očuvan unutar riječi; Na-/protiv 322/323 dokumentiran izvornim komentarom.
- Sačuvane tiskane nepravilnosti: `4.54.e i d` (309), `4.54 a i c` bez dodane točke (310). Bez uredničkog popravljanja.
- 4.98 a–c (326) i 4.98 d–e (327) imaju odvojena mjesta i razjašnjene natpise; izvorni identiteti `primjer-4-98-a` i `primjer-4-98-b` sačuvani.
- 52 ugrađene slike; 16 neodobrenih PROVISIONAL poveznica s pojedinačnim razlozima. Svih 68 ima alt/opis, natpis, tiskanu stranicu i MuseScore placeholder.
- Jedina otisnuta prozna fusnota u ovom rasponu, `\* Ton »d« je anticipacija.`, sačuvana je točno jednom neposredno uz blok 4.67. Izrez 4.67 ostaje blokiran zbog preklapanja raspona fusnote i fermate/zvjezdice; nije odobrena proza u slici niti oštećena notacija.
- Sve lokalne Markdown poveznice u tri izlazna Markdown dokumenta razriješene su relativno prema svakoj datoteci. Poglavlje koristi `../images/…`, a ne putanje relativne korijenu. Putanje u JSON manifestu ostaju relativne korijenu repozitorija.

## Potpuna mapa mjesta i pojedinačni ishodi

| # | Identitet / izvorno mjesto | Tiskana / PDF str. | Izrez | Izvornik | Ishod |
| --- | --- | --- | --- | --- | --- |
| 1 | `primjer-4-53` / 4.53 | 309 / 155 | [PNG](../../../images/04-neakordicki-b/primjer-4-53.png) | [stranica](../../../sources/pages/page-309.png) | cleanup_required |
| 2 | `primjer-4-54` / 4.54 | 309 / 155 | [PNG](../../../images/04-neakordicki-b/primjer-4-54.png) | [stranica](../../../sources/pages/page-309.png) | cleanup_required |
| 3 | `primjer-4-55` / 4.55 | 310 / 156 | [PNG](../../../images/04-neakordicki-b/primjer-4-55.png) | [stranica](../../../sources/pages/page-310.png) | cleanup_required |
| 4 | `primjer-4-56` / 4.56 | 310 / 156 | [PNG](../../../images/04-neakordicki-b/primjer-4-56.png) | [stranica](../../../sources/pages/page-310.png) | cleanup_required |
| 5 | `primjer-4-57` / 4.57 | 310 / 156 | [PNG](../../../images/04-neakordicki-b/primjer-4-57.png) | [stranica](../../../sources/pages/page-310.png) | cleanup_required |
| 6 | `primjer-4-58` / 4.58 | 310 / 156 | [PNG](../../../images/04-neakordicki-b/primjer-4-58.png) | [stranica](../../../sources/pages/page-310.png) | cleanup_required |
| 7 | `primjer-4-59` / 4.59 | 311 / 156 | [PNG](../../../images/04-neakordicki-b/primjer-4-59.png) | [stranica](../../../sources/pages/page-311.png) | independent_pass |
| 8 | `primjer-4-60` / 4.60 | 311 / 156 | [PNG](../../../images/04-neakordicki-b/primjer-4-60.png) | [stranica](../../../sources/pages/page-311.png) | cleanup_required |
| 9 | `primjer-4-61` / 4.61 | 312 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-61.png) | [stranica](../../../sources/pages/page-312.png) | cleanup_required |
| 10 | `primjer-4-62` / 4.62 | 312 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-62.png) | [stranica](../../../sources/pages/page-312.png) | cleanup_required |
| 11 | `primjer-4-63` / 4.63 | 312 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-63.png) | [stranica](../../../sources/pages/page-312.png) | cleanup_required |
| 12 | `primjer-4-64` / 4.64 | 312 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-64.png) | [stranica](../../../sources/pages/page-312.png) | cleanup_required |
| 13 | `primjer-4-65` / 4.65 | 313 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-65.png) | [stranica](../../../sources/pages/page-313.png) | cleanup_required |
| 14 | `primjer-4-66` / 4.66 | 313 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-66.png) | [stranica](../../../sources/pages/page-313.png) | cleanup_required |
| 15 | `primjer-4-67` / 4.67 | 313 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-67.png) | [stranica](../../../sources/pages/page-313.png) | cleanup_required |
| 16 | `primjer-4-68` / 4.68 | 313 / 157 | [PNG](../../../images/04-neakordicki-b/primjer-4-68.png) | [stranica](../../../sources/pages/page-313.png) | cleanup_required |
| 17 | `primjer-4-69` / 4.69 | 314 / 158 | [PNG](../../../images/04-neakordicki-b/primjer-4-69.png) | [stranica](../../../sources/pages/page-314.png) | independent_pass |
| 18 | `primjer-4-70` / 4.70 | 314 / 158 | [PNG](../../../images/04-neakordicki-b/primjer-4-70.png) | [stranica](../../../sources/pages/page-314.png) | independent_pass |
| 19 | `primjer-4-71` / 4.71 | 314 / 158 | [PNG](../../../images/04-neakordicki-b/primjer-4-71.png) | [stranica](../../../sources/pages/page-314.png) | cleanup_required |
| 20 | `zadatak-4-315-1` / zadatak 1 | 315 / 158 | [PNG](../../../images/04-neakordicki-b/zadatak-4-315-1.png) | [stranica](../../../sources/pages/page-315.png) | independent_pass |
| 21 | `zadatak-4-315-2` / zadatak 2 | 315 / 158 | [PNG](../../../images/04-neakordicki-b/zadatak-4-315-2.png) | [stranica](../../../sources/pages/page-315.png) | independent_pass |
| 22 | `zadatak-4-315-3` / zadatak 3 | 315 / 158 | [PNG](../../../images/04-neakordicki-b/zadatak-4-315-3.png) | [stranica](../../../sources/pages/page-315.png) | independent_pass |
| 23 | `zadatak-4-315-4` / zadatak 4 | 315 / 158 | [PNG](../../../images/04-neakordicki-b/zadatak-4-315-4.png) | [stranica](../../../sources/pages/page-315.png) | independent_pass |
| 24 | `zadatak-4-315-5` / zadatak 5 | 315 / 158 | [PNG](../../../images/04-neakordicki-b/zadatak-4-315-5.png) | [stranica](../../../sources/pages/page-315.png) | independent_pass |
| 25 | `zadatak-4-316-6` / zadatak 6 | 316 / 159 | [PNG](../../../images/04-neakordicki-b/zadatak-4-316-6.png) | [stranica](../../../sources/pages/page-316.png) | independent_pass |
| 26 | `zadatak-4-316-7` / zadatak 7 | 316 / 159 | [PNG](../../../images/04-neakordicki-b/zadatak-4-316-7.png) | [stranica](../../../sources/pages/page-316.png) | independent_pass |
| 27 | `zadatak-4-316-8` / zadatak 8 | 316 / 159 | [PNG](../../../images/04-neakordicki-b/zadatak-4-316-8.png) | [stranica](../../../sources/pages/page-316.png) | independent_pass |
| 28 | `zadatak-4-317-9` / zadatak 9 | 317 / 159 | [PNG](../../../images/04-neakordicki-b/zadatak-4-317-9.png) | [stranica](../../../sources/pages/page-317.png) | independent_pass |
| 29 | `zadatak-4-317-3-realizacija` / Realizacija zadatka 3 | 317 / 159 | [PNG](../../../images/04-neakordicki-b/zadatak-4-317-3-realizacija.png) | [stranica](../../../sources/pages/page-317.png) | independent_pass |
| 30 | `primjer-4-72` / 4.72 | 318 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-72.png) | [stranica](../../../sources/pages/page-318.png) | independent_pass |
| 31 | `primjer-4-73` / 4.73 | 318 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-73.png) | [stranica](../../../sources/pages/page-318.png) | independent_pass |
| 32 | `primjer-4-74` / 4.74 | 318 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-74.png) | [stranica](../../../sources/pages/page-318.png) | independent_pass |
| 33 | `primjer-4-75` / 4.75 | 318 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-75.png) | [stranica](../../../sources/pages/page-318.png) | independent_pass |
| 34 | `primjer-4-76` / 4.76 | 319 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-76.png) | [stranica](../../../sources/pages/page-319.png) | independent_pass |
| 35 | `primjer-4-77` / 4.77 | 319 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-77.png) | [stranica](../../../sources/pages/page-319.png) | independent_pass |
| 36 | `primjer-4-78` / 4.78 | 319 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-78.png) | [stranica](../../../sources/pages/page-319.png) | independent_pass |
| 37 | `primjer-4-79` / 4.79 | 319 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-79.png) | [stranica](../../../sources/pages/page-319.png) | independent_pass |
| 38 | `primjer-4-80` / 4.80 | 319 / 160 | [PNG](../../../images/04-neakordicki-b/primjer-4-80.png) | [stranica](../../../sources/pages/page-319.png) | independent_pass |
| 39 | `primjer-4-81` / 4.81 | 320 / 161 | [PNG](../../../images/04-neakordicki-b/primjer-4-81.png) | [stranica](../../../sources/pages/page-320.png) | independent_pass |
| 40 | `primjer-4-82` / 4.82 | 320 / 161 | [PNG](../../../images/04-neakordicki-b/primjer-4-82.png) | [stranica](../../../sources/pages/page-320.png) | independent_pass |
| 41 | `zadatak-4-321-1` / zadatak 1 | 321 / 161 | [PNG](../../../images/04-neakordicki-b/zadatak-4-321-1.png) | [stranica](../../../sources/pages/page-321.png) | independent_pass |
| 42 | `zadatak-4-321-2` / zadatak 2 | 321 / 161 | [PNG](../../../images/04-neakordicki-b/zadatak-4-321-2.png) | [stranica](../../../sources/pages/page-321.png) | independent_pass |
| 43 | `zadatak-4-321-3` / zadatak 3 | 321 / 161 | [PNG](../../../images/04-neakordicki-b/zadatak-4-321-3.png) | [stranica](../../../sources/pages/page-321.png) | independent_pass |
| 44 | `zadatak-4-321-4` / zadatak 4 | 321 / 161 | [PNG](../../../images/04-neakordicki-b/zadatak-4-321-4.png) | [stranica](../../../sources/pages/page-321.png) | independent_pass |
| 45 | `zadatak-4-321-5` / zadatak 5 | 321 / 161 | [PNG](../../../images/04-neakordicki-b/zadatak-4-321-5.png) | [stranica](../../../sources/pages/page-321.png) | independent_pass |
| 46 | `zadatak-4-322-4-realizacija` / Realizacija zadatka 4 | 322 / 162 | [PNG](../../../images/04-neakordicki-b/zadatak-4-322-4-realizacija.png) | [stranica](../../../sources/pages/page-322.png) | independent_pass |
| 47 | `primjer-4-83` / 4.83 | 322 / 162 | [PNG](../../../images/04-neakordicki-b/primjer-4-83.png) | [stranica](../../../sources/pages/page-322.png) | independent_pass |
| 48 | `primjer-4-84` / 4.84 | 322 / 162 | [PNG](../../../images/04-neakordicki-b/primjer-4-84.png) | [stranica](../../../sources/pages/page-322.png) | independent_pass |
| 49 | `primjer-4-85` / 4.85 | 323 / 162 | [PNG](../../../images/04-neakordicki-b/primjer-4-85.png) | [stranica](../../../sources/pages/page-323.png) | independent_pass |
| 50 | `primjer-4-86` / 4.86 | 323 / 162 | [PNG](../../../images/04-neakordicki-b/primjer-4-86.png) | [stranica](../../../sources/pages/page-323.png) | independent_pass |
| 51 | `primjer-4-87` / 4.87 | 323 / 162 | [PNG](../../../images/04-neakordicki-b/primjer-4-87.png) | [stranica](../../../sources/pages/page-323.png) | independent_pass |
| 52 | `primjer-4-88` / 4.88 | 323 / 162 | [PNG](../../../images/04-neakordicki-b/primjer-4-88.png) | [stranica](../../../sources/pages/page-323.png) | independent_pass |
| 53 | `primjer-4-89` / 4.89 | 324 / 163 | [PNG](../../../images/04-neakordicki-b/primjer-4-89.png) | [stranica](../../../sources/pages/page-324.png) | independent_pass |
| 54 | `primjer-4-90` / 4.90 | 324 / 163 | [PNG](../../../images/04-neakordicki-b/primjer-4-90.png) | [stranica](../../../sources/pages/page-324.png) | independent_pass |
| 55 | `primjer-4-91` / 4.91 | 324 / 163 | [PNG](../../../images/04-neakordicki-b/primjer-4-91.png) | [stranica](../../../sources/pages/page-324.png) | independent_pass |
| 56 | `primjer-4-92` / 4.92 | 325 / 163 | [PNG](../../../images/04-neakordicki-b/primjer-4-92.png) | [stranica](../../../sources/pages/page-325.png) | independent_pass |
| 57 | `primjer-4-93` / 4.93 | 325 / 163 | [PNG](../../../images/04-neakordicki-b/primjer-4-93.png) | [stranica](../../../sources/pages/page-325.png) | independent_pass |
| 58 | `primjer-4-94` / 4.94 | 325 / 163 | [PNG](../../../images/04-neakordicki-b/primjer-4-94.png) | [stranica](../../../sources/pages/page-325.png) | independent_pass |
| 59 | `primjer-4-95` / 4.95 | 326 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-95.png) | [stranica](../../../sources/pages/page-326.png) | independent_pass |
| 60 | `primjer-4-96` / 4.96 | 326 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-96.png) | [stranica](../../../sources/pages/page-326.png) | independent_pass |
| 61 | `primjer-4-97` / 4.97 | 326 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-97.png) | [stranica](../../../sources/pages/page-326.png) | independent_pass |
| 62 | `primjer-4-98-a` / 4.98 a–c | 326 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-98-a.png) | [stranica](../../../sources/pages/page-326.png) | independent_pass |
| 63 | `primjer-4-98-b` / 4.98 d–e | 327 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-98-b.png) | [stranica](../../../sources/pages/page-327.png) | independent_pass |
| 64 | `primjer-4-99` / 4.99 | 327 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-99.png) | [stranica](../../../sources/pages/page-327.png) | independent_pass |
| 65 | `primjer-4-100` / 4.100 | 327 / 164 | [PNG](../../../images/04-neakordicki-b/primjer-4-100.png) | [stranica](../../../sources/pages/page-327.png) | independent_pass |
| 66 | `primjer-4-101` / 4.101 | 328 / 165 | [PNG](../../../images/04-neakordicki-b/primjer-4-101.png) | [stranica](../../../sources/pages/page-328.png) | independent_pass |
| 67 | `primjer-4-102` / 4.102 | 328 / 165 | [PNG](../../../images/04-neakordicki-b/primjer-4-102.png) | [stranica](../../../sources/pages/page-328.png) | independent_pass |
| 68 | `primjer-4-103` / 4.103 | 328 / 165 | [PNG](../../../images/04-neakordicki-b/primjer-4-103.png) | [stranica](../../../sources/pages/page-328.png) | independent_pass |

## Blokade i ručni pregled

### primjer-4-53 — tiskana str. 309

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisna slova i harmonijska analiza iznad, unutar i ispod notnoga primjera. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-54 — tiskana str. 309

**cleanup_required; PROVISIONAL; nije odobreno.** Olovkom dopisana akordička slova iznad varijanti i strani trag uz gornji rub. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-55 — tiskana str. 310

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisni krugovi oko notacije; donji rub zahvaća olovku uz sljedeći primjer. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-56 — tiskana str. 310

**cleanup_required; PROVISIONAL; nije odobreno.** Olovkom nacrtan krug oko gornjih nota i zvjezdice u varijanti b. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-57 — tiskana str. 310

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisni krugovi oko oznaka NE, uključujući tragove uz gornji rub. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-58 — tiskana str. 310

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisni krugovi oko NE i odrezani strani tragovi olovke uz gornji rub. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-60 — tiskana str. 311

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisni krugovi, strelice i analiza unutar notacije te strani tragovi uz gornji/desni rub. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-61 — tiskana str. 312

**cleanup_required; PROVISIONAL; nije odobreno.** Blijedi rukopisni obris oko DA u varijanti c i potez koji dodiruje gornji rub. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-62 — tiskana str. 312

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisni kružni luk ispod početnoga gornjeg akorda varijante b. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-63 — tiskana str. 312

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisni krugovi oko NE/nota i zakrivljeni trag iznad b, sve do gornjega ruba. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-64 — tiskana str. 312

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisne brojke uz gornje note b i krugovi oko basovih nota. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-65 — tiskana str. 313

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisna harmonijska analiza i krugovi u basu/ispod njega; donji rub reže rukopisno T. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-66 — tiskana str. 313

**cleanup_required; PROVISIONAL; nije odobreno.** Rukopisna analiza i krugovi u basu/ispod njega te strani trag prethodnoga primjera uz gornji rub. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-67 — tiskana str. 313

**cleanup_required; PROVISIONAL; nije odobreno.** BLOKIRANO: otisnuta fusnota i potpuna donja fermata/zvjezdica dijele vertikalni raspon; uklanjanje proze donjim rezom odrezalo bi notaciju. Prisutan je i rukopis. Ne odobravati zadržanu prozu niti odrezati fermatu ili zvjezdicu. Siguran pravokutni izrez samo iz izvornika nije utvrđen; potrebni su ručni pregled i nova neovisna provjera.

### primjer-4-68 — tiskana str. 313

**cleanup_required; PROVISIONAL; nije odobreno.** Olovkom nacrtana petlja iznad drugoga takta i strani podcrtani fragment uz gornji lijevi rub; vrlo tijesan razmak. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

### primjer-4-71 — tiskana str. 314

**cleanup_required; PROVISIONAL; nije odobreno.** Opsežna rukopisna analiza ispod basa, odrezana donjim rubom; neki tragovi dijele vertikalni raspon s donjom fermatom. Rukopis zahtijeva ručni pregled; siguran pravokutni zamjenski izrez nije certificiran. Mogućnost novoga izreza nije ovime isključena.

Sirovi neovisni razlozi i `source_limited` sačuvani su u manifestu radi sljedivosti, ali nisu pretvoreni u tvrdnju da je novi izrez nemoguć. Sigurni zamjenski pravokutnici nisu certificirani. Nema nečitljive ili nedovršene proze prema dostavljenim tekstnim pregledima. Otvorena pitanja tiču se slika, osobito rukopisa i bloka 4.67.

## Predaja

**Djelomična integracija spremna za daljnji rad, ne za konačno dovršenje.** Svih 68 mjesta evidentirano; 52 neovisno prolaze, 16 zahtijeva čišćenje/ručni pregled i ponovnu neovisnu provjeru. Prije završetka M09 potrebna je i slikovna integracija 329–348 izvan ovoga zadatka. Nije dodano ljudsko odobrenje i milestone nije zatvoren.

# Integracija — tiskane str. 156–174 / PDF 79–88

**PROVISIONAL: dodano 54 tekstna mjesta i 55 slikovnih dijelova; 42 pass, 13 cleanup required. Ukupno u konačnom manifestu: 128 dijelova, 107 pass i 21 cleanup required. Nije spremno za konačno prihvaćanje niti dovršetak miljokaza.**

## Opseg i očuvanje

Jedan integracijski radnik, bez delegiranja, modelskih podprocesa/API poziva ili GUI-ja. Dodane su samo tiskane str. 156–174, PDF 79–88 (od 1), uz puni provjereni tekst. Sačuvani su svi odlomci, naslovi, upute, fusnota 4 i grčki tekst, latinski pjevani tekstovi i zvjezdaste napomene, oznake izvora i međustraničnih nastavaka. Jedina normalizacija teksta jest razmak u brojčanim naslovima (2.9.6, 2.9.7 i 2.10); ne mijenjaju se razmaci unutar poziva u prozi. Str. 174 izričito je prazna, bez izmišljenog sadržaja. Nema prijavljenog nečitljivog ili dvosmislenog tiskanog teksta; rukopisne bilješke nisu tiskani sadržaj.

Prethodni sadržaj poglavlja kroz str. 155 sačuvan je točno, bajt po bajt, uključujući njegovu povijesnu napomenu o tadašnjem kraju integracije; dodano objašnjenje označuje nastavak, bez izmjene napomene. Prethodni REVIEW također je sačuvan kao točan bajtni prefiks. Prethodnih 73 zapisa konačnog manifesta ostalo je nepromijenjeno po vrijednostima i redoslijedu; dodano je 55 zapisa.

Nije mijenjan sirovi/ispravljeni ulazni manifest, slika, zajednički tracker ni MILESTONES.md; nema commit/push, ljudskog odobrenja, novog samoodobravanja izreza ili dovršavanja miljokaza.

## Ulazi

- [review-candidates/book/M04/text-156-174.md](review-candidates/book/M04/text-156-174.md)
- [review-candidates/book/M04/text-156-174-review.json](review-candidates/book/M04/text-156-174-review.json)
- [review-candidates/book/M04/images-corrected-156-174.json](review-candidates/book/M04/images-corrected-156-174.json)
- [review-candidates/book/M04/visual-review-156-174.json](review-candidates/book/M04/visual-review-156-174.json)
- [review-candidates/book/M04/recrop-review-156-174.json](review-candidates/book/M04/recrop-review-156-174.json)
- [sources/index.json](sources/index.json)

## Promijenjene datoteke — samo četiri

- [chapters/02-dijatonika-c.md](chapters/02-dijatonika-c.md)
- [images/02-dijatonika-c/REVIEW.md](images/02-dijatonika-c/REVIEW.md)
- [review-candidates/book/M04/images-integrated.json](review-candidates/book/M04/images-integrated.json)
- [review-candidates/book/M04/INTEGRATION-156-174.md](review-candidates/book/M04/INTEGRATION-156-174.md)

## Provjere

- 54 jedinstvena tekstna mjesta odgovaraju 55 jedinstvenih dijelova i putanja; 2.409 ima dva dijela u jednom mjestu. Zadatak 15 ima zasebna mjesta na str. 161 i 162. Svi dijelovi raspoređeni su točno jednom.
- Prvi neovisni pregled jest JSON objekt s poljem `reviews`: 41 PASS, 13 izvorno blokiranih RECROP_REQUIRED i jedan popravljiv RECROP_REQUIRED. Zasebni pregled zamjenskog zadatka 13 donosi još jedan PASS; korišten je isključivo prihvaćeni zamjenski izrez `images/02-dijatonika-c/recrops/zadatak-2-9-6-13.png`.
- Ugrađene su točno 42 odobrene slike, a 13 blokiranih izreza samo je povezano uz PROVISIONAL — cleanup required. Svih 55 dijelova ima potpis, tiskanu i PDF stranicu te MuseScore rezervirano mjesto. Prihvaćena varijanta 2.409.b ne odobrava blokiranu 2.409.a.
- Svaki izrez uspoređen je s izvornim pravokutnikom: jednaka veličina, način boje i svaki piksel. Svih 19 izvornih stranica ponovno je uspoređeno s odgovarajućim polovicama svježih PDF rendera 79–88 pri 300 dpi u memoriji: svi su identični. Nisu pisane ili mijenjane slike.
- Preslikavanje svih 19 tiskanih stranica na PDF, izvorni PNG, lijevu/desnu polovicu i pravokutnik provjereno je prema sources/index.json. Novi metapodaci koriste isključivo PDF stranice od 1.
- Uklanjanjem samo dodanih slikovnih blokova dobiven je točan provjereni ulaz, uz jedinu dopuštenu normalizaciju razmaka naslova. Sve oznake izvora, nastavci, fusnota i pjevani tekstovi ostali su sačuvani.
- Sve Markdown poveznice u cijelom poglavlju, REVIEW-u i ovom izvještaju te sve putanje konačnih zapisa provjerene su prema korijenu repozitorija. U integriranim izlazima nema apsolutnih repozitorijskih putanja. SHA-256 otisci novih izreza i izvora zapisani su u konačnim zapisima; ulazne datoteke i slike ostale su nepromijenjene.
- Završna provjera obuhvatila je 381 pojavljivanje Markdown poveznica u ta tri dokumenta; sve se razrješavaju. Prethodni prefiksi poglavlja i REVIEW-a te prethodna 73 zapisa manifesta ponovno su provjereni nakon pisanja.

### Otisci očuvanih prefiksa

- Poglavlje: 44295 bajtova, SHA-256 `c8ed223be4fc8b321574ad6c781f23b7fe30d1210c6d6c8afc93d7e9529e7baa`.
- REVIEW: 20334 bajtova, SHA-256 `f4c48f30a7f34dc848401a4661cd3a02fc0c089a25bdb3263e7ec8d52fa7c50b`.

## Izvori — tiskana stranica i PDF stranica od 1

| Tiskana str. | PDF str. | Polovica | Izvorni PNG | Pravokutnik PDF rendera [lijevo, gore, desno, dolje) |
| --- | --- | --- | --- | --- |
| 156 | 79 | left | [sources/pages/page-156.png](sources/pages/page-156.png) | `[0, 0, 1878, 2575]` |
| 157 | 79 | right | [sources/pages/page-157.png](sources/pages/page-157.png) | `[1878, 0, 3756, 2575]` |
| 158 | 80 | left | [sources/pages/page-158.png](sources/pages/page-158.png) | `[0, 0, 1885, 2598]` |
| 159 | 80 | right | [sources/pages/page-159.png](sources/pages/page-159.png) | `[1885, 0, 3771, 2598]` |
| 160 | 81 | left | [sources/pages/page-160.png](sources/pages/page-160.png) | `[0, 0, 1885, 2598]` |
| 161 | 81 | right | [sources/pages/page-161.png](sources/pages/page-161.png) | `[1885, 0, 3771, 2598]` |
| 162 | 82 | left | [sources/pages/page-162.png](sources/pages/page-162.png) | `[0, 0, 1883, 2589]` |
| 163 | 82 | right | [sources/pages/page-163.png](sources/pages/page-163.png) | `[1883, 0, 3766, 2589]` |
| 164 | 83 | left | [sources/pages/page-164.png](sources/pages/page-164.png) | `[0, 0, 1885, 2598]` |
| 165 | 83 | right | [sources/pages/page-165.png](sources/pages/page-165.png) | `[1885, 0, 3771, 2598]` |
| 166 | 84 | left | [sources/pages/page-166.png](sources/pages/page-166.png) | `[0, 0, 1880, 2583]` |
| 167 | 84 | right | [sources/pages/page-167.png](sources/pages/page-167.png) | `[1880, 0, 3761, 2583]` |
| 168 | 85 | left | [sources/pages/page-168.png](sources/pages/page-168.png) | `[0, 0, 1880, 2583]` |
| 169 | 85 | right | [sources/pages/page-169.png](sources/pages/page-169.png) | `[1880, 0, 3761, 2583]` |
| 170 | 86 | left | [sources/pages/page-170.png](sources/pages/page-170.png) | `[0, 0, 1880, 2583]` |
| 171 | 86 | right | [sources/pages/page-171.png](sources/pages/page-171.png) | `[1880, 0, 3761, 2583]` |
| 172 | 87 | left | [sources/pages/page-172.png](sources/pages/page-172.png) | `[0, 0, 1883, 2589]` |
| 173 | 87 | right | [sources/pages/page-173.png](sources/pages/page-173.png) | `[1883, 0, 3766, 2589]` |
| 174 | 88 | left | [sources/pages/page-174.png](sources/pages/page-174.png) | `[0, 0, 1883, 2589]` |

## Cjelovita mapa svih 54 tekstna mjesta

Mjesta su navedena lokalno (1–54) i globalno u manifestu (73–126). Svaka poveznica koristi punu putanju relativnu korijenu repozitorija.

| Lokalno / globalno mjesto | Točna oznaka provjerenog teksta | Tiskana str. | PDF str. | Svi dijelovi i odluke |
| --- | --- | --- | --- | --- |
| 1 / 73 | primjer 2.373 | 156 | 79 | dio 1/1: [images/02-dijatonika-c/primjer-2-373.png](images/02-dijatonika-c/primjer-2-373.png) — pass |
| 2 / 74 | primjer 2.374 a–b | 157 | 79 | dio 1/1: [images/02-dijatonika-c/primjer-2-374.png](images/02-dijatonika-c/primjer-2-374.png) — pass |
| 3 / 75 | primjer 2.375 | 157 | 79 | dio 1/1: [images/02-dijatonika-c/primjer-2-375.png](images/02-dijatonika-c/primjer-2-375.png) — pass |
| 4 / 76 | primjer 2.376 (Haydn: Simfonija br. 94, u G-duru) | 157 | 79 | dio 1/1: [images/02-dijatonika-c/primjer-2-376.png](images/02-dijatonika-c/primjer-2-376.png) — pass |
| 5 / 77 | primjer 2.377 (Beethoven: Koncert za klavir i orkestar u G-duru, op. 58) | 157 | 79 | dio 1/1: [images/02-dijatonika-c/primjer-2-377.png](images/02-dijatonika-c/primjer-2-377.png) — pass |
| 6 / 78 | primjer 2.378 | 158 | 80 | dio 1/1: [images/02-dijatonika-c/primjer-2-378.png](images/02-dijatonika-c/primjer-2-378.png) — **PROVISIONAL — cleanup required** |
| 7 / 79 | primjer 2.379 | 158 | 80 | dio 1/1: [images/02-dijatonika-c/primjer-2-379.png](images/02-dijatonika-c/primjer-2-379.png) — **PROVISIONAL — cleanup required** |
| 8 / 80 | primjer 2.380 a–c | 159 | 80 | dio 1/1: [images/02-dijatonika-c/primjer-2-380.png](images/02-dijatonika-c/primjer-2-380.png) — pass |
| 9 / 81 | zadatak 2 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-2.png](images/02-dijatonika-c/zadatak-2-9-6-2.png) — pass |
| 10 / 82 | zadatak 3 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-3.png](images/02-dijatonika-c/zadatak-2-9-6-3.png) — pass |
| 11 / 83 | zadatak 4 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-4.png](images/02-dijatonika-c/zadatak-2-9-6-4.png) — pass |
| 12 / 84 | zadatak 5 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-5.png](images/02-dijatonika-c/zadatak-2-9-6-5.png) — pass |
| 13 / 85 | zadatak 6 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-6.png](images/02-dijatonika-c/zadatak-2-9-6-6.png) — pass |
| 14 / 86 | zadatak 7 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-7.png](images/02-dijatonika-c/zadatak-2-9-6-7.png) — pass |
| 15 / 87 | zadatak 8 | 160 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-8.png](images/02-dijatonika-c/zadatak-2-9-6-8.png) — pass |
| 16 / 88 | zadatak 9 | 161 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-9.png](images/02-dijatonika-c/zadatak-2-9-6-9.png) — pass |
| 17 / 89 | zadatak 10 | 161 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-10.png](images/02-dijatonika-c/zadatak-2-9-6-10.png) — pass |
| 18 / 90 | zadatak 11 | 161 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-11.png](images/02-dijatonika-c/zadatak-2-9-6-11.png) — pass |
| 19 / 91 | zadatak 12 | 161 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-12.png](images/02-dijatonika-c/zadatak-2-9-6-12.png) — pass |
| 20 / 92 | zadatak 13 (Allegretto) | 161 | 81 | dio 1/1: [images/02-dijatonika-c/recrops/zadatak-2-9-6-13.png](images/02-dijatonika-c/recrops/zadatak-2-9-6-13.png) — pass |
| 21 / 93 | zadatak 14 | 161 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-14.png](images/02-dijatonika-c/zadatak-2-9-6-14.png) — pass |
| 22 / 94 | zadatak 15, početak, nastavak na stranici 162 | 161 | 81 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-15-pocetak.png](images/02-dijatonika-c/zadatak-2-9-6-15-pocetak.png) — pass |
| 23 / 95 | zadatak 15, nastavak sa stranice 161 | 162 | 82 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-15-nastavak.png](images/02-dijatonika-c/zadatak-2-9-6-15-nastavak.png) — pass |
| 24 / 96 | zadatak 16 | 162 | 82 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-16.png](images/02-dijatonika-c/zadatak-2-9-6-16.png) — pass |
| 25 / 97 | zadatak 17 | 162 | 82 | dio 1/1: [images/02-dijatonika-c/zadatak-2-9-6-17.png](images/02-dijatonika-c/zadatak-2-9-6-17.png) — pass |
| 26 / 98 | primjer 2.381 a–b | 162 | 82 | dio 1/1: [images/02-dijatonika-c/primjer-2-381.png](images/02-dijatonika-c/primjer-2-381.png) — **PROVISIONAL — cleanup required** |
| 27 / 99 | primjer 2.382 a–b | 163 | 82 | dio 1/1: [images/02-dijatonika-c/primjer-2-382.png](images/02-dijatonika-c/primjer-2-382.png) — **PROVISIONAL — cleanup required** |
| 28 / 100 | primjer 2.383 a–b | 164 | 83 | dio 1/1: [images/02-dijatonika-c/primjer-2-383.png](images/02-dijatonika-c/primjer-2-383.png) — **PROVISIONAL — cleanup required** |
| 29 / 101 | primjer 2.384 | 164 | 83 | dio 1/1: [images/02-dijatonika-c/primjer-2-384.png](images/02-dijatonika-c/primjer-2-384.png) — **PROVISIONAL — cleanup required** |
| 30 / 102 | primjer 2.385 | 165 | 83 | dio 1/1: [images/02-dijatonika-c/primjer-2-385.png](images/02-dijatonika-c/primjer-2-385.png) — pass |
| 31 / 103 | primjer 2.386 a–f | 166 | 84 | dio 1/1: [images/02-dijatonika-c/primjer-2-386.png](images/02-dijatonika-c/primjer-2-386.png) — pass |
| 32 / 104 | primjer 2.387 | 167 | 84 | dio 1/1: [images/02-dijatonika-c/primjer-2-387.png](images/02-dijatonika-c/primjer-2-387.png) — pass |
| 33 / 105 | primjer 2.388 | 167 | 84 | dio 1/1: [images/02-dijatonika-c/primjer-2-388.png](images/02-dijatonika-c/primjer-2-388.png) — pass |
| 34 / 106 | primjer 2.389 | 167 | 84 | dio 1/1: [images/02-dijatonika-c/primjer-2-389.png](images/02-dijatonika-c/primjer-2-389.png) — pass |
| 35 / 107 | primjer 2.390 | 167 | 84 | dio 1/1: [images/02-dijatonika-c/primjer-2-390.png](images/02-dijatonika-c/primjer-2-390.png) — pass |
| 36 / 108 | primjer 2.391 (Dorski) | 168 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-391.png](images/02-dijatonika-c/primjer-2-391.png) — **PROVISIONAL — cleanup required** |
| 37 / 109 | primjer 2.392 (Frigijski) | 168 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-392.png](images/02-dijatonika-c/primjer-2-392.png) — **PROVISIONAL — cleanup required** |
| 38 / 110 | primjer 2.393 (Lidijski) | 168 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-393.png](images/02-dijatonika-c/primjer-2-393.png) — pass |
| 39 / 111 | primjer 2.394 (Miksolidijski) | 168 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-394.png](images/02-dijatonika-c/primjer-2-394.png) — pass |
| 40 / 112 | primjer 2.395 (Eolski) | 168 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-395.png](images/02-dijatonika-c/primjer-2-395.png) — pass |
| 41 / 113 | primjer 2.396 | 169 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-396.png](images/02-dijatonika-c/primjer-2-396.png) — pass |
| 42 / 114 | primjer 2.397 | 169 | 85 | dio 1/1: [images/02-dijatonika-c/primjer-2-397.png](images/02-dijatonika-c/primjer-2-397.png) — pass |
| 43 / 115 | primjer 2.398 | 170 | 86 | dio 1/1: [images/02-dijatonika-c/primjer-2-398.png](images/02-dijatonika-c/primjer-2-398.png) — pass |
| 44 / 116 | primjer 2.399 (Grieg: Lirski komadi VIII, 48) | 171 | 86 | dio 1/1: [images/02-dijatonika-c/primjer-2-399.png](images/02-dijatonika-c/primjer-2-399.png) — **PROVISIONAL — cleanup required** |
| 45 / 117 | primjer 2.400 (Grieg: Lirski komadi IX, 57) | 171 | 86 | dio 1/1: [images/02-dijatonika-c/primjer-2-400.png](images/02-dijatonika-c/primjer-2-400.png) — **PROVISIONAL — cleanup required** |
| 46 / 118 | primjer 2.401 (Skrjabin: Sonata za klavir br. 3) | 171 | 86 | dio 1/1: [images/02-dijatonika-c/primjer-2-401.png](images/02-dijatonika-c/primjer-2-401.png) — **PROVISIONAL — cleanup required** |
| 47 / 119 | primjer 2.402 (Chopin: Mazurka op. 68 br. 3) | 171 | 86 | dio 1/1: [images/02-dijatonika-c/primjer-2-402.png](images/02-dijatonika-c/primjer-2-402.png) — pass |
| 48 / 120 | primjer 2.403 (R. Strauss: Don Juan) | 172 | 87 | dio 1/1: [images/02-dijatonika-c/primjer-2-403.png](images/02-dijatonika-c/primjer-2-403.png) — pass |
| 49 / 121 | primjer 2.404 (Chopin: Mazurka op. 24 br. 2) | 172 | 87 | dio 1/1: [images/02-dijatonika-c/primjer-2-404.png](images/02-dijatonika-c/primjer-2-404.png) — pass |
| 50 / 122 | primjer 2.405 (Debussy: »Les sons et les parfums tournent dans l’air du soir«) | 172 | 87 | dio 1/1: [images/02-dijatonika-c/primjer-2-405.png](images/02-dijatonika-c/primjer-2-405.png) — pass |
| 51 / 123 | primjer 2.406 (Grieg: Koncert za klavir i orkestar u a-molu) | 172 | 87 | dio 1/1: [images/02-dijatonika-c/primjer-2-406.png](images/02-dijatonika-c/primjer-2-406.png) — pass |
| 52 / 124 | primjer 2.407 (Debussy: La Cathédrale engloutie) | 173 | 87 | dio 1/1: [images/02-dijatonika-c/primjer-2-407.png](images/02-dijatonika-c/primjer-2-407.png) — pass |
| 53 / 125 | primjer 2.408 (Debussy: La sérénade interrompue) | 173 | 87 | dio 1/1: [images/02-dijatonika-c/primjer-2-408.png](images/02-dijatonika-c/primjer-2-408.png) — **PROVISIONAL — cleanup required** |
| 54 / 126 | primjer 2.409 a–b (Dvořak: Simfonija br. 9 u e-molu) | 173 | 87 | dio 1/2: [images/02-dijatonika-c/primjer-2-409-a.png](images/02-dijatonika-c/primjer-2-409-a.png) — **PROVISIONAL — cleanup required**; dio 2/2: [images/02-dijatonika-c/primjer-2-409-b.png](images/02-dijatonika-c/primjer-2-409-b.png) — pass |

## Pojedinačne preostale blokade

| Dio | Tiskana / PDF str. | Razlog neovisnog pregleda |
| --- | --- | --- |
| [primjer-2-378](images/02-dijatonika-c/primjer-2-378.png) | 158 / 80 | Bottom edge includes upper border/letter fragments of following boxed C-fis-C title. Lowest bass stems of 378 extend into that same vertical band; a horizontal cut removing the title would clip intended notation. Not scan specks. |
| [primjer-2-379](images/02-dijatonika-c/primjer-2-379.png) | 158 / 80 | Top edge contains preceding 378 bass-stem tails to the right of the boxed C-fis-C title. Retaining the entire title and complete full-width notation precludes excluding those tails with one rectangle. |
| [primjer-2-381](images/02-dijatonika-c/primjer-2-381.png) | 162 / 82 | Handwritten chord names above a/b and handwritten text below a are inside the required example bounds, with partial handwriting at top. Printed bottom 5 is complete, confirmed against doubled source detail. No complete clean rectangle can remove the interleaved handwriting. |
| [primjer-2-382](images/02-dijatonika-c/primjer-2-382.png) | 163 / 82 | Extensive handwriting above/between both variants and around lower analyses, including circles/arrows and right-edge writing. These are identifiable pencil annotations, not specks; cannot exclude without losing printed content. |
| [primjer-2-383](images/02-dijatonika-c/primjer-2-383.png) | 164 / 83 | Handwritten chord names and analyses interleave a/b and extend into left/top/bottom margins. Printed variants are present but a clean complete rectangle is impossible on this source. |
| [primjer-2-384](images/02-dijatonika-c/primjer-2-384.png) | 164 / 83 | Pencil chord labels above staff and handwritten analyses below overlap the required Es-Fes title and printed lower analysis band. Not removable by a complete rectangular source crop. |
| [primjer-2-391](images/02-dijatonika-c/primjer-2-391.png) | 168 / 85 | Handwritten chord letters above and Roman numerals below the staff are interleaved with complete printed Dorski example; lower handwriting reaches bottom edge. These are annotations rather than scan specks. No clean complete rectangle. |
| [primjer-2-392](images/02-dijatonika-c/primjer-2-392.png) | 168 / 85 | Top edge contains a definite handwritten numeral/tail from preceding analysis, right of Frigijski title. Doubled source detail confirms its vertical band overlaps the title, so moving top down would sacrifice the title. Not an isolated speck. |
| [primjer-2-399](images/02-dijatonika-c/primjer-2-399.png) | 171 / 86 | Bottom edge contains stem/beam fragments of following 400 at left while lowest inverted fermata of 399 lies in the same vertical band at right. A full-content rectangle cannot remove the foreign fragments. |
| [primjer-2-400](images/02-dijatonika-c/primjer-2-400.png) | 171 / 86 | Top includes preceding 399 inverted fermata; bottom includes following Skrjabin attribution and slur. These overlap the vertical extent of 400 highest stems and lowest slur/fermata. No clean rectangle retains all intended notation. |
| [primjer-2-401](images/02-dijatonika-c/primjer-2-401.png) | 171 / 86 | Top edge includes 400 slur, stem and inverted-fermata fragments. Complete Skrjabin attribution shares their vertical band; removing them with a horizontal cut loses identifying text. |
| [primjer-2-408](images/02-dijatonika-c/primjer-2-408.png) | 173 / 87 | Bottom edge includes multiple highest-stem tips of following 409a. Complete 408 lowest staccato marks reach the same vertical band, preventing a clean full-width rectangle. Foreign tips are notation, not specks. |
| [primjer-2-409-a](images/02-dijatonika-c/primjer-2-409-a.png) | 173 / 87 | Top edge retains preceding 408 lowest staccato fragment above the Dvorak attribution. Highest 409a stems overlap this band; moving top down clips them. Number, a, attribution and lower notation otherwise present; no safe complete rectangle. |

Za svih 13 blokiranih dijelova neovisni pregled ne nalazi siguran potpuni pravokutnik: potrebni su dopušteno rješenje izvornog ograničenja i novi neovisni pregled. Nije dopušteno prešutno prihvatiti tuđe fragmente ili rukopis, odrezati pripadajuću notaciju, retuširati ili generirati marginu. Prethodnih 8 blokiranih dijelova ostaje nepromijenjeno; kumulativno ih je 21.

**Spremnost:** provjereni tekst prenesen je u cijelosti, a 42 neovisno odobrena dijela ugrađena su. Integracija ostaje PROVISIONAL i nije spremna za konačno prihvaćanje zbog 13 novih izvorno blokiranih dijelova. Rad staje na tiskanoj str. 174 / PDF str. 88; ništa nakon te granice nije preuzeto.

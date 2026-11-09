# Integracija — tiskane str. 137–155 / PDF 69–78

**Djelomična, PROVISIONAL integracija: 72 tekstna mjesta, 73 slikovna dijela, 65 pass i 8 cleanup required. Nije spremno za završno prihvaćanje.**

## Opseg i ograničenja

Jedan integracijski radnik; bez delegiranja, modelskih/API poziva ili GUI-ja. Prenesen je puni već provjereni tekst, bez sažimanja, samo uz normalizaciju razmaka u brojčanim naslovima. Sva proza, zadaci, oznake izvora i međustraničnih nastavaka sačuvani su; nema zasebnih fusnota u ovom dodijeljenom tekstu. Nečitljiv tekst nije prijavljen. Integracijski radnik nije sam pregledavao niti odobravao izreze: odluke su prenesene iz zasebnoga neovisnog pregleda. Nije izvršeno retuširanje, rezanje, ljudsko odobravanje, dovršavanje miljokaza, commit ili push. Nije mijenjan sirovi manifest, slike ni zajednički tracker.

## Ulazi

- [Provjereni tekst 137–155](review-candidates/book/M04/text-137-155.md)
- [Pregled teksta](review-candidates/book/M04/text-137-155-review.json)
- [Sirovi manifest: 73 dijela](review-candidates/book/M04/images-137-155.json)
- [Neovisni vizualni pregled: 65 PASS / 8 RECROP_REQUIRED](review-candidates/book/M04/visual-review-137-155.json)
- [Indeks izvornih stranica](sources/index.json)

## Stvorene datoteke — isključivo ove četiri

- [chapters/02-dijatonika-c.md](chapters/02-dijatonika-c.md)
- [images/02-dijatonika-c/REVIEW.md](images/02-dijatonika-c/REVIEW.md)
- [review-candidates/book/M04/images-integrated.json](review-candidates/book/M04/images-integrated.json)
- [review-candidates/book/M04/INTEGRATION-137-155.md](review-candidates/book/M04/INTEGRATION-137-155.md)

## Provjere

- 72 jedinstvena para (broj primjera, tiskana stranica) u tekstu točno odgovaraju 72 mjesta manifesta; 73 jedinstvena ID-a i putanje. Jedno mjesto 2.325 ima dva dijela, a 2.305 ima dva mjesta na različitim stranicama. Ukupno je 71 različit broj primjera (2.302–2.372).
- 65 prihvaćenih dijelova ugrađeno je s alternativnim tekstom, potpisom, tiskanom/PDF stranicom i MuseScore rezerviranim mjestom. Osam blokiranih dijelova ima samo vidljive PROVISIONAL poveznice na neodobrene izvorne izreze, potpis, izvor i razlog; nisu ugrađeni kao odobrene slike.
- Za svih 73 dijela provedena je izravna provjera svakoga piksela prema izvornom pravokutniku. Za svih 19 izvornih stranica ponovno su u memoriji generirani PDF renderi 69–78 na 300 dpi i uspoređene njihove indeksirane polovice: potpuna jednakost. Nije stvorena ni promijenjena slika.
- Preslikavanje tiskane stranice, PDF stranice, izvorne PNG putanje, lijeve/desne polovice i pravokutnika raširene stranice provjereno je prema `sources/index.json`. Svi novi zapisi koriste samo PDF stranice numerirane od 1; nema metapodataka indeksa koji počinju od nule.
- Izvorne oznake svih 19 stranica i svi međustranični nastavci su sačuvani. Provjera proze uspoređuje izvorni tekst s integriranim tekstom nakon uklanjanja samo novododanih slikovnih blokova i normalizacije razmaka naslova.
- Provjerene su sve putanje u konačnim zapisima te sve Markdown poveznice u novim dokumentima prema korijenu repozitorija.
- Završna automatska provjera prošla je: 257 pojavljivanja Markdown poveznica razrješava se prema korijenu repozitorija; 65 ugrađenih slika, 8 neodobrenih poveznica i 73 MuseScore rezervirana mjesta točno odgovaraju konačnim zapisima. Nakon uklanjanja samo dodanih slikovnih blokova tekst se potpuno podudara s provjerenim ulazom, uz jedinu dopuštenu normalizaciju razmaka naslova. Ponovno su provjereni SHA-256 otisci svih 73 izreza i pripadnih izvornih PNG-ova.

## Preslikavanje izvora — PDF stranice od 1

| Tiskana str. | PDF str. | Polovica | Izvorni PNG | Pravokutnik u PDF renderu [lijevo, gore, desno, dolje) |
| --- | --- | --- | --- | --- |
| 137 | 69 | right | [sources/pages/page-137.png](sources/pages/page-137.png) | `[1885, 0, 3771, 2598]` |
| 138 | 70 | left | [sources/pages/page-138.png](sources/pages/page-138.png) | `[0, 0, 1878, 2575]` |
| 139 | 70 | right | [sources/pages/page-139.png](sources/pages/page-139.png) | `[1878, 0, 3756, 2575]` |
| 140 | 71 | left | [sources/pages/page-140.png](sources/pages/page-140.png) | `[0, 0, 1885, 2598]` |
| 141 | 71 | right | [sources/pages/page-141.png](sources/pages/page-141.png) | `[1885, 0, 3771, 2598]` |
| 142 | 72 | left | [sources/pages/page-142.png](sources/pages/page-142.png) | `[0, 0, 1878, 2575]` |
| 143 | 72 | right | [sources/pages/page-143.png](sources/pages/page-143.png) | `[1878, 0, 3756, 2575]` |
| 144 | 73 | left | [sources/pages/page-144.png](sources/pages/page-144.png) | `[0, 0, 1885, 2598]` |
| 145 | 73 | right | [sources/pages/page-145.png](sources/pages/page-145.png) | `[1885, 0, 3771, 2598]` |
| 146 | 74 | left | [sources/pages/page-146.png](sources/pages/page-146.png) | `[0, 0, 1885, 2598]` |
| 147 | 74 | right | [sources/pages/page-147.png](sources/pages/page-147.png) | `[1885, 0, 3771, 2598]` |
| 148 | 75 | left | [sources/pages/page-148.png](sources/pages/page-148.png) | `[0, 0, 1885, 2598]` |
| 149 | 75 | right | [sources/pages/page-149.png](sources/pages/page-149.png) | `[1885, 0, 3771, 2598]` |
| 150 | 76 | left | [sources/pages/page-150.png](sources/pages/page-150.png) | `[0, 0, 1893, 2619]` |
| 151 | 76 | right | [sources/pages/page-151.png](sources/pages/page-151.png) | `[1893, 0, 3786, 2619]` |
| 152 | 77 | left | [sources/pages/page-152.png](sources/pages/page-152.png) | `[0, 0, 1880, 2583]` |
| 153 | 77 | right | [sources/pages/page-153.png](sources/pages/page-153.png) | `[1880, 0, 3761, 2583]` |
| 154 | 78 | left | [sources/pages/page-154.png](sources/pages/page-154.png) | `[0, 0, 1903, 2649]` |
| 155 | 78 | right | [sources/pages/page-155.png](sources/pages/page-155.png) | `[1903, 0, 3806, 2649]` |

## Cjelovita mapa svih 72 tekstna mjesta

Redoslijed mjesta i dijelova je numeriran od 1. Dva dijela 2.325 izričito ostaju u jednom retku/mjestu; nastavak 2.305 na str. 140 ostaje zasebno mjesto. Svaka putanja je puna putanja relativna korijenu repozitorija.

| Mjesto | Točna oznaka u provjerenom tekstu | Tiskana str. | PDF str. | Slikovni dijelovi i konačne odluke |
| --- | --- | --- | --- | --- |
| 1 | primjer 2.302 | 137 | 69 | dio 1/1: [images/02-dijatonika-c/primjer-2-302.png](images/02-dijatonika-c/primjer-2-302.png) — pass |
| 2 | primjer 2.303 | 137 | 69 | dio 1/1: [images/02-dijatonika-c/primjer-2-303.png](images/02-dijatonika-c/primjer-2-303.png) — pass |
| 3 | primjer 2.304 a–b | 138 | 70 | dio 1/1: [images/02-dijatonika-c/primjer-2-304.png](images/02-dijatonika-c/primjer-2-304.png) — pass |
| 4 | primjer 2.305 a–b | 139 | 70 | dio 1/1: [images/02-dijatonika-c/primjer-2-305-p139.png](images/02-dijatonika-c/primjer-2-305-p139.png) — pass |
| 5 | primjer 2.305 c (nastavak sa str. 139) | 140 | 71 | dio 1/1: [images/02-dijatonika-c/primjer-2-305-p140.png](images/02-dijatonika-c/primjer-2-305-p140.png) — pass |
| 6 | primjer 2.306 | 140 | 71 | dio 1/1: [images/02-dijatonika-c/primjer-2-306.png](images/02-dijatonika-c/primjer-2-306.png) — pass |
| 7 | primjer 2.307 a–b | 140 | 71 | dio 1/1: [images/02-dijatonika-c/primjer-2-307.png](images/02-dijatonika-c/primjer-2-307.png) — pass |
| 8 | primjer 2.308 | 141 | 71 | dio 1/1: [images/02-dijatonika-c/primjer-2-308.png](images/02-dijatonika-c/primjer-2-308.png) — pass |
| 9 | primjer 2.309 | 141 | 71 | dio 1/1: [images/02-dijatonika-c/primjer-2-309.png](images/02-dijatonika-c/primjer-2-309.png) — pass |
| 10 | primjer 2.310 | 141 | 71 | dio 1/1: [images/02-dijatonika-c/primjer-2-310.png](images/02-dijatonika-c/primjer-2-310.png) — pass |
| 11 | primjer 2.311 | 142 | 72 | dio 1/1: [images/02-dijatonika-c/primjer-2-311.png](images/02-dijatonika-c/primjer-2-311.png) — pass |
| 12 | primjer 2.312 | 142 | 72 | dio 1/1: [images/02-dijatonika-c/primjer-2-312.png](images/02-dijatonika-c/primjer-2-312.png) — pass |
| 13 | primjer 2.313 | 142 | 72 | dio 1/1: [images/02-dijatonika-c/primjer-2-313.png](images/02-dijatonika-c/primjer-2-313.png) — pass |
| 14 | primjer 2.314 | 143 | 72 | dio 1/1: [images/02-dijatonika-c/primjer-2-314.png](images/02-dijatonika-c/primjer-2-314.png) — pass |
| 15 | primjer 2.315 | 143 | 72 | dio 1/1: [images/02-dijatonika-c/primjer-2-315.png](images/02-dijatonika-c/primjer-2-315.png) — pass |
| 16 | primjer 2.316 | 143 | 72 | dio 1/1: [images/02-dijatonika-c/primjer-2-316.png](images/02-dijatonika-c/primjer-2-316.png) — pass |
| 17 | primjer 2.317 | 144 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-317.png](images/02-dijatonika-c/primjer-2-317.png) — **PROVISIONAL — cleanup required** |
| 18 | primjer 2.318 | 144 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-318.png](images/02-dijatonika-c/primjer-2-318.png) — **PROVISIONAL — cleanup required** |
| 19 | primjer 2.319 | 144 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-319.png](images/02-dijatonika-c/primjer-2-319.png) — pass |
| 20 | primjer 2.320 | 144 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-320.png](images/02-dijatonika-c/primjer-2-320.png) — pass |
| 21 | primjer 2.321 | 145 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-321.png](images/02-dijatonika-c/primjer-2-321.png) — **PROVISIONAL — cleanup required** |
| 22 | primjer 2.322 | 145 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-322.png](images/02-dijatonika-c/primjer-2-322.png) — pass |
| 23 | primjer 2.323 | 145 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-323.png](images/02-dijatonika-c/primjer-2-323.png) — **PROVISIONAL — cleanup required** |
| 24 | primjer 2.324 | 145 | 73 | dio 1/1: [images/02-dijatonika-c/primjer-2-324.png](images/02-dijatonika-c/primjer-2-324.png) — **PROVISIONAL — cleanup required** |
| 25 | primjer 2.325 | 145 | 73 | dio 1/2: [images/02-dijatonika-c/primjer-2-325-score.png](images/02-dijatonika-c/primjer-2-325-score.png) — **PROVISIONAL — cleanup required**; dio 2/2: [images/02-dijatonika-c/primjer-2-325-analysis.png](images/02-dijatonika-c/primjer-2-325-analysis.png) — pass |
| 26 | primjer 2.326 | 146 | 74 | dio 1/1: [images/02-dijatonika-c/primjer-2-326.png](images/02-dijatonika-c/primjer-2-326.png) — pass |
| 27 | primjer 2.327 | 146 | 74 | dio 1/1: [images/02-dijatonika-c/primjer-2-327.png](images/02-dijatonika-c/primjer-2-327.png) — pass |
| 28 | primjer 2.328 a–b | 146 | 74 | dio 1/1: [images/02-dijatonika-c/primjer-2-328.png](images/02-dijatonika-c/primjer-2-328.png) — pass |
| 29 | primjer 2.329 a–b | 147 | 74 | dio 1/1: [images/02-dijatonika-c/primjer-2-329.png](images/02-dijatonika-c/primjer-2-329.png) — pass |
| 30 | primjer 2.330 | 147 | 74 | dio 1/1: [images/02-dijatonika-c/primjer-2-330.png](images/02-dijatonika-c/primjer-2-330.png) — pass |
| 31 | primjer 2.331 | 147 | 74 | dio 1/1: [images/02-dijatonika-c/primjer-2-331.png](images/02-dijatonika-c/primjer-2-331.png) — pass |
| 32 | primjer 2.332 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-332.png](images/02-dijatonika-c/primjer-2-332.png) — pass |
| 33 | primjer 2.333 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-333.png](images/02-dijatonika-c/primjer-2-333.png) — pass |
| 34 | primjer 2.334 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-334.png](images/02-dijatonika-c/primjer-2-334.png) — pass |
| 35 | primjer 2.335 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-335.png](images/02-dijatonika-c/primjer-2-335.png) — pass |
| 36 | primjer 2.336 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-336.png](images/02-dijatonika-c/primjer-2-336.png) — pass |
| 37 | primjer 2.337 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-337.png](images/02-dijatonika-c/primjer-2-337.png) — pass |
| 38 | primjer 2.338 | 148 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-338.png](images/02-dijatonika-c/primjer-2-338.png) — pass |
| 39 | primjer 2.339 | 149 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-339.png](images/02-dijatonika-c/primjer-2-339.png) — pass |
| 40 | primjer 2.340 | 149 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-340.png](images/02-dijatonika-c/primjer-2-340.png) — pass |
| 41 | primjer 2.341 | 149 | 75 | dio 1/1: [images/02-dijatonika-c/primjer-2-341.png](images/02-dijatonika-c/primjer-2-341.png) — pass |
| 42 | primjer 2.342 | 150 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-342.png](images/02-dijatonika-c/primjer-2-342.png) — pass |
| 43 | primjer 2.343 | 150 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-343.png](images/02-dijatonika-c/primjer-2-343.png) — pass |
| 44 | primjer 2.344 | 150 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-344.png](images/02-dijatonika-c/primjer-2-344.png) — pass |
| 45 | primjer 2.345 | 150 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-345.png](images/02-dijatonika-c/primjer-2-345.png) — pass |
| 46 | primjer 2.346 | 150 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-346.png](images/02-dijatonika-c/primjer-2-346.png) — pass |
| 47 | primjer 2.347 | 151 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-347.png](images/02-dijatonika-c/primjer-2-347.png) — **PROVISIONAL — cleanup required** |
| 48 | primjer 2.348 | 151 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-348.png](images/02-dijatonika-c/primjer-2-348.png) — **PROVISIONAL — cleanup required** |
| 49 | primjer 2.349 | 151 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-349.png](images/02-dijatonika-c/primjer-2-349.png) — pass |
| 50 | primjer 2.350 | 151 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-350.png](images/02-dijatonika-c/primjer-2-350.png) — pass |
| 51 | primjer 2.351 | 151 | 76 | dio 1/1: [images/02-dijatonika-c/primjer-2-351.png](images/02-dijatonika-c/primjer-2-351.png) — pass |
| 52 | primjer 2.352 | 152 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-352.png](images/02-dijatonika-c/primjer-2-352.png) — pass |
| 53 | primjer 2.353 | 152 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-353.png](images/02-dijatonika-c/primjer-2-353.png) — pass |
| 54 | primjer 2.354 | 152 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-354.png](images/02-dijatonika-c/primjer-2-354.png) — pass |
| 55 | primjer 2.355 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-355.png](images/02-dijatonika-c/primjer-2-355.png) — pass |
| 56 | primjer 2.356 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-356.png](images/02-dijatonika-c/primjer-2-356.png) — pass |
| 57 | primjer 2.357 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-357.png](images/02-dijatonika-c/primjer-2-357.png) — pass |
| 58 | primjer 2.358 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-358.png](images/02-dijatonika-c/primjer-2-358.png) — pass |
| 59 | primjer 2.359 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-359.png](images/02-dijatonika-c/primjer-2-359.png) — pass |
| 60 | primjer 2.360 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-360.png](images/02-dijatonika-c/primjer-2-360.png) — pass |
| 61 | primjer 2.361 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-361.png](images/02-dijatonika-c/primjer-2-361.png) — pass |
| 62 | primjer 2.362 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-362.png](images/02-dijatonika-c/primjer-2-362.png) — pass |
| 63 | primjer 2.363 | 153 | 77 | dio 1/1: [images/02-dijatonika-c/primjer-2-363.png](images/02-dijatonika-c/primjer-2-363.png) — pass |
| 64 | primjer 2.364 | 154 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-364.png](images/02-dijatonika-c/primjer-2-364.png) — pass |
| 65 | primjer 2.365 | 154 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-365.png](images/02-dijatonika-c/primjer-2-365.png) — pass |
| 66 | primjer 2.366 | 154 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-366.png](images/02-dijatonika-c/primjer-2-366.png) — pass |
| 67 | primjer 2.367 | 154 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-367.png](images/02-dijatonika-c/primjer-2-367.png) — pass |
| 68 | primjer 2.368 a–b | 155 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-368.png](images/02-dijatonika-c/primjer-2-368.png) — pass |
| 69 | primjer 2.369 | 155 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-369.png](images/02-dijatonika-c/primjer-2-369.png) — pass |
| 70 | primjer 2.370 | 155 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-370.png](images/02-dijatonika-c/primjer-2-370.png) — pass |
| 71 | primjer 2.371 | 155 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-371.png](images/02-dijatonika-c/primjer-2-371.png) — pass |
| 72 | primjer 2.372 | 155 | 78 | dio 1/1: [images/02-dijatonika-c/primjer-2-372.png](images/02-dijatonika-c/primjer-2-372.png) — pass |

## Neriješene blokade i sljedeća granica

Izvorno ograničeni neodobreni dijelovi: 2.317 i 2.318 (str. 144), 2.321, 2.323, 2.324 i notni dio 2.325 (str. 145), 2.347 i 2.348 (str. 151). Svi imaju pojedinačne razloge u `images/02-dijatonika-c/REVIEW.md` i konačnim zapisima. Za njih neovisni pregled nije predložio siguran cjeloviti pravokutnik; potrebno je dopušteno rješenje izvornog ograničenja i novi neovisni pregled. Prihvaćen drugi dio 2.325 ne čini cijeli primjer prihvaćenim.

Integracija staje na tiskanoj str. 155. [Provjereni tekst 156–174](review-candidates/book/M04/text-156-174.md) i [njegov tekstni pregled](review-candidates/book/M04/text-156-174-review.json) postoje, ali slike za taj nastavak i njihova integracija još su na čekanju. Ti tekstovi ovdje nisu preuzeti.

**Spremnost za integraciju:** tekstni dio 137–155 prenesen je, 65 slikovnih dijelova integrirano je prema neovisnim prolazima; potpuno prihvaćanje i dovršetak ostaju blokirani s 8 izvorno ograničenih dijelova.

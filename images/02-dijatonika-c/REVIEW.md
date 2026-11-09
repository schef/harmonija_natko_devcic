# Pregled slika — tiskane str. 137–155

Opseg: tiskane str. 137–155; PDF str. 69–78, isključivo numeracija od 1. Izvorne slike i sirovi manifest nisu izmijenjeni.

**Rezultat: 65 pass, 8 cleanup required (izvorno ograničenje); 72 tekstna mjesta, 73 slikovna dijela. Nije spremno za dovršetak integracije.**

Ovo prenosi odluke zasebnoga neovisnog vizualnog preglednika, ne predstavlja novo samoodobravanje izreza niti ljudsko odobrenje. Neovisni pregled obuhvatio je sve propisane stavke: samo namjeravani primjer; tiskani broj ili dokumentirani nastavak; sve oznake i varijante; cjelovite krajeve crtovlja; neodrezanu notaciju, analizu i atribuciju; izvornu bijelu marginu gdje je moguća; odsutnost tuđeg sadržaja; sva četiri ruba u punoj rezoluciji; slaganje putanje, broja, potpisa i tiskane stranice. Pojedinačni razlozi iz izvornog izvještaja preneseni su u tablici.

Izvori pregleda:

- [Neovisni vizualni pregled (JSON)](review-candidates/book/M04/visual-review-137-155.json)
- [Neovisni vizualni pregled (izvještaj)](review-candidates/book/M04/visual-review-137-155.md)
- [Provjereni tekst](review-candidates/book/M04/text-137-155.md)
- [Pregled teksta](review-candidates/book/M04/text-137-155-review.json)
- [Izvorni manifest](review-candidates/book/M04/images-137-155.json)
- [Konačni integracijski zapisi](review-candidates/book/M04/images-integrated.json)
- [Cjelovita mapa tekstnih mjesta](review-candidates/book/M04/INTEGRATION-137-155.md)

## Potvrda izvora i preslikavanja

Svih 73 izreza ponovno je programski uspoređeno s izvornim pravokutnikom: jednaka veličina, način boje i svaki piksel. Svih 19 izvornih PNG-ova ponovno je uspoređeno s pripadnom polovicom svježega 300-dpi rendera PDF stranica 69–78; svi su identični. Preslikavanje tiskana stranica → PDF stranica, strana i pravokutnik raširene stranice provjereno je prema `sources/index.json`. Nije bilo ponovnoga rezanja, čišćenja, dodavanja rubova ili prepravljanja slika.

## Iznimke identiteta i blokade

- 2.305: dva zasebna tekstna mjesta, str. 139 (a–b s brojem) i 140 (nastavak c bez ponovljenoga broja u izvoru). Oba prolaze.
- 2.325: jedno tekstno mjesto na str. 145, dva dijela. `-score` sadrži broj, cijeli notni zapis i prvi redak analize C: IV♭ te je **cleanup required** zbog tuđe prethodne analize. `-analysis` sadrži Des: III, II₆ i Ces: III₆ bez podnožja te je **pass**; izvor ondje ne ponavlja broj. Cjeloviti primjer nije odobren.
- Osam izvorno ograničenih dijelova: 2.317, 2.318, 2.321, 2.323, 2.324, 2.325 (notni dio), 2.347 i 2.348. Za njih neovisni pregled nije našao siguran potpuni pravokutnik. Ne predlaže se brisanje, slikanje, izmišljanje margine ili prešutno odobravanje. U poglavlju su samo jasno označene PROVISIONAL poveznice, ne ugrađene slike.

## Odluka za svaki slikovni dio

Brojevi mjesta i dijelova počinju od 1. `pass` je prenesena neovisna odluka PASS; `cleanup required` prenesena je odluka RECROP_REQUIRED. Sve poveznice su relativne korijenu repozitorija.

| Mjesto / dio | Primjer | Tiskana str. / PDF str. | Izrez | Odluka | Razlog neovisnog pregleda |
| --- | --- | --- | --- | --- | --- |
| 1 / 1 od 1 | 2.302 | 137 / 69 | [primjer-2-302](images/02-dijatonika-c/primjer-2-302.png) | pass | Schumann attribution, number, both staves, modulation analysis and source-open right staff ends complete; four edges clean. |
| 2 / 1 od 1 | 2.303 | 137 / 69 | [primjer-2-303](images/02-dijatonika-c/primjer-2-303.png) | pass | Beethoven attribution, slurs, final barline and complete Es/Des analysis retained; no 137 footer or adjacent analysis. |
| 3 / 1 od 1 | 2.304 | 138 / 70 | [primjer-2-304](images/02-dijatonika-c/primjer-2-304.png) | pass | Number, a/b variants and both analysis rows complete; no prose at top or bottom; four edges clean. |
| 4 / 1 od 1 | 2.305 | 139 / 70 | [primjer-2-305-p139](images/02-dijatonika-c/primjer-2-305-p139.png) | pass | Number, variants a/b, arrow and both C/G analyses complete; isolated source speck is not foreign lettering; footer excluded. |
| 5 / 1 od 1 | 2.305 | 140 / 71 | [primjer-2-305-p140](images/02-dijatonika-c/primjer-2-305-p140.png) | pass | Correct c continuation of 2.305; no number repeated in source. Brace, final barline, lowest note and C/G figured analysis complete. |
| 6 / 1 od 1 | 2.306 | 140 / 71 | [primjer-2-306](images/02-dijatonika-c/primjer-2-306.png) | pass | Number, C-G title, complete staves and C:VI/G:II analysis; four edges clean. |
| 7 / 1 od 1 | 2.307 | 140 / 71 | [primjer-2-307](images/02-dijatonika-c/primjer-2-307.png) | pass | Both a/b variants, numbers, final barlines and complete analysis figures preserved; no footer. |
| 8 / 1 od 1 | 2.308 | 141 / 71 | [primjer-2-308](images/02-dijatonika-c/primjer-2-308.png) | pass | Number, C-G, tie and C:V/G:I analysis complete; four edges clean. |
| 9 / 1 od 1 | 2.309 | 141 / 71 | [primjer-2-309](images/02-dijatonika-c/primjer-2-309.png) | pass | Number, C-F and C:I/F:V analysis complete; incidental bottom speck is not a prose fragment. |
| 10 / 1 od 1 | 2.310 | 141 / 71 | [primjer-2-310](images/02-dijatonika-c/primjer-2-310.png) | pass | Number, all five measures and C:II/F:VI analysis complete; 141 footer excluded. |
| 11 / 1 od 1 | 2.311 | 142 / 72 | [primjer-2-311](images/02-dijatonika-c/primjer-2-311.png) | pass | Number and C:IV/F:I analysis complete; narrow lower source gap clean of next title. |
| 12 / 1 od 1 | 2.312 | 142 / 72 | [primjer-2-312](images/02-dijatonika-c/primjer-2-312.png) | pass | Number, C-F and complete C:VI/F:III analysis; no previous example or following prose. |
| 13 / 1 od 1 | 2.313 | 142 / 72 | [primjer-2-313](images/02-dijatonika-c/primjer-2-313.png) | pass | Number, accidentals, complete bass stems and C:III7/D:II7 retained; footer excluded. |
| 14 / 1 od 1 | 2.314 | 143 / 72 | [primjer-2-314](images/02-dijatonika-c/primjer-2-314.png) | pass | Number and C:IV/B:V analysis complete; small genuine bottom margin before prose, no prose fragment. |
| 15 / 1 od 1 | 2.315 | 143 / 72 | [primjer-2-315](images/02-dijatonika-c/primjer-2-315.png) | pass | Number, C-A, chained G/A analysis and all lowest glyphs complete; next title excluded. |
| 16 / 1 od 1 | 2.316 | 143 / 72 | [primjer-2-316](images/02-dijatonika-c/primjer-2-316.png) | pass | Number, C-Es and complete multilevel B/Es analysis; previous analysis and footer excluded. |
| 17 / 1 od 1 | 2.317 | 144 / 73 | [primjer-2-317](images/02-dijatonika-c/primjer-2-317.png) | **PROVISIONAL — cleanup required** | Top contains a thin fragment of the preceding prose/underline; bottom contains 2.318 C-E title, clef tip and upper marks. Its own A:IV-natural analysis and lowest bass stem overlap the following title vertically. A single rectangle cannot retain the complete numbered example and analysis while excluding 2.318; top-only trimming would not cure it. |
| 18 / 1 od 1 | 2.318 | 144 / 73 | [primjer-2-318](images/02-dijatonika-c/primjer-2-318.png) | **PROVISIONAL — cleanup required** | Top includes 2.317 C:II/A:IV-natural analysis and a bass-stem fragment. Required C-E title is at the same heights, so moving top below foreign ink would clip this example's title. Source also has short marks immediately above the upper staff. No safe complete single rectangle. |
| 19 / 1 od 1 | 2.319 | 144 / 73 | [primjer-2-319](images/02-dijatonika-c/primjer-2-319.png) | pass | Number, C-H, bass ledger note/stem and C:III/H:IV-natural analysis complete. Isolated top speck is separated from previous analysis, not a partial glyph. |
| 20 / 1 od 1 | 2.320 | 144 / 73 | [primjer-2-320](images/02-dijatonika-c/primjer-2-320.png) | pass | Number, C-Es, full bass stem and C:IV-flat/Es:II retained; small source flecks below analysis are not footer/letter fragments; 144 excluded. |
| 21 / 1 od 1 | 2.321 | 145 / 73 | [primjer-2-321](images/02-dijatonika-c/primjer-2-321.png) | **PROVISIONAL — cleanup required** | Faint deliberate angular handwritten-looking strokes to the right of As:VI are visible on enlarged source and crop, unlike isolated scan specks. Their position lies inside the required score/analysis rectangle; excluding them by an edge would clip notation or analysis. No safe single rectangle without prohibited erasure. |
| 22 / 1 od 1 | 2.322 | 145 / 73 | [primjer-2-322](images/02-dijatonika-c/primjer-2-322.png) | pass | Number, C-Des, full staves and C:IV-flat/Des:III retained; no preceding handwriting or following prose. |
| 23 / 1 od 1 | 2.323 | 145 / 73 | [primjer-2-323](images/02-dijatonika-c/primjer-2-323.png) | **PROVISIONAL — cleanup required** | Top clips in the descender of prose word pet, touching/overlapping the C-Cis title; bottom contains following Es-Fis title and clef tip. Own H/Cis analysis extends below that following title. No single rectangle can remove these foreign marks and retain all required title/analysis. |
| 24 / 1 od 1 | 2.324 | 145 / 73 | [primjer-2-324](images/02-dijatonika-c/primjer-2-324.png) | **PROVISIONAL — cleanup required** | Top contains 2.323 H/Cis analysis; bottom contains 2.325 C-Ces title, clef tip and note-stem tips. Own lower Fis analysis interleaves the following score/title, while own Es-Fis title interleaves the preceding analysis. No safe complete single rectangle. |
| 25 / 1 od 2 | 2.325 | 145 / 73 | [primjer-2-325-score](images/02-dijatonika-c/primjer-2-325-score.png) | **PROVISIONAL — cleanup required** | Top contains foreign 2.324 D:IV-flat and Fis:IV-natural analysis at the same heights as required C-Ces title and upper stems. Own number, complete score, lowest bass stem and first analysis line C:IV-flat are retained; lower-analysis split excludes footer correctly. Nevertheless no single rectangle can exclude preceding analysis without losing required own content. |
| 25 / 2 od 2 | 2.325 | 145 / 73 | [primjer-2-325-analysis](images/02-dijatonika-c/primjer-2-325-analysis.png) | pass | Correct second part of one 2.325 slot: full Des:III, II6 and Ces:III6 preserved. First C:IV-flat line and complete lowest stem remain in -score. No repeated source number here; running footer and 145 fully excluded. |
| 26 / 1 od 1 | 2.326 | 146 / 74 | [primjer-2-326](images/02-dijatonika-c/primjer-2-326.png) | pass | Number, E-Des and all multilevel analysis through lowest Des:II complete; no following prose. |
| 27 / 1 od 1 | 2.327 | 146 / 74 | [primjer-2-327](images/02-dijatonika-c/primjer-2-327.png) | pass | Number, C-Ges, three sequence brackets, bass stems and final barline complete; four edges clean. |
| 28 / 1 od 1 | 2.328 | 146 / 74 | [primjer-2-328](images/02-dijatonika-c/primjer-2-328.png) | pass | Number and both a/b systems, all accidentals, lowest stems and final barlines retained; task paragraph excluded. |
| 29 / 1 od 1 | 2.329 | 147 / 74 | [primjer-2-329](images/02-dijatonika-c/primjer-2-329.png) | pass | Number, a/b variants, bracket and both C/a analyses complete; prose excluded at both edges. |
| 30 / 1 od 1 | 2.330 | 147 / 74 | [primjer-2-330](images/02-dijatonika-c/primjer-2-330.png) | pass | Number, C-a, lowest bass note/stem and C:VII6/a:II6 complete; adjacent 2.331 excluded. |
| 31 / 1 od 1 | 2.331 | 147 / 74 | [primjer-2-331](images/02-dijatonika-c/primjer-2-331.png) | pass | Number, C-e, lowest final bass ledger note and C:I/e:VI complete; neighbour and 147 excluded. |
| 32 / 1 od 1 | 2.332 | 148 / 75 | [primjer-2-332](images/02-dijatonika-c/primjer-2-332.png) | pass | Number, C-h, complete C:V/h:VI analysis and staff ends; no prose or adjacent example. |
| 33 / 1 od 1 | 2.333 | 148 / 75 | [primjer-2-333](images/02-dijatonika-c/primjer-2-333.png) | pass | Number, C-d and full C:IV/d:III analysis; clean narrow bottom gap before next example. |
| 34 / 1 od 1 | 2.334 | 148 / 75 | [primjer-2-334](images/02-dijatonika-c/primjer-2-334.png) | pass | Number, C-g, all measures and C:I/g:IV retained; no preceding analysis or following titles. |
| 35 / 1 od 1 | 2.335 | 148 / 75 | [primjer-2-335](images/02-dijatonika-c/primjer-2-335.png) | pass | Number, C-c and C:V/c:V complete; no adjacent 2.336 ink; four edges clean. |
| 36 / 1 od 1 | 2.336 | 148 / 75 | [primjer-2-336](images/02-dijatonika-c/primjer-2-336.png) | pass | Number, C-f and C:I/f:V complete. Isolated lower-right source fleck is not handwriting or foreign notation. |
| 37 / 1 od 1 | 2.337 | 148 / 75 | [primjer-2-337](images/02-dijatonika-c/primjer-2-337.png) | pass | Number, C-b, 3/2 signatures, all ledger lines, dotted chords and C:IV/b:V complete. |
| 38 / 1 od 1 | 2.338 | 148 / 75 | [primjer-2-338](images/02-dijatonika-c/primjer-2-338.png) | pass | Number, C-es and all II6-flat/VII6 figures retained; final barline complete; 148 excluded. |
| 39 / 1 od 1 | 2.339 | 149 / 75 | [primjer-2-339](images/02-dijatonika-c/primjer-2-339.png) | pass | Number, C-gis, full accidentals and complete chained E/gis analysis; four edges clean. |
| 40 / 1 od 1 | 2.340 | 149 / 75 | [primjer-2-340](images/02-dijatonika-c/primjer-2-340.png) | pass | Number, B-cis, all bass ledger notes/stems and complete A/cis analysis; prose excluded. |
| 41 / 1 od 1 | 2.341 | 149 / 75 | [primjer-2-341](images/02-dijatonika-c/primjer-2-341.png) | pass | Number, C-as and complete C/Es/as analysis retained; no prose or 149 footer. |
| 42 / 1 od 1 | 2.342 | 150 / 76 | [primjer-2-342](images/02-dijatonika-c/primjer-2-342.png) | pass | Number, A-b, tie, complete A/C/b figured analysis and lowest stems; following task text excluded. |
| 43 / 1 od 1 | 2.343 | 150 / 76 | [primjer-2-343](images/02-dijatonika-c/primjer-2-343.png) | pass | Number, a-e, accidentals and a:I6/e:IV6 complete; neighbouring example excluded. |
| 44 / 1 od 1 | 2.344 | 150 / 76 | [primjer-2-344](images/02-dijatonika-c/primjer-2-344.png) | pass | Number, a-h, ties and a:V-natural/h:IV complete; final barline/stem intact as scanned, no neighbouring ink. |
| 45 / 1 od 1 | 2.345 | 150 / 76 | [primjer-2-345](images/02-dijatonika-c/primjer-2-345.png) | pass | Number, a-fis, full final bass accidental/ledger note and a:VII6/fis:II6 complete. |
| 46 / 1 od 1 | 2.346 | 150 / 76 | [primjer-2-346](images/02-dijatonika-c/primjer-2-346.png) | pass | Number, a-d, low bass stem and a:VI/d:III complete; no 150 footer. |
| 47 / 1 od 1 | 2.347 | 151 / 76 | [primjer-2-347](images/02-dijatonika-c/primjer-2-347.png) | **PROVISIONAL — cleanup required** | Bottom contains the upper portion of next a-c title and clef tip. Own g:V2 analysis overlaps that title vertically. Removing foreign ink with a horizontal bottom edge clips own analysis; moving a side edge clips required number/staves. No safe complete single rectangle. |
| 48 / 1 od 1 | 2.348 | 151 / 76 | [primjer-2-348](images/02-dijatonika-c/primjer-2-348.png) | **PROVISIONAL — cleanup required** | Top contains lower g:V2 analysis of 2.347, interleaved vertically with own required a-c title. A top edge below the previous analysis would remove part of own title. No safe complete single rectangle. |
| 49 / 1 od 1 | 2.349 | 151 / 76 | [primjer-2-349](images/02-dijatonika-c/primjer-2-349.png) | pass | Number, a-f, full final bass ledger note and a:III/f:V retained; preceding analysis excluded. |
| 50 / 1 od 1 | 2.350 | 151 / 76 | [primjer-2-350](images/02-dijatonika-c/primjer-2-350.png) | pass | Number, a-b, long slur and a:VI/b:V retained; following prose excluded. |
| 51 / 1 od 1 | 2.351 | 151 / 76 | [primjer-2-351](images/02-dijatonika-c/primjer-2-351.png) | pass | Number, a-ais, both 3/2 signatures and complete a/H/ais analysis; lowest stems intact, 151 excluded. |
| 52 / 1 od 1 | 2.352 | 152 / 77 | [primjer-2-352](images/02-dijatonika-c/primjer-2-352.png) | pass | Number, c-dis, complete double-sharp/accidentals and all G/H/dis analysis levels; prose excluded. |
| 53 / 1 od 1 | 2.353 | 152 / 77 | [primjer-2-353](images/02-dijatonika-c/primjer-2-353.png) | pass | Number, a-as, all staves and complete a/B/as analysis; four edges clean. |
| 54 / 1 od 1 | 2.354 | 152 / 77 | [primjer-2-354](images/02-dijatonika-c/primjer-2-354.png) | pass | Number, fis-b and full fis/g/b analysis preserved; following task paragraph excluded. |
| 55 / 1 od 1 | 2.355 | 153 / 77 | [primjer-2-355](images/02-dijatonika-c/primjer-2-355.png) | pass | Number, a-C, all notation and a:VI/C:IV complete; neighbouring 2.356 and following row excluded. |
| 56 / 1 od 1 | 2.356 | 153 / 77 | [primjer-2-356](images/02-dijatonika-c/primjer-2-356.png) | pass | Number, a-G, tie, low sharp/stem and a:I/G:II complete; four edges clean. |
| 57 / 1 od 1 | 2.357 | 153 / 77 | [primjer-2-357](images/02-dijatonika-c/primjer-2-357.png) | pass | Number, a-D, low bass stem and a:V-natural/D:II complete; adjacent rows/column excluded. |
| 58 / 1 od 1 | 2.358 | 153 / 77 | [primjer-2-358](images/02-dijatonika-c/primjer-2-358.png) | pass | Number, a-A, tie and a:V/A:V complete; no neighbouring marks at four edges. |
| 59 / 1 od 1 | 2.359 | 153 / 77 | [primjer-2-359](images/02-dijatonika-c/primjer-2-359.png) | pass | Number, a-E, 3/2 signatures, ties, dots and a:V/E:I complete; following title excluded. |
| 60 / 1 od 1 | 2.360 | 153 / 77 | [primjer-2-360](images/02-dijatonika-c/primjer-2-360.png) | pass | Number, a-H, low stems and a:V/H:IV retained; neighbouring examples excluded. |
| 61 / 1 od 1 | 2.361 | 153 / 77 | [primjer-2-361](images/02-dijatonika-c/primjer-2-361.png) | pass | Number, a-Fis, full lowest bass accidental and a:VII6/Fis:II6-natural analysis retained. Enlarged lower edge confirms final natural is complete, with two genuine blank pixel rows below its main ink; tight gap before 2.363 title, no foreign glyph. |
| 62 / 1 od 1 | 2.362 | 153 / 77 | [primjer-2-362](images/02-dijatonika-c/primjer-2-362.png) | pass | Number, a-F and complete a:IV6/F:VI6 retained; isolated bottom source speck is not foreign text. |
| 63 / 1 od 1 | 2.363 | 153 / 77 | [primjer-2-363](images/02-dijatonika-c/primjer-2-363.png) | pass | Number, a-B, 3/2 signatures, upper stems and a:VI/B:V complete; no preceding natural fragment or following prose. |
| 64 / 1 od 1 | 2.364 | 154 / 78 | [primjer-2-364](images/02-dijatonika-c/primjer-2-364.png) | pass | Number, a-Cis, ties and all a/H/Cis analysis levels retained; prose excluded. |
| 65 / 1 od 1 | 2.365 | 154 / 78 | [primjer-2-365](images/02-dijatonika-c/primjer-2-365.png) | pass | Number, g-Fis, final low sharp/ledger note and full g/D/Fis analysis retained; outside right source mark excluded. |
| 66 / 1 od 1 | 2.366 | 154 / 78 | [primjer-2-366](images/02-dijatonika-c/primjer-2-366.png) | pass | Number, a-As, full low flat note/stem and complete a/b/As analysis retained; four edges clean. |
| 67 / 1 od 1 | 2.367 | 154 / 78 | [primjer-2-367](images/02-dijatonika-c/primjer-2-367.png) | pass | Number, h-Des and full h/c/Des analysis retained. Heavy/filled source noteheads are original scan quality, not crop damage; task text excluded. |
| 68 / 1 od 1 | 2.368 | 155 / 78 | [primjer-2-368](images/02-dijatonika-c/primjer-2-368.png) | pass | Number, a/b variants, all upper/lower brackets and C/a analyses complete; small irregular source flecks below left staff are scan dirt, not lettering or handwriting. |
| 69 / 1 od 1 | 2.369 | 155 / 78 | [primjer-2-369](images/02-dijatonika-c/primjer-2-369.png) | pass | Number, C-g, both brackets and C:IV/g:VII analysis retained; adjacent 2.370 excluded. |
| 70 / 1 od 1 | 2.370 | 155 / 78 | [primjer-2-370](images/02-dijatonika-c/primjer-2-370.png) | pass | Number, C-d, both brackets, bass stems and C:I/d:VII analysis retained; prose excluded. |
| 71 / 1 od 1 | 2.371 | 155 / 78 | [primjer-2-371](images/02-dijatonika-c/primjer-2-371.png) | pass | Number, C-g, lower bracket, complete C:IV/g:VII and II4/3 figures retained; prose and footer excluded. |
| 72 / 1 od 1 | 2.372 | 155 / 78 | [primjer-2-372](images/02-dijatonika-c/primjer-2-372.png) | pass | Number, C-d, lower bracket and complete C:I/d:VII and II4/3 figures retained; 155 footer fully excluded. |

## Stanje predaje

Tekst 137–155 provjeren je i prenesen bez sažimanja, s izvornim oznakama stranica i nastavaka. U tom tekstu nema zasebnih fusnota. Tekstni pregled ne prijavljuje nečitljiv tekst. Osam slikovnih blokada ostaje neriješeno; potrebna je nova dopuštena odluka o izvornom materijalu i neovisan pregled bilo kakve buduće zamjene. Str. 156–174: provjeren tekst, slike i integracija na čekanju. Miljokaz nije dovršen.


---

# Dodatak pregleda — tiskane str. 156–174 / PDF 79–88

**PROVISIONAL: 54 tekstna mjesta, 55 slikovnih dijelova; 42 pass, 13 cleanup required (izvorno ograničenje). Kumulativno: 128 dijelova, 107 pass i 21 cleanup required. Nije spremno za konačno prihvaćanje.**

Ovaj dodatak samo prenosi neovisne odluke, bez samoodobravanja ili ljudskog odobrenja. Prvi pregled: 41 PASS, 13 izvorno blokiranih RECROP_REQUIRED i jedan popravljiv RECROP_REQUIRED. Zasebni ponovni pregled prihvatio je zamjenski izrez zadatka 13 (Allegretto): ukupno 42 PASS. Sirovi manifest i slike nisu mijenjani. Svih 55 integriranih izreza uspoređeno je sa svim pikselima deklariranog izvornog pravokutnika; svih 19 izvornih PNG-ova odgovara svježim 300-dpi renderima PDF stranica 79–88 u memoriji. Sve četiri rubne provjere i ostale stavke obveznog vizualnog pregleda prenesene su iz neovisnih odluka, ne proglašavaju se novim integratorovim vizualnim pregledom.

Izvori:

- [Provjereni tekst](review-candidates/book/M04/text-156-174.md)
- [Tekstni pregled: svih 19 stranica verified](review-candidates/book/M04/text-156-174-review.json)
- [Ispravljeni ulazni manifest: 55 dijelova](review-candidates/book/M04/images-corrected-156-174.json)
- [Neovisni vizualni pregled: objekt s poljem reviews](review-candidates/book/M04/visual-review-156-174.json)
- [Neovisni ponovni pregled: zadatak 13 PASS](review-candidates/book/M04/recrop-review-156-174.json)
- [Konačni integracijski zapisi: 128 dijelova](review-candidates/book/M04/images-integrated.json)
- [Cjelovita mapa svih 54 mjesta i izvora](review-candidates/book/M04/INTEGRATION-156-174.md)

Zadatak 15 zadržava zaseban početak na str. 161 i nastavak na str. 162 bez ponovljenog broja u izvoru. Primjer 2.409 ostaje jedno tekstno mjesto s dva dijela: a je blokiran, b prolazi i nema ponovno otisnutog broja ni atribucije; odobrenje b ne odobrava cijeli primjer. Prazna str. 174 izričito je zabilježena, bez izmišljenog sadržaja.

Za svih 13 blokiranih dijelova nije predložen siguran cjelovit pravokutnik. U poglavlju ostaju samo vidljive neodobrene izvorne poveznice s pojedinačnim razlogom, potpisom, tiskanom/PDF stranicom i MuseScore rezerviranim mjestom. Potrebno je dopušteno rješenje izvornog ograničenja i novi neovisni pregled; bez retuširanja, generiranja rubova ili prešutnog prihvaćanja. Nema prijavljenog nečitljivog teksta; rukopis nije transkribiran kao tiskani sadržaj.

## Odluka za svaki od 55 novih dijelova

Mjesto je globalno, uz lokalni broj 1–54 u zagradi. Sve putanje su relativne korijenu repozitorija; PDF stranice numerirane su od 1.

| Mjesto / dio | Primjer ili zadatak | Tiskana / PDF str. | Izrez | Odluka | Razlog neovisnog pregleda |
| --- | --- | --- | --- | --- | --- |
| 73 (1) / 1 od 1 | 2.373 | 156 / 79 | [primjer-2-373](images/02-dijatonika-c/primjer-2-373.png) | pass | Number, complete grand staff, upper and lower brackets and all fermatas intact; four edges clean with source whitespace. |
| 74 (2) / 1 od 1 | 2.374 | 157 / 79 | [primjer-2-374](images/02-dijatonika-c/primjer-2-374.png) | pass | Number, a/b titles and both analyses including lowest 6/4 retained; all staff ends and four margins clean. |
| 75 (3) / 1 od 1 | 2.375 | 157 / 79 | [primjer-2-375](images/02-dijatonika-c/primjer-2-375.png) | pass | Number, C(c)-Es(es) title and full lower analysis retained; four edges clean and staff ends complete. |
| 76 (4) / 1 od 1 | 2.376 | 157 / 79 | [primjer-2-376](images/02-dijatonika-c/primjer-2-376.png) | pass | Haydn attribution, number and C:VI/G:II analysis complete. Narrow lower source gap remains clean; no following attribution included. |
| 77 (5) / 1 od 1 | 2.377 | 157 / 79 | [primjer-2-377](images/02-dijatonika-c/primjer-2-377.png) | pass | Complete Beethoven attribution, number, slurs and lower multi-line analysis retained. Tight top separation is clean; other edges have genuine margins. |
| 78 (6) / 1 od 1 | 2.378 | 158 / 80 | [primjer-2-378](images/02-dijatonika-c/primjer-2-378.png) | **PROVISIONAL — cleanup required** | Bottom edge includes upper border/letter fragments of following boxed C-fis-C title. Lowest bass stems of 378 extend into that same vertical band; a horizontal cut removing the title would clip intended notation. Not scan specks. |
| 79 (7) / 1 od 1 | 2.379 | 158 / 80 | [primjer-2-379](images/02-dijatonika-c/primjer-2-379.png) | **PROVISIONAL — cleanup required** | Top edge contains preceding 378 bass-stem tails to the right of the boxed C-fis-C title. Retaining the entire title and complete full-width notation precludes excluding those tails with one rectangle. |
| 80 (8) / 1 od 1 | 2.380 | 159 / 80 | [primjer-2-380](images/02-dijatonika-c/primjer-2-380.png) | pass | Number, a/b/c, all three systems, tonal labels and lowest analyses complete; all four edges clean. |
| 81 (9) / 1 od 1 | zadatak 2 | 160 / 81 | [zadatak-2-9-6-2](images/02-dijatonika-c/zadatak-2-9-6-2.png) | pass | Exercise ID 2, whole staff and lowest figured-bass 4/sharp retained; four edges clean. |
| 82 (10) / 1 od 1 | zadatak 3 | 160 / 81 | [zadatak-2-9-6-3](images/02-dijatonika-c/zadatak-2-9-6-3.png) | pass | ID 3, complete staff, final note/dot and all stacked figures retained; four clean source margins. |
| 83 (11) / 1 od 1 | zadatak 4 | 160 / 81 | [zadatak-2-9-6-4](images/02-dijatonika-c/zadatak-2-9-6-4.png) | pass | ID 4, both staff rows and complete lower figures/accidentals retained; all four edges clean. |
| 84 (12) / 1 od 1 | zadatak 5 | 160 / 81 | [zadatak-2-9-6-5](images/02-dijatonika-c/zadatak-2-9-6-5.png) | pass | ID 5, both rows, all figures and lowest accidentals retained with clean genuine margins. |
| 85 (13) / 1 od 1 | zadatak 6 | 160 / 81 | [zadatak-2-9-6-6](images/02-dijatonika-c/zadatak-2-9-6-6.png) | pass | ID 6, complete staff/clef/signatures, low note and final barline intact; all edges clean. |
| 86 (14) / 1 od 1 | zadatak 7 | 160 / 81 | [zadatak-2-9-6-7](images/02-dijatonika-c/zadatak-2-9-6-7.png) | pass | ID 7, all notation including final low whole note intact; clean four-edge source margins. |
| 87 (15) / 1 od 1 | zadatak 8 | 160 / 81 | [zadatak-2-9-6-8](images/02-dijatonika-c/zadatak-2-9-6-8.png) | pass | ID 8, high slurs, signatures, lower clef and staff ends intact. Tiny isolated top speck is source noise, not a foreign character. |
| 88 (16) / 1 od 1 | zadatak 9 | 161 / 81 | [zadatak-2-9-6-9](images/02-dijatonika-c/zadatak-2-9-6-9.png) | pass | ID 9, both long slurs, clef and final barline complete; four edges clean. |
| 89 (17) / 1 od 1 | zadatak 10 | 161 / 81 | [zadatak-2-9-6-10](images/02-dijatonika-c/zadatak-2-9-6-10.png) | pass | ID 10, signatures, complete upper slur and full staff retained; clean source margins. |
| 90 (18) / 1 od 1 | zadatak 11 | 161 / 81 | [zadatak-2-9-6-11](images/02-dijatonika-c/zadatak-2-9-6-11.png) | pass | ID 11, slurs, lower ties and final low whole note retained; all four edges clean. |
| 91 (19) / 1 od 1 | zadatak 12 | 161 / 81 | [zadatak-2-9-6-12](images/02-dijatonika-c/zadatak-2-9-6-12.png) | pass | ID 12, parenthesized accidental, slurs and complete staff retained; following Allegretto excluded and four edges clean. |
| 92 (20) / 1 od 1 | zadatak 13 | 161 / 81 | [zadatak-2-9-6-13](images/02-dijatonika-c/recrops/zadatak-2-9-6-13.png) | pass | Corrected crop retains the complete Allegretto title with genuine top whitespace, exercise ID 13, all three staff rows, clefs/signatures, notes/rests, slurs/ties, lower stems/beams and final barline. Independently inspected the actual replacement at native resolution against the authoritative source page. All four edges are clean; no preceding clef fragment, neighbouring exercise, prose, page number or handwriting is included. The declared source-only rectangle is reproduced exactly without resampling, retouching or an artificial border. |
| 93 (21) / 1 od 1 | zadatak 14 | 161 / 81 | [zadatak-2-9-6-14](images/02-dijatonika-c/zadatak-2-9-6-14.png) | pass | ID 14 and all four staff rows/slurs complete; lowest final note and four genuine margins intact. |
| 94 (22) / 1 od 1 | zadatak 15 | 161 / 81 | [zadatak-2-9-6-15-pocetak](images/02-dijatonika-c/zadatak-2-9-6-15-pocetak.png) | pass | ID 15 and complete beginning row retained with slurs; footer and page number excluded. Correctly paired to continuation on 162. |
| 95 (23) / 1 od 1 | zadatak 15 | 162 / 82 | [zadatak-2-9-6-15-nastavak](images/02-dijatonika-c/zadatak-2-9-6-15-nastavak.png) | pass | Both continuation rows through final barline intact; four margins clean. No repeated ID printed here; identification supplied by paired beginning on 161. |
| 96 (24) / 1 od 1 | zadatak 16 | 162 / 82 | [zadatak-2-9-6-16](images/02-dijatonika-c/zadatak-2-9-6-16.png) | pass | ID 16, complete slurs, clef and staff ends retained; four edges clean. |
| 97 (25) / 1 od 1 | zadatak 17 | 162 / 82 | [zadatak-2-9-6-17](images/02-dijatonika-c/zadatak-2-9-6-17.png) | pass | ID 17, both rows, upper slurs and lowest beam retained; chapter heading excluded and four edges clean. |
| 98 (26) / 1 od 1 | 2.381 | 162 / 82 | [primjer-2-381](images/02-dijatonika-c/primjer-2-381.png) | **PROVISIONAL — cleanup required** | Handwritten chord names above a/b and handwritten text below a are inside the required example bounds, with partial handwriting at top. Printed bottom 5 is complete, confirmed against doubled source detail. No complete clean rectangle can remove the interleaved handwriting. |
| 99 (27) / 1 od 1 | 2.382 | 163 / 82 | [primjer-2-382](images/02-dijatonika-c/primjer-2-382.png) | **PROVISIONAL — cleanup required** | Extensive handwriting above/between both variants and around lower analyses, including circles/arrows and right-edge writing. These are identifiable pencil annotations, not specks; cannot exclude without losing printed content. |
| 100 (28) / 1 od 1 | 2.383 | 164 / 83 | [primjer-2-383](images/02-dijatonika-c/primjer-2-383.png) | **PROVISIONAL — cleanup required** | Handwritten chord names and analyses interleave a/b and extend into left/top/bottom margins. Printed variants are present but a clean complete rectangle is impossible on this source. |
| 101 (29) / 1 od 1 | 2.384 | 164 / 83 | [primjer-2-384](images/02-dijatonika-c/primjer-2-384.png) | **PROVISIONAL — cleanup required** | Pencil chord labels above staff and handwritten analyses below overlap the required Es-Fes title and printed lower analysis band. Not removable by a complete rectangular source crop. |
| 102 (30) / 1 od 1 | 2.385 | 165 / 83 | [primjer-2-385](images/02-dijatonika-c/primjer-2-385.png) | pass | Number, all six modal labels, every upper/lower bracket and full staff retained; four clean source margins. |
| 103 (31) / 1 od 1 | 2.386 | 166 / 84 | [primjer-2-386](images/02-dijatonika-c/primjer-2-386.png) | pass | Number, variants a-f, all twelve modal titles and six complete rows retained, including lowest ledger notes; four clean margins. |
| 104 (32) / 1 od 1 | 2.387 | 167 / 84 | [primjer-2-387](images/02-dijatonika-c/primjer-2-387.png) | pass | Number, Dorski/d-mol labels, circled note, both staves and brace intact; four clean margins, no neighbouring example. |
| 105 (33) / 1 od 1 | 2.388 | 167 / 84 | [primjer-2-388](images/02-dijatonika-c/primjer-2-388.png) | pass | Number, Frigijski/e-mol labels, circled note and both staves intact; all four edges clean. |
| 106 (34) / 1 od 1 | 2.389 | 167 / 84 | [primjer-2-389](images/02-dijatonika-c/primjer-2-389.png) | pass | Number, Lidijski/F-dur labels, circled note and complete staves retained; four clean genuine margins. |
| 107 (35) / 1 od 1 | 2.390 | 167 / 84 | [primjer-2-390](images/02-dijatonika-c/primjer-2-390.png) | pass | Number, Miksolidijski/G-dur labels, circled note and complete staves retained; four edges clean. |
| 108 (36) / 1 od 1 | 2.391 | 168 / 85 | [primjer-2-391](images/02-dijatonika-c/primjer-2-391.png) | **PROVISIONAL — cleanup required** | Handwritten chord letters above and Roman numerals below the staff are interleaved with complete printed Dorski example; lower handwriting reaches bottom edge. These are annotations rather than scan specks. No clean complete rectangle. |
| 109 (37) / 1 od 1 | 2.392 | 168 / 85 | [primjer-2-392](images/02-dijatonika-c/primjer-2-392.png) | **PROVISIONAL — cleanup required** | Top edge contains a definite handwritten numeral/tail from preceding analysis, right of Frigijski title. Doubled source detail confirms its vertical band overlaps the title, so moving top down would sacrifice the title. Not an isolated speck. |
| 110 (38) / 1 od 1 | 2.393 | 168 / 85 | [primjer-2-393](images/02-dijatonika-c/primjer-2-393.png) | pass | Number, Lidijski title, all notation and lowest bass stems retained; four edges clean. |
| 111 (39) / 1 od 1 | 2.394 | 168 / 85 | [primjer-2-394](images/02-dijatonika-c/primjer-2-394.png) | pass | Number, complete Miksolidijski title, upper stems and lowest bass stems retained; clean margins on all four edges. |
| 112 (40) / 1 od 1 | 2.395 | 168 / 85 | [primjer-2-395](images/02-dijatonika-c/primjer-2-395.png) | pass | Number, Eolski title, all notation and lowest bass stem retained; page number excluded and four margins clean. |
| 113 (41) / 1 od 1 | 2.396 | 169 / 85 | [primjer-2-396](images/02-dijatonika-c/primjer-2-396.png) | pass | Number, all three systems and Latin lyric lines, asterisk and printed Dorski ending note retained. This printed note belongs to the example, not foreign body prose. Four margins clean. |
| 114 (42) / 1 od 1 | 2.397 | 169 / 85 | [primjer-2-397](images/02-dijatonika-c/primjer-2-397.png) | pass | Number, both systems, all lyrics and printed Frigijski ending note complete; staff ends and four margins clean, no page number. |
| 115 (43) / 1 od 1 | 2.398 | 170 / 86 | [primjer-2-398](images/02-dijatonika-c/primjer-2-398.png) | pass | Number, both systems, all Latin lyrics and printed Miksolidijski ending note retained; surrounding body paragraph excluded and four edges clean. |
| 116 (44) / 1 od 1 | 2.399 | 171 / 86 | [primjer-2-399](images/02-dijatonika-c/primjer-2-399.png) | **PROVISIONAL — cleanup required** | Bottom edge contains stem/beam fragments of following 400 at left while lowest inverted fermata of 399 lies in the same vertical band at right. A full-content rectangle cannot remove the foreign fragments. |
| 117 (45) / 1 od 1 | 2.400 | 171 / 86 | [primjer-2-400](images/02-dijatonika-c/primjer-2-400.png) | **PROVISIONAL — cleanup required** | Top includes preceding 399 inverted fermata; bottom includes following Skrjabin attribution and slur. These overlap the vertical extent of 400 highest stems and lowest slur/fermata. No clean rectangle retains all intended notation. |
| 118 (46) / 1 od 1 | 2.401 | 171 / 86 | [primjer-2-401](images/02-dijatonika-c/primjer-2-401.png) | **PROVISIONAL — cleanup required** | Top edge includes 400 slur, stem and inverted-fermata fragments. Complete Skrjabin attribution shares their vertical band; removing them with a horizontal cut loses identifying text. |
| 119 (47) / 1 od 1 | 2.402 | 171 / 86 | [primjer-2-402](images/02-dijatonika-c/primjer-2-402.png) | pass | Number, full Chopin attribution, lower stems, slurs and final barline retained; four edges clean, prose/page number excluded. |
| 120 (48) / 1 od 1 | 2.403 | 172 / 87 | [primjer-2-403](images/02-dijatonika-c/primjer-2-403.png) | pass | Number, R. Strauss attribution, full grand staff and lowest ties retained; all edges clean with genuine margins. |
| 121 (49) / 1 od 1 | 2.404 | 172 / 87 | [primjer-2-404](images/02-dijatonika-c/primjer-2-404.png) | pass | Number, Chopin attribution, upper slurs/staccatos and lowest staccatos retained; all staff ends and four margins clean. |
| 122 (50) / 1 od 1 | 2.405 | 172 / 87 | [primjer-2-405](images/02-dijatonika-c/primjer-2-405.png) | pass | Number, complete long Debussy attribution, grace note and both lowest 8va labels retained; all four edges clean. |
| 123 (51) / 1 od 1 | 2.406 | 172 / 87 | [primjer-2-406](images/02-dijatonika-c/primjer-2-406.png) | pass | Number, full Grieg attribution, upper triplet brackets and lowest bass/grace/8va notation intact; right staff ends as printed, four genuine margins, no page number. |
| 124 (52) / 1 od 1 | 2.407 | 173 / 87 | [primjer-2-407](images/02-dijatonika-c/primjer-2-407.png) | pass | Number, Debussy attribution, both systems, all low ledger notes, ties and 8va labels retained; four edges clean and following paragraph excluded. |
| 125 (53) / 1 od 1 | 2.408 | 173 / 87 | [primjer-2-408](images/02-dijatonika-c/primjer-2-408.png) | **PROVISIONAL — cleanup required** | Bottom edge includes multiple highest-stem tips of following 409a. Complete 408 lowest staccato marks reach the same vertical band, preventing a clean full-width rectangle. Foreign tips are notation, not specks. |
| 126 (54) / 1 od 2 | 2.409 | 173 / 87 | [primjer-2-409-a](images/02-dijatonika-c/primjer-2-409-a.png) | **PROVISIONAL — cleanup required** | Top edge retains preceding 408 lowest staccato fragment above the Dvorak attribution. Highest 409a stems overlap this band; moving top down clips them. Number, a, attribution and lower notation otherwise present; no safe complete rectangle. |
| 126 (54) / 2 od 2 | 2.409 | 173 / 87 | [primjer-2-409-b](images/02-dijatonika-c/primjer-2-409-b.png) | pass | Variant b and entire reduction, including complete lower enclosing bracket and real bottom margin, retained. Narrow sides exclude page number. No repeated number/attribution exists here; paired a supplies them. Four edges clean. |

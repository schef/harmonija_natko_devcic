# M08 — vizualni pregled i zapreke

Obuhvat: tiskane stranice **277–308**, 32 stranice; PDF stranice **139–155** (numeracija od 1). Ovo nije potvrda dovršenog milestonea.

## Odluka

- **81 independent_pass**: neovisno odobreni izrezi ugrađeni su u poglavlje.
- **22 cleanup_required**: vidljivo PROVISIONAL / NEODOBRENO; samo poveznice na neodobrene izvorne izreze, bez ugrađivanja.
- **2 source_damage**: vidljivo SOURCE DAMAGE / NOTATION UNCERTAIN / NEODOBRENO; samo poveznice. `crop_review_status: independent_pass` potvrđuje granice, ne čitljivost oštećene notacije.

Izvornih 82 PASS u visual-review.json uključuje dva oštećena izvora: to je 80 nekvalificiranih prolaza, a ne 82 odobrena primjera. Zaseban neovisni PASS za recrop zadatka 3 na str. 307 daje ukupno 81 odobreni izrez. Od 23 prvotna neprolaza taj je jedan riješen; preostala 22 ostaju blokirana. Odluke su preuzete od neovisnog preglednika, a ne donesene samopregledom integratora.

## Odvojene zapreke oštećenog izvora

- **4.z290-9-realizacija-cont**, tiskana 290 / PDF 146: abrazija u donjoj crtovnici prvoga sustava blizu drugoga takta te istrošena tinta uz lijevu stranu idućega sustava. Granice prolaze, ali zahvaćena notacija nije potvrđena.
- **4.31**, tiskana 295 / PDF 148: abrazija u gornjoj crtovnici varijante c. Granice prolaze; izgubljena ili istrošena notacija nije protumačena ni odobrena.

Ni jedan oštećeni izvor nije popravljen, retuširan ili prešutno odobren. Potrebna je neovisna provjera notacije ili neoštećeni izvor.

## Neriješeni izrezi

Na str. 277–285 i 290–291 izvorne rukopisne bilješke zahvaćaju primjere. Na str. 303 nastavak zadatka 2 i zadatak 3 imaju preklop tuđih figura/luka koji nije sigurno razdvojiv pravokutnikom. Coverage-recrop zadatka 3 vraća njegov luk, ali **nije prošao** pregled. Ne smije se zamijeniti prošlim recropom zadatka 3 na str. 307. Nijedan od tih 22 slučaja nije riješen digitalnim čišćenjem.

## Neovisni dokazi i integracija

- [visual-review.json](../../review-candidates/book/M08/visual-review.json)
- [recrop-review.json](../../review-candidates/book/M08/recrop-review.json)
- [images-integrated.json](../../review-candidates/book/M08/images-integrated.json)
- [INTEGRATION.md](../../review-candidates/book/M08/INTEGRATION.md)
- [Poglavlje](../../chapters/04-neakordicki-a.md)

## Svih 105 odluka po izvornim slotovima

| Slot | Identitet / izvorna oznaka | Tiskana / PDF str. | Status | Izrez |
| --- | --- | --- | --- | --- |
| 001 | `progresija-277` — nenumerirana harmonijska progresija u odlomku o zaostajalicama | 277 / 139 | `independent_pass` | [izvorni izrez](progresija-277.png) |
| 002 | `4.1` — 4.1 a–b | 277 / 139 | `cleanup_required` | [izvorni izrez](primjer-4-1.png) |
| 003 | `4.1-c` — 4.1 c (nastavak) | 278 / 140 | `cleanup_required` | [izvorni izrez](primjer-4-1-c.png) |
| 004 | `4.2` — 4.2 | 278 / 140 | `cleanup_required` | [izvorni izrez](primjer-4-2.png) |
| 005 | `4.3` — 4.3 | 280 / 141 | `cleanup_required` | [izvorni izrez](primjer-4-3.png) |
| 006 | `4.4` — 4.4 | 281 / 141 | `cleanup_required` | [izvorni izrez](primjer-4-4.png) |
| 007 | `4.5` — 4.5 | 281 / 141 | `cleanup_required` | [izvorni izrez](primjer-4-5.png) |
| 008 | `4.6` — 4.6 | 282 / 142 | `independent_pass` | [izvorni izrez](primjer-4-6.png) |
| 009 | `4.7` — 4.7 | 282 / 142 | `cleanup_required` | [izvorni izrez](primjer-4-7.png) |
| 010 | `4.8` — 4.8 | 282 / 142 | `independent_pass` | [izvorni izrez](primjer-4-8.png) |
| 011 | `4.9` — 4.9 | 282 / 142 | `cleanup_required` | [izvorni izrez](primjer-4-9.png) |
| 012 | `4.10` — 4.10 | 283 / 142 | `cleanup_required` | [izvorni izrez](primjer-4-10.png) |
| 013 | `4.11` — 4.11 | 283 / 142 | `cleanup_required` | [izvorni izrez](primjer-4-11.png) |
| 014 | `4.12` — 4.12 | 283 / 142 | `cleanup_required` | [izvorni izrez](primjer-4-12.png) |
| 015 | `4.13` — 4.13 | 283 / 142 | `independent_pass` | [izvorni izrez](primjer-4-13-coverage-recrop.png) |
| 016 | `4.14` — 4.14 | 284 / 143 | `cleanup_required` | [izvorni izrez](primjer-4-14.png) |
| 017 | `4.15` — 4.15 | 284 / 143 | `cleanup_required` | [izvorni izrez](primjer-4-15.png) |
| 018 | `4.16` — 4.16 | 284 / 143 | `cleanup_required` | [izvorni izrez](primjer-4-16.png) |
| 019 | `4.17` — 4.17 | 285 / 143 | `cleanup_required` | [izvorni izrez](primjer-4-17.png) |
| 020 | `4.18` — 4.18 | 285 / 143 | `independent_pass` | [izvorni izrez](primjer-4-18.png) |
| 021 | `4.19` — 4.19 | 286 / 144 | `independent_pass` | [izvorni izrez](primjer-4-19.png) |
| 022 | `4.20` — 4.20 | 286 / 144 | `independent_pass` | [izvorni izrez](primjer-4-20.png) |
| 023 | `4.21` — 4.21 a–c | 286 / 144 | `independent_pass` | [izvorni izrez](primjer-4-21.png) |
| 024 | `4.21-cont` — 4.21 d–f (nastavak) | 287 / 144 | `independent_pass` | [izvorni izrez](primjer-4-21-cont.png) |
| 025 | `4.z287-1` — zadatak 1 | 287 / 144 | `independent_pass` | [izvorni izrez](zadatak-4-287-1.png) |
| 026 | `4.z287-2` — zadatak 2 | 287 / 144 | `independent_pass` | [izvorni izrez](zadatak-4-287-2.png) |
| 027 | `4.z287-3` — zadatak 3 (početak) | 287 / 144 | `independent_pass` | [izvorni izrez](zadatak-4-287-3.png) |
| 028 | `4.z288-3-cont` — zadatak 3 (nastavak) | 288 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-288-3-cont.png) |
| 029 | `4.z288-4` — zadatak 4 | 288 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-288-4.png) |
| 030 | `4.z288-5` — zadatak 5 | 288 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-288-5.png) |
| 031 | `4.z288-6` — zadatak 6 | 288 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-288-6.png) |
| 032 | `4.z288-7` — zadatak 7 | 288 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-288-7.png) |
| 033 | `4.z288-8` — zadatak 8 | 288 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-288-8.png) |
| 034 | `4.z289-9` — zadatak 9 | 289 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-289-9.png) |
| 035 | `4.z289-10` — zadatak 10 | 289 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-289-10.png) |
| 036 | `4.z289-11` — zadatak 11 | 289 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-289-11.png) |
| 037 | `4.z289-12` — zadatak 12 | 289 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-289-12.png) |
| 038 | `4.z289-13` — zadatak 13 | 289 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-289-13.png) |
| 039 | `4.z289-9-realizacija` — Realizacija zadatka 9 (početak) | 289 / 145 | `independent_pass` | [izvorni izrez](zadatak-4-289-9-realizacija-naslov-recrop.png) |
| 040 | `4.z290-9-realizacija-cont` — Realizacija zadatka 9 (nastavak) | 290 / 146 | `source_damage` | [izvorni izrez](zadatak-4-290-9-realizacija-cont.png) |
| 041 | `4.22` — 4.22 | 290 / 146 | `cleanup_required` | [izvorni izrez](primjer-4-22.png) |
| 042 | `4.23` — 4.23 | 291 / 146 | `cleanup_required` | [izvorni izrez](primjer-4-23.png) |
| 043 | `4.24` — 4.24 | 291 / 146 | `cleanup_required` | [izvorni izrez](primjer-4-24.png) |
| 044 | `4.25` — 4.25 | 291 / 146 | `cleanup_required` | [izvorni izrez](primjer-4-25.png) |
| 045 | `4.26` — 4.26 | 291 / 146 | `cleanup_required` | [izvorni izrez](primjer-4-26.png) |
| 046 | `4.27` — 4.27 | 292 / 147 | `independent_pass` | [izvorni izrez](primjer-4-27.png) |
| 047 | `4.28` — 4.28 | 292 / 147 | `independent_pass` | [izvorni izrez](primjer-4-28.png) |
| 048 | `4.29` — 4.29 | 292 / 147 | `independent_pass` | [izvorni izrez](primjer-4-29.png) |
| 049 | `4.30` — 4.30 | 292 / 147 | `independent_pass` | [izvorni izrez](primjer-4-30.png) |
| 050 | `4.z293-1` — 4.1.3 — zadatak 1 | 293 / 147 | `independent_pass` | [izvorni izrez](zadatak-4-293-1.png) |
| 051 | `4.z293-2` — 4.1.3 — zadatak 2 | 293 / 147 | `independent_pass` | [izvorni izrez](zadatak-4-293-2.png) |
| 052 | `4.z293-3` — 4.1.3 — zadatak 3 | 293 / 147 | `independent_pass` | [izvorni izrez](zadatak-4-293-3.png) |
| 053 | `4.z293-4` — 4.1.3 — zadatak 4 | 293 / 147 | `independent_pass` | [izvorni izrez](zadatak-4-293-4.png) |
| 054 | `4.z293-5` — 4.1.3 — zadatak 5 | 293 / 147 | `independent_pass` | [izvorni izrez](zadatak-4-293-5.png) |
| 055 | `4.z293-6` — 4.1.3 — zadatak 6 (početak) | 293 / 147 | `independent_pass` | [izvorni izrez](zadatak-4-293-6.png) |
| 056 | `4.z294-6-cont` — 4.1.3 — zadatak 6 (nastavak) | 294 / 148 | `independent_pass` | [izvorni izrez](zadatak-4-294-6-cont.png) |
| 057 | `4.z294-7` — 4.1.3 — zadatak 7 | 294 / 148 | `independent_pass` | [izvorni izrez](zadatak-4-294-7.png) |
| 058 | `4.z294-5-realizacija` — 4.1.3 — Realizacija zadatka 5 | 294 / 148 | `independent_pass` | [izvorni izrez](zadatak-4-294-5-realizacija-naslov-recrop.png) |
| 059 | `4.31` — 4.31 a–d | 295 / 148 | `source_damage` | [izvorni izrez](primjer-4-31.png) |
| 060 | `4.32` — 4.32 a–c | 295 / 148 | `independent_pass` | [izvorni izrez](primjer-4-32.png) |
| 061 | `4.33` — 4.33 a–c | 295 / 148 | `independent_pass` | [izvorni izrez](primjer-4-33.png) |
| 062 | `4.34` — 4.34 a–c | 295 / 148 | `independent_pass` | [izvorni izrez](primjer-4-34.png) |
| 063 | `4.35` — 4.35 a–e | 296 / 149 | `independent_pass` | [izvorni izrez](primjer-4-35.png) |
| 064 | `4.z296-1` — 4.1.4 — zadatak 1 | 296 / 149 | `independent_pass` | [izvorni izrez](zadatak-4-296-1.png) |
| 065 | `4.z296-2` — 4.1.4 — zadatak 2 | 296 / 149 | `independent_pass` | [izvorni izrez](zadatak-4-296-2.png) |
| 066 | `4.z297-3` — 4.1.4 — zadatak 3 | 297 / 149 | `independent_pass` | [izvorni izrez](zadatak-4-297-3.png) |
| 067 | `4.z297-4` — 4.1.4 — zadatak 4 | 297 / 149 | `independent_pass` | [izvorni izrez](zadatak-4-297-4.png) |
| 068 | `4.z297-3-realizacija` — 4.1.4 — Realizacija zadatka 3 | 297 / 149 | `independent_pass` | [izvorni izrez](zadatak-4-297-3-realizacija-naslov-recrop.png) |
| 069 | `4.36` — 4.36 a–d | 298 / 150 | `independent_pass` | [izvorni izrez](primjer-4-36.png) |
| 070 | `4.37` — 4.37 a–b | 298 / 150 | `independent_pass` | [izvorni izrez](primjer-4-37.png) |
| 071 | `4.z298-1` — 4.1.5 — zadatak 1 (početak) | 298 / 150 | `independent_pass` | [izvorni izrez](zadatak-4-298-1.png) |
| 072 | `4.z299-1-cont` — 4.1.5 — zadatak 1 (nastavak) | 299 / 150 | `independent_pass` | [izvorni izrez](zadatak-4-299-1-cont.png) |
| 073 | `4.z299-2` — 4.1.5 — zadatak 2 | 299 / 150 | `independent_pass` | [izvorni izrez](zadatak-4-299-2.png) |
| 074 | `4.38` — 4.38 a–f | 299 / 150 | `independent_pass` | [izvorni izrez](primjer-4-38.png) |
| 075 | `4.39` — 4.39 a–c | 300 / 151 | `independent_pass` | [izvorni izrez](primjer-4-39.png) |
| 076 | `4.40` — 4.40 a–b | 300 / 151 | `independent_pass` | [izvorni izrez](primjer-4-40.png) |
| 077 | `4.41` — 4.41 a–e | 300 / 151 | `independent_pass` | [izvorni izrez](primjer-4-41.png) |
| 078 | `4.42` — 4.42 a–d | 301 / 151 | `independent_pass` | [izvorni izrez](primjer-4-42.png) |
| 079 | `4.43` — 4.43 a–d | 301 / 151 | `independent_pass` | [izvorni izrez](primjer-4-43.png) |
| 080 | `4.44` — 4.44 a–d | 301 / 151 | `independent_pass` | [izvorni izrez](primjer-4-44.png) |
| 081 | `4.45` — 4.45 a–d | 302 / 152 | `independent_pass` | [izvorni izrez](primjer-4-45.png) |
| 082 | `4.z302-1` — 4.1.6 — zadatak 1 | 302 / 152 | `independent_pass` | [izvorni izrez](zadatak-4-302-1.png) |
| 083 | `4.z302-2` — 4.1.6 — zadatak 2 (početak) | 302 / 152 | `independent_pass` | [izvorni izrez](zadatak-4-302-2.png) |
| 084 | `4.z303-2-cont` — 4.1.6 — zadatak 2 (nastavak) | 303 / 152 | `cleanup_required` | [izvorni izrez](zadatak-4-303-2-cont.png) |
| 085 | `4.z303-3` — 4.1.6 — zadatak 3 | 303 / 152 | `cleanup_required` | [izvorni izrez](zadatak-4-303-3-coverage-recrop.png) |
| 086 | `4.z303-4` — 4.1.6 — zadatak 4 | 303 / 152 | `independent_pass` | [izvorni izrez](zadatak-4-303-4.png) |
| 087 | `4.z303-5` — 4.1.6 — zadatak 5 | 303 / 152 | `independent_pass` | [izvorni izrez](zadatak-4-303-5.png) |
| 088 | `4.z303-6` — 4.1.6 — zadatak 6 | 303 / 152 | `independent_pass` | [izvorni izrez](zadatak-4-303-6.png) |
| 089 | `4.z303-3-realizacija` — 4.1.6 — Realizacija zadatka 3 (početak) | 303 / 152 | `independent_pass` | [izvorni izrez](zadatak-4-303-3-realizacija-naslov-recrop.png) |
| 090 | `4.z304-3-realizacija-cont` — 4.1.6 — Realizacija zadatka 3 (nastavak; oznake * i **) | 304 / 153 | `independent_pass` | [izvorni izrez](zadatak-4-304-3-realizacija-cont.png) |
| 091 | `sifra-appoggiature-304` — 4.1.6 — šifra trostruke appoggiature u bilješci ** (9/7/4 > 8/3) | 304 / 153 | `independent_pass` | [izvorni izrez](sifra-appoggiature-304.png) |
| 092 | `4.46` — 4.46 a–h, itd. | 304 / 153 | `independent_pass` | [izvorni izrez](primjer-4-46.png) |
| 093 | `4.47` — 4.47 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](primjer-4-47.png) |
| 094 | `4.48` — 4.48 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](primjer-4-48.png) |
| 095 | `4.49` — 4.49 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](primjer-4-49.png) |
| 096 | `4.50` — 4.50 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](primjer-4-50.png) |
| 097 | `4.51` — 4.51 a–b | 306 / 154 | `independent_pass` | [izvorni izrez](primjer-4-51.png) |
| 098 | `4.52` — 4.52 — (Chopin: Mazurka op. 63 br. 1) | 306 / 154 | `independent_pass` | [izvorni izrez](primjer-4-52.png) |
| 099 | `4.z306-1` — 4.1.7 — zadatak 1 | 306 / 154 | `independent_pass` | [izvorni izrez](zadatak-4-306-1-coverage-recrop.png) |
| 100 | `4.z306-2` — 4.1.7 — zadatak 2 (početak) | 306 / 154 | `independent_pass` | [izvorni izrez](zadatak-4-306-2-coverage-recrop.png) |
| 101 | `4.z307-2-cont` — 4.1.7 — zadatak 2 (nastavak) | 307 / 154 | `independent_pass` | [izvorni izrez](zadatak-4-307-2-cont.png) |
| 102 | `4.z307-3` — 4.1.7 — zadatak 3 | 307 / 154 | `independent_pass` | [izvorni izrez](recrops/zadatak-4-307-3.png) |
| 103 | `4.z307-4` — 4.1.7 — zadatak 4 | 307 / 154 | `independent_pass` | [izvorni izrez](zadatak-4-307-4.png) |
| 104 | `4.z307-5` — 4.1.7 — zadatak 5 | 307 / 154 | `independent_pass` | [izvorni izrez](zadatak-4-307-5.png) |
| 105 | `4.z308-3-realizacija` — 4.1.7 — Realizacija zadatka 3 | 308 / 155 | `independent_pass` | [izvorni izrez](zadatak-4-308-3-realizacija-naslov-recrop.png) |

## Razlozi neodobravanja

- **4.1**, tiskana str. 277, `cleanup_required`: Printed number and variants a–b are retained, but source handwriting lies above, between and below the staves and within the example's rectangular extent. Fails the no-handwriting checklist; no safe rectangular replacement proposed.
- **4.1-c**, tiskana str. 278, `cleanup_required`: Continuation c correctly pairs with 4.1 on page 277; the source does not repeat its number. Handwritten analysis remains around and within the notation, including the lower edge. No safe rectangular replacement proposed.
- **4.2**, tiskana str. 278, `cleanup_required`: Number, variants a–b and staff ends are present, but handwriting overlaps the interior and lower analysis region. Cannot approve under the no-handwriting checklist; no safe rectangular replacement proposed.
- **4.3**, tiskana str. 280, `cleanup_required`: Number and variants a–c are present. Handwriting at the upper/left boundaries and among the printed notation and figures prevents a clean score-only rectangle.
- **4.4**, tiskana str. 281, `cleanup_required`: Number, a–b and printed analysis are retained, but handwritten analysis occupies the space between the staves and around the upper and lower notation. No safe rectangular replacement proposed.
- **4.5**, tiskana str. 281, `cleanup_required`: Complete a–b notation is accompanied by source handwriting within the example and beneath the bass. Fails the no-handwriting and clean-margin requirements.
- **4.7**, tiskana str. 282, `cleanup_required`: Number and both printed demonstrations are intact, but handwriting remains above and within the staff/analysis area and near the lower edge. No safe rectangular replacement proposed.
- **4.9**, tiskana str. 282, `cleanup_required`: Number and all printed material are present, but source handwriting is visible above and within the example. Keeping all printed notation does not yield a handwriting-free rectangle.
- **4.10**, tiskana str. 283, `cleanup_required`: Number and a–c are retained, but handwritten harmonic analysis remains below the bass and inside the printed example's extent. No safe rectangular replacement proposed.
- **4.11**, tiskana str. 283, `cleanup_required`: Printed number, NE labels and notation are complete. Handwritten figures immediately beneath the bass intrude into the lower margin; enlarged source inspection shows no safe horizontal cut demonstrated that preserves every low stem and removes the handwriting.
- **4.12**, tiskana str. 283, `cleanup_required`: Number, a–d and notation are retained, but handwritten analysis remains within/below the bass region, including the bottom boundary. No safe rectangular replacement proposed.
- **4.14**, tiskana str. 284, `cleanup_required`: Number and Bach chorale attribution are retained. Source handwriting intrudes between the staves and throughout the lower annotation area; no clean score-only rectangle proposed.
- **4.15**, tiskana str. 284, `cleanup_required`: Number, Bach chorale attribution and staff ends are present, but handwritten analysis remains at the upper and lower boundaries and within the example. No safe rectangular replacement proposed.
- **4.16**, tiskana str. 284, `cleanup_required`: Number, Bach chorale attribution and notation are retained. Handwritten marks occur inside the example and at its upper/lower boundaries; cannot pass the clean-source checklist by the current crop.
- **4.17**, tiskana str. 285, `cleanup_required`: Number, both rows and variants a–i are retained. Source handwriting is interspersed with notation/analysis and reaches the upper and side regions. No safe rectangular replacement proposed.
- **4.z290-9-realizacija-cont**, tiskana str. 290, `source_damage`: Both continuation systems and printed analysis are within clean boundaries; paired title on page 289 is correct. White abrasion already in the source removes ink in the first system's lower staff near its second measure, with further worn ink near the next system's left side. This is source damage, not crop clipping; exact affected notation is not certified.
- **4.22**, tiskana str. 290, `cleanup_required`: Number and a–e are retained, but faint handwritten analysis lies within the staff/analysis area and near the top. No safe rectangular replacement proposed.
- **4.23**, tiskana str. 291, `cleanup_required`: Number, a–c and printed notation/figures are retained, but faint handwriting occurs between staves and alongside/below bass figures. No safe rectangular replacement proposed.
- **4.24**, tiskana str. 291, `cleanup_required`: Number and a–c are retained. Handwritten figures remain above and between staves and below printed analysis; cannot pass the no-handwriting checklist.
- **4.25**, tiskana str. 291, `cleanup_required`: Number and a–c are retained, but handwritten analysis occurs within the notation area and below printed figures. No safe rectangular replacement proposed.
- **4.26**, tiskana str. 291, `cleanup_required`: Number and a–b are complete, but extensive handwritten arrows and harmonic analysis are interspersed with the score and extend into top/bottom margins. No safe rectangular replacement proposed.
- **4.31**, tiskana str. 295, `source_damage`: Number, a–d, all available printed notation and analysis retained inside clean margins. White abrasion in variant c's upper staff is already present in the authoritative source, not introduced by cropping. Missing/worn notation there remains source-limited and is not interpreted here.
- **4.z303-2-cont**, tiskana str. 303, `cleanup_required`: Complete two-row continuation and low figures retained, but bottom includes part of exercise 3's upper slur. Enlarged source confirms exercise 2's lowest figures overlap exercise 3's slur in vertical range. Straight rectangular separation cannot retain both complete examples without foreign ink; no safe rectangle proposed.
- **4.z303-3**, tiskana str. 303, `cleanup_required`: Current extractor recrop restores exercise ID 3 and its complete upper slur, but partial preceding exercise-2 figures remain at the top. Enlarged source confirms vertical overlap; moving top down would clip the intended slur. No safe rectangular replacement proposed.

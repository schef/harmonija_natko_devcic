# M11 integration hand-off

**Text integration verified; image integration remains provisional: 36 independent passes and 8 cleanup-required slots. Not ready for milestone completion.**

## Scope and boundaries

- Assigned printed pages **379–411**, PDF pages **190–206 (1-based)**; all 33 text pages have supplied visual-verification records. Source mapping is checked against `sources/index.json`, not a guessed offset.
- `chapters/05-rekapitulacija.md`: actual numbered chapter 5, printed 379–385.
- `chapters/dodaci.md`: unnumbered OBILJEŽAVANJE AKORDA 386–387; blank 388; terms 389–392; concept index 393–405; blank 406; name index 407–408; contents 409–411.
- Split at the actual source-page 386 marker, not at 389. The original boundary/output-section comments before 386 remain at the end of chapter 5; no printed prose moves across that source boundary.

## Text fidelity and formatting

All ten shards are concatenated in source order. Every paragraph, heading, table row, name, reference, range, footnote 8, continuation comment and printed anomaly is preserved verbatim. Only trailing file-boundary newlines are normalized to one newline when concatenating. **No heading levels or heading spacing changed.** Editorial table-header disclaimers are retained, as are original table breaks at page boundaries. No table is treated as an image slot. Blanks 388 and 406 retain only source/editorial metadata; no blank-page prose is invented. Source anomalies including Qurstand, Septimmenakkord, 76. 175, 166. 167, missing/terminal commas, unsorted Wagner references and the printed contents 2.9.3/2.9.4 wording remain unchanged.

Image captions are editorial footnotes (`m11v01`–`m11v44`) linked immediately at the original visual markers. Each supplies the actual printed page, PDF page and MuseScore TODO. These uniquely named footnotes cannot collide with source footnote 8. Inline parentheses and punctuation remain in the verified prose exactly once; blocked glyphs are explicit unapproved placeholders, not guessed notation.

## Image provenance and status

44 visual slots: 19 score/exercise-realization parts and 25 inline glyphs, all on printed 379–387. Original independent review: 35 PASS, 8 source-layout blocks and one recrop required. The separate recrop review approves only task 6 at `images/05-rekapitulacija/recrops/primjer-5-6.png`, yielding **36 independent_pass + 8 cleanup_required**. No original manifests or images are modified. All 44 declared rectangles exactly match decoded RGB source pixels, including the blocked rectangles; provenance is not a substitute for edge approval.

Legacy `primjer-5-N` means printed ZADACI task N, not example 5.N. Realizations are identified as realizations of tasks 4 and 9. Tasks 10 and 13 retain first-part/continuation captions without inventing a repeated printed number.

| Slot | Identity / printed caption | Printed / PDF | Crop | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 01 | `M11-primjer-5-1` — Zadatak 1. | 379 / 190 | [PNG](../../../images/05-rekapitulacija/primjer-5-1.png) | independent_pass | [review](visual-review.json) |
| 02 | `M11-primjer-5-2` — Zadatak 2. | 379 / 190 | [PNG](../../../images/05-rekapitulacija/primjer-5-2.png) | independent_pass | [review](visual-review.json) |
| 03 | `M11-primjer-5-3` — Zadatak 3. | 380 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-3.png) | independent_pass | [review](visual-review.json) |
| 04 | `M11-primjer-5-4` — Zadatak 4. | 380 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-4.png) | independent_pass | [review](visual-review.json) |
| 05 | `M11-primjer-5-5` — Zadatak 5. | 380 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-5.png) | independent_pass | [review](visual-review.json) |
| 06 | `M11-primjer-5-6` — Zadatak 6. | 380 / 191 | [PNG](../../../images/05-rekapitulacija/recrops/primjer-5-6.png) | independent_pass | [review](recrop-review.json) |
| 07 | `M11-primjer-5-7` — Zadatak 7. | 381 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-7.png) | independent_pass | [review](visual-review.json) |
| 08 | `M11-primjer-5-8` — Zadatak 8. | 381 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-8.png) | independent_pass | [review](visual-review.json) |
| 09 | `M11-primjer-5-9` — Zadatak 9. | 381 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-9.png) | cleanup_required | [review](visual-review.json) |
| 10 | `M11-primjer-5-10-part-1` — Zadatak 10., prvi dio. | 381 / 191 | [PNG](../../../images/05-rekapitulacija/primjer-5-10-part-1.png) | cleanup_required | [review](visual-review.json) |
| 11 | `M11-primjer-5-10-part-2` — Zadatak 10., nastavak sa str. 381. | 382 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-10-part-2.png) | independent_pass | [review](visual-review.json) |
| 12 | `M11-primjer-5-11` — Zadatak 11. | 382 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-11.png) | cleanup_required | [review](visual-review.json) |
| 13 | `M11-primjer-5-12` — Zadatak 12. | 382 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-12.png) | cleanup_required | [review](visual-review.json) |
| 14 | `M11-primjer-5-13-part-1` — Zadatak 13., prvi dio. | 382 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-13-part-1.png) | independent_pass | [review](visual-review.json) |
| 15 | `M11-primjer-5-13-part-2` — Zadatak 13., nastavak sa str. 382. | 383 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-13-part-2.png) | independent_pass | [review](visual-review.json) |
| 16 | `M11-primjer-5-14` — Zadatak 14. | 383 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-14.png) | independent_pass | [review](visual-review.json) |
| 17 | `M11-primjer-5-15` — Zadatak 15. | 383 / 192 | [PNG](../../../images/05-rekapitulacija/primjer-5-15.png) | independent_pass | [review](visual-review.json) |
| 18 | `M11-slika-384-1` — Realizacija zadatka 4. | 384 / 193 | [PNG](../../../images/05-rekapitulacija/slika-384-1.png) | independent_pass | [review](visual-review.json) |
| 19 | `M11-slika-385-1` — Realizacija zadatka 9. | 385 / 193 | [PNG](../../../images/05-rekapitulacija/slika-385-1.png) | independent_pass | [review](visual-review.json) |
| 20 | `M11-slika-386-1` — Oznaka povišene kvarte: ♯4. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-1-recrop-m11.png) | cleanup_required | [review](visual-review.json) |
| 21 | `M11-slika-386-2` — Brojka 4 precrtana kosim potezom. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-2-recrop-m11.png) | cleanup_required | [review](visual-review.json) |
| 22 | `M11-slika-386-3` — Kosi potezi za ponavljanje prethodne oznake. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-3-recrop-m11.png) | independent_pass | [review](visual-review.json) |
| 23 | `M11-slika-386-4` — Precrtana brojka 5 u francuskom obilježavanju. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-4-recrop-m11.png) | independent_pass | [review](visual-review.json) |
| 24 | `M11-slika-386-5` — Precrtana brojka 7 u francuskom obilježavanju. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-5-recrop-m11.png) | cleanup_required | [review](visual-review.json) |
| 25 | `M11-slika-386-6` — Francuska oznaka dominantnog septakorda. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-6.png) | independent_pass | [review](visual-review.json) |
| 26 | `M11-slika-386-7` — Francuska oznaka dominantnog kvintsekstakorda. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-7.png) | independent_pass | [review](visual-review.json) |
| 27 | `M11-slika-386-8` — Francuska oznaka dominantnog terckvartakorda. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-8.png) | independent_pass | [review](visual-review.json) |
| 28 | `M11-slika-386-9` — Francuska oznaka dominantnog sekundakorda. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-9.png) | independent_pass | [review](visual-review.json) |
| 29 | `M11-slika-386-10` — Francuska oznaka prvog obrata smanjenog septakorda. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-10.png) | independent_pass | [review](visual-review.json) |
| 30 | `M11-slika-386-11` — Francuska oznaka drugog obrata smanjenog septakorda. | 386 / 194 | [PNG](../../../images/dodaci/slika-386-11.png) | independent_pass | [review](visual-review.json) |
| 31 | `M11-slika-387-1` — Varijanta oznake s razrješilicom. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-1.png) | independent_pass | [review](visual-review.json) |
| 32 | `M11-slika-387-2` — Varijanta oznake s povisilicom. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-2.png) | independent_pass | [review](visual-review.json) |
| 33 | `M11-slika-387-3` — Varijanta oznake sa snizilicom. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-3.png) | independent_pass | [review](visual-review.json) |
| 34 | `M11-slika-387-4` — Francuska oznaka dominantnog nonakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-4.png) | independent_pass | [review](visual-review.json) |
| 35 | `M11-slika-387-5` — Francuska oznaka prvog obrata dominantnog nonakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-5.png) | independent_pass | [review](visual-review.json) |
| 36 | `M11-slika-387-6` — Francuska oznaka drugog obrata dominantnog nonakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-6.png) | independent_pass | [review](visual-review.json) |
| 37 | `M11-slika-387-7` — Francuska oznaka trećeg obrata dominantnog nonakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-7.png) | independent_pass | [review](visual-review.json) |
| 38 | `M11-slika-387-8` — Francuska oznaka zaostajalice na basov ton kvintakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-8.png) | independent_pass | [review](visual-review.json) |
| 39 | `M11-slika-387-9` — Francuska oznaka zaostajalice na basov ton sekstakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-9.png) | independent_pass | [review](visual-review.json) |
| 40 | `M11-slika-387-10` — Francuska oznaka zaostajalice na basov ton kvintsekstakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-10.png) | independent_pass | [review](visual-review.json) |
| 41 | `M11-slika-387-11` — Oznaka rješenja zaostajalice na basov ton kvintsekstakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-11.png) | independent_pass | [review](visual-review.json) |
| 42 | `M11-slika-387-12` — Francuska oznaka zaostajalice na basov ton terckvartakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-12.png) | independent_pass | [review](visual-review.json) |
| 43 | `M11-slika-387-13` — Oznaka rješenja zaostajalice na basov ton terckvartakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-13-recrop-m11.png) | independent_pass | [review](visual-review.json) |
| 44 | `M11-slika-387-14` — Alternativna oznaka smanjene kvinte odnosno smanjenog kvintakorda. | 387 / 194 | [PNG](../../../images/dodaci/slika-387-14-recrop-m11.png) | cleanup_required | [review](visual-review.json) |

## Eight unresolved slots — recrop required

- **Slot 09, M11-primjer-5-9, p. 381:** Bottom edge contains coherent upper portions of the following exercise 10 title Andantino. Exercise 9's low ending slurs occupy the same vertical band elsewhere across the width. Raising the bottom would clip those slurs; moving a side would lose exercise content. No safe single source rectangle certified. Printed 9 and remaining notation otherwise present; requires a separately reviewed source-only multipart solution, not erasure.
- **Slot 10, M11-primjer-5-10-part-1, p. 381:** Top contains cut-off low slurs/accidental from exercise 9, while Andantino genuinely belongs to exercise 10 and must remain. Their vertical ranges overlap. No safe full-width rectangle certified. Printed 10 and three systems retained; continuation pairing is correct, but this first part is not clean.
- **Slot 12, M11-primjer-5-11, p. 382:** Contains unrelated Risoluto title of exercise 12 at lower left. The genuine final reduction, its low beams and closing chord of exercise 11 extend into the same vertical band at right. Removing the title by a straight bottom crop would remove the reduction. No safe single rectangle certified. Printed 11 and four main systems are otherwise intact.
- **Slot 13, M11-primjer-5-12, p. 382:** Top-right edge retains cut-off reduction/beams and chord belonging to exercise 11. Risoluto belongs to exercise 12 at top left and cannot be discarded. No safe single rectangle certified because the two occupy the same vertical range. Printed 12, five systems, riten. and low ending sharp otherwise retained.
- **Slot 20, M11-slika-386-1, p. 386:** Complete sharp and 4 retained, but coherent tops of the next prose line remain at lower right. Sharp descender and next-line ink overlap in vertical range; shortening the rectangle clips the sharp. No safe combined rectangle certified. A split sharp/4 representation would need new extraction and review; no stitching or retouch approved.
- **Slot 21, M11-slika-386-2, p. 386:** Slashed 4 and its lower slash tip retained, but right edge contains coherent fragments of closing parenthesis, not scan specks. Full glyph and parenthesis overlap in horizontal range, so narrowing would clip glyph. Text already supplies parentheses; do not integrate fragments or duplicate punctuation. No safe glyph-only rectangle certified.
- **Slot 24, M11-slika-386-5, p. 386:** Bottom-left black blob is coherent next-line i dot, not part of the slashed 7 or a random speck. Enlarged source also shows upper slash ink at y=1724, while current top=1725 loses its first tip pixel; extending to 1724 includes preceding-line descender at left. Lower slash reaches y=1773 and i dot begins y=1774. Tested temporary alternatives were rejected; no safe complete rectangular glyph-only replacement certified. Keep notation/separation uncertainty on parent hold; do not clip tips or paint out prose.
- **Slot 44, M11-slika-387-14, p. 387:** Full overbar and 5 retained, but coherent sentence period remains at lower right and is already represented after the text slot. Full overbar extends farther right than the period's left edge, preventing a clean glyph-only rectangle without clipping notation. No safe replacement rectangle certified; do not shorten overbar, erase period or duplicate punctuation.

Do not clip genuine notation, erase adjacent ink, synthesize glyphs, add borders, or silently approve a source-limited rectangle. A new source-only solution needs independent review.

## 33-page coverage and tables

| Printed | PDF (1-based) | Output | Verified shard | Data rows |
| --- | --- | --- | --- | --- |
| 379 | 190 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 380 | 191 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 381 | 191 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 382 | 192 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 383 | 192 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 384 | 193 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 385 | 193 | [05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md) | [text-379-387.md](text-379-387.md) | 0 |
| 386 | 194 | [dodaci.md](../../../chapters/dodaci.md) | [text-379-387.md](text-379-387.md) | 0 |
| 387 | 194 | [dodaci.md](../../../chapters/dodaci.md) | [text-379-387.md](text-379-387.md) | 0 |
| 388 | 195 | [dodaci.md](../../../chapters/dodaci.md) | [text-388-389.md](text-388-389.md) | 0 |
| 389 | 195 | [dodaci.md](../../../chapters/dodaci.md) | [text-388-389.md](text-388-389.md) | 15 |
| 390 | 196 | [dodaci.md](../../../chapters/dodaci.md) | [text-390-391.md](text-390-391.md) | 22 |
| 391 | 196 | [dodaci.md](../../../chapters/dodaci.md) | [text-390-391.md](text-390-391.md) | 20 |
| 392 | 197 | [dodaci.md](../../../chapters/dodaci.md) | [text-392.md](text-392.md) | 21 |
| 393 | 197 | [dodaci.md](../../../chapters/dodaci.md) | [text-393.md](text-393.md) | 37 |
| 394 | 198 | [dodaci.md](../../../chapters/dodaci.md) | [text-394.md](text-394.md) | 38 |
| 395 | 198 | [dodaci.md](../../../chapters/dodaci.md) | [text-395-396.md](text-395-396.md) | 39 |
| 396 | 199 | [dodaci.md](../../../chapters/dodaci.md) | [text-395-396.md](text-395-396.md) | 41 |
| 397 | 199 | [dodaci.md](../../../chapters/dodaci.md) | [text-397-399.md](text-397-399.md) | 42 |
| 398 | 200 | [dodaci.md](../../../chapters/dodaci.md) | [text-397-399.md](text-397-399.md) | 29 |
| 399 | 200 | [dodaci.md](../../../chapters/dodaci.md) | [text-397-399.md](text-397-399.md) | 41 |
| 400 | 201 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 45 |
| 401 | 201 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 43 |
| 402 | 202 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 43 |
| 403 | 202 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 39 |
| 404 | 203 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 34 |
| 405 | 203 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 5 |
| 406 | 204 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 0 |
| 407 | 204 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 23 |
| 408 | 205 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 10 |
| 409 | 205 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 32 |
| 410 | 206 | [dodaci.md](../../../chapters/dodaci.md) | [text-400-410.md](text-400-410.md) | 38 |
| 411 | 206 | [dodaci.md](../../../chapters/dodaci.md) | [text-411.md](text-411.md) | 29 |

All 730 table lines (including editorial headers/separators) passed exact sequence equality after reversing image additions; every data row and reference is unchanged. Supplied text-review JSON schemas were read using verified / visually_verified / all_rows_verified and pdf_page / pdf_page_1based.

## Validation

- PASS: full text exact roundtrip after removing only new image blocks and editorial image-caption notes.
- PASS: every source-page marker 379–411 occurs exactly once, in order, across the two outputs; PDF values equal the actual source index.
- PASS: blank 388/406 contain no non-comment text.
- PASS: all original tables, names, ranges, references, footnote 8 and source continuations preserved.
- PASS: all 44 marker identities/pages match catalog records and review decisions; review evidence/image paths agree.
- PASS: all 44 PNGs decoded and compared pixel-for-pixel against their source rectangles; RGB hashes and dimensions recorded in images-integrated.json.
- PASS: 36 approved embeds, 8 provisional non-embed source-crop links; every slot retains caption, source page and MuseScore placeholder.
- PASS: all generated Markdown local file links resolve relative to their containing file; editorial image-footnote definitions each occur exactly once.
- No fresh visual approval is asserted. No image, raw manifest, global tracker, unrelated user work, commit or push was changed.

## Files created

- [chapters/05-rekapitulacija.md](../../../chapters/05-rekapitulacija.md)
- [chapters/dodaci.md](../../../chapters/dodaci.md)
- [images/05-rekapitulacija/REVIEW.md](../../../images/05-rekapitulacija/REVIEW.md)
- [images/dodaci/REVIEW.md](../../../images/dodaci/REVIEW.md)
- [review-candidates/book/M11/images-integrated.json](images-integrated.json)
- [review-candidates/book/M11/INTEGRATION.md](INTEGRATION.md)

## Readiness

No unreadable prose is reported in supplied text reviews. The eight image holds above are the remaining incomplete source-layout separations (one glyph also has a clipped-tip concern); they remain visibly provisional. This bounded integration is ready for parent inspection, **not final milestone completion**. No human approval is requested or claimed.

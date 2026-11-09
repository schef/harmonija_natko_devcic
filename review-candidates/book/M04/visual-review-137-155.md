# Independent visual review — printed pages 137–155

**73 reviewed: 65 PASS, 8 RECROP_REQUIRED, 0 unreviewed. Not ready for integration.**

Assigned source: printed **137–155**, PDF **69–78 (1-based)** / indices **68–77 (0-based)** of `pdfcoffee.com_natko-devi-harmonija-pdf-free.pdf`.

## Scope and verification

- One independent reviewer; no delegation, model/API calls, or GUI. No candidate images, manifests, chapter, or milestone tracker were edited. No commit/push or human approval was requested or performed.
- Compared every crop with the authoritative source page, including number, variants, attribution, notation, analysis, lowest stems, staff ends and continuation content.
- Inspected **all four edges of all 73 crops at native resolution**, using separately labelled edge strips, native-size crop sheets divided into smaller groups where needed, and enlarged tight/ambiguous source details. Grey labels on temporary review sheets are outside the actual crops, not added image borders.
- Verified all 73 image files are pixel-identical to the source rectangles in `review-candidates/book/M04/images-137-155.json`.
- Independently rendered PDF pages 69–78 with `pdftoppm -r 300 -png`; **all 19 indexed source-page halves are pixel-identical to the fresh PDF render**. Thus the comparison did not rely on an unverified derivative or embedded OCR.
- Read-only mapping check: **72 unique visual slots** in `review-candidates/book/M04/text-137-155.md` exactly match the manifest's unique `(example, printed_page)` pairs. There are **71 distinct example numbers**, 2.302–2.372; 2.305 spans two page slots; 2.325 has two images in one slot. All 73 IDs and image paths are accounted for.
- A PASS includes a clean four-edge/source check: genuine source whitespace on feasible edges; no clipped own notation/analysis/attribution; no foreign prose, running header/footer, printed page number, neighbouring notation or handwriting. Incidental isolated scan flecks were distinguished from structured handwritten strokes and partial printed characters.
- This is image/visual-slot review, not a new prose-transcription review or approval of an as-yet-unperformed chapter integration. Manifest captions/page references match the source; chapter image alt text has not been independently integrated here.

## Source-limited failures and rectangle proposals

All eight failures are **source-limited for a single rectangular crop**. A foreign element lies inside the bounding rectangle required to preserve all own content. Merely tightening the crop would clip a required title, number, staff, stem or analysis. The current crops must not be accepted merely because the main staves remain visible.

**No safe replacement rectangle is proposed.** Every `proposed_rect` is `null`; no untested coordinates are presented. Accordingly there were **zero proposal crops to test**. Temporary native/enlarged inspection crops were made only under `/tmp/opencode/m04-visual-137-155/`. No erasure, painting, artificial margin, or retouching was applied. A future separately assigned source-only multipart extraction could be assessed independently; it is not silently authorized or approved by this report.

| ID | Required correction / source limitation |
| --- | --- |
| `primjer-2-317` | Top contains a thin fragment of preceding prose/underline. Bottom contains 2.318's C–E title, clef tip and upper marks. Its own A:IV-natural analysis and low bass stem interleave the next title. Top-only tightening cannot cure the lower contamination. |
| `primjer-2-318` | Upper edge includes previous C:II/A:IV-natural analysis and a low stem fragment. Own C–E title occupies overlapping heights. Short source marks also sit just above the upper staff. Lowering the top would remove own title. |
| `primjer-2-321` | Enlarged source shows faint deliberate angular handwritten-looking strokes beside As:VI, not merely random isolated dirt. They lie within the required score/analysis bounds. A side/bottom cut would clip required content. |
| `primjer-2-323` | Upper edge admits the descender of prose word *pet*, touching/overlapping C–Cis. Lower edge admits next Es–Fis title and clef tip; own H/Cis analysis extends below that title. |
| `primjer-2-324` | Upper edge admits 2.323 H/Cis analysis; lower edge admits 2.325 C–Ces title, clef tip and stem tips. Its own Es–Fis title and Fis analysis interleave those neighbouring elements. |
| `primjer-2-325-score` | Upper edge admits 2.324 D:IV-flat and Fis:IV-natural analysis at the heights required by own C–Ces title and upper stems. Its own number, entire score, low stem and first analysis line are complete, but foreign analysis remains. |
| `primjer-2-347` | Lower edge admits the upper part of next a–c title and clef tip; own g:V2 analysis overlaps that title vertically. |
| `primjer-2-348` | Upper edge admits preceding g:V2 analysis, vertically overlapping own a–c title. Lowering the top would clip that title. |

## Multipart and tight-edge findings

- **2.305:** `-p139` includes the number and variants a/b on printed 139. `-p140` is the correct c continuation on printed 140; the source does not repeat the number. Both PASS. No fabricated number or stitching is required.
- **2.325:** the single printed-145 slot correctly maps to `-score` and `-analysis`. The score part retains **the entire lowest bass stem** and first analysis line **C:IV-flat**. The analysis part retains **Des:III, II6, Ces:III6** completely, with original white margins and **no running footer or printed 145**. Its absent repeated number is a legitimate part exception. The lower part PASS does not override the score part's upper contamination.
- **2.361:** enlarged lower edge preserves the complete final natural in the Fis analysis; the main ink ends at source row 1761, followed by two genuine blank rows before crop bottom 1764. The neighbouring title begins below the crop. This very tight but intact source gap was checked explicitly, not mistaken for clipping.
- **2.302:** the source itself has open right staff ends at this excerpt; they are all retained. A nonexistent final barline was not required or added.
- Small isolated dots/flecks in 2.305, 2.309, 2.319, 2.320, 2.336, 2.362 and 2.368 are not partial neighbouring characters. The structured faint strokes in 2.321 are materially different and remain a failure.
- Heavy/filled noteheads in 2.367 are present in the authoritative scan; they were not caused by cropping. No example was omitted as unreadable. The faint handwriting's exact reading is uncertain; its foreign, structured appearance is sufficient to flag it without inventing a transcription.

## Per-image decisions

All image paths are repository-root-relative. **Rect = `null` for every entry** (no safe replacement proposed); **SL** is the `source_limited` boolean. Detailed reasons and machine-readable fields are in `review-candidates/book/M04/visual-review-137-155.json`.

| ID | Image | Printed page | Decision | Reason | Rect | SL |
| --- | --- | ---: | --- | --- | --- | --- |
| primjer-2-302 | images/02-dijatonika-c/primjer-2-302.png | 137 | PASS | Schumann attribution, full staves/open ends and analysis; edges clean. | null | false |
| primjer-2-303 | images/02-dijatonika-c/primjer-2-303.png | 137 | PASS | Beethoven attribution, slurs, final barline and Es/Des analysis; no footer. | null | false |
| primjer-2-304 | images/02-dijatonika-c/primjer-2-304.png | 138 | PASS | Number, a/b variants and both analysis rows; no prose. | null | false |
| primjer-2-305-p139 | images/02-dijatonika-c/primjer-2-305-p139.png | 139 | PASS | Number, a/b, arrow and analyses complete; source speck only. | null | false |
| primjer-2-305-p140 | images/02-dijatonika-c/primjer-2-305-p140.png | 140 | PASS | Correct c continuation; no repeated number in source; full analysis. | null | false |
| primjer-2-306 | images/02-dijatonika-c/primjer-2-306.png | 140 | PASS | C–G, number, staves and C:VI/G:II complete. | null | false |
| primjer-2-307 | images/02-dijatonika-c/primjer-2-307.png | 140 | PASS | Both a/b variants and full figured analysis; no footer. | null | false |
| primjer-2-308 | images/02-dijatonika-c/primjer-2-308.png | 141 | PASS | Number, tie, C–G and C:V/G:I intact. | null | false |
| primjer-2-309 | images/02-dijatonika-c/primjer-2-309.png | 141 | PASS | C–F, number and C:I/F:V complete; bottom speck not prose. | null | false |
| primjer-2-310 | images/02-dijatonika-c/primjer-2-310.png | 141 | PASS | Five measures, number and C:II/F:VI complete; footer excluded. | null | false |
| primjer-2-311 | images/02-dijatonika-c/primjer-2-311.png | 142 | PASS | C:IV/F:I intact; narrow lower gap contains no next title. | null | false |
| primjer-2-312 | images/02-dijatonika-c/primjer-2-312.png | 142 | PASS | C–F, number and C:VI/F:III complete; no prose. | null | false |
| primjer-2-313 | images/02-dijatonika-c/primjer-2-313.png | 142 | PASS | Full stems, accidentals and C:III7/D:II7; no footer. | null | false |
| primjer-2-314 | images/02-dijatonika-c/primjer-2-314.png | 143 | PASS | Number and C:IV/B:V complete; small genuine margin before prose. | null | false |
| primjer-2-315 | images/02-dijatonika-c/primjer-2-315.png | 143 | PASS | C–A, number and full chained G/A analysis; no next title. | null | false |
| primjer-2-316 | images/02-dijatonika-c/primjer-2-316.png | 143 | PASS | Number, C–Es and all lower B/Es analysis levels; no footer. | null | false |
| primjer-2-317 | images/02-dijatonika-c/primjer-2-317.png | 144 | RECROP_REQUIRED | Prose/underline fragment at top; next title/clef at bottom interleaves own analysis. | null | true |
| primjer-2-318 | images/02-dijatonika-c/primjer-2-318.png | 144 | RECROP_REQUIRED | Previous analysis/stem intrudes above staff, interleaving required title. | null | true |
| primjer-2-319 | images/02-dijatonika-c/primjer-2-319.png | 144 | PASS | Number, C–H, low ledger stem and full analysis; top speck only. | null | false |
| primjer-2-320 | images/02-dijatonika-c/primjer-2-320.png | 144 | PASS | Number, C–Es, low stem and analysis complete; no 144 footer. | null | false |
| primjer-2-321 | images/02-dijatonika-c/primjer-2-321.png | 145 | RECROP_REQUIRED | Faint structured handwritten-looking strokes beside As:VI inside required rectangle. | null | true |
| primjer-2-322 | images/02-dijatonika-c/primjer-2-322.png | 145 | PASS | Number, C–Des and full analysis; previous handwriting excluded. | null | false |
| primjer-2-323 | images/02-dijatonika-c/primjer-2-323.png | 145 | RECROP_REQUIRED | Prose descender at top; following Es–Fis title/clef at bottom; interleaved analysis. | null | true |
| primjer-2-324 | images/02-dijatonika-c/primjer-2-324.png | 145 | RECROP_REQUIRED | Previous analysis at top; next title/clef/stems at bottom interleave own content. | null | true |
| primjer-2-325-score | images/02-dijatonika-c/primjer-2-325-score.png | 145 | RECROP_REQUIRED | Full own score/stem/first analysis line, but previous D/Fis analysis intrudes at top. | null | true |
| primjer-2-325-analysis | images/02-dijatonika-c/primjer-2-325-analysis.png | 145 | PASS | Complete lower Des/II6/Ces analysis part; no repeated source number; no footer. | null | false |
| primjer-2-326 | images/02-dijatonika-c/primjer-2-326.png | 146 | PASS | Number, E–Des and every analysis level through Des:II; no prose. | null | false |
| primjer-2-327 | images/02-dijatonika-c/primjer-2-327.png | 146 | PASS | Number, C–Ges, three brackets, stems and final barline complete. | null | false |
| primjer-2-328 | images/02-dijatonika-c/primjer-2-328.png | 146 | PASS | Number, full a/b systems and lowest stems; task text excluded. | null | false |
| primjer-2-329 | images/02-dijatonika-c/primjer-2-329.png | 147 | PASS | Number, a/b, bracket and both analyses complete; no prose. | null | false |
| primjer-2-330 | images/02-dijatonika-c/primjer-2-330.png | 147 | PASS | Number, C–a, lowest bass stem and full figures; neighbour excluded. | null | false |
| primjer-2-331 | images/02-dijatonika-c/primjer-2-331.png | 147 | PASS | Number, C–e, final low ledger note and full analysis; footer excluded. | null | false |
| primjer-2-332 | images/02-dijatonika-c/primjer-2-332.png | 148 | PASS | Number, C–h and C:V/h:VI intact; no adjacent ink or prose. | null | false |
| primjer-2-333 | images/02-dijatonika-c/primjer-2-333.png | 148 | PASS | Number, C–d and C:IV/d:III complete; narrow bottom edge clean. | null | false |
| primjer-2-334 | images/02-dijatonika-c/primjer-2-334.png | 148 | PASS | Number, C–g and C:I/g:IV complete; adjacent rows excluded. | null | false |
| primjer-2-335 | images/02-dijatonika-c/primjer-2-335.png | 148 | PASS | Number, C–c and C:V/c:V intact; neighbour excluded. | null | false |
| primjer-2-336 | images/02-dijatonika-c/primjer-2-336.png | 148 | PASS | Number, C–f and C:I/f:V complete; isolated source fleck only. | null | false |
| primjer-2-337 | images/02-dijatonika-c/primjer-2-337.png | 148 | PASS | Number, 3/2, ledger lines, dots and C:IV/b:V complete. | null | false |
| primjer-2-338 | images/02-dijatonika-c/primjer-2-338.png | 148 | PASS | Number, C–es and full figured analysis; no footer. | null | false |
| primjer-2-339 | images/02-dijatonika-c/primjer-2-339.png | 149 | PASS | Number, C–gis, accidentals and all E/gis analysis intact. | null | false |
| primjer-2-340 | images/02-dijatonika-c/primjer-2-340.png | 149 | PASS | Number, B–cis, low ledger stems and all A/cis analysis intact. | null | false |
| primjer-2-341 | images/02-dijatonika-c/primjer-2-341.png | 149 | PASS | Number, C–as and full C/Es/as analysis; no prose/footer. | null | false |
| primjer-2-342 | images/02-dijatonika-c/primjer-2-342.png | 150 | PASS | Number, A–b, tie, lowest stems and full A/C/b analysis. | null | false |
| primjer-2-343 | images/02-dijatonika-c/primjer-2-343.png | 150 | PASS | Number, a–e and a:I6/e:IV6 complete; neighbour excluded. | null | false |
| primjer-2-344 | images/02-dijatonika-c/primjer-2-344.png | 150 | PASS | Number, a–h, ties, figures and source barline/stem intact. | null | false |
| primjer-2-345 | images/02-dijatonika-c/primjer-2-345.png | 150 | PASS | Number, a–fis, final low accidental and full figured analysis. | null | false |
| primjer-2-346 | images/02-dijatonika-c/primjer-2-346.png | 150 | PASS | Number, a–d, low stem and a:VI/d:III; no footer. | null | false |
| primjer-2-347 | images/02-dijatonika-c/primjer-2-347.png | 151 | RECROP_REQUIRED | Next a–c title/clef intrudes at bottom, interleaving own g:V2. | null | true |
| primjer-2-348 | images/02-dijatonika-c/primjer-2-348.png | 151 | RECROP_REQUIRED | Previous g:V2 intrudes at top, interleaving own a–c title. | null | true |
| primjer-2-349 | images/02-dijatonika-c/primjer-2-349.png | 151 | PASS | Number, a–f, low ledger note and a:III/f:V; no previous analysis. | null | false |
| primjer-2-350 | images/02-dijatonika-c/primjer-2-350.png | 151 | PASS | Number, a–b, long slur and a:VI/b:V; no prose. | null | false |
| primjer-2-351 | images/02-dijatonika-c/primjer-2-351.png | 151 | PASS | Number, a–ais, 3/2, stems and all a/H/ais analysis; no footer. | null | false |
| primjer-2-352 | images/02-dijatonika-c/primjer-2-352.png | 152 | PASS | Number, c–dis, double-sharp and full G/H/dis analysis; no prose. | null | false |
| primjer-2-353 | images/02-dijatonika-c/primjer-2-353.png | 152 | PASS | Number, a–as and complete a/B/as analysis; edges clean. | null | false |
| primjer-2-354 | images/02-dijatonika-c/primjer-2-354.png | 152 | PASS | Number, fis–b and full fis/g/b analysis; task text excluded. | null | false |
| primjer-2-355 | images/02-dijatonika-c/primjer-2-355.png | 153 | PASS | Number, a–C and a:VI/C:IV; adjacent examples excluded. | null | false |
| primjer-2-356 | images/02-dijatonika-c/primjer-2-356.png | 153 | PASS | Number, a–G, tie, low sharp/stem and a:I/G:II complete. | null | false |
| primjer-2-357 | images/02-dijatonika-c/primjer-2-357.png | 153 | PASS | Number, a–D, low stem and complete a/D analysis; no neighbour. | null | false |
| primjer-2-358 | images/02-dijatonika-c/primjer-2-358.png | 153 | PASS | Number, a–A, tie and a:V/A:V; four edges clean. | null | false |
| primjer-2-359 | images/02-dijatonika-c/primjer-2-359.png | 153 | PASS | Number, a–E, 3/2, ties/dots and a:V/E:I; next title excluded. | null | false |
| primjer-2-360 | images/02-dijatonika-c/primjer-2-360.png | 153 | PASS | Number, a–H, low stems and a:V/H:IV complete; no neighbour. | null | false |
| primjer-2-361 | images/02-dijatonika-c/primjer-2-361.png | 153 | PASS | Full lowest natural checked enlarged; two blank rows below main ink, no next title. | null | false |
| primjer-2-362 | images/02-dijatonika-c/primjer-2-362.png | 153 | PASS | Number, a–F and a:IV6/F:VI6 complete; isolated bottom speck only. | null | false |
| primjer-2-363 | images/02-dijatonika-c/primjer-2-363.png | 153 | PASS | Number, a–B, 3/2, upper stems and a:VI/B:V; no prose or prior glyph. | null | false |
| primjer-2-364 | images/02-dijatonika-c/primjer-2-364.png | 154 | PASS | Number, a–Cis, ties and full a/H/Cis analysis; no prose. | null | false |
| primjer-2-365 | images/02-dijatonika-c/primjer-2-365.png | 154 | PASS | Number, g–Fis, low sharp and full g/D/Fis analysis; outer mark excluded. | null | false |
| primjer-2-366 | images/02-dijatonika-c/primjer-2-366.png | 154 | PASS | Number, a–As, low flat/stem and full a/b/As analysis. | null | false |
| primjer-2-367 | images/02-dijatonika-c/primjer-2-367.png | 154 | PASS | Number, h–Des and full analysis; heavy source noteheads not crop damage. | null | false |
| primjer-2-368 | images/02-dijatonika-c/primjer-2-368.png | 155 | PASS | Number, a/b, all brackets and analyses; irregular source dirt not handwriting. | null | false |
| primjer-2-369 | images/02-dijatonika-c/primjer-2-369.png | 155 | PASS | Number, C–g, both brackets and C:IV/g:VII; neighbour excluded. | null | false |
| primjer-2-370 | images/02-dijatonika-c/primjer-2-370.png | 155 | PASS | Number, C–d, both brackets, low stems and C:I/d:VII complete. | null | false |
| primjer-2-371 | images/02-dijatonika-c/primjer-2-371.png | 155 | PASS | Number, C–g, lower bracket and full II4/3 analysis; no footer/prose. | null | false |
| primjer-2-372 | images/02-dijatonika-c/primjer-2-372.png | 155 | PASS | Number, C–d, bracket and full II4/3 analysis; no 155 footer. | null | false |

## PDF index mapping

For this assigned range, **PDF page (1-based) = `floor(printed_page / 2) + 1`** and **PDF index (0-based) = `floor(printed_page / 2)`**. A spread's left printed page is `2 × PDF page − 2`; its right printed page is `2 × PDF page − 1`. For example, PDF 70 contains printed 138/139. The table was checked against `sources/index.json` and the freshly rendered PDF halves.

| PDF page (1-based) | PDF index (0-based) | Left printed page | Right printed page | Reviewed |
| ---: | ---: | ---: | ---: | --- |
| 69 | 68 | 136 | 137 | 137 only |
| 70 | 69 | 138 | 139 | 138–139 |
| 71 | 70 | 140 | 141 | 140–141 |
| 72 | 71 | 142 | 143 | 142–143 |
| 73 | 72 | 144 | 145 | 144–145 |
| 74 | 73 | 146 | 147 | 146–147 |
| 75 | 74 | 148 | 149 | 148–149 |
| 76 | 75 | 150 | 151 | 150–151 |
| 77 | 76 | 152 | 153 | 152–153 |
| 78 | 77 | 154 | 155 | 154–155 |

## Hand-off

1. **Assigned pages:** printed 137–155 / PDF 69–78; all reviewed.
2. **Only repository files created:** `review-candidates/book/M04/visual-review-137-155.json` and `review-candidates/book/M04/visual-review-137-155.md`.
3. **Examples extracted by this reviewer:** none. Independently reviewed all 73 already-extracted crops, covering 2.302–2.372 and their printed pages listed above.
4. **Results:** 65 PASS; 8 RECROP_REQUIRED; 0 unreviewed. All eight failures source-limited; no safe single-rectangle proposals.
5. **Ambiguities:** exact reading of faint handwriting beside 2.321 uncertain; do not erase or invent. Interleaved source layouts on printed 144, 145 and 151 prevent clean complete single rectangles for the flagged examples. No omission or fabricated completion is approved.
6. **Integration readiness:** **NO**. Preserve source pixels; do not mark the milestone complete until the failures have an independently reviewed, source-faithful resolution. Passing the lower 2.325 analysis part does not pass its score part or the whole slot.

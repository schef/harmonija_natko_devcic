# M08 — independent visual review

## Outcome

**105/105 current candidates reviewed: 82 PASS, 23 RECROP_REQUIRED, 0 unreviewed. M08 is not ready for complete image integration.**

Assigned range: printed pages **277–308**, **1-based PDF pages 139–155**. All 32 authoritative source PNG pages were opened, including page 279, which has no candidate image. No examples were extracted or images changed by this reviewer.

The record-level decisions, exact current image paths, printed source pages, reasons, source limitations and the one tested replacement rectangle are in `review-candidates/book/M08/visual-review.json`. Its 105 identities and image paths match `review-candidates/book/M08/images-complete.json` exactly, including all nine current extractor recrops.

### Counts

| Category | Count |
| --- | ---: |
| PASS, no identified source limitation | 80 |
| PASS as a crop, but source abrasion affects notation | 2 |
| RECROP_REQUIRED: source handwriting within the example's rectangular extent | 20 |
| RECROP_REQUIRED: page 303 exercise-2/exercise-3 overlap | 2 |
| RECROP_REQUIRED: removable foreign stroke on page 307 | 1 |
| Total source-limited records, including the two crop passes | 24 |
| Unreviewed | 0 |

`source_limited: true` does **not** waive a failed checklist item. Handwriting and overlapping neighbouring notation still fail. The two abrasion records pass only the crop review: missing source ink is not certified as readable notation.

## Review method and scope

- Used `review-candidates/book/M08/images-complete.json` as the current-candidate inventory, rather than substituting older image files.
- Opened every authoritative source page `sources/pages/page-277.png` through `sources/pages/page-308.png` and inspected all current crops on page-labelled review sheets made without resizing their source pixels.
- Inspected **all four edges of every crop** on separate native-resolution edge strips. Vertical edge strips were rotated, not rescaled, so their complete lengths could be inspected. Enlarged source regions were additionally inspected for the page 277 inline progression, page 283 low stems/handwriting, page 303 overlap and page 307 foreign stroke.
- Compared decoded RGB pixels for all 105 images against the corresponding manifest rectangle in the authoritative source PNG: **105 exact matches**, with no dimension mismatch or differing decoded pixels. This establishes that the candidates have no added border or retouching within those rectangles; source damage and handwriting remain source pixels.
- Matched the inventory to all **49 visual slots** in `review-candidates/book/M08/text-277-292.md` and **56 visual slots** in `review-candidates/book/M08/text-293-308.md`, checking printed identity, variants, realization title, attribution, continuation relationship and source-page caption. These files contain visual placeholders, not final embedded Markdown image/alt-text blocks; final chapter embedding and alt text are not approved by this review.
- Checked printed numbers/IDs, all visible variants, full staff starts and ends, slurs/ties, low stems, analysis, callouts and feasible genuine blank margins. No synthetic blank margin was used to resolve a failed edge.

The manifest's PDF page numbers are consistent with `floor(printed_page / 2) + 1` over this range and are treated as **1-based indices**, not zero-based indices. No prose transcription review or independent reconstruction of damaged notation is claimed.

## Actionable findings

### One fully tested source-only recrop

**`4.z307-3`, printed page 307, PDF page 154: RECROP_REQUIRED.**

Current image: `images/04-neakordicki-a/zadatak-4-307-3.png`.

An unrelated small diagonal stroke lies at source approximately **x224–230, y692–694**, in the left margin between the second and third staff rows. It is not part of the exercise. The current left edge at x220 retains it.

Tested replacement rectangle, in the same `[left, top, right, bottom]` pixel convention as the manifest:

```json
[232, 355, 1742, 1071]
```

Source: `sources/pages/page-307.png`. This changes only the left edge. The proposed full source crop and all four edges were opened and inspected; it removes the entire stroke and retains the complete printed ID 3, all four staff starts, notation, lowest notes and final barline. The very small remaining left whitespace is genuine and feasible given the mark's proximity. No other replacement rectangle is asserted safe.

This is a **proposal only**, not an applied image edit. The current candidate remains RECROP_REQUIRED. Temporary source-only test crops were confined to the approved temporary directory.

### Page 303: genuinely overlapping vertical ranges

Both **`4.z303-2-cont`** and **`4.z303-3`** remain **RECROP_REQUIRED**, source-limited.

- Exercise 2's low final figures extend into the vertical range occupied by exercise 3's upper slur.
- The exercise-2 continuation retains foreign slur ink at its bottom.
- The current exercise-3 recrop restores the intended complete slur, but retains partial exercise-2 figures at its top.
- Enlarged source inspection confirms this is not fixed by moving a horizontal boundary into a clean gap: a clean gap spanning the required rectangle does not exist. Moving the exercise-3 top down would clip its slur; moving the exercise-2 bottom up would lose intended analysis.

No guessed rectangle, retouching, masking, invented notation or artificial margin is proposed. These two source-limited failures block strict score-only approval.

### Handwriting: 20 strict-checklist failures

The following candidates retain handwriting within the complete printed example's rectangular extent, sometimes also touching a crop boundary:

- Page 277: `4.1`.
- Page 278: `4.1-c`, `4.2`.
- Page 280: `4.3`.
- Page 281: `4.4`, `4.5`.
- Page 282: `4.7`, `4.9`.
- Page 283: `4.10`, `4.11`, `4.12`.
- Page 284: `4.14`, `4.15`, `4.16`.
- Page 285: `4.17`.
- Page 290: `4.22`.
- Page 291: `4.23`, `4.24`, `4.25`, `4.26`.

These are not passed merely because the printed notes remain visible. No fully safe handwriting-free rectangular replacement is supplied. In particular, enlarged inspection of `4.11` shows handwriting immediately adjacent to the bass/low stems; an untested bottom cut must not be substituted as a safe repair.

## Nine current extractor recrops

| Record | Printed page | Decision | Independently verified result |
| --- | ---: | --- | --- |
| `4.13` | 283 | PASS | Complete lowest bass stem restored, with genuine lower whitespace. |
| `4.z289-9-realizacija` | 289 | PASS | Complete printed realization title and first system retained. |
| `4.z294-5-realizacija` | 294 | PASS | Complete printed realization title and both systems retained. |
| `4.z297-3-realizacija` | 297 | PASS | Complete printed realization title and all three systems retained. |
| `4.z303-3` | 303 | RECROP_REQUIRED | Upper slur restored, but foreign figured-bass fragments remain because of source overlap. |
| `4.z303-3-realizacija` | 303 | PASS | Complete printed realization title and low bass stem retained. |
| `4.z306-1` | 306 | PASS | Full final figures retained; neighbouring exercise-2 top excluded. |
| `4.z306-2` | 306 | PASS | Full high opening note/ledger line retained with genuine upper separation. |
| `4.z308-3-realizacija` | 308 | PASS | Complete printed realization title, five systems and final double barline retained. |

Thus **8/9 extractor recrops pass**. This review confirms their current coverage fixes; it did not create additional extraction files.

## Source damage, unnumbered figures and continuations

- **Page 290, `4.z290-9-realizacija-cont`: PASS as a crop, source-limited.** Abrasion removes ink in the lower staff of the first system near its second measure; worn ink is also visible near the following system's left side. These losses occur inside the source, not at a crop boundary. Exact lost notation remains unreadable/uncertified here; no reconstruction was performed.
- **Page 295, `4.31`: PASS as a crop, source-limited.** Variant c has missing/worn upper-staff ink already visible in the authoritative source. The rectangle retains the surrounding material and is not responsible for that loss. Exact missing notation remains uncertified.
- **Page 277, `progresija-277`: PASS.** This is genuinely unnumbered. The complete inline progression, stacked figures and final I are retained. The following comma and surrounding prose are excluded. Do not assign an invented printed example number.
- **Page 304, `sifra-appoggiature-304`: PASS.** This is genuinely unnumbered. Complete `9/7/4 > 8/3` figure and convergence strokes are retained, with no surrounding footnote prose. Do not assign an invented printed number.
- Missing repeated numbers on source continuations are acceptable only with their correct pairings: `4.1-c` with page 277 `4.1`; `4.21-cont` with page 286 `4.21`; page 288 exercise 3 with page 287; page 290 realization 9 with page 289; page 294 exercise 6 with page 293; page 299 exercise 1 with page 298; page 303 exercise 2 with page 302; page 304 realization 3 with page 303; page 307 exercise 2 with page 306. Their captions/slots establish those relationships. Pairing correctness does not override a handwriting/overlap failure.

No further unreadable source region is specifically certified by this review. Source noise or faintness must not be silently replaced with invented notation during later transcription.

## Complete per-page decision index

Every ID below has its own reason and exact image path in the JSON report. A dash means no record of that decision on that page, not an unreviewed record.

| Printed page | PASS | RECROP_REQUIRED |
| ---: | --- | --- |
| 277 | `progresija-277` | `4.1` |
| 278 | — | `4.1-c`, `4.2` |
| 279 | No visual candidate; source page opened | — |
| 280 | — | `4.3` |
| 281 | — | `4.4`, `4.5` |
| 282 | `4.6`, `4.8` | `4.7`, `4.9` |
| 283 | `4.13` | `4.10`, `4.11`, `4.12` |
| 284 | — | `4.14`, `4.15`, `4.16` |
| 285 | `4.18` | `4.17` |
| 286 | `4.19`, `4.20`, `4.21` | — |
| 287 | `4.21-cont`, `4.z287-1`, `4.z287-2`, `4.z287-3` | — |
| 288 | `4.z288-3-cont`, `4.z288-4`, `4.z288-5`, `4.z288-6`, `4.z288-7`, `4.z288-8` | — |
| 289 | `4.z289-9`, `4.z289-10`, `4.z289-11`, `4.z289-12`, `4.z289-13`, `4.z289-9-realizacija` | — |
| 290 | `4.z290-9-realizacija-cont` (source damage) | `4.22` |
| 291 | — | `4.23`, `4.24`, `4.25`, `4.26` |
| 292 | `4.27`, `4.28`, `4.29`, `4.30` | — |
| 293 | `4.z293-1`, `4.z293-2`, `4.z293-3`, `4.z293-4`, `4.z293-5`, `4.z293-6` | — |
| 294 | `4.z294-6-cont`, `4.z294-7`, `4.z294-5-realizacija` | — |
| 295 | `4.31` (source damage), `4.32`, `4.33`, `4.34` | — |
| 296 | `4.35`, `4.z296-1`, `4.z296-2` | — |
| 297 | `4.z297-3`, `4.z297-4`, `4.z297-3-realizacija` | — |
| 298 | `4.36`, `4.37`, `4.z298-1` | — |
| 299 | `4.z299-1-cont`, `4.z299-2`, `4.38` | — |
| 300 | `4.39`, `4.40`, `4.41` | — |
| 301 | `4.42`, `4.43`, `4.44` | — |
| 302 | `4.45`, `4.z302-1`, `4.z302-2` | — |
| 303 | `4.z303-4`, `4.z303-5`, `4.z303-6`, `4.z303-3-realizacija` | `4.z303-2-cont`, `4.z303-3` |
| 304 | `4.z304-3-realizacija-cont`, `sifra-appoggiature-304`, `4.46` | — |
| 305 | `4.47`, `4.48`, `4.49`, `4.50` | — |
| 306 | `4.51`, `4.52`, `4.z306-1`, `4.z306-2` | — |
| 307 | `4.z307-2-cont`, `4.z307-4`, `4.z307-5` | `4.z307-3` |
| 308 | `4.z308-3-realizacija` | — |

## Handoff

1. **Assignment:** printed 277–308; 1-based PDF 139–155.
2. **Repository files created/changed by this review only:** `review-candidates/book/M08/visual-review.json` and `review-candidates/book/M08/visual-review.md`.
3. **Extraction:** none performed; all 105 existing candidates reviewed, with source pages indexed above and individually in JSON.
4. **Image results:** 82 PASS, 23 RECROP_REQUIRED, zero unreviewed; all nine current extractor recrops included.
5. **Source limitations:** 20 handwriting failures, two vertical-overlap failures, two crop passes with damaged/uncertified source notation. One additional removable foreign-stroke failure has a fully tested rectangle.
6. **Integration readiness:** review handoff complete, but **not ready to mark M08 complete**. Apply/re-review the page 307 proposal and resolve the strict-checklist source-limited failures without clipping or retouching. Final image embedding/alt text and prose review remain integration responsibilities. No manifests, images, chapter files or tracker were edited; no commit, push or approval exception was made.

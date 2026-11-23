# Independent visual review — M09, printed pages 309–328

## Outcome

**68/68 records reviewed: 52 PASS, 16 RECROP_REQUIRED, 0 unreviewed. Not ready for integration as a complete image set.**

Reviewed manifest: `review-candidates/book/M09/images-309-328.json`.
Authoritative sources: `sources/pages/page-309.png` through `sources/pages/page-328.png`.
Assigned printed pages **309–328**, **1-based PDF pages 155–165**.
This reviewer did not extract these images. One worker; no delegation, model subprocess, external API, GUI, retouching, image/manifest/chapter/tracker changes, commit or push.

Per-image decisions and specific reasons are in `review-candidates/book/M09/visual-review-309-328.json`. Image paths remain repository-root-relative. Every crop was opened individually at its native pixel dimensions and compared with its authoritative page; each top, bottom, left and right edge was inspected, including lowest stems/figures, labels, staff ends and attribution/title bounds. The faint circle in 4.62 was additionally inspected enlarged in `/tmp/opencode/m09-62-annotation-detail.png`.

## Provenance and exact-pixel checks

- **68/68** images have exactly the same decoded pixel bytes, color mode and dimensions as `Image.open(source_image).crop(rect)`. Comparison was exact, not perceptual or an encoded-PNG file hash. Rectangles use source pixels, exclusive right/bottom. No artificial border, retouching or resampling was found in the delivered crops.
- **68/68** records agree with `sources/index.json` for source path, printed page, image dimensions and 1-based PDF page. The verified mapping is `pdf_page = printed_page // 2 + 1`, not a zero-based PDF index. The index identifies the PNGs as lossless halves of 300-dpi PDF spreads. This review checked that index mapping and visible printed folios; it did not independently re-render the PDF.
- Mapping: 309 → PDF 155/right; 310–311 → 156/left–right; 312–313 → 157/left–right; 314–315 → 158/left–right; 316–317 → 159/left–right; 318–319 → 160/left–right; 320–321 → 161/left–right; 322–323 → 162/left–right; 324–325 → 163/left–right; 326–327 → 164/left–right; 328 → 165/left.
- Record filenames, printed example/exercise identities, source pages and manifest captions agree. Realization titles are present for the realization of exercise 3 on 317 and exercise 4 on 322. The text candidates still use visual-slot comments, so this is not a claim that final Markdown image alt text and caption integration has already been completed.

## Page-by-page coverage

| Printed page | PDF page (1-based) | Records inspected | PASS | RECROP_REQUIRED |
| --- | --- | --- | ---: | ---: |
| 309 | 155 | 4.53–4.54 | 0 | 2 |
| 310 | 156 | 4.55–4.58 | 0 | 4 |
| 311 | 156 | 4.59–4.60 | 1 | 1 |
| 312 | 157 | 4.61–4.64 | 0 | 4 |
| 313 | 157 | 4.65–4.68 | 0 | 4 |
| 314 | 158 | 4.69–4.71 | 2 | 1 |
| 315 | 158 | Exercises 1–5 | 5 | 0 |
| 316 | 159 | Exercises 6–8 | 3 | 0 |
| 317 | 159 | Exercise 9; realization of exercise 3 | 2 | 0 |
| 318 | 160 | 4.72–4.75 | 4 | 0 |
| 319 | 160 | 4.76–4.80 | 5 | 0 |
| 320 | 161 | 4.81–4.82 | 2 | 0 |
| 321 | 161 | Exercises 1–5 | 5 | 0 |
| 322 | 162 | Realization of exercise 4; 4.83–4.84 | 3 | 0 |
| 323 | 162 | 4.85–4.88 | 4 | 0 |
| 324 | 163 | 4.89–4.91 | 3 | 0 |
| 325 | 163 | 4.92–4.94 | 3 | 0 |
| 326 | 164 | 4.95–4.97; 4.98 a–c | 4 | 0 |
| 327 | 164 | 4.98 d–e; 4.99–4.100 | 3 | 0 |
| 328 | 165 | 4.101–4.103 | 3 | 0 |
| **Total** | | **68** | **52** | **16** |

## Blocking findings

**RECROP_REQUIRED:** 4.53, 4.54, 4.55, 4.56, 4.57, 4.58, 4.60, 4.61, 4.62, 4.63, 4.64, 4.65, 4.66, 4.67, 4.68 and 4.71.

These contain meaningful handwritten letters, circles, arrows or harmonic analysis; several also intersect that foreign ink at a crop edge. Faint structured marks were not dismissed as dust. In particular, 4.62 contains a hand-drawn circle beneath variant b's starting upper chord despite the manifest's empty review note. Internal handwriting cannot be removed by merely adjusting an outer rectangle without losing printed material. `RECROP_REQUIRED` here means the crop fails the checklist; it does **not** promise that a compliant rectangle exists in this source. Retouching is not an allowed solution.

### 4.67 — source-layout blocker, not an approved exception

The crop retains the full lower printed fermata, printed score asterisk, example number and Bach attribution. It also retains the printed footnote sentence, independently transcribed in `review-candidates/book/M09/text-313-316.md`. The sentence overlaps the lower fermata's vertical range in the source layout, so cutting it away at the bottom would cut required notation. Handwritten analysis is also present. **The retained footnote prose prevents approval.** Do not clip the fermata/asterisk, treat the footnote as score content, or mark this image PASS merely because the notes are visible. No safe rectangular replacement is proposed.

### 4.98 — valid cross-page pairing

`primjer-4-98-a.png` contains printed number 4.98 and actual variants **a–c** on 326. `primjer-4-98-b.png` contains actual variants **d–e** on 327, without a repeated printed number. Both are PASS as paired parts, not as invented variants a/b. The manifest captions identify example 4.98 and their distinct printed source pages; `review-candidates/book/M09/text-319-333.md` explicitly provides separate `4.98 a–c; page 326` and `4.98 d–e; page 327` visual slots. Preserve that distinction in final alt text/captions; do not add a fake example number to the second source crop.

## Source limitations versus crop failures

`source_limited` is true on **4 records**: 4.67, 4.74, 4.102 and 4.103. It flags the footnote/fermata source-layout conflict or a source notation/abrasion caveat, not an automatic failure or permission to repair pixels. Handwritten contamination is documented explicitly in failure reasons rather than being reclassified as uncertain notation.

- **4.74: PASS, source_limited true.** The irregular/open right endpoints of c, including small endpoint damage, are already present in the source. The crop preserves the available ending with source whitespace. No claim that missing notes have been reconstructed or that a fuller ending was verified elsewhere.
- **4.102: PASS, source_limited true.** Grain/abrasion makes fine glyph contours in the right upper-staff cluster less certain. Pixels are preserved exactly; any music transcription should treat this as a source-reading caveat, not crop loss.
- **4.103: PASS, source_limited true.** Abrasion/grain at the bass opening/signatures and staff contours is present in the authoritative source. All available notation and the lowest fermata survive; page number 328 is excluded. No reconstructed notation.
- Other open staff endings (for example 4.70, 4.87, 4.94–4.96 and 4.100) agree with the source and do not by themselves imply missing notation.
- Isolated dust specks and normal scan grain were distinguished from shaped handwriting/partial foreign characters. PASS does not assert that a historical scan is dust-free.

## Replacement rectangles and hand-off

**No `proposed_rect` values are supplied.** No fully safe score-complete replacement rectangle was established for the failed records; none is guessed. Therefore there are no proposed source crops to test, and no untested rectangle is being handed off. The only temporary diagnostic was the enlarged 4.62 detail under `/tmp/opencode`.

Files created by this review only:

1. `review-candidates/book/M09/visual-review-309-328.json`
2. `review-candidates/book/M09/visual-review-309-328.md`

Musical examples extracted by this reviewer: **none**. Existing records reviewed: **68**, covering the example/exercise and printed-page assignments above. **52 pass; 16 require correction or resolution of source blockers; 0 remain unreviewed.** No human approval sought or implied. The complete assignment is **not ready for integration** until the 16 failures are resolved and independently reviewed again; passing source-limited records retain their caveats.
